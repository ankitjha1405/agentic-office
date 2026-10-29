---
key: ENG-7
title: "Product Quest: sitemap lists Pro-locked learning items (to-check 3)"
type: bug
product: Product Quest
status: In Review
category: In Review
priority: P3
owner: frontend-engineer-2
reporter: product-lead
created: 2026-10-29
due: 2026-10-30
links: [/Users/ankitkumar/dev/product-quest-fixes/src/app/sitemap.ts]
---

## Goal
Product lead decides whether Pro-locked items stay in the sitemap; engineering implements the decision.

## Acceptance criteria
- [ ] Decision with reason recorded by product-lead
- [ ] Decision implemented (or no-op recorded); access still decided only via src/lib/entitlements.ts
- [ ] tsc and eslint clean; one commit if code changed; bugs.md updated

## Notes / log
- 2026-10-29 · coo (Ankit): CEO asked for a decision with product-lead. Routed to product-lead and CTO.
- 2026-10-29 · product-lead (Arjun): Decision: drop locked items from sitemap. A locked visitor sees only lock badge + title + "This is part of Pro." (thin). Filter via filterAccessible() from entitlements.ts with a free, entry-level visitor viewer (select accessTier + requiredStageLevelId); no inline tier check. Discovery stays via /learning and /upgrade.
- 2026-10-29 · cto (Rahul): Owner frontend-engineer-2 confirmed. File: src/app/sitemap.ts only (~l.19-21: select accessTier + requiredStageLevelId, pass through filterAccessible() from entitlements.ts:140). Needs a visitor Viewer without creating an app_user row; check getViewer signature first.
- 2026-10-29 · frontend-engineer-2 (Nikhil): no code change, stopped per brief. Viewer = {userId, planKey, stageOrder, levelOrder}; getViewer inserts via provisionUser so unusable. Floor is the lowest stage.sortOrder/stageLevel.sortOrder row (provision.ts l.20-25), seed values 1/1, but sitemap has no such data and a literal would hardcode data (invariant 4). Decision needed: allow one read-only floor query in sitemap.ts (same orderBy as provision.ts) to build the viewer, then filterAccessible(); not run: tests/commit (shell blocked)
- 2026-10-29 · frontend-engineer-2 (Nikhil): sitemap.ts now selects accessTier + requiredStageLevelId, reads floor stage/level order (read-only, same orderBy as provision.ts), builds free viewer literal (userId unused by filterAccessible) and filters via filterAccessible(); not run: tests/commit (shell blocked)
- 2026-10-29 · coo (Ankit): Approved the read-only floor-level select. Reviewed sitemap.ts and filterAccessible: read-only, no user created, access still decided in entitlements.ts. bugs.md updated. Open: tests and commit (shell blocked).
