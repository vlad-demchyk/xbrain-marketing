# XBrain Marketing

One plugin for marketing and SEO of your own products. Built for Claude Desktop (Cowork and chat);
the same plugin installs in Claude Code.

Start with the `marketing-start` skill: it asks which product, creates its product card and walks the
30-day plan.

## What is inside

**Own skills** (from the book «Основи маркетингу і продажу», data as of October 2026):

| Skill | What it does |
|---|---|
| `marketing-start` | Entry point and the 30-day plan |
| `marketing-benchmarks` | Numbers with sources; refreshes them on request |
| `platform-pack` | Platform choice and playbooks: LinkedIn, Instagram, Threads, Reddit, TikTok |
| `hook-lab` | Ten hooks, short-video scripts, AIDA / PAS / Before-After-Bridge |
| `funnel-audit` | AARRR funnel with numbers, the weakest step, one hypothesis |
| `trust-check` | Dark patterns, disclosure, promise match, awareness stages |
| `geo-check` | Is the product mentioned in AI answers, and which sources to earn |
| `weekly-review` | Weekly numbers, what worked, next hypothesis |

**Selected from [marketingskills](https://github.com/coreyhaines31/marketingskills)** (Corey Haines,
MIT), with the product context moved to the product card: `product-marketing` (extended with
positioning and narrative), `customer-research`, `competitors`, `copywriting`, `copy-editing`,
`social`, `video`, `image`, `ad-creative`, `ads`, `cro`, `signup`, `onboarding`, `pricing`,
`paywalls`, `churn-prevention`, `launch`, `referrals`, `lead-magnets`, `free-tools`,
`community-marketing`, `content-strategy`, `emails`, `public-relations`, `directory-submissions`,
`analytics`, `ab-testing`, `aso`, `ai-seo`, `seo-audit`, `marketing-psychology`.

**Selected from [claude-seo](https://github.com/AgriciDaniel/claude-seo)** (AgriciDaniel, MIT), only
the skills that need no Python scripts or local servers: `seo-plan`, `seo-page`, `seo-content`,
`seo-content-brief`, `seo-schema`, `seo-sitemap`, `seo-hreflang`, `seo-competitor-pages`.

**Agents** (Cowork and Claude Code; greyed out in plain chat): `copywriter`, `video-scripter`,
`carousel-designer`, `community-scout` (read-only), `marketing-analyst`. None of them publishes
anything.

## Where the product card lives

1. The brain, when XBrain tools are connected: `Projects/<project>/Marketing/product-marketing.md`.
2. A working folder: `marketing/<product>/product-marketing.md` (drafts, research, visuals and
   reviews go next to it).
3. Chat only: the Claude project's knowledge.

## Install

**Claude Desktop** (Cowork and chat): Customize → Plugins → Add → **Add marketplace**, enter
`vlad-demchyk/xbrain-marketing`, then install **xbrain-marketing**. Updates come from this repository.
Without a marketplace: download the zip from the
[releases](https://github.com/vlad-demchyk/xbrain-marketing/releases) (or build it with
`scripts/build-zip.sh`) and use Customize → Plugins → Add → Upload plugin. Start a new task for the
plugin to load.

**Claude Code**:

```sh
claude plugin marketplace add vlad-demchyk/xbrain-marketing
claude plugin install xbrain-marketing@xbrain-marketing
```

Plugins added in Claude Desktop also sync to Claude Code; disable it there with
`claude plugin disable xbrain-marketing@xbrain-marketing` if you work on marketing only in Desktop.

**Releases**: raise `version` in `.claude-plugin/plugin.json`, check with `claude plugin validate .`,
build the zip with `scripts/build-zip.sh` and attach it to a GitHub release.

The brain (XBrain) is optional: with its tools connected the product card lives in the brain,
otherwise in the working folder or the Claude project's knowledge.

## Licenses

MIT. Third-party skills keep their authors' copyright: see `LICENSE-marketingskills` and
`LICENSE-claude-seo`.
