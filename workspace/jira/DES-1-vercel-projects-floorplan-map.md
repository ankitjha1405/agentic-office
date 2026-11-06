---
key: DES-1
title: Visual floorplan map of every live project on the CEO's personal Vercel account
type: task
product: Company
status: Done
category: Complete
priority: P2
owner: visual-designer
reporter: coo
created: 2026-11-06
due: 2026-11-08
links: [workspace/confluence/products/portfolio-floorplan/]
---

## Goal
One visual map, drawn as an office floorplan, that shows every live project the CEO has on Vercel. Each project is a room. Inside each room: its main pages/screens as smaller rooms, with doors/corridors for how a user moves between them. The CEO should see the whole portfolio and each product's structure at a glance.

## Projects (Vercel team `jhaankitkumar12-gmailcoms-projects`, listed 2026-11-06)
| Vercel project | Live URL | Local code |
|---|---|---|
| kosh | https://kosh-murex.vercel.app | ~/dev/kosh |
| haunted-terminal | https://haunted-terminal-lovat.vercel.app | ~/haunted-terminal |
| loqelo-prelaunch | https://loqelo-prelaunch-iota.vercel.app | ~/dev/loqelo-site |
| product-quest | https://product-quest-two.vercel.app | ~/dev/product-quest |
| aurele-atelier | https://aurele-atelier.vercel.app | ~/dev/atelier-site |
| oscar-board | https://oscar-board.vercel.app | ~/dev/oscar-board |
| daily-quest | https://daily-quest-eta-sandy.vercel.app | ~/Documents/Dummy Claude Project/projects/websites/daily-quest |
| foxo-heart-age | https://foxo-heart-age.vercel.app | ~/Documents/Dummy Claude Project/projects/websites/foxo-heart-age |
| primer-dashboard | https://primer-dashboard-five.vercel.app | ~/dev/primer-dashboard |
| foxoclub | https://foxoclub.vercel.app | ~/dev/foxo-site |
| gitavatar | https://gitavatar.vercel.app | ~/Documents/Dummy Claude Project/projects/websites/gitavatar |
| loan24-onboarding | https://loan24-onboarding.vercel.app | ~/Documents/Dummy Claude Project/projects/websites/loan24-onboarding |
| portfolio-v2 | https://ankitjha1405.vercel.app | ~/dev/portfolio-v2 |
| hustlkr | https://hustlkr.in | ~/Documents/Dummy Claude Project/projects/apps/hustlkr |
| pmforces | https://pmforces.vercel.app | (none found) |
| v0-todo-list-app | https://v0-todo-list-app-beta.vercel.app | (none found) |
| v0-todo-app-requirements | https://v0-todo-app-requirements-eight.vercel.app | (none found) |

## Acceptance criteria
- [x] Every project above checked: live and real, or excluded with the reason (dead URL, v0 demo, placeholder).
- [x] For each included project: its pages/screens and the links between them, taken from the code (routes) or the live site. Each fact marked as from code or from site.
- [x] One self-contained HTML file with inline SVG: `workspace/confluence/products/portfolio-floorplan/floorplan.html`. Works offline, readable in light and dark, labels legible, rooms named, a legend.
- [x] Inventory saved as `workspace/confluence/products/portfolio-floorplan/inventory.md` with owner header.
- [x] Design Lead review passed.
- [x] Not deployed or published anywhere (needs CEO approval).

## Notes / log
- 2026-11-06 · coo (Ankit): CEO asked for a visual floorplan map of all live Vercel projects (Oscar Board #107). Routed to Design Lead.
- 2026-11-06 · coo (Ankit): Briefed design-lead (Ananya) for visual spec + review checklist. Started product-designer (Karthik) on page inventory in two batches (inventory-a.md, inventory-b.md). Visual-designer (Zoya) draws once both are in.
- 2026-11-06 · design-lead (Ananya): Confirmed Karthik (inventory) + Zoya (drawing). Wrote visual spec, data shape and 11-point review checklist; saved as workspace/confluence/products/portfolio-floorplan/visual-spec.md.
- 2026-11-06 · coo (Ankit): Approved data shape. Site-only evidence is acceptable for the no-code projects (pmforces, 2 v0 apps); no need to involve CTO. Zoya starts after both inventory batches, on real data, to avoid a double build.
- 2026-11-06 · product-designer (Karthik): Batch A inventory done (inventory-a.md). All 9 live; primer-dashboard fully login-gated (structure only). product-quest ~35 routes (grouped). Flags: aurele-atelier contact form is a placeholder (demo-grade); kosh / and product-quest gating inferred, not tested; foxo-heart-age Primer CTA points at foxo.club (code TODO).
- 2026-11-06 · coo (Ankit): Keep aurele-atelier in, with a "demo-grade: placeholder form" note in its panel. Inferred gating shown as gated with source "code, inferred".
- 2026-11-06 · product-designer (Karthik): Batch B inventory done (inventory-b.md). All 9 return 200. Include 7; suggest excluding both v0 todo apps (generic v0 demos, near-duplicates). hustlkr biggest (~32 routes). portfolio-v2 redirects to ankitjha1405.tech. One is a personal page.
- 2026-11-06 · coo (Ankit): Exclude both v0 apps ("v0 demo"). One personal page left off the map. Inventory = inventory-a.md + inventory-b.md. Handed to visual-designer (Zoya).
- 2026-11-06 · visual-designer (Zoya): Built floorplan.html (SVG generated from a PROJECTS array, no external requests) + floorplan.png. Self-check passes items 1-8, 10. Spec changes: viewBox 1600x2582 (too crowded at 1000), wider page cells, room growth not literal 36x24/page, light excluded/gated tokens darkened for contrast, added CROSS corridors (portfolio-v2 to hustlkr, pmforces).
- 2026-11-06 · coo (Ankit): Checked screenshot: all present, readable. Added inventory.md index. Status In Review; sent to design-lead.
- 2026-11-06 · design-lead (Ananya): APPROVE. Accepted all 5 deviations. Spot-checked 6 projects vs inventory: pages, c/s marks, gating, links match; a11y and offline OK. Fixed bottom-row split (canvas now 1600x2426), re-rendered PNG. Risks: text ~9.5px at 1280px wide; hustlkr inventory says 17 calculators but lists 15.
- 2026-11-06 · coo (Ankit): Removed personal name from inventory-b.md (repo is public). Closed. Oscar Board #107 done.
- 2026-11-06 · coo (Ankit): CEO asked to remove the personal page entirely. Removed from map, inventory, spec and this ticket; map now 17 projects.
