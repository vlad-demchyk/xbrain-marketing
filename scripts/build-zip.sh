#!/bin/sh
# Builds dist/xbrain-marketing-<version>.zip for Claude Desktop: Customize → Plugins → Add → Upload plugin.
set -eu
root=$(cd "$(dirname "$0")/.." && pwd)
version=$(python3 -c "import json;print(json.load(open('$root/.claude-plugin/plugin.json'))['version'])")
out="$root/dist/xbrain-marketing-$version.zip"
mkdir -p "$root/dist"
rm -f "$out"
cd "$root"
zip -qr "$out" .claude-plugin/plugin.json skills agents README.md LICENSE LICENSE-marketingskills LICENSE-claude-seo -x '*.DS_Store'
echo "$out"
