#!/usr/bin/env python3
"""Publish a week's approved social items from the package's publish.json.

Usage:
  publish.py MANIFEST [--due] [--item ID] [--dry-run] [--force-time]

  --due         publish every item whose state is "approved" and whose time has come
  --item ID     publish this one item (still only when it is "approved")
  --dry-run     say what would be published, call nothing
  --force-time  with --item: do not wait for its time

Only the standard library. Keys come from the manifest's env file (never printed):
  THREADS_ACCESS_TOKEN, THREADS_USER_ID                       for threads
  IG_ACCESS_TOKEN, IG_USER_ID                                 for instagram
  SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY                     for instagram media

Instagram takes media only by a public URL: the files go to a public Supabase Storage bucket for
the time the container is made, and are deleted once the post is published (or has failed).
The manifest is rewritten after every item, so a crash never publishes an item twice: an item is
"publishing" before the first call and stays so if the run dies; such an item needs a person.
"""
import datetime
import json
import mimetypes
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

THREADS = "https://graph.threads.net/v1.0"
GRAPH = "https://graph.facebook.com/v21.0"
PLACEHOLDER = re.compile(r"\[[^\]]+\]")


class Failure(Exception):
    pass


def load_env(path):
    values = {}
    with open(os.path.expanduser(path)) as handle:
        for line in handle:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                values[key.strip()] = value.strip()
    return values


def http(method, url, *, params=None, data=None, headers=None, raw=None):
    headers = dict(headers or {})
    body = raw
    if params is not None:
        if method == "GET":
            url += ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
        else:
            body = urllib.parse.urlencode(params).encode()
    if data is not None:
        body = json.dumps(data).encode()
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=body, method=method, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            text = response.read().decode() or "{}"
            return json.loads(text)
    except urllib.error.HTTPError as error:
        detail = error.read().decode(errors="replace")[:500]
        raise Failure(f"{method} {url.split('?')[0]} -> {error.code}: {detail}") from None


# --- storage ---------------------------------------------------------------------------------


class Storage:
    def __init__(self, env, bucket):
        self.base = env["SUPABASE_URL"].rstrip("/") + "/storage/v1"
        key = env["SUPABASE_SERVICE_ROLE_KEY"]
        # A new secret key (sb_secret_...) is not a JWT: the gateway reads it from apikey alone.
        self.auth = {"apikey": key} if key.startswith("sb_") else {"Authorization": f"Bearer {key}", "apikey": key}
        self.bucket = bucket
        self.ready = False

    def ensure_bucket(self):
        if self.ready:
            return
        try:
            http("GET", f"{self.base}/bucket/{self.bucket}", headers=self.auth)
        except Failure as error:
            if " 404" not in str(error) and " 400" not in str(error):
                raise
            http("POST", f"{self.base}/bucket", headers=self.auth, data={
                "id": self.bucket, "name": self.bucket, "public": True,
                "file_size_limit": 104857600, "allowed_mime_types": ["image/png", "image/jpeg", "video/mp4"],
            })
        self.ready = True

    def upload(self, local, remote):
        self.ensure_bucket()
        kind = mimetypes.guess_type(local)[0] or "application/octet-stream"
        with open(local, "rb") as handle:
            http("POST", f"{self.base}/object/{self.bucket}/{remote}", raw=handle.read(),
                 headers={**self.auth, "Content-Type": kind, "x-upsert": "true"})
        return f"{self.base}/object/public/{self.bucket}/{urllib.parse.quote(remote)}"

    def delete(self, remotes):
        if remotes:
            http("DELETE", f"{self.base}/object/{self.bucket}", headers=self.auth, data={"prefixes": remotes})


# --- platforms -------------------------------------------------------------------------------


def threads_publish(item, text, env, results):
    token, user = env["THREADS_ACCESS_TOKEN"], env["THREADS_USER_ID"]
    auth = {"Authorization": f"Bearer {token}"}
    if len(text) > 500:
        raise Failure(f"text is {len(text)} characters, Threads allows 500")
    params = {"media_type": "TEXT", "text": text}
    if item.get("reply_to"):
        target = results.get(item["reply_to"], item["reply_to"])
        params["reply_to_id"] = target
    if item.get("poll"):
        options = item["poll"]
        if not 2 <= len(options) <= 4 or any(len(option) > 25 for option in options):
            raise Failure("a poll has 2-4 options of at most 25 characters")
        params["poll_attachment"] = json.dumps({f"option_{'abcd'[i]}": option for i, option in enumerate(options)})
    container = http("POST", f"{THREADS}/{user}/threads", params=params, headers=auth)["id"]
    time.sleep(5)
    published = http("POST", f"{THREADS}/{user}/threads_publish", params={"creation_id": container}, headers=auth)["id"]
    link = http("GET", f"{THREADS}/{published}", params={"fields": "permalink"}, headers=auth).get("permalink", "")
    return published, link


def ig_wait(container, token, minutes=10):
    deadline = time.time() + minutes * 60
    while time.time() < deadline:
        status = http("GET", f"{GRAPH}/{container}", params={"fields": "status_code,status", "access_token": token})
        code = status.get("status_code")
        if code == "FINISHED":
            return
        if code in ("ERROR", "EXPIRED"):
            raise Failure(f"container {container}: {status.get('status', code)}")
        time.sleep(5)
    raise Failure(f"container {container} not ready after {minutes} min")


