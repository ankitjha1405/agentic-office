---
owner: product-designer
status: draft
created: 2026-11-06
task: DES-1 (batch A, 9 projects)
---

# Portfolio floorplan: page inventory, batch A

Tags: [code] = read from local repo routes/components. [site] = seen on live URL (HTTP check 2026-11-06, title/meta only; no login).
Summary: 9/9 respond. 8 are live and real, 1 is live but fully login-gated (primer-dashboard). None excluded as dead. Note: an HTTP 200 does not prove the content, only that the site answers.

| # | Project | Liveness | Gate | Stack |
|---|---|---|---|---|
| 1 | kosh | Live [site] | Mostly auth | Next 16, React 19, Tailwind 4, SQLite/own sessions [code] |
| 2 | haunted-terminal | Live [site] | None | Static HTML in `site/` + zsh/Python tool [code] |
| 3 | loqelo-prelaunch | Live [site] | None | Vite + vanilla JS, i18n, Vercel functions [code] |
| 4 | product-quest | Live [site] | Mostly auth | Next 16, React 19, Supabase, Drizzle, Tailwind 4 [code] |
| 5 | aurele-atelier | Live [site] | None | Static HTML/CSS/JS [code] |
| 6 | oscar-board | Live [site] | Fully auth | Static HTML + Vercel functions, Neon Postgres [code] |
| 7 | daily-quest | Live [site] | None (sync needs passphrase) | Static HTML + vanilla JS, Turso [code] |
| 8 | foxo-heart-age | Live [site] | None | Static HTML + vanilla JS SPA, Resend email [code] |
| 9 | primer-dashboard | Live, login wall (307 to /login) [site] | Fully auth | Next 15, React 19, SQLite/libSQL [code] |

---

## 1. kosh
Voice-first personal finance coach for India; reads statements/SMS, plans goals. [code][site]
Has API (ingest, mcp, tts). [code]

**Pages** (Next app router) [code]
1. `/welcome` landing (public)
2. `/signup` public (redirects to `/` if signed in)
3. `/login` public (same)
4. `/onboarding` voice interview, uploads, persona
5. `/` Home: balance, planned/unplanned, savings (auth: `requireUser`)
6. `/spends` plan vs actual, imports, categories, subscriptions (auth)
7. `/savings` mutual funds, FDs, crypto, emergency fund (auth)
8. `/profile` persona, goals, connections, log out (auth)
9. `/chat` "Kuber" assistant (auth)

**Links** [code]
- Main nav (all auth pages): Home, Spends, Savings, Profile, Kuber (chat). Bottom tab bar on mobile.
- Signup leads to onboarding; onboarding "Skip" opens demo account; onboarding ends at Home.
- Home links to /spends, /savings, /onboarding.

Odd: root `/` is auth-gated; the public front door is `/welcome` (unconfirmed how anonymous `/` redirects; not tested).

## 2. haunted-terminal
A ghost lives in your terminal (zsh, Gemma on-device); install guide page. [site][code]
**Pages**: single page `site/index.html`, sections in order [code]: Hero ("A ghost moves into your terminal", sound toggle, ghost) > What happens ("Four things happen") > Welcome card > Safety ("Spooky on the surface, careful underneath") > Install ("Three steps", macOS/Linux zsh) > Footer/track. Also downloadable `ghost`, `ghost.zsh`, `install.sh`, `haunt.mp3` copied into site at build. [code]
**Links**: hero CTA scrolls to Install; install.sh is the end action. [code, CTA target inferred]
Gate: none.

