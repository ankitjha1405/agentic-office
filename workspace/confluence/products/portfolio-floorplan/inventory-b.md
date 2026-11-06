---
owner: product-designer
status: draft
created: 2026-11-06
task: DES-1 (batch B, 9 projects)
---

# Page inventory, batch B

Checked 2026-11-06 with `curl` (HTTP status) and page text. Tags: [code] = from local source, [site] = from live site. No login, build or deploy done.

## Summary

| Project | Liveness | Include? |
|---|---|---|
| foxoclub | Live [site] HTTP 200 | Include |
| gitavatar | Live [site] 200 | Include |
| loan24-onboarding | Live [site] 200 | Include (prototype, not a product) |
| portfolio-v2 | Live [site] 307 to ankitjha1405.tech, then 200 | Include |
| hustlkr | Live [site] 200 | Include |
| pmforces | Live [site] 200 | Include |
| v0-todo-list-app | Live but template [site] | Suggest exclude |
| v0-todo-app-requirements | Live but template [site] | Suggest exclude |

---

## 1. foxoclub
- Live: https://foxoclub.vercel.app, 200 [site]
- What: Marketing homepage for FOXO, a longevity health system in India (224 biomarkers, 9 systems, 12-week protocol). [site]
- Stack: Next.js 16, React 19, Tailwind 4, particle-field/three.js visuals [code]. Has API: `/api/ome` (POST, powers the OME chat) [code].
- Pages: one route `/` [code]. Sections in order [code]: Hero, Story, HealthcareWaits, Process ("how it works", `#primer`), Pricing (`#pricing`), Stories, Faq (`#faq`), Begin. OME chat widget (`#ome`) is a section component [code]. No auth.
- Links: Nav anchors: How it works (`#primer`), OME (`#ome`), Pricing, FAQ. Nav CTA "Get Primer" goes to `#pricing` [code]. Footer links out to the Unfold Longevity Substack [site].

## 2. gitavatar
- Live: https://gitavatar.vercel.app, 200 [site]
- What: Turns a GitHub username's avatar into ASCII art / README markdown. [site]
- Stack: Single static `index.html`, vanilla JS and canvas; a separate Python CLI `gitavatar.py` exists locally [code].
- Pages: one screen `/` [code]. Flow: username form, Generate, then options panel (width, style, contrast, invert, trim, caption), result tabs Preview / Markdown, buttons Copy markdown and Download .md [code]. No auth, no API.
- Links: None between pages. Output markdown links to the user's github.com profile [code].

## 3. loan24-onboarding
- Live: https://loan24-onboarding.vercel.app, 200 [site]
- What: Mobile-first interactive prototype of a self-serve lending onboarding flow ("onboarding that builds its own evidence"). Not a real lender. [code]
- Stack: Single static `index.html`, vanilla JS, no package.json [code].
- Pages: one URL `/`; screens are JS states inside a phone frame, grouped in 5 steps [code]:
  1. Identity: welcome, mobile, otp, profile
  2. Documents: docintro, doccap
  3. Details: headcount, quiz, signature
  4. Premises: premises, primer, permdenied (camera off), capture, resumelater
  5. Result: assessing, offline, verified, adaptive, moreproof, selfie, handover, evidence
  Also a left rail with demo script modes and a Restart button. No auth, no API.
- Links (primary flow) [code]: welcome, then mobile/otp/profile, docs, details, premises, capture, assessing, result. Branches: camera denied goes permdenied, then retry or resumelater; adaptive/moreproof loops back to extra capture; "Resume later" returns to the flow.

## 4. portfolio-v2
- Live: https://ankitjha1405.vercel.app redirects (307) to https://ankitjha1405.tech/, 200 [site]. Odd: the Vercel URL is not the canonical one; the site's own JSON-LD still points at ankitjha1405.vercel.app [site].
- What: Ankit Jha's personal portfolio, "Product Manager & AI Builder". [site]
- Stack: Next.js 16, React 19, Tailwind 4 [code]. No API.
- Pages: one route `/` [code]. Sections in order [code]: Hero, Services, Projects (`#featured-work`), About, Testimonials, Contact. Resume link at top [site]. No auth.
- Links: Nav anchors `#home`, services/work/about, and CTA `#contact` [code]. Outbound [site]: hustlkr.in, pmforces.vercel.app, dotmystyle.com, webbres.com, a Pitch deck, GitHub, LinkedIn, mailto. So this site links to hustlkr and pmforces (useful for corridors on the map).

