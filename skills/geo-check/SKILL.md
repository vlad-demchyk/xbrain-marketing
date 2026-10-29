---
name: geo-check
description: "A quick visibility probe in AI answers: asks the questions buyers ask (best X for Y, X vs Z, alternatives to Z), records whether ChatGPT, Perplexity, Gemini or Google AI Overviews mention the product, who they mention instead and which sources they cite, then lists the sources to earn. Use it on 'do AI assistants recommend us', 'are we in ChatGPT answers', 'GEO check', 'чи згадує нас ШІ', 'перевір GEO'. For optimizing pages for AI citation, see ai-seo."
metadata:
  version: 1.0.0
---

# GEO check

Before buying, people ask AI assistants, and the assistants cite reviews, comparisons, discussions
and media more than brand sites: 82% of cited links are earned media (Muck Rack, Dec 2025); only 12%
of cited URLs rank in Google's top 10 (Ahrefs, Aug 2025). To be recommended, the product needs to be
**mentioned in other people's sources**. Reply in the user's language.

## 1. Questions

From the product card (see `product-marketing`) write 8–12 buyer questions in the audience's
language: "best [category] for [segment]", "[competitor] alternatives", "[product] vs
[competitor]", "how to [job to be done]", "is [product] good for [use case]".

## 2. Probe

- With web search available: search each question and read the AI answers and the pages they draw
  on where the tool shows them.
- The assistants themselves (ChatGPT, Perplexity, Gemini, AI Overviews) are outside this
  conversation: give the user the question list to run, or use a connector if one is configured.
  Never claim to have asked an assistant you could not reach.

Record per question and engine: mentioned (yes/no, position), competitors named, sources cited.

## 3. Read the result

- Which competitors are named most, and on which sources they appear.
- The source types that dominate (Reddit threads, review sites, listicles, YouTube, media).
- Shares swing month to month (Reddit in ChatGPT answers fell from ~60% to ~10% in six weeks of
  2025), so spread presence; re-run monthly.

## 4. Output

1. The table of results.
2. The 10 sources worth earning a mention in, ordered by how often they are cited, with the path
   to each (answer a thread, pitch a listicle author, submit to a directory (`directory-submissions`),
   a guest post (`public-relations`), a comparison page (`seo-competitor-pages`)).
3. Page fixes for citation readiness: hand over to `ai-seo`.
4. The date, to re-run in a month.
