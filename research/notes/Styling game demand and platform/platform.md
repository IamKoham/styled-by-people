# Launch Platform for a Fashion Styling Game (status as of Nov 21, 2026)

Scope: a solo non-engineer founder, an 18+ Gen Z mid-market styling game (real affordable items, challenges, head-to-head voting, shoppable looks with affiliate links, coin packs and passes), a web prototype first, US first.
Method note: I ran about 22 web searches and fetches. Many findings come from search-result summaries rather than full-page reads. Items marked [UNVERIFIED] are either single-source or from my background knowledge without a page fetched this session.

## 1. Where 18–30s spend time styling and shopping (app vs web vs social)

### Takeaway
Phone time is overwhelmingly in apps (about 94% by Sensor Tower's 2025 data), and shopping momentum is moving to apps (app sessions up, shopping-site traffic down). Web still matters as the low-friction entry point that social links open into. I found no clean Gen Z fashion-shopping-by-channel split.

### Cited Findings
- Sensor Tower, State of Mobile 2026 (covering 2025): users spent less than 6% of smartphone time in browsers, so roughly 94% was in apps, at about 3.6 hours/day per user. — [Sensor Tower State of Web 2026 PDF (via adindex)](https://adindex.ru/publication/analitics/search/345004/img/sensor_tower__state_of_web_2026.pdf); [MobiLoud summary](https://www.mobiloud.com/blog/mobile-apps-vs-the-mobile-web)
- Sources disagree on growth in app time: +3.8% YoY (MobiLoud, citing Sensor Tower) vs +1.1% (Review42). — [MobiLoud](https://www.mobiloud.com/blog/mobile-apps-vs-the-mobile-web); [Review42](https://resources.review42.com/app-usage-statistics/)
- eMarketer: web browsing time dropped 4.4% as social and streaming apps took more attention. — [eMarketer](https://www.emarketer.com/content/web-browsing-time-drops-social-streaming-apps-capture-more-attention)
- Shopping-website traffic fell 1% YoY while ecommerce app sessions rose 13%. — [MediaPost](https://www.mediapost.com/publications/article/409259/ecommerce-growth-shifts-to-apps-and-ai-from-websit.html)
- One claim puts app purchases slightly ahead of mobile web (54% vs 46%), but the original source isn't clear. [UNVERIFIED] — [MobiLoud](https://www.mobiloud.com/blog/mobile-apps-vs-mobile-websites)
- MobiLoud (an app-builder vendor, so biased) benchmark across 3 brands: app conversion of 9.06% vs 1.14% on mobile web for one brand; for another, the app drove 35% of mobile revenue from 2% of mobile users. — [MobiLoud shopping app trends](https://www.mobiloud.com/blog/shopping-app-trends-report)
- Roblox says its US 18–34 cohort is growing more than 50% YoY (Q1 2026, age-checked data, partly extrapolated) and monetizes over 50% higher than under-18s. — [Roblox newsroom, Apr 30 2026](https://about.roblox.com/newsroom/2026/04/roblox-fuels-high-fidelity-games-over-18-players-increases-qualifying-devex-rate-42)
- Business Insider framed Roblox's 2025 commerce push as Roblox wanting to become "the new shopping mall for Gen Z." — [Business Insider NL](https://www.businessinsider.nl/roblox-wants-to-become-the-new-shopping-mall-for-gen-z/)

### Inferences
- Retention and habit happen in apps. Discovery for this audience happens in social apps (TikTok, Instagram), whose links open a web page or in-app browser. That favors a web prototype for acquisition tests, with an app needed later for retention and push.
- App conversion numbers come from loyal, already-installed users (selection bias). They don't mean a new user converts better if forced to install first.

### Gaps
- No reliable 2025–2026 split of Gen Z or 18–30 fashion purchases by channel (app vs web vs social commerce such as TikTok Shop). Look for eMarketer, Piper Sandler "Taking Stock With Teens" (which covers teens, not 18+), or Sensor Tower shopping reports.
- No Gen Z-specific app vs web time share found.

## 2. Platforms where styling-game competitors succeeded or failed

### Takeaway
Every durable commercial styling game is either app-native (Covet, Drest, Zepeto, Everskies) or Roblox-native (Dress to Impress, the breakout). Polyvore, the web-first shoppable-collage community, was shut down by an acquirer, not because of its platform. I found no successful PWA-first styling game.

### Cited Findings
- **Covet Fashion (iOS/Android, Crowdstar, later Glu, later EA):** Glu bought control of Crowdstar for about $45.5M in Nov 2016. At that point Covet had 30M+ downloads and ranked around #80 top-grossing on the App Store, and it made up most of Crowdstar's roughly $48M annual revenue. — [PocketGamer.biz](https://www.pocketgamer.biz/news/64353/glu-mobile-appoints-new-ceo-and-acquires-control-of-covet-fashion-dev-crowdstar-for-45-million/). In the first year after the deal, Covet and Design Home together made $110M+, with Design Home at 64%. — [PocketGamer.biz](https://www.pocketgamer.biz/data-and-research/64788/is-glu-mobiles-45-million-crowdstar-acquisition-already-paying-off/). Crowdstar had earlier dropped new Facebook games to focus on smartphones, an early sign that social-platform games were losing to mobile. — [PocketGamer.biz](https://www.pocketgamer.biz/news/40375/crowdstar-cans-new-facebook-games-as-studio-switches-focus-to-smartphones/). I found no 2025–2026 shutdown report for Covet. Covet's model of real-brand items and challenges with voting is the closest analog to this concept.
- **Drest (luxury styling):** soft-launched in Oct 2019, with 100+ luxury brands (Gucci, Prada, Burberry, and others). — [FashionNetwork, Oct 3 2019](https://au.fashionnetwork.com/news/New-styling-app-drest-combines-gaming-with-ecommerce,1144231.html). Glossy says Drest 2.0 would debut in spring 2024 on Android and iOS, "expanding the audience of a game that was formerly iOS-only." — [Glossy](https://www.glossy.co/fashion/mobile-fashion-gaming-is-gaining-traction/). This conflicts with the 2019 report of Google Play availability. A third-party tracker shows about 1.3M Android installs (estimate). — [AppGoblin](https://appgoblin.info/apps/com.drest.drestpro). Drest ran Unity Ads and ironSource playable ads on iOS and Android (AU/CA) and lifted IPM 78% over about 4 months. — [Unity case study](https://unity.com/resources/drest). The specific claim that Drest rebuilt in Unity as a cross-platform game in 2024 is [UNVERIFIED]: I found Unity Ads evidence, not engine confirmation.
- **Dress to Impress (Roblox):** built by a teen developer, about 9.7B visits. — [RoWatcher](https://rowatcher.com/news/dress-to-impress-how-a-teen-developer-s-fashion-game-hit-9-7-billion-visits). It routinely led Roblox in concurrent players in Sept 2024, peaking around 651K CCU after a promotion. — [Pocket Tactics](https://pockettactics.com/dress-to-impress-visits); [Gameranx on its adult audience](https://gameranx.com/updates/id/538084/article/is-a-roblox-fashion-game-bringing-in-a-big-adult-audience/). Estimated lifetime revenue is about $83M (modeled, not official), and peak CCU was 128K in the July 2026 period. — [Profitable.app](https://profitable.app/roblox/games/dress-to-impress). Another tracker estimates about $820K/month at low confidence. — [RoWatcher game page](https://rowatcher.com/games/5203828273). Its core loop (theme, style, runway vote) is close to this concept, but it uses avatar items rather than real shoppable products.
- **Everskies (PocketzWorld):** a dress-up social game with user-created, traded items. The iOS app was released Mar 3, 2022, and it is also on Google Play. — [App Store](https://apps.apple.com/us/app/everskies/id1604095327); [Apptopia](https://apptopia.com/google-play/app/com.everskies.app/about). Reviews cite bugs and moderation complaints. Its web origin (everskies.com, before the app) is from background knowledge [UNVERIFIED]. No user count found.
- **Polyvore (web, shoppable collages):** SSENSE bought its assets from Verizon/Oath and shut the site down immediately on Apr 5, 2018, causing user backlash. — [TechCrunch, Apr 5 2018](https://techcrunch.com/2018/04/05/polyvore-is-shutting-down-after-being-acquired-by-fashion-e-commerce-site-ssense); [Business of Fashion](https://www.businessoffashion.com/articles/news-analysis/ssense-shuts-down-polyvore-sparking-outrage-among-fans)
- **Zepeto (Naver Z, app):** 400M+ registered users per a Sept 2025 press release. That counts registrations, not activity. MAU estimates run from about 10M to 20M (dates unclear). — [Naver press release](https://navercorp.com/en/media/pressReleasesDetail?seq=31216); [Digiday](https://digiday.com/marketing/what-marketers-need-to-know-about-zepeto-the-korean-metaverse-platform/)
- **Infinity Nikki (Infold; PC, PS5, mobile):** no data gathered this session. [GAP]

### Inferences
- The pattern is "native app (big UA budgets) or Roblox (free discovery)." The web-first example, Polyvore, was a community and shopping site rather than a game. It proves demand for shoppable look-making on the web but offers no monetization proof for games.
- Covet shows that real-brand styling with voting can reach top-100 grossing on mobile. It did that with a professional studio and paid UA.

### Gaps
- Infinity Nikki revenue and platform split. Covet's current revenue and status. Everskies MAU. Confirmation of Drest's Unity rebuild and its Android launch date.

## 3. Cost to build and run, and fees per platform

### Takeaway
Store fees are falling: Apple 15% for small businesses, US link-outs at 0% for now, and Google's US settlement setting fees around 10–20%. Web payments cost about 3% (Stripe). Roblox pays creators about $0.0038 per earned Robux, which works out to roughly a 25–30% net share of consumer spend. Build-cost figures were not found in reliable sources.

### Cited Findings
- **Apple Small Business Program:** 15% commission for developers earning under $1M/year, otherwise 30%. — [Apple Developer](https://developer.apple.com/app-store/small-business-program/) [standing policy since 2021; page not re-fetched this session]
- **Epic v. Apple (US external purchase links):**
  - Apr 30, 2025: the district court found Apple in willful violation and barred any commission on link-outs, so US apps could link to web checkout at 0%.
  - Dec 11, 2025: the Ninth Circuit largely upheld this but said Apple may charge a commission tied to costs "genuinely and reasonably necessary" for coordinating external links, excluding security and privacy costs, and sent the rate back to the district court. Apple may also stop developer links from being more prominent than its own IAP buttons. — [MacRumors, Dec 11 2025](https://www.macrumors.com/2025/12/11/apple-app-store-fees-external-payment-links/); [Fenwick](https://www.fenwick.com/insights/publications/ninth-circuit-largely-upholds-ruling-in-epic-v-apple)
  - Early Apr 2026: Apple won a stay pending a Supreme Court petition.
  - Apr 28, 2026: the Ninth Circuit reversed the stay. As of Apr 29, 2026, Apple cannot collect any commission on US link-out purchases, and Judge Gonzalez Rogers is to set what fee, if any, Apple may charge. — [MacRumors, Apr 29 2026](https://www.macrumors.com/2026/04/29/epic-games-wins-reversal-app-store-fee-battle/); [Michael Tsai blog, Apr 30 2026](https://mjtsai.com/blog/2026/04/30/external-purchase-fee-stay-reversed/)
  - Status as of Nov 2026: no final fee found. The MacRumors page showed no later update on this. [Check before launch.]
- **Google Play (US):** Epic and Google settled on Mar 4, 2026. Per TechCrunch, the service fee becomes 20% on IAP (new installs) and 10% on subscriptions. Google's help page lists external transactions at 10% for auto-renewing subscriptions and 20% for other digital content, with 10% on the first $1M of annual revenue, plus a per-install fee for the external content links program. Fees reportedly started around Jun 30, 2026 for the US, UK, and EEA. Final court approval was still pending in some reports. — [TechCrunch, Mar 4 2026](https://techcrunch.com/2026/03/04/google-settles-with-epic-games-drops-its-play-store-commissions-to-20); [Google Play Help](https://support.google.com/googleplay/android-developer/answer/15582165?hl=en); [Android Headlines, Jun 2026](https://www.androidheadlines.com/2026/06/google-play-store-external-billing-fee-changes.html). Google's longstanding 15% on the first $1M also applies. [Background, UNVERIFIED this session]
- **EU DMA:** alternative payments and external links are allowed in the EU under Apple's DMA terms (Core Technology Fee and commission structures). No 2026 figures were gathered. [GAP; less relevant since the launch is US-first]
- **Web payments:** Stripe's standard US card rate is about 2.9% + $0.30. — [Stripe pricing](https://stripe.com/pricing) [standard published rate; page not re-fetched]. Small coin packs get hit hard by the fixed $0.30: on a $1.99 pack that is about 18%.
- **Roblox DevEx:** raised 8.5% in Sept 2025 (RDC), so 100,000 earned Robux now cash out at $380 instead of $350 ($0.0038/Robux). — [PocketGamer.biz](https://www.pocketgamer.biz/roblox-creators-will-now-earn-85-more-from-developer-exchange); [Roblox RDC 2025](https://corp.roblox.com/newsroom/2025/09/roblox-rdc-2025). From Jun 8, 2026, the rate is 42% higher on spend by age-checked US 18+ players in eligible games using R15 avatars, covering game passes, subscriptions, select items, and private servers. — [Roblox, Apr 30 2026](https://about.roblox.com/newsroom/2026/04/roblox-fuels-high-fidelity-games-over-18-players-increases-qualifying-devex-rate-42). Creators earned $1.5B+ through DevEx in 2025. — same source
- Roblox effective creator share: creators keep about 70% of Robux on game-pass sales, and consumers pay about $0.01 per Robux. [Background, UNVERIFIED this session.] At $0.0038 per earned Robux, that is about 27% of consumer spend, or about 38% on qualifying 18+ US spend.
- **Telegram Stars:** Telegram takes no commission, but Stars are bought through Apple or Google IAP, and conversion losses are large. One example: 100 Stars cost the user about $2.40 and withdraw at about $1.30 (about 54%). — [WN Hub](https://wnhub.io/news/monetization/item-47137) [secondary]

### Inferences
- For coin packs, US iOS web checkout via link-out (0% Apple fee as of Apr 2026, plus about 3% Stripe) beats IAP (15%). This is legally unstable: a district-court fee could arrive at any time in 2026–2027.
- On Roblox, real-world prices and affiliate commerce are mostly out of reach (see Q5), and the creator keeps roughly a quarter to a third of spend. In exchange, there is no UA cost and no infrastructure cost (Roblox hosts and runs the servers).
- A web prototype (no-code or low-code such as Bubble, FlutterFlow, Framer plus Supabase, or AI-assisted coding) can plausibly be built for low thousands of dollars or less. A native iOS/Android build by agencies or freelancers typically runs much higher. These are my estimates, not sourced.

### Gaps
- No sourced build-cost benchmarks for a simple 2D styling game by platform. No sourced comparison of no-code tools. No final district-court fee for Apple. No 2026 DMA fee schedule. Roblox's current consumer Robux price was not re-verified.

## 4. Discoverability on each platform

### Takeaway
App stores need paid UA. US iOS game CPIs ran about $2–5 for casual and simulation genres in 2025–2026, much higher for puzzle and match. Roblox offers built-in algorithmic discovery (Dress to Impress grew organically), and TikTok Mini Games ties discovery to short-video content. Web relies on SEO, portals, and social links.

### Cited Findings
- Liftoff (Feb 2024–Feb 2025, global): average casual-game CPI of $1.41 on iOS and $0.14 on Android. — [Liftoff 2025 Casual Gaming Apps Report](https://liftoff.ai/?p=34267); [GameDevReports summary](https://gamedevreports.substack.com/p/liftoff-and-singular-casual-games)
- AppsFlyer Q3 2026 US benchmarks: hypercasual $1.96 iOS / $1.55 Android; simulation $4.23 iOS / $2.50 Android; puzzle $9.48 iOS; match $21.63 iOS. — [AppsFlyer gaming benchmarks Q3 2026](https://www.appsflyer.com/?p=549948) [via search summary; the page was not fetched in full]
- AppTweak (2025, US, all games, Apple Search Ads): median cost per tap $2.03, CPI $4.63. [via search summary] — [Segwise summary](https://segwise.ai/blog/cpi-ipm-roas-benchmarks-optimizing-ad-spend/)
- Drest raised IPM 78% with playable ads, showing that paid UA is central to app-based styling games. — [Unity](https://unity.com/resources/drest)
- Roblox discovery: Dress to Impress grew to billions of visits from a teen solo developer with no paid UA. — [RoWatcher](https://rowatcher.com/news/dress-to-impress-how-a-teen-developer-s-fashion-game-hit-9-7-billion-visits). Roblox runs Incubator and Jumpstart programs, with 8,000+ applicants, and specifically targets 18+ experiences. — [Roblox, Apr 2026](https://about.roblox.com/newsroom/2026/04/roblox-fuels-high-fidelity-games-over-18-players-increases-qualifying-devex-rate-42)
- TikTok Mini Games: "Growth Max for Mini Games" automates player acquisition with in-feed instant play and supports immediate in-app ad monetization (D0 ROAS bidding). It was described as in testing in one TikTok PDF and promoted as live in a May 2026 blog. — [TikTok Ads blog](https://ads.tiktok.com/business/en/blog/tiktok-growth-max-mini-games); [PPC Land](https://ppc.land/tiktok-growth-max-brings-instant-play-ad-monetization-to-mini-games/). TikTok also runs a game-incentive program for creator videos. — [TikTok for Developers](https://developers.tiktok.com/doc/game-incentive-creator-videos)
- Web portals: Poki reports about 100M monthly users and says 625M players visited Poki.com in 2025. CrazyGames claims 50–60M MAU, while Semrush estimates about 35M. — [Poki State of Web Gaming 2026, Jun 25 2026](https://poki.com/blog/state-of-web-gaming-report-2026); [Mobidictum interview](https://mobidictum.com/pokis-web-gaming-interview-michiel-van-amerongen); [Tech Insider](https://tech-insider.org/crazygames-vs-poki-vs-coolmath-games-2026/). Web portals skew hypercasual and puzzle (79% of web games are hypercasual). — [PocketGamer.biz](https://www.pocketgamer.biz/report-hypercasual-and-puzzle-games-dominate-the-browser-gaming-space/)

### Inferences
- A solo founder can't afford app-store UA at $2–5+ per install with unproven retention. Web plus organic TikTok and Instagram content (outfit videos linking to a play URL) is the cheapest discovery test. Roblox is the cheapest proven path to scale, but its audience skews younger, and real-product shopping is limited there.

### Gaps
- No sourced data on App Store featuring odds or organic share for indie games. No fashion or dress-up-specific CPI found. No figures on TikTok Mini Games reach in the US.

## 5. Outbound shopping and affiliate links and brand deals

### Takeaway
Native apps and the web can freely link out to retailers for physical goods. Apple's IAP rules only cover digital goods. Roblox blocks generic off-platform links but now has sanctioned commerce: a Shopify integration for physical goods (US, 2025) and an Approved Merchandiser Program. TikTok and Discord policies on affiliate links inside mini games were not confirmed.

### Cited Findings
- Apple App Review Guidelines: apps may use payment methods other than IAP for physical goods and services consumed outside the app (Guideline 3.1.5(a)/3.1.3(e)). That allows affiliate and retailer links for real clothing. — [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) [standing rule; page not re-fetched this session]. Coins and passes are digital and need IAP, or a US link-out per Q3.
- Google Play's payments policy similarly exempts physical goods from Play Billing. [Background, UNVERIFIED this session]
- **Roblox commerce (May 2025):** Roblox launched a Shopify integration letting creators sell physical products inside experiences, plus an Approved Merchandiser Program (AMP) that links real-world purchases to avatar items. — [Roblox newsroom, May 2025](https://corp.roblox.com/newsroom/2025/05/roblox-launches-shopify-integration-amp-licensing-program); [TechCrunch, May 15 2025](https://techcrunch.com/2025/05/15/roblox-now-lets-creators-sell-physical-products-within-their-experiences)
  - Seller requirements: 18+, ID-verified, 2FA, and the registered owner of the Shopify store.
  - Buyer requirements: US only, 13+ (18+ in Texas).
  - Goods must meet Roblox commerce standards. — [Roblox Creator Docs: Commerce products](https://create.roblox.com/docs/en-us/production/monetization/commerce-products); [DevForum](https://devforum.roblox.com/t/expanding-how-commerce-can-help-you-earn-and-grow-your-communities/3651181)
  - Fit with this concept: the integration sells your own Shopify catalog, not affiliate links to third-party retailers. Generic external links are not allowed in Roblox experiences outside sanctioned programs. That restriction is [UNVERIFIED]: I did not find the text of the off-platform-link policy.
- Facebook Instant Games/Web Games: Meta required all games to migrate to a "Zero Permissions" platform (Jul 31, 2025). A secondary source reports legacy web games sunsetting around Sept 2026. — [Meta for Developers, Jul 31 2025](https://developers.facebook.com/blog/post/2025/07/31/web-and-instant-games-changes/); [PPC Land](https://ppc.land/meta-announces-web-games-sunset-by-september-2026/)
- Discord launched in-platform purchases of in-game items in Dec 2025. — [TechCrunch, Dec 2 2025](https://techcrunch.com/2025/12/02/discord-users-can-now-buy-in-game-items-without-leaving-the-platform)

### Inferences
- The affiliate-plus-brand-deal model fits a native app or web far better than Roblox. On Roblox, brand deals become virtual-item and licensing deals (AMP), not affiliate revenue from real affordable items.

### Gaps
- TikTok Mini Games policy on outbound commerce and affiliate links. Discord Activities rules on external links. Roblox's exact off-platform link policy text. Snapchat games status. None of these were found this session.

## 6. In-platform options (TikTok, Meta, Snap, Discord, Telegram): reach and limits

### Takeaway
TikTok Mini Games is the most relevant in-social option. It is live in the US with IAP and ads, but it requires business verification and a lengthy US approval. Meta's Instant Games is shrinking or migrating. Discord Activities is open with IAP but skews toward gamer friend groups. Telegram's mini-app audience collapsed after the tap-to-earn bubble and is crypto-skewed and weak in the US.

### Cited Findings
- **TikTok Mini Games:**
  - Monetization: in-app ads (rewarded and interstitial) and IAP. Requires TikTok for Developers business verification and tax information. — [TikTok Developers: Monetization overview](https://developers.tiktok.com/docs/en/monetization-overview); [Enable monetization](https://developers.tiktok.com/docs/en/enable-monetization-features)
  - US launch: the workflow includes verifying as a mini-games publisher and applying separately for US launch. — [TikTok Developers: Integration workflow](https://developers.tiktok.com/docs/en/mini-games-integration-workflow). A third-party guide says US launch needs USDS third-party risk management review, taking 15–30 business days. [secondary] — [DEV Community](https://dev.to/ipfoxy/how-to-monetize-tiktok-minis-in-2026-developer-guide-for-mini-games-short-dramas-2d3j)
  - US analytics show only once a game passes 1,000 unique US users. — [TikTok Developers: Analytics](https://developers.tiktok.com/docs/en/mini-game-analytics)
  - An Aug 2025 pilot ran with Voodoo, Nitro Games, Aim Lab, and others. — [Front Office Sports](https://frontofficesports.com/tiktok-tests-mobile-games-with-marquee-developers/)
  - No fashion mini games were identified, and the revenue share was not found.
- **Meta Instant Games:** Messenger dropped Instant Games in 2019. In Jul 2025, Meta announced a migration to a Zero Permissions platform and extended IAP to Facebook mobile apps. — [Meta, Jul 31 2025](https://developers.facebook.com/blog/post/2025/07/31/web-and-instant-games-changes/); [PocketGamer.biz on the 2019 Messenger removal](https://www.pocketgamer.biz/facebook-pulls-instant-games-from-messenger). An Instagram Instant Games product was not found.
- **Discord Activities:** open to all developers since Sept 2024 via the Embedded App SDK. Supports IAP (durable and consumable SKUs) with a platform fee plus processing. In-platform item purchases followed in Dec 2025, and a gaming update came Mar 9, 2026. — [Discord blog](https://discord.com/blog/build-where-the-world-plays); [GamesBeat](https://gamesbeat.com/discord-opens-activities-in-app-games-and-features-to-all-developers/); [TechCrunch, Dec 2025](https://techcrunch.com/2025/12/02/discord-users-can-now-buy-in-game-items-without-leaving-the-platform); [Discord Dev support: Premium Apps](https://support-dev.discord.com/hc/en-us/articles/23810643331735)
- **Telegram Mini Apps:**
  - Telegram passed 1B MAU in 2025, and 500M+ users interacted with Mini Apps monthly in 2024. — [Game World Observer](https://gameworldobserver.com/?p=28151) [via search summary]
  - PropellerAds: Mini App MAU peaked at 1.44B in Sept 2024, then fell to 150–190M by mid-2025 as tap-to-earn churned. — [TechIntelPro on PropellerAds 2025 report](https://techintelpro.com/news/marketing/advertising/propellerads-telegram-mini-apps-ad-report-2025-highlights)
  - Payments run in Stars, bought through Apple or Google IAP, with heavy conversion loss (see Q3).
- **Snapchat games:** no 2025–2026 data gathered. [GAP]

### Inferences
- These are distribution channels, not homes. Each has its own SDK, payments, and review process. TikTok's audience and aesthetic fit Gen Z fashion best, but adding affiliate links and a voting community inside a mini game is unproven. A sensible order: web prototype first, then a TikTok Mini Game port as an acquisition experiment.

### Gaps
- TikTok Mini Games' revenue share, its US user reach, and any fashion titles. Snapchat game status. Whether an Instagram-specific games surface exists. Discord's exact platform fee percentage.

## 7. Can a PWA or mobile web game feel good enough on a phone?

### Takeaway
Yes for a 2D drag-and-drop styling loop. Web portals show large mobile web gaming audiences. iOS limits remain: push notifications only work after the user adds the app to the Home Screen (iOS 16.4+), install is a manual step, and there are EU wrinkles. The usual path is web to validate, then wrap or build native once retention is proven.

### Cited Findings
- iOS web push works only for Home Screen-installed web apps (iOS 16.4+). Declarative Web Push arrived in iOS 18.4, also limited to installed apps. — [MagicBell](https://www.magicbell.com/blog/pwa-ios-limitations-safari-support-complete-guide); [Progressier](https://progressier.com/pwa-capabilities/declarative-web-push)
- EU: Apple announced removing standalone Home Screen web apps in iOS 17.4 (Feb 2024), then reversed in Mar 2024. — [MacRumors, Feb 15 2024](https://www.macrumors.com/2024/02/15/ios-17-4-web-apps-removed-apple/); [GSMArena](https://m.gsmarena.com/apple_backtracks_wont_remove_progressive_web_apps_in_the_eu_after_all-news-61836.php)
- iOS 26 (Sept 2025): every site added to the Home Screen opens as a web app by default. [UNVERIFIED, vendor source] — [MobiLoud](https://www.mobiloud.com/blog/progressive-web-apps-ios)
- Mobile web gaming scale: Naavik, citing Similarweb, estimates 28% of unique visitors to top browser-game sites are on mobile. Poki puts its own mobile share at about 40%. — [Naavik](https://naavik.co/digest/web-gaming-strikes-back/); [Poki report 2026](https://poki.com/blog/state-of-web-gaming-report-2026)
- Nov 2025 press: "Video games' hottest new platform is an old one: websites," on studios moving web-first, partly because of the US link-out ruling. — [The Star (syndicated), Nov 10 2025](https://www.thestar.com.my/tech/tech-news/2025/11/10/video-games-hottest-new-platform-is-an-old-one-websites)
- Web-first, then app: Everskies appears to have started on the web before launching apps in Mar 2022. [UNVERIFIED] — [App Store](https://apps.apple.com/us/app/everskies/id1604095327)

### Inferences
- A styling game is mostly 2D image layering, drag and drop, and feeds, which suits mobile web well. The real web penalties are retention (no push without install, no home-screen presence) and payment friction. With the 2025–2026 US rulings, many games now push web stores even from native apps, so a web checkout built for the prototype stays useful later.
- Typical path: responsive web or PWA, then a native wrapper (Capacitor/Expo) or a native rebuild once D7/D30 retention is proven, keeping web checkout for coins via US link-out.

### Gaps
- No named web-first styling game with sourced success metrics. No sourced D30 retention comparison between web games and native apps.
