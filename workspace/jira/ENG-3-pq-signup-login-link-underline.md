---
key: ENG-3
title: "Product Quest: underline the Log in link on /signup (BUG-005)"
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
The inline "Log in" link on /signup is not told apart by colour alone.

## Acceptance criteria
- [ ] Link is underlined
- [ ] e2e `F09-E1 axe` passes (no `link-in-text-block`)
- [ ] tsc and eslint clean; one commit; bugs.md updated

## Notes / log
- 2026-10-29 · coo (Ankit): CEO asked for the fix. Routed to CTO.
- 2026-10-29 · cto (Rahul): Owner frontend-engineer-1 confirmed. File: src/app/signup/page.tsx:51, swap hover:underline for underline. One-line change.
- 2026-10-29 · frontend-engineer-1 (Sneha): signup/page.tsx Log in link hover:underline -> underline; not run: tests/commit (shell blocked)
- 2026-10-29 · coo (Ankit): Reviewed diff: matches criteria. bugs.md updated. Open: tests and commit (shell blocked); waiting on CEO.
