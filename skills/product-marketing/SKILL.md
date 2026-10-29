---
name: product-marketing
description: "Creates and updates a product's card: positioning, audience, alternatives, narrative, proof and voice, the context every other xbrain-marketing skill reads. Use it when the user wants to create or update their product marketing context document. Also use when the user mentions 'product context,' 'marketing context,' 'set up context,' 'positioning,' 'who is my target audience,' 'describe my product,' 'ICP,' 'ideal customer profile,' or wants to avoid repeating foundational information across marketing tasks. Use this at the start of any new project before using other marketing skills — it creates the product card that all other skills reference for product, audience, and positioning context."
metadata:
  version: 2.0.0
---

# Product Marketing Context

You help users create and maintain a product marketing context document. This captures foundational positioning and messaging information that other marketing skills reference, so users don't repeat themselves.

The document is the **product card**. One card per product.

## Where the product card lives

Use the first place that applies, and tell the user which one you used:

1. **The brain** (XBrain tools connected, e.g. `note_read`, `search`): the note `Projects/<project>/Marketing/product-marketing.md` of the product's project. Find the project with `session_info`; read with `note_read`, change it by sections.
2. **A working folder** (Cowork or Claude Code with file access): `marketing/<product-slug>/product-marketing.md` in that folder.
3. **Chat only** (no files, no brain): look for the card in the Claude project's knowledge. If it is not there, produce the card as one Markdown document and ask the user to add it to the project's knowledge, so the next chats see it.

Several products: each has its own card; ask which product the task is about when it is not obvious.

## Workflow

### Step 1: Check for Existing Context

First, check the places above for an existing card. Also check older locations (`.agents/product-marketing.md`, `.claude/product-marketing.md`, `product-marketing-context.md`); if a card is found there, offer to move it to the place above.

**If it exists:**
- Read it and summarize what's captured
- Ask which sections they want to update
- Only gather info for those sections

**If it doesn't exist, offer two options:**

1. **Auto-draft from what exists** (recommended): You'll study what is available (the repo or working folder, the live site via web fetch, the brain's project notes) and draft a V1 of the context document. The user then reviews, corrects, and fills gaps. This is faster than starting from scratch.

2. **Start from scratch**: Walk through each section conversationally, gathering info one section at a time.

Most users prefer option 1. After presenting the draft, ask: "What needs correcting? What's missing?"

### Step 2: Gather Information

**If auto-drafting:**
1. Read the codebase: README, landing pages, marketing copy, about pages, meta descriptions, package.json, any existing docs
2. Draft all sections based on what you find
3. Present the draft and ask what needs correcting or is missing
4. Iterate until the user is satisfied

**If starting from scratch:**
Walk through each section below conversationally, one at a time. Don't dump all questions at once.

For each section:
1. Briefly explain what you're capturing
2. Ask relevant questions
3. Confirm accuracy
4. Move to the next

Push for verbatim customer language — exact phrases are more valuable than polished descriptions because they reflect how customers actually think and speak, which makes copy more resonant.

---

## Sections to Capture

### 1. Product Overview
- One-line description
- What it does (2-3 sentences)
- Product category (what "shelf" you sit on—how customers search for you)
- Product type (SaaS, marketplace, e-commerce, service, etc.)
- Business model and pricing

### 2. Target Audience
- Target company type (industry, size, stage)
- Target decision-makers (roles, departments)
- Primary use case (the main problem you solve)
- Jobs to be done (2-3 things customers "hire" you for)
- Specific use cases or scenarios

### 3. Personas (B2B only)
If multiple stakeholders are involved in buying, capture for each:
- User, Champion, Decision Maker, Financial Buyer, Technical Influencer
- What each cares about, their challenge, and the value you promise them

### 4. Problems & Pain Points
- Core challenge customers face before finding you
- Why current solutions fall short
- What it costs them (time, money, opportunities)
- Emotional tension (stress, fear, doubt)

### 5. Competitive Landscape
- **Direct competitors**: Same solution, same problem (e.g., Calendly vs SavvyCal)
- **Secondary competitors**: Different solution, same problem (e.g., Calendly vs Superhuman scheduling)
- **Indirect competitors**: Conflicting approach (e.g., Calendly vs personal assistant)
- How each falls short for customers

### 6. Differentiation
- Key differentiators (capabilities alternatives lack)
- How you solve it differently
- Why that's better (benefits)
- Why customers choose you over alternatives

### 7. Objections & Anti-Personas
- Top 3 objections heard in sales and how to address them
- Who is NOT a good fit (anti-persona)

