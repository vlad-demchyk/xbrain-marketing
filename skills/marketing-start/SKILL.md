---
name: marketing-start
description: "The entry point of xbrain-marketing: starts marketing for a product and runs the 30-day plan (foundation, funnel, content, amplification), saying which skill or agent handles each step. Use it on 'start marketing for my product', 'where do I begin', 'marketing plan', '30-day plan', 'what should I do this week in marketing', 'почнімо маркетинг', 'з чого почати', 'план на 30 днів'."
metadata:
  version: 1.0.0
---

# Marketing start

The chain: **to whom and why you are valuable** (positioning) → **how they learn about it**
(narrative, attention, ads, social) → **how interest becomes money** (conversion, sales). Reply in
the user's language; write public content in the audience's language.

## Step 0. Which product, which card

Ask which product, unless it is clear. Look for its card (see `product-marketing`, "Where the product
card lives"). No card: start there, the whole plan depends on it.

## The 30-day plan

Track the boxes where the card lives (a `plan.md` next to it, or the brain's task for the product).
Each step names its skill.

### Week 1. Foundation
- [ ] 3–5 conversations with potential customers on JTBD questions; keep verbatim phrases
  (`customer-research`). Questions: what happened that you started looking now? what did you try and
  why did it not fit? what does success look like in 3 months? what if nothing changes?
- [ ] Positioning statement, tested on 3 people: can they retell what it is and for whom
  (`product-marketing`, section Positioning).
- [ ] The five-part narrative and one contrarian claim (`product-marketing`, section Narrative).
- [ ] A proof portfolio: 3 claims, 3 proofs, where each is shown (`product-marketing`, Proof Points).

### Week 2. Funnel
- [ ] The funnel with numbers and its weakest step (`funnel-audit`).
- [ ] The landing's first screen: the positioning's promise, one proof, one button (`cro`,
  `copywriting`).
- [ ] A lead magnet in the profiles (`lead-magnets`, `free-tools`).
- [ ] No dark patterns in signup, pricing, cancellation (`trust-check`).

### Week 3. Content
- [ ] Two platforms and 3–4 content pillars (`platform-pack`).
- [ ] Ten hooks and three short videos with subtitles (`hook-lab`, `video`).
- [ ] Two carousels (`platform-pack`, the `carousel-designer` agent).
- [ ] 20 minutes a day of replies and comments in the niche.
- [ ] Three useful answers in a relevant subreddit, no self-promotion (`platform-pack` Reddit,
  `community-marketing`).

### Week 4. Amplify and measure
- [ ] The best organic post as a small paid test (`ads`, `ad-creative`).
- [ ] A test collaboration with 1–2 micro creators, with rights to use the content in ads.
- [ ] The AI visibility probe (`geo-check`).
- [ ] The weekly review and the next hypothesis (`weekly-review`).

## Other skills in this plugin

| Need | Skill |
|---|---|
| Numbers to cite | `marketing-benchmarks` |
| Research, competitors | `customer-research`, `competitors` |
| Writing and editing | `copywriting`, `copy-editing`, `emails` |
| Social and video | `social`, `platform-pack`, `hook-lab`, `video`, `image` |
| Ads | `ads`, `ad-creative` |
| Conversion | `cro`, `signup`, `onboarding`, `pricing`, `paywalls`, `churn-prevention`, `ab-testing`, `analytics` |
| Growth loops | `launch`, `referrals`, `lead-magnets`, `free-tools`, `community-marketing`, `public-relations`, `directory-submissions` |
| App stores | `aso` |
| Psychology | `marketing-psychology` |
| Content and SEO | `content-strategy`, `seo-plan`, `seo-audit`, `seo-page`, `seo-content`, `seo-content-brief`, `seo-schema`, `seo-sitemap`, `seo-hreflang`, `seo-competitor-pages` |
| AI search | `ai-seo`, `geo-check` |
| Trust | `trust-check` |

## Agents (Cowork and Claude Code only)

`copywriter`, `video-scripter`, `carousel-designer`, `community-scout`, `marketing-analyst`. Use one
when the user asks to delegate a piece of work; one at a time, and bring its result back to the user.