## 5. hustlkr
- Live: https://hustlkr.in, 200 [site]
- What: Personal-finance and "adulting" app for young Indians: calculators, Adulting Score, dashboard, journeys, articles, paid Elite tier. [site][code]
- Stack: Next.js 16, React 19, Tailwind 4, Supabase (auth + DB), Razorpay payments [code]. Has API: `/api/razorpay/webhook` [code].
- Auth: middleware redirects to `/login` unless path starts with `/login` or `/onboarding`. Note the matcher covers `/` too, so check if the landing page is gated in prod; the live `/` returns 200 publicly [code][site]. Treat all pages below except landing, login, onboarding, privacy as auth-gated [code].
- Pages (about 32 routes; grouped) [code]:
  - `/` landing: sections Why HustlKr (`#problem`), Features, Pricing, How it works (public) [site]
  - `/login` (public), `/onboarding` (public; redirects to `/home` if already onboarded)
  - `/privacy` (public)
  - `/home` dashboard (gated)
  - `/profile` (gated)
  - `/journey` list, `/journey/[slug]`, `/journey/[slug]/start` (gated)
  - `/articles/[slug]` (gated)
  - `/tools` index plus 17 calculators (gated): sip, lumpsum, goal-sip, emi, salary, income-tax, net-worth, rent-vs-buy, emergency-fund, financial-freedom, financial-health-score, home-loan-eligibility, dream-purchase-planner, car-purchase, bike-purchase
  - `/elite` (gated, paid): `/elite/chat`, `/elite/mentorship`
- Links [code]: Landing nav goes to anchors, "Log in" to `/login`, "Start Free" to `/onboarding`, footer to `/privacy`. Login links to `/onboarding`. After onboarding goes to `/home`. App nav: `/home`, `/journey`, `/tools` (tools tab), `/elite`, `/profile`. Elite goes to chat and mentorship.


## 7. pmforces
- Live: https://pmforces.vercel.app, 200 [site]
- What: PM interview practice platform with AI evaluation and Codeforces-style ratings. [site]
- Stack: Looks like Next.js (route redirect behaviour, `/auth/*` paths); exact version unknown [site]. No local code. Probably has API (auth, AI evaluation) but not visible from outside.
- Pages (public routes returned 200; found via landing nav) [site]:
  - `/` landing (hero, social proof, nav)
  - `/questions` question bank
  - `/leaderboard`
  - `/pricing`
  - `/auth/signin`, `/auth/signup`
  - `/dashboard` is auth-gated: 307 redirect to `/auth/signin` [site]. Other signed-in screens (interview session, results, profile) not visible without login: unknown.
- Links [site]: Landing nav goes to Questions, Leaderboard, Pricing, Sign in, Sign up. Sign in/up lead to `/dashboard`.

## 8. v0-todo-list-app: suggest exclude
- Live: https://v0-todo-list-app-beta.vercel.app, 200 [site]
- What: Title "v0 App", "Created with v0". Bare Todo App: add-task box, empty state "No tasks yet" [site].
- Stack: unknown (v0 generated, likely Next.js). Single screen `/`. No nav, no auth [site].
- Reason to exclude: generic v0 demo/template, no product identity.

## 9. v0-todo-app-requirements: suggest exclude
- Live: https://v0-todo-app-requirements-eight.vercel.app, 200 [site]
- What: Title "v0 App", "Created with v0". "Todo Application" with Add New Task form (title, description) and filters [site].
- Stack: unknown (v0 generated). Single screen `/`. No nav, no auth [site].
- Reason to exclude: a v0 demo, near-duplicate of #8, likely a requirements experiment. If CEO wants one kept, merge both into a single small room.

---

## Notes for the map
- Real products by size: hustlkr (largest, about 32 routes), foxoclub, pmforces, loan24 prototype (about 20 states), then single-page sites.
- Cross-links worth drawing: portfolio-v2 to hustlkr and pmforces [site].
- Not checked: whether `/` on hustlkr is meant to be public (middleware matcher says gated, live site is public). Page counts for pmforces signed-in area are unknown.
