---
title: Portfolio floorplan: visual spec
owner: design-lead
status: approved
created: 2026-11-06
updated: 2026-11-06
task: DES-1
---

## Data shape (per project, built from inventory-a.md + inventory-b.md)
`{project, kind, url, status: live|gated|excluded, reason, pages:[{name, path, auth?, src: code|site}], links:[[fromPath, toPath]]}`

## Canvas
One SVG, viewBox 1600x1000, scales to width; under 900px scrolls inside its own frame. No label under 12px at 100%.

## Floor layout
Four wings around a central lobby ("Portfolio", holds the legend). Inventory may move a project between wings.
- Top left, Products: kosh, oscar-board, product-quest, daily-quest, primer-dashboard, haunted-terminal, hustlkr, gitavatar
- Top right, Foxo and work: foxo-heart-age, foxoclub, loan24-onboarding, loqelo-prelaunch
- Bottom left, Sites and portfolio: portfolio-v2, aurele-atelier
- Bottom right, Experiments and excluded: pmforces, v0-todo-list-app, v0-todo-app-requirements
Test early for crowding; adjust within these rules.

## Rooms
- Size: 160x120 base + 36x24 per page, snapped to a 20px grid. Each page a 60x40 sub-room; >8 pages use 4 columns. Size shows page count only (say so in legend).
- Pages: rounded rects, monospace route label ("/pricing"). Small "c"/"s" dot = from code / from site.
- Doors: 14px wall gap with small arc. Corridors: 6px light strip between doors; arrowhead if one-way. Only real links. Each room has a front door facing the lobby, labelled with URL host.
- Gated pages: dashed wall + lock icon + "login" tag.
- Excluded projects: grey, hatched, no page rooms, one-line reason.

## Tokens (light / dark), on :root, redefined under prefers-color-scheme: dark (guarded by :root:not([data-theme=light])) and :root[data-theme=dark]
--bg #F6F3EC / #14161A · --wall #2B2F36 / #C9CDD4 · --room #FFFFFF / #1E2228 · --page #EEF2F7 / #262B33 · --corridor #E3DCCB / #323843 · --text #1B1E23 / #ECEEF2 · --accent #1F7A5C / #4CC9A0 · --gated #B4571B / #F0A267 · --excluded #8A8F98 / #7B818B · one wing tint each at ~12% opacity.

## Type
System UI stack; ui-monospace for routes. Wing titles 20px, project names 16px semibold, pages 12px.

## Legend (lobby)
Live room, gated, excluded, door, corridor, sizing rule, c/s marker, data date.

## Interaction
Hover/focus highlights a room. Click/Enter opens side panel: name, URL (plain text, not a link), status, page list with c/s marks, exclusion reason. Esc closes. Rooms: tabindex, role="button", aria-label. Visually hidden <ul> mirrors all content. No libraries, no external requests, works offline.

## Review checklist
1. All 17 projects present (included, or excluded with reason).
2. Pages and links match inventory; c/s marks right; no invented routes.
3. Contrast ≥4.5:1 text, ≥3:1 walls, both themes.
4. Gated/excluded not colour-only.
5. Keyboard + screen reader work; panel does not trap focus.
6. No overlap/clipping; no label <12px; reads at 1280px.
7. One file, no external requests.
8. Legend complete, sizing rule stated.
9. inventory.md has owner header and dates.
10. No deploy, publish or auto-opened URLs.
11. Zoya and Karthik logged in task file.
