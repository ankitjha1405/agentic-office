---
key: ENG-5
title: "Product Quest: unknown /learning/<slug> returns 200, not 404 (BUG-001)"
type: bug
product: Product Quest
status: In Review
category: In Review
priority: P3
owner: frontend-engineer-2
reporter: cto
created: 2026-10-29
due: 2026-10-30
links: [/Users/ankitkumar/dev/product-quest-fixes/replica/bugs.md]
---

## Goal
Unknown learning slugs return HTTP 404. Fix only if the change is small and safe; otherwise record why not.

## Acceptance criteria
- [ ] Either: e2e `F11-N1` passes with a small, safe change, committed; or: a written reason it was not fixed, in this log and bugs.md
- [ ] tsc and eslint clean

## Notes / log
- 2026-10-29 · coo (Ankit): CEO asked for the fix. Routed to CTO.
- 2026-10-29 · cto (Rahul): Owner frontend-engineer-2 confirmed. No small safe fix: (app)/loading.tsx wraps every child segment in Suspense, so headers (200) flush before any check in page/layout; generateMetadata+notFound does not help (metadata streams for non-bot UAs, Next 16 docs). Real fixes are a per-route loading.tsx refactor or a proxy existence check (~0.5-1 day each). Recommend won't-fix now (S4, noindex present); record reason in bugs.md.
- 2026-10-29 · frontend-engineer-2 (Nikhil): agree with won't-fix; a loading.tsx refactor or proxy check is not small or safe for an S4 with noindex present.
- 2026-10-29 · coo (Ankit): Won't-fix reason written to bugs.md BUG-001. Waiting on the CEO to agree; then Complete.
