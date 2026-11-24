# Styled by People: project context

*Last updated: 21 November 2026. "Styled by People" is a working name.*

## The idea in one line

A mid-market styling game, like Drest or Covet Fashion but with affordable clothes: players style real outfits at real prices for real-life briefs, other players vote head-to-head, and every look can be saved and shopped.

**Thesis:** AI can style you, but only people can tell you it works. In a 2026 survey, only 2% of young Americans trust AI for fashion advice, while 34% trust friends.

**Goal:** a real business, not a side project. Validate demand cheaply before building.

---

## Audience

- **Core:** US women aged 18–30, plus people new to fashion who can't afford a stylist and fans of styling games.
- **Wedge:** 18–24-year-olds starting their first jobs (94% of Gen Z look for work-outfit advice).
- **Spenders:** 25–30-year-olds.
- **Secondary:** men, reached through menswear and gender-neutral briefs.
- **Launch:** 18+ (or a 17+ store rating), US first, then the UK, Canada and Australia. A teen mode comes later, set up separately.

---

## Game design decisions

### Core loop
1. Get a brief (client, body, goal, occasion, budget).
2. Style the client from real items.
3. Enter the challenge (costs Tags).
4. Other players vote A vs B.
5. Results appear when the challenge ends, as stars.
6. Save and shop the look.

### Challenges
- Daily, weekly, real-world events and seasons, plus "recreate the trend" challenges.
- **Not every challenge has a budget cap.**
- **The body type comes from the client brief, not the player.** Briefs describe goals ("wants to look taller") rather than labels ("pear shape").
- Use theme names, not trademarks: "Desert festival," "Gala night," "The look for under $150." No celebrity or designer names.

### Currencies
| Currency | Used for | How you get it |
|---|---|---|
| **Coins** | Clothes. Pegged 1:1 to real prices ($45 item = 45 coins) | Prizes, coin packs |
| **Tags** | Challenge entry | Daily check-in, voting, tag packs |

Tags rules (numbers still to finalize):
- **5 tags** to enter a challenge
- **Daily check-in** gives x tags (placeholder 10)
- **Storage cap** of y tags (placeholder 30). Bought tags can go above the cap
- **Every 3 votes** earn tags (placeholder 5). If you're full, earned tags wait until there's room
- Keep the daily gift low enough that voting and packs still matter

### Voting
- **A vs B head-to-head**, in its own **Vote tab**, available anytime.
- After voting, both looks' **current star ratings** appear ("may change before the challenge ends").
- **Results only when the challenge ends.** Players see **stars only**: head-to-head wins convert to stars behind the scenes.
- **Never sell anything that affects votes** (no paid boosts, multipliers or extra votes).
- Fairness ideas: more weight for trusted voters, no downvotes.

### Challenge theme items (decided 23 Nov 2026)
- Each challenge requires **at least 1–2 theme items** in the look to qualify (for example, "Workwear" items for the interview challenge).
- Theme items must be owned to submit, like any other item.
- Still open: how many qualifying items per theme (several to choose from, at different prices); whether a free or loaned option exists; whether sponsored brand items can be theme items.

