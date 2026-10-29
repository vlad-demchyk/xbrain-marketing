---
name: funnel-audit
description: "Maps a product's funnel with numbers (AARRR: acquisition, activation, retention, referral, revenue), finds the weakest step and picks one hypothesis to test this week. Use it on 'where am I losing users', 'why don't people pay', 'what should I improve first', 'funnel', 'conversion is low', 'де шукати конверсії', 'воронка', 'чому не купують'. For fixing a specific page, then use cro, signup, onboarding, paywalls or pricing."
metadata:
  version: 1.0.0
---

# Funnel audit

Conversion is the share of people who take the next step. Growth is rarely found by doubling
traffic; it is found at the **weakest transition**, because every step multiplies the ones after.

Read the product card first (see `product-marketing`). Reply in the user's language.

## 1. Draw the funnel with numbers

Ask for the numbers for the last 30 days (rough is fine; say which are estimates):

| Stage | Question | Measure |
|---|---|---|
| Acquisition | Where do they come from? | Visitors by channel, CTR, cost per click |
| Activation | Did they reach the first result ("aha")? | % of signups reaching it |
| Retention | Do they come back? | Return on day 1/7/30 |
| Referral | Do they bring others? | Invites per user |
| Revenue | Do they pay? | Conversion to paid, average order, LTV |

Compute each transition rate and compare with the benchmarks in `marketing-benchmarks`
(landing 6.6% median, SaaS 3.8%; trial signups 4.5%, freemium 9%; trial → paid 48.8% with card,
18.2% without, freemium 2.6%). The user's own history beats any benchmark.

## 2. The multiplication lesson

Revenue = visitors × signup × activation × payment × price. A 20% lift at any step gives the same
20% more revenue. So the question is not "which step gives more" but **"which step is cheapest to
lift by 20%"**: usually the weakest one, where simple fixes suffice, rather than buying traffic.

## 3. Where conversions usually hide

- **Broken promise**: the ad promises one thing, the page talks about another. The first screen
  repeats the ad's hook.
- **Friction**: extra fields, signup before showing value, a card "just in case".
- **No proof** next to the button: reviews, numbers, a demo.
- **No next step** after signup: an empty screen instead of a first action (see `onboarding`).
- **Wrong traffic**: cheap clicks from people who do not need it. Sometimes the right move is a
  higher cost per click.
- **Model choice**: freemium doubles signups but few pay; a card-required trial filters hard but half
  of the rest pays. Pick by where the bottleneck is.
- **Referral as a channel**: Dropbox gave 500 MB to both sides, asked at signup and near the storage
  limit; the reward was part of the product (see `referrals`).

## 4. Output

1. The funnel table with rates and the benchmark next to each.
2. The weakest transition and the evidence.
3. **One** hypothesis for this week: "If we [change], [metric] will move from X to Y, because
   [reason]." How to measure it, and when to decide (see `ab-testing` for sample size).
4. Which skill handles the fix (`cro`, `signup`, `onboarding`, `paywalls`, `pricing`, `referrals`).
