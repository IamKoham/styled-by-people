# Architecture decisions

*Started 25 November 2026. A running log of tech-design decisions made in architect and PM sessions. Read `context.md` on the `project-materials` branch for the product concept.*

**How to read this:** each decision has an ID, what was decided, why, and what it means for the build. Parked items and pending questions are at the end. Cost figures are rough estimates, not quotes.

---

## Summary

| ID | Area | Decision |
|---|---|---|
| D1 | North star | Long-term product is a social commerce platform (B), with a human styling network (C) as a later option. The game (A) is the path to distribution |
| D2 | Catalog | Every item is a real product record with a game layer on top, never a game-only asset |
| D3 | Catalog | No price comparison, multi-retailer listings or stock tracking. One brand, one Buy link per item |
| D4 | Catalog | Coin cost is locked at listing. The Buy button says "See current price". Weekly automated dead-link check |
| D5 | Catalog | Launch at Boutique size (~300 wearable items, ~30 new a week), designed to grow to Store size (~3,000, ~300 a week). No Marketplace |
| D6 | Art | Avatar art is AI-generated from day one (no hand illustration), with automated and human quality checks, in its own pipeline service |
| D7 | Rendering | Layered avatar everywhere: styling, voting, results, sharing and Shop the look. Photoreal render is a possible V2 extra only |
| D8 | Bodies | 3 launch bodies (petite, mid-size, plus), with skin tone, hair and face as free layers. Every image tagged with a body ID |
| D9 | Bodies | The AI fits each garment to the base body. No size modelling |
| D10 | Bodies | "Styling preview" label, and items are hidden on bodies outside the brand's size range |
| D11 | Challenges | Submissions close before voting opens (no overlap) |
| D12 | Challenges | Staggered calendar: a daily challenge every day, one weekly challenge, 1–2 event challenges a month |
| D13 | Challenges | Series: linked challenges with one story, running in the daily or weekly slot |
| D14 | Rewards | Every challenge pays rewards. Entering every episode of a series earns a bigger completion bonus |
| D15 | Rewards | All rewards are in-game only (coins, items, Tags, cosmetics, badges) |
| D16 | Voting | No Skip. Every pair needs a pick |
| D17 | Voting | The system serves one challenge at a time to vote on. Players can't browse challenges |
| D18 | Voting | No penalty for voting against the crowd. Only mechanical abuse is filtered |
| D19 | Voting | Voters never see their own look |
| D20 | Voting | Entrants can vote in their own challenge. Drift is measured, not punished |
| D21 | Voting rewards | Voting pays Tags only. Tags come from the daily gift, voting, or buying (with coins or real money) |
| D22 | Stars | % of head-to-heads won maps to stars by fixed thresholds. The percentage is never shown to players |

---

## North star

### D1. Build toward social commerce, through a game
- **Decision:** the five-year product is **B, a social commerce platform** where the game is how people discover clothes, and the moat is "people-verified style" data and brand relationships. **C, a human styling network** (top players paid to style real customers), stays an option. **A, the game**, is how we build distribution first.
- **Why:** in-app purchases earn far more per player at launch, but the thesis ("only people can tell you it works") points beyond a game.
- **What it means for the build:**
  1. The product record is the core of the data model, and the game is a layer on top (see D2).
  2. Every interaction is logged as data from day one: try-ons, swaps, votes, saves, Buy-link clicks, abandoned looks.
  3. **Stylist reputation is its own system, separate from game rank.** Game rank can reset each season. A stylist's track record (win rate by brief type, body and budget) never resets, because it's the CV for option C.

---

## Catalog and items

### D2. Items are real products with a game layer
- **Decision:** every item is stored as a real product (brand, Buy link, price at listing, simple tags such as category, style and colour). Game data sits on top (avatar art per body, coin cost, wears).
- **Why:** it lets votes become commerce and brand signals ("this blouse won 71% of its head-to-heads on petite bodies in interview briefs") without rebuilding the core later.
- **What it means for the build:** items enter through a product intake flow, not as manually added game content. The tags are what make the data useful.

### D3. Keep commerce light
- **Decision:** no price comparison, no "where is it cheaper", no multi-retailer listings, no live stock tracking. One brand and one Buy link per item, from the brand or its chosen retailer.
- **Why:** price comparison works against brand loyalty and sponsorship, and tracking stock and accuracy across retailers is costly and makes us responsible for errors. The goal is: style, have fun, get validation, buy if you want.

### D4. Pricing and link rules
- **Decision:**
  - The coin cost is **locked when the item is listed** (pegged 1:1 to the price at listing), so the game economy stays stable during challenges.
  - The Buy button says **"See current price"**, so we never show a stale price as if it's live.
  - An **automated weekly check** finds dead Buy links and hides the Buy button. The item stays playable in closets.

### D5. Boutique first, designed for Store
- **Decision:** launch with **~300 wearable items and ~30 new a week**. The pipeline is designed to scale to **~3,000 items and ~300 a week**. A Marketplace (30,000+ items, everything wearable) is ruled out.
- **Why:** a curated rack suits the product and makes brand rights simpler. A Marketplace would be messy and drift into "we're a store".
- **What it means for the build:** growing is a change in volume only, so the pipeline and data model don't change.