def instagram_publish(item, caption, env, storage, folder, prefix):
    token, user = env["IG_ACCESS_TOKEN"], env["IG_USER_ID"]
    media = item["media"]
    alts = item.get("alt", [])
    if len(caption) > 2200:
        raise Failure(f"caption is {len(caption)} characters, Instagram allows 2200")
    uploaded = []
    try:
        urls = []
        for path in media:
            remote = f"{prefix}/{item['id']}/{os.path.basename(path)}"
            urls.append(storage.upload(os.path.join(folder, path), remote))
            uploaded.append(remote)

        def child(url, index, carousel):
            params = {"access_token": token}
            if url.lower().endswith(".mp4"):
                params.update({"media_type": "REELS" if not carousel else "VIDEO", "video_url": url})
            else:
                params["image_url"] = url
                if index < len(alts) and alts[index]:
                    params["alt_text"] = alts[index]
            if carousel:
                params["is_carousel_item"] = "true"
            else:
                params["caption"] = caption
            container = http("POST", f"{GRAPH}/{user}/media", params=params)["id"]
            ig_wait(container, token)
            return container

        if len(urls) > 1:
            if len(urls) > 10:
                raise Failure("a carousel holds at most 10 items")
            children = [child(url, index, True) for index, url in enumerate(urls)]
            parent = http("POST", f"{GRAPH}/{user}/media", params={
                "media_type": "CAROUSEL", "children": ",".join(children), "caption": caption, "access_token": token,
            })["id"]
            ig_wait(parent, token)
        else:
            parent = child(urls[0], 0, False)
        published = http("POST", f"{GRAPH}/{user}/media_publish", params={"creation_id": parent, "access_token": token})["id"]
        link = http("GET", f"{GRAPH}/{published}", params={"fields": "permalink", "access_token": token}).get("permalink", "")
        return published, link
    finally:
        try:
            storage.delete(uploaded)
        except Failure as error:
            print(f"warning: media not deleted ({error}); delete {uploaded} by hand", file=sys.stderr)


# --- the run ---------------------------------------------------------------------------------


def text_of(item, folder):
    if "text_file" in item:
        with open(os.path.join(folder, item["text_file"])) as handle:
            return handle.read().strip()
    return item.get("text", "").strip()


def when(item):
    return datetime.datetime.fromisoformat(item["at"])


def save(manifest, path):
    temporary = path + ".tmp"
    with open(temporary, "w") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    os.replace(temporary, path)


def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        sys.exit(__doc__)
    path = os.path.abspath(args[0])
    folder = os.path.dirname(path)
    due = "--due" in args
    dry = "--dry-run" in args
    only = args[args.index("--item") + 1] if "--item" in args else None
    force = "--force-time" in args
    if not due and not only:
        sys.exit("say --due or --item ID")

    with open(path) as handle:
        manifest = json.load(handle)
    env = load_env(manifest["env"])
    results = {item["id"]: item["result"]["id"] for item in manifest["items"] if item.get("result", {}).get("id")}
    storage = None
    now = datetime.datetime.now()
    log_path = os.path.expanduser(manifest.get("log", os.path.join(os.path.dirname(os.path.expanduser(manifest["env"])), "posted.log")))
    failed = False

    for item in manifest["items"]:
        if only and item["id"] != only:
            continue
        if item.get("state") != "approved":
            if only:
                print(f"{item['id']}: state is {item.get('state')!r}, only 'approved' is published")
            continue
        if not (force and only) and when(item) > now:
            if only:
                print(f"{item['id']}: its time {item['at']} has not come")
            continue
        body = text_of(item, folder)
        if PLACEHOLDER.search(body):
            print(f"{item['id']}: the text still has a [placeholder]; fill it before publishing")
            failed = True
            continue
        if item.get("reply_to") and item["reply_to"] not in results and not item["reply_to"].isdigit():
            print(f"{item['id']}: it answers {item['reply_to']}, which is not published yet")
            continue
        if dry:
            print(f"{item['id']}: would publish to {item['platform']} ({len(body)} characters, {len(item.get('media', []))} media)")
            continue

        item["state"] = "publishing"
        save(manifest, path)
        try:
            if item["platform"] == "threads":
                published, link = threads_publish(item, body, env, results)
            elif item["platform"] == "instagram":
                storage = storage or Storage(env, manifest.get("storage", {}).get("bucket", "social"))
                prefix = manifest.get("storage", {}).get("prefix", "misc")
                published, link = instagram_publish(item, body, env, storage, folder, prefix)
            else:
                raise Failure(f"no adapter for {item['platform']}")
        except (Failure, KeyError, OSError) as error:
            item["state"] = "failed"
            item["error"] = str(error)
            save(manifest, path)
            print(f"{item['id']}: failed: {error}")
            failed = True
            continue
        stamp = datetime.datetime.now().isoformat(timespec="seconds")
        item["state"] = "published"
        item["result"] = {"id": published, "permalink": link, "at": stamp}
        item.pop("error", None)
        results[item["id"]] = published
        save(manifest, path)
        with open(log_path, "a") as log:
            log.write(f"{stamp}\t{item['platform']}\t{item['id']}\t{published}\t{link}\n")
        print(f"{item['id']}: published {link}")

    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
