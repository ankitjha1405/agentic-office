---
key: ENG-1
title: "Product Quest: text and accent button colour contrast (BUG-002, BUG-003)"
type: bug
product: Product Quest
status: In Review
category: In Review
priority: P2
owner: frontend-engineer-1
reporter: cto
created: 2026-10-29
due: 2026-10-30
links: [/Users/ankitkumar/dev/product-quest-fixes/replica/bugs.md]
---

## Goal
Muted/faint text and white-on-accent buttons pass WCAG AA 4.5:1. Change the design tokens once, not per page. Keep the look.

## Acceptance criteria
- [ ] New `--text-faint`, `--text-muted` and `--accent` values pass 4.5:1 on every background they are used on
- [ ] Design lead signs off the new values
- [ ] axe colour-contrast e2e tests (F0x-E1) pass; no assertion weakened
- [ ] `npx tsc --noEmit` and `npx eslint` clean
- [ ] One commit on fix/e2e-bugs; bugs.md says "fixed in <hash>"

## Notes / log
- 2026-10-29 · coo (Ankit): CEO asked for the fix. Routed to CTO. Work only in the worktree /Users/ankitkumar/dev/product-quest-fixes. No push, no data-writing scripts.
- 2026-10-29 · design-lead (Ananya): signed off --text-faint #6F6B7D -> #8D899C (5.41:1 on surface, 4.65:1 on surface-3); --accent #9B6CFF -> #7F4DF0 (4.97:1 with white); --accent-hover #AD85FF -> #6F3FDB (6.16:1); --text-muted #9C98A8 unchanged (token already passes, QA's #64626d is not the token value, find the opacity/override). Switch 3 raw text-[var(--accent)] uses to --accent-text.
- 2026-10-29 · cto (Rahul): Owner frontend-engineer-1 confirmed. Files: src/app/globals.css (tokens, ~l.46-49) plus the 3 text-[var(--accent)] call sites (e.g. learning/[slug]/page.tsx:58). Find the #64626d override on the home hero card before touching --text-muted. Do after ENG-3 check: accent change may shift link contrast.
- 2026-10-29 · frontend-engineer-1 (Sneha): globals.css --text-faint #8D899C, --accent #7F4DF0, --accent-hover #6F3FDB; 3 raw text-[var(--accent)] -> --accent-text (solve-editor:95, learning/[slug]:58, profile:161); no static #64626d found in src (home hero JourneyCard uses plain tokens), so no spot fix; not run: tests/commit (shell blocked)
- 2026-10-29 · coo (Ankit): Reviewed diff against acceptance criteria: matches design sign-off. bugs.md updated. Open: tsc/eslint/e2e and commit not run (shell blocked in session); waiting on CEO.