---

## Art and rendering

### D6. AI-generated art in its own pipeline
- **Decision:** avatar art is **AI-generated from launch**. There's no hand illustration. Quality checks are built in, and the art pipeline is a separate service.
- **Pipeline:**
  ```
  Product photos
    → AI generates the item on each base body (and each variant, such as tucked)
    → Automated checks (colour matches the product, aligned to the pose, no AI artefacts)
    → Human review (approve / regenerate / reject)
    → Brand approval (optional at first, required for sponsored items)
    → Published to the catalog
  ```
- **Open:** where the input photos come from and what rights we need. See P1.

### D7. Layered avatar everywhere
- **Decision:** looks are built by stacking pre-approved transparent images on a fixed pose. Players see the **layered avatar in voting, results, sharing and Shop the look**.
- **Why:** every look is judged on the same reviewed art, so votes reflect styling, not render luck. There's no per-look cost and nothing to check at vote time. Cost grows with items, not combinations.
- **What it means for the build:**
  - Fixed layer order: `body → base → bottoms → tops (tucked or untucked) → outerwear → shoes → accessories → hair`.
  - Each item records its **slot**, its **layer order** and the **variants it needs**.
  - Share cards and results are made by flattening the stack into one image.
  - The photoreal "render my look" stays a possible V2 extra.

### D8. Three launch bodies
- **Decision:** launch with **petite, mid-size and plus**. Skin tones, hair and faces vary as body layers at almost no art cost. One front-facing pose. Taller, curvier and menswear bodies come later.
- **Why:** body positivity is core to the pitch ("model photos look great because they're models; here you see it on a body like yours"), and 3 bodies keeps generation and review manageable (~90 images a week at Boutique size).
- **What it means for the build:**
  - Every art image carries a body ID from day one, so adding bodies only means more generation.
  - In challenges, the brief sets the body. In Today's Rack, the player picks the body closest to their own.

### D9. The AI fits garments to the body
- **Decision:** the AI fits each garment to the base body. We don't model sizes or decide whether the model wears S, M or L.

### D10. Honesty safeguards for fit
- **Decision:**
  - Every look shows a **"Styling preview. Check the brand's size guide."** label.
  - Each item stores the **sizes the brand sells**, and is hidden on bodies outside that range.
- **Why:** every image shows a perfect fit, so these protect the body-positivity promise when a player taps Buy.

---

## Challenge lifecycle

### D11. Submit first, then vote
- **Decision:** a challenge's submission window closes before its voting window opens.
- **Why:** it's fair (every entry gets the same voting window) and **players can't copy looks** they've seen in the Vote tab.
- **What it means for the build:** challenge state machine `scheduled → open for submissions → voting → tallying → results`. Overlapping challenges keep the Vote tab busy.
- **Still to decide:** the minimum number of head-to-heads per entry (proposal: 20). If votes fall short, lengthen the voting window rather than lower the minimum.

### D12. Staggered calendar
- **Decision (assumed, confirm):**
  - **Daily challenge, every day:** 24h submit, then 24h vote. Each day a player has one look to style, one challenge to vote on and one set of results.
  - **Weekly challenge:** Mon–Fri submit, Sat–Sun vote, results Monday. This is the bigger prize and the future sponsored slot.
  - **Event challenges:** 1–2 a month, tied to real moments (graduation, festival season, wedding season).
  - **Today's Rack:** daily free play, no submission or voting.
- **Team load:** about 8 briefs a week from a template (client, body, occasion, budget, goal). Theme items come from the weekly drop, so drops are planned around upcoming challenges, and theme tags (for example "Workwear") are reused.
- **Volume check at Phase 2 (200 players):** a daily challenge with ~40 entries × 20 head-to-heads ÷ 2 ≈ 400 votes in 24h, about 2 votes per player per day.

### D13. Series
- **Decision:** challenges can be linked in a **series**: one client and one story across several episodes, run in the daily slot (one episode a day, e.g. "First Job Week") or the weekly slot (one a week, e.g. "Wedding Season").
- **Why:** shows off limited wears and cost per wear, adds a reason to come back, makes a bigger sponsored package, and cuts brief-writing cost.
- **What it means for the build:** each episode is a normal challenge. The series is a layer on top with a series score, a completion bonus and optional rules (for example "no repeating the full outfit").

### D14. Rewards per challenge, bigger rewards for a full series
- **Decision:** every challenge gives its own rewards (coins, items, Tags) based on stars. Entering **every episode** of a series earns a bigger completion bonus. Missing an episode keeps what was already won but loses the series bonus.

### D15. In-game rewards only
- **Decision:** all rewards are in-game: coins, items, Tags, cosmetics, badges. No real money, gift cards or physical prizes.
- **Why:** Tags can be bought, so real prizes would make challenges paid-entry contests with prizes decided by player vote, which is regulated across US states.
- **Later:** real prizes only in brand-sponsored challenges with free entry and official rules, after legal review.

---

## Voting and ranking