### Daily "Today's Rack" (decided 23 Nov 2026)
- A free daily section with **open inventory**: anyone can try **any** item on the model, with no Tags and no budget walls.
- Looks can be saved, shared and shopped (Buy links). Light feedback (likes), not ranked votes.
- **Trying is not owning:** to use an item in a challenge you must buy it with coins (or unlock or win it).
- Purpose: a generous start, a reason to come back daily, a home for shoppers who don't want to play (Advait's view), and a "try before you buy" step that makes players want items for challenges (Samruddhi's view).
- Rule: never reward clicking Buy links.
- Still open: a small daily reward or streak; which body the player styles; a daily prompt; whether the newest drops appear here immediately or after a delay.

### Items and closet
- **Limited wears** per item (teaches cost per wear); basics last longer than trend pieces.
- An owned item stays in your closet until its wears run out.

### Progression and retention
- More votes → more prizes → stylist rank → brand unlocks.
- Daily and weekly challenges, real-world event tie-ins, level unlocks, daily check-in.

### Onboarding
A guided first challenge, step by step, with a free first entry.

### Social
Strangers at launch. Friends plus "borrow from a friend" in V2.

### Profile
An optional persona or stylist name.

### Avatar
- **Long-term direction:** an illustrated 2D avatar (Covet's approach): an artist draws base bodies and every item per body, possibly sped up with AI.
- **Current mockup:** **Gemini-generated photoreal looks**, one image per top + trousers combination, on a consistent model.
- **Pre-generate, don't generate live:** each item is made once per body ahead of time; the game just shows or layers images.

### V2 and later
- Style your real closet
- Friends and borrowing
- An optional "render my look" for sharing

---

## Business model

| Stream | Role | Notes |
|---|---|---|
| **In-app purchases** | Main revenue | Coin packs, tag packs, a $4.99 monthly card, a $9.99 season pass, cosmetics. Web packs start at $4.99 |
| **Brand-sponsored challenges** | Second | Start with free "exposure for items" swaps (Covet's model) |
| **Affiliate links** | Small | Mostly proof of clicks for brand pitches |
| **Trend data** | Later, at scale | Aggregated and anonymous; never individual or under-18 data |

**Growth:** paid micro-creators first (about $5–15K per wave of 10), then organic "my closet" and "10 things under $200" posts. Reward **referrals**, never posts. Linking social accounts for free tags still needs a policy check.

**Brands:** small mid-market labels first (Princess Polly, Oh Polly, Edikted, Good American). **Avoid Shein.**

---

## Key research findings

- **Open lane:** no game combines real affordable clothes, real prices, body-based briefs and player voting.
- **Need:**
  - 94% of Gen Z report the "nothing to wear" feeling (survey sample unverified).
  - 58% of US shoppers have bought a dupe.
  - Stylists cost $75–350 an hour.
- **Competitors:**
  - Covet Fashion is declining (about $8–12M a year in the US, estimated).
  - Drest moved to luxury brand sponsorships.
  - Dress to Impress proved voting goes viral, but spite-voting is its top complaint.
- **Money:** in-app purchases earn about $0.50–4.50 per engaged player a month, against $0.01–0.11 from affiliate links (estimates).
- **Market size (US):**
  - TAM: $26.7B in US mobile game spending.
  - SAM: about 3.5M likely players, worth $21–189M a year.
  - SOM: 100–250K players, worth $0.6–13.5M a year.
- **Platform:**
  - A mobile web prototype first.
  - A native app once retention is proven (94% of phone time is in apps).
  - Roblox only as a side experiment: it blocks affiliate links.
- **Benchmarks to beat:** the median game keeps under 1% of players at day 30; the top 10% keep about 4%.
- **Legal (not legal advice):**
  - Brands must opt in before their product images are modified.
  - Event names and "dupe" claims are actively litigated.
  - Launching 18+ keeps compliance manageable.

---

## Plan

1. **Phase 1, weeks 1–8:** a TikTok and Instagram challenge account ("the look for under $X"), plus one creator wave and outreach to 10 small brands.
   - Go if: ~1,000 engaged followers, 50+ submissions per challenge, 3 interested brands.
2. **Phase 2, weeks 8–16:** a mobile web prototype with 200 players.
   - Go if: day-30 retention near 4%.
3. **Phase 3:** a game-design cofounder, a legal review, a native app, and a pre-seed raise.

The founder prefers desk research over customer interviews; the live TikTok test replaces interviews.

---

## Files in this folder

| File | What it is |
|---|---|
| `styled-by-people.html` | Pitch report (also published privately as an artifact: https://claude.ai/artifact/KhRYFQGqzjA6Vmm6dTAS7M) |
| `mockup-src.html` | Mockup source. **Edit this one** |
| `build-mockup.py` | Embeds images into the mockup. Run `python build-mockup.py` after edits or new images |
| `styled-by-people-mockup.html` | Built mockup (local only; contains Amazon product photos, so don't publish) |
| `mockup-images/` | Product photos, the base model and generated outfits |
| `context.md` | This file |
| `research/` | Copies of both research reports and their notes |

**GitHub (private):** https://github.com/IamKoham/styled-by-people. The `main` branch is a README for now; all materials are on `project-materials`.

Research reports (one folder up):
- `../reports/Mid market styling game landscape.md`
- `../reports/Styling game demand and platform.md`

---

## Current mockup: First Job Interview challenge

- **Client:** Maya, 5'1", petite. Goal: look polished and a little taller. Budget: $65.
- **Items:** 3 tops and 2 trousers from Amazon. **The prices are placeholders.**

| ID | Item | Image | Placeholder price | Amazon link |
|---|---|---|---|---|
| t1 | Floral ruffle pleated blouse | `interview-top-1.jpg.jpg` | $26 | https://www.amazon.com/dp/B0BZ4WLVR8 |
| t2 | Rust mock-neck pleated blouse | `interview-top-2.jpg` | $30 | https://www.amazon.com/dp/B0F7RPXRK2 |
| t3 | Navy sleeveless mock-neck knit | `interview-top-3.jpg` | $24 | https://www.amazon.com/dp/B0HDSXHBBM |
| b1 | Brown high-waist pleated wide-leg trousers | `interview-bottom-1.jpg` | $36 | https://www.amazon.com/dp/B0HC674XY3 |
| b2 | Black high-waist pleated wide-leg trousers | `interview-bottom-2.jpg` | $34 | https://www.amazon.com/dp/B0DN67RR2Z |

- **Where players can buy in the mockup:** a "Buy on Amazon" link under every item card while styling, and a "Shop this look" list right after entering, in My looks while waiting, and on the results.
- **Images:** all 6 combinations generated in Gemini (`Outfit1`, `outfit 2`–`outfit 6`), plus `Base model.webp`.
- **Tabs:** Challenges, Vote, My looks. Includes the daily check-in, store and demo tools (simulate next day, reset).
- **Amazon is blocked in the founder's Chrome site permissions**, so product pages can't be read automatically.

---

## Open questions

1. Real prices for the 5 interview items
2. Final tag numbers: daily gift, cap, voting reward
3. When voting happens relative to entering (still being discussed)
4. Next two challenges: festival and quiet luxury, or new ideas
5. Base model consistency (its face differs slightly from the outfit images)
6. Final product name
7. Brand strategy and image permissions
8. Whether linking social accounts for rewards is allowed on each platform
9. Illustrator test: style, cost per item, number of base bodies