### 8. Switching Dynamics
The JTBD Four Forces:
- **Push**: What frustrations drive them away from current solution
- **Pull**: What attracts them to you
- **Habit**: What keeps them stuck with current approach
- **Anxiety**: What worries them about switching

### 9. Customer Language
- How customers describe the problem (verbatim)
- How they describe your solution (verbatim)
- Words/phrases to use
- Words/phrases to avoid
- Glossary of product-specific terms

### 10. Brand Voice
- Tone (professional, casual, playful, etc.)
- Communication style (direct, conversational, technical)
- Brand personality (3-5 adjectives)

### 11. Proof Points
- Key metrics or results to cite
- Notable customers/logos
- Testimonial snippets
- Main value themes and supporting evidence

### 12. Positioning (April Dunford, "Obviously Awesome")
Work through it in this order, each answer built on the previous one:
1. **Competitive alternatives**: what customers would do if the product did not exist (often a spreadsheet, a freelancer, a habit, or doing nothing).
2. **Unique attributes**: facts the alternatives lack, not adjectives.
3. **Value**: what each attribute gives the customer ("sync in 1 s" → "the team never loses edits").
4. **Best-fit customers**: who gets the most value and buys fastest.
5. **Market category**: the frame in which the value is obvious. A new category is tied to a known one ("like X, but for Y").

Then one positioning statement: *For [segment] who [situation], [product] is a [category] that [main value]. Unlike [alternative], we [proof of difference].*

### 13. Strategic Narrative
Five sentences, the product appears only in the last: the change in the world; winners and losers of that change; the promised land; the obstacles; the proof that this product gets people there. Add one contrarian claim the category would disagree with.

### 14. Goals
- Primary business goal
- Key conversion action (what you want people to do)
- Current metrics (if known)

---

## Step 3: Create the Document

After gathering information, create the product card (see "Where the product card lives") with this structure:

```markdown
# Product Marketing Context

*Last updated: [date]*

## Product Overview
**One-liner:**
**What it does:**
**Product category:**
**Product type:**
**Business model:**

## Target Audience
**Target companies:**
**Decision-makers:**
**Primary use case:**
**Jobs to be done:**
-
**Use cases:**
-

## Personas
| Persona | Cares about | Challenge | Value we promise |
|---------|-------------|-----------|------------------|
| | | | |

## Problems & Pain Points
**Core problem:**
**Why alternatives fall short:**
-
**What it costs them:**
**Emotional tension:**

## Competitive Landscape
**Direct:** [Competitor] — falls short because...
**Secondary:** [Approach] — falls short because...
**Indirect:** [Alternative] — falls short because...

## Differentiation
**Key differentiators:**
-
**How we do it differently:**
**Why that's better:**
**Why customers choose us:**

## Objections
| Objection | Response |
|-----------|----------|
| | |

**Anti-persona:**

## Switching Dynamics
**Push:**
**Pull:**
**Habit:**
**Anxiety:**

## Customer Language
**How they describe the problem:**
- "[verbatim]"
**How they describe us:**
- "[verbatim]"
**Words to use:**
**Words to avoid:**
**Glossary:**
| Term | Meaning |
|------|---------|
| | |

## Brand Voice
**Tone:**
**Style:**
**Personality:**

## Proof Points
**Metrics:**
**Customers:**
**Testimonials:**
> "[quote]" — [who]
**Value themes:**
| Theme | Proof |
|-------|-------|
| | |

## Positioning
**Statement:**
**Alternatives:**
**Unique attributes → value:**
**Best-fit customers:**
**Category:**

## Narrative
1. Change:
2. Winners and losers:
3. Promised land:
4. Obstacles:
5. Proof:
**Contrarian claim:**

## Channels
**Primary platforms (1-2):**
**Content pillars:**
**Profile call to action / lead magnet:**

## Goals
**Business goal:**
**Conversion action:**
**Current metrics:**
```

---

## Step 4: Confirm and Save

- Show the completed document
- Ask if anything needs adjustment
- Save it where the card lives (brain note, working folder, or hand it over for the project's knowledge)
- Tell them: "Other marketing skills will now use this context automatically. Run this skill again any time to update it."

---

## Tips

- **Be specific**: Ask "What's the #1 frustration that brings them to you?" not "What problem do they solve?"
- **Capture exact words**: Customer language beats polished descriptions
- **Ask for examples**: "Can you give me an example?" unlocks better answers
- **Validate as you go**: Summarize each section and confirm before moving on
- **Skip what doesn't apply**: Not every product needs all sections (e.g., Personas for B2C)