### Voting flow (draft, agreed in principle)
1. The player opens the Vote tab and the system serves the next pair from **one challenge** (D17).
2. The brief is at the top (client, body, occasion, budget, goal). Voters judge against the brief.
3. Two anonymous looks on the same body, as layered avatars, each showing total price against budget. No usernames or ranks.
4. The player taps one. No Skip (D16), no downvote.
5. Both looks' current stars appear ("may change before the challenge ends"), then the next pair loads.

**Behind the scenes:** looks with the fewest head-to-heads are served first so every entry reaches the minimum (proposed 20). A voter never sees their own look or the same pair twice.

### D16. No Skip
- **Decision:** every pair needs a pick.
- **Note:** close calls add noise, which averages out over 20+ head-to-heads.

### D17. One challenge at a time
- **Decision:** the system chooses which challenge a player votes on. Players can't scroll or choose.
- **Why:** gives control over the timeline, so every entry reaches its minimum head-to-heads before results.

### D18. No penalty for taste
- **Decision:** voters are never weighted down for disagreeing with the majority. Style is subjective.
- **What we do filter:** mechanical abuse only (bots, sub-second taps, always picking the same side).
- **Replaces:** the earlier "more weight for trusted voters" idea in `context.md`.

### D19. Never vote on your own look
- **Decision:** a voter's own look is never served to them.

### D20. Entrants can vote in their own challenge
- **Decision:** yes.
- **Why:** players are the voter pool, and few people play a game only to vote.
- **Safeguard:** measure whether entrants' votes drift from non-entrants' in the same challenge. Act only if data shows real gaming.

### D21. Voting pays Tags only
- **Decision:** the only reward for voting is Tags. No coins, streaks or badges for voting.
- **The Tags loop:**
  ```
            ┌── Daily gift: x Tags (free, up to the cap of y)
  Tags  ◄───┼── Voting: Tags every 3 votes (free)
            └── Buying: with coins or real money (bought Tags can go above the cap)
    │
    ▼
  Challenge entry (5 Tags)
  ```
- **New compared with `context.md`:** Tags can be bought with game coins, not only real money. The coin-to-Tag exchange rate is set in the economy area.
- **Constraint for the economy area:** the daily gift must be smaller than a regular player's entry habit, or voting becomes pointless. About 8–9 challenges a week × 5 Tags is ~45 Tags a week. The placeholder of 10 a day (70 a week) is too generous. Roughly 3–5 a day is the range to test.
- **Proposed safeguard:** a daily cap on Tags earned from voting (to stop bot farming). Voting itself can continue past the cap.

### D22. Stars from fixed thresholds, percentage hidden
- **Decision:** a look's share of head-to-heads won converts to stars with fixed bands, the same in every challenge. Everyone gets at least 1 star. **Players never see the percentage**, only stars, so the star system stays intact and a low score doesn't feel bad.
- **Starting bands (live setting):** 80%+ = 5★, 60–79% = 4★, 40–59% = 3★, 20–39% = 2★, under 20% = 1★.
- **What it means for the build:**
  - The percentage never leaves the server. The API returns star counts only.
  - The "current stars" shown after a vote follow the same rule.
  - Payouts are tuned through coins per star (live setting), not by changing the bands.
  - Raw win rates are kept internally for brand reports and stylist reputation.
- **Later option:** because the percentage is hidden, the score behind the stars could be adjusted for opponent strength with no visible change to players. Not adopted.

---

## Parked items

| ID | Item | Notes |
|---|---|---|
| P1 | How we get clothing photos and the rights to generate from them | Raised: AI output from a brand's photo may count as a derivative work needing permission; affiliate image licences usually forbid modification; garment designs are mostly unprotected in the US, but prints, graphics and logos can be. Options discussed: shooting products ourselves, brand opt-in through a portal. The PM believes there are more options. Revisit |
| P2 | Legal review timing | Proposed moving the IP lawyer review from Phase 3 to before Phase 2 (when 200 real players see the product). Not yet confirmed |

## Pending questions

| # | Question | Options | Recommendation |
|---|---|---|---|
| Q10 | What if a challenge gets too few votes (under 20 head-to-heads per entry)? | A: extend voting automatically, up to a limit, then release. B: release on time anyway. C: extend, then refund Tags and give a flat 3 stars | A, with the Vote tab pushing the struggling challenge first |
| — | Daily challenge from launch, or start lighter in Phase 2? | Daily from launch, or 3 a week + weekly | Daily from launch (assumed in D12) |

## Areas still to cover

1. ~~North star~~
2. ~~Catalog and items~~ (except P1)
3. ~~Avatar and rendering~~
4. ~~Challenge lifecycle~~
5. **Voting and ranking** (in progress: Q8, pairing logic, spite and bot detection, trusted voters)
6. Economy: coins, Tags and wears as a ledger, purchases, fraud, web and app-store payments
7. Commerce: Shop the look, affiliate attribution, sponsored challenges, brand portal
8. Identity, social and safety: accounts, friends and borrowing, moderation, 18+ and a later teen mode
9. Data and analytics: retention metrics for the Phase 2 go/no-go, the later trend-data product
10. Platform and infrastructure: web to native, services, scaling and cost