## 3. loqelo-prelaunch
Pre-launch waitlist for a local-pros marketplace, "Launching February 2027". [site]
Has API (`/api/subscribe`, `/api/geo`). [code]
**Pages** [code]
1. `/` single page, sections: Hero (#top) > How it works (#how, 4 steps) > Both sides (#sides) > Inside (#inside) > Join waitlist (#join) > FAQ (#faq)
2. `/privacy.html`
**Links** [code]: header anchors to #how, #inside, #join, #faq; language switch EN/DE/NL/PL via `?lang=`; footer to /privacy.html; hero CTA to #join (inferred).

## 4. product-quest
Practice-first platform for aspiring PMs: cases, AI feedback, skill profile. [site][code]
Has API (billing checkout, webhooks, cron sync-jobs, auth callback/signout). [code]
**Pages** (~35 routes) [code]
Public: `/` marketing (site group), `/login`, `/signup`, `/signup/verify`, `/forgot-password`, `/forgot-password/reset`, `/diagnostic` (+ `/diagnostic/start`, `/diagnostic/result/[id]`, `/diagnostic/plan/[id]`).
Onboarding (signed in): `/onboarding` (router) > `/goal` > `/focus` > `/resume` > `/assess` > `/roadmap` > `/schedule`.
App shell "(app)" (signed in): `/home`, `/cases` (+ `/cases/feedback/[id]`), `/learning` (+ `/learning/[slug]`, lesson, tests), `/games` (+ `/games/[key]/play`), `/jobs`, `/mentorship`, `/plan`, `/profile`, `/upgrade`.
Other: `/cases/attempt/[id]` (attempt screen).
**Links** [code]
- App nav: Home, Cases, Learning, Games, Jobs, Mentorship, Plan?, Profile, Upgrade.
- Marketing CTAs go to /diagnostic, /cases, /mentorship, /onboarding/goal; login/signup links.
- `/onboarding` redirects to `/home` when finished, else next onboarding step.
Gate: middleware only refreshes the Supabase session; actual gating is per-page (not verified). Diagnostic appears open to anonymous users (inferred).

## 5. aurele-atelier
Independent atelier: gold rings, bespoke watches, leather straps. [site]
**Pages**: single page `index.html` [code]. Sections: Hero > Three lines (rings/watches/straps) > Manifesto > Process > Collection gallery (#collection, built by `products.js`, with #rings #watches #straps) > Atelier (#atelier) > Contact (#contact, form).
**Links** [code]: nav Collection, Atelier, Contact; CTA "Book a consultation" to #contact; mobile Menu overlay.
Odd [code][site]: contact form posts to Formspree placeholder `your-form-id` (live HTML contains it) and the email is `studio@aurele.example`. Form does not work, treat as demo/placeholder content. Real site, but not a working business page.

## 6. oscar-board
Personal Kanban (projects > tasks) for Ankit. [code]
Has API (login, projects, tasks; bearer token for CLI). [code]
**Screens** [code]
1. `/login.html` (public)
2. `/` (index.html) board: side list of projects, stats, kanban columns, breadcrumbs
3. Task dialog (with subtasks) and project dialog, as modals on the board
**Links** [code]: any 401 redirects to /login.html; login success goes to /; logout returns to /login.html; breadcrumbs move project > task > parent task.
Gate: everything except login. Not visited.

## 7. daily-quest
5 to 10 minute daily reels-style learning feed with spaced review. [code][site]
Has API (`/api/sync` passphrase-guarded, `/api/remind`). [code]
**Screens** (hash routes, one HTML page) [code]: `#today`, `#library`, `#plan` (Curriculum), `#progress`; plus a bottom sheet overlay.
**Links** [code]: top nav Today / Library / Curriculum / Progress. Default is #today. No login; sync is optional passphrase.

## 8. foxo-heart-age
FOXO free health calculators (heart age, Framingham, BMR, TDEE...). [site][code]
Has API (`/api/report`, emails result via Resend). [code]
**Screens** (hash SPA, `#/`) [code]
1. `#/` hub: calculators grouped by category + Primer promo
2. `#/age-of-heart-calculator` (custom tool)
3. `#/framingham-heart-risk-calculator`
4. `#/bmr-calculator`
5. `#/tdee-calculator`
6. `#/ascvd-score-calculator`
7. `#/calories-burned-calculator`
(+ any further tools in `tools.js`; only first 6 listed)
Each tool page: form > result > tabs (Next steps / About / Evidence) > related calculators. [code]
**Links** [code]: logo and "All health tools" go to hub; breadcrumbs back to hub; related calculators; external CTA "Explore the FOXO Primer Plan" to https://foxo.club (code TODO: should point at the Primer Plan page). Gate: none.

## 9. primer-dashboard
Internal "Primer Journey" member dashboard (SQLite, daily xlsx upload). [code][site]
Has API (auth, comments, members, prefs, upload). [code]
**Pages** [code]: `/login` (public), `/` dashboard (member list/stages, upload sheet button), `/member/[code]` member detail (comments, flag, test/staff toggle).
**Links** [code]: any unauth request redirects to `/login?next=...` (confirmed [site]: root returns 307 to /login); dashboard rows open /member/[code].
Gate: everything except login. Not visited beyond login; internal tool, handle with care (member data) in any shared visual: show structure only.
