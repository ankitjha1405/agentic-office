---
key: ENG-4
title: "Product Quest: page titles for /signup, /home, /profile (BUG-006)"
type: bug
product: Product Quest
status: In Review
category: In Review
priority: P3
owner: frontend-engineer-1
reporter: cto
created: 2026-10-29
due: 2026-10-30
links: [/Users/ankitkumar/dev/product-quest-fixes/replica/bugs.md]
---

## Goal
/signup, /home and /profile have their own titles, set the same way as the other pages.

## Acceptance criteria
- [ ] Metadata added following the existing pattern
- [ ] e2e `F09-E2` and `F10-E2` pass
- [ ] tsc and eslint clean; one commit; bugs.md updated

## Notes / log
- 2026-10-29 · coo (Ankit): CEO asked for the fix. Routed to CTO.
- 2026-10-29 · cto (Rahul): Owner frontend-engineer-1 confirmed. Files: src/app/signup/page.tsx, src/app/(app)/home/page.tsx, src/app/(app)/profile/page.tsx; add `export const metadata` like login/pricing. None of the three exports metadata today.
- 2026-10-29 · frontend-engineer-1 (Sneha): added export const metadata title 'Sign up' / 'Home' / 'Profile' (root layout template '%s · Product Quest' appends brand; all three are server components); not run: tests/commit (shell blocked)
- 2026-10-29 · coo (Ankit): Reviewed diff: matches criteria. bugs.md updated. Open: tests and commit (shell blocked); waiting on CEO.
