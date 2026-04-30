---
name: Project state snapshot — 2026-04-30
description: Full working state of NextCRM Designer at end of session. All Figma sections built, decisions sealed, pending work. Read this first when resuming.
type: project
originSessionId: 760c92ac-8a84-4d34-865f-7ab0d8a8baa2
---
# Project State — 2026-04-30

**Why:** End-of-session checkpoint. Captures every Figma section built, every decision sealed, and what's pending so the next session resumes cleanly.

**How to apply:** Read this on session start. Cross-reference with the Figma dashboard file (`NFCl7XHHO3xlUjE1Y2UUpg`) and the NextCRM-Designer git repo (https://github.com/valera56856/NextCRM_Designer).

---

## Repos & files

| What | Where |
|------|-------|
| Canonical design system doc | `NextCRM-Designer/DESIGN.md` (committed `b99cdbe` or later) |
| Agent routing rules | `NextCRM-Designer/CLAUDE.md` |
| Figma DS extract (47 pages, source of truth: `H1Ngineb53cAIqPWdqD585`) | `memory/figma-ds/` + `NextCRM-Designer/docs/` |
| Dashboard file extract (24 pages: `NFCl7XHHO3xlUjE1Y2UUpg`) | `memory/figma-dashboard/` + `NextCRM-Designer/dashboard/` |
| UX knowledge base (6 deep refs) | `memory/design-skills/ux-*.md` |
| Feedback memories (3 corrections) | `memory/design-skills/feedback-*.md` |
| Plugin API cookbook | `memory/design-skills/figma-plugin-api-cookbook.md` |
| Visual checklist + UX heuristics | `memory/design-skills/visual-design-checklist.md`, `ux-heuristics.md` |
| Project playbook | `memory/design-skills/working-on-nextcrm.md` |
| Audit reports | `NextCRM-Designer/design-reviews/` |

---

## Figma sections built on page `🟡 Центр сповіщень` (`10647:120412`)

All built during this session. Page is in dashboard file `NFCl7XHHO3xlUjE1Y2UUpg`.

### Section 1: `Notification Center — Full Flow PC` (`10885:5273`)
17 frames across 4 rows. Spec-compliant per user-provided notification rules.

**Row 1 — PC Bell flow (6 frames):**
- A1 Closed: bell with `06` badge
- A2 Hover bell: tooltip preview
- A3 Open dropdown: 6 unread, all `EDF9FF` highlighted, `Прочитати` on each
- A3.5 Auto-read: items still visible, normal bg, no dots, badge gone
- A4 Empty: after "Прочитати все"
- A5 Click notification: side drawer with order #8453 detail + "from notification" banner

**Row 2 — PC Inbox page (4 frames):**
- B1 Default: filter sidebar + 8 notifs
- B2 Filtered "Критичні": active chip + 6 critical items
- B3 Empty state
- B4 Click row: notification detail drawer with timeline

**Row 3 — PC Settings (1 frame):**
- C1 Notification preferences: per-event × per-channel matrix

**Row 4 — Mobile (6 frames):**
- M1 Closed
- M2 Open list (full-screen, only unread, highlighted)
- M2.5 Auto-read
- M3 Detail bottom sheet
- M4 Empty
- M5 Settings

**Cross-flow arrows:** purple dashed for cross-row, blue solid in-row, green for mobile.

**Real DS components used:** Logo (`df41f5a1...`, blue variant), 23+ verified Material icon keys.

### Section 2: `Menu Structure — Group & Sub-Item Icons` (`10898:5950`)
Visualizes sidebar menu structure with 4 groups and 9 sub-items. All icons distinct, color-coded per group. Plus assembled sidebar preview on the right.

**Layout:** vertical auto-layout (no overlap issues).

**Icons assigned** (see DESIGN.md "Menu Structure" section for full keys):
- 1. Початок роботи [blue] → Швидкий старт (`flash_on`), Налаштування (`settings`)
- 2. Робота з продажами [green] → Клієнти (`people`), Замовлення (`shopping_cart`), Платежі (`payments`)
- 3. Товари та склад [orange] → Товари (`storefront`), Склад (`warehouse`), Складські операції (`local_shipping`)
- 4. Фінанси та аналітика [indigo] → Платежі (`payments`), Аналітика (`insights`)

### Section 3: `Icon Alternatives — pick best per menu slot` (`10900:5324`)
Comparison sheet: 13 slots × 3 candidates = 39 icon options. Current pick highlighted in blue with `CURRENT` badge. Use this when user wants to swap an icon — reference by name.

---

## Decisions sealed during session

1. **NextCRM aesthetic** = Industrial/Utilitarian (not playful, not marketing-flashy). References: Stripe Dashboard, Linear, KeyCRM.
2. **Roboto** primary font. Resist Inter/Space Grotesk (convergence trap).
3. **Blue 600 (`#1886FE`)** primary. 6 semantic role colors. Restrained palette.
4. **Spacing**: 4/8 hybrid grid via tokens.
5. **No emoji as icons**, ever. Only DS Material Symbols.
6. **Match existing system**, never recreate generic. Use real existing frames as base.
7. **Notification spec rules** (user-provided): only unread in dropdown, max 15, EDF9FF highlight, Прочитати on each, auto-read state preserves visibility.
8. **Real DS Logo** (`df41f5a13a1fc34dda0cf516ae99d5bb25007afe`, blue variant) — never custom-drawn.
9. **Sidebar item heights**: fixed 40px (HUG default broke spacing — see plugin-api-cookbook).
10. **Menu icon assignments** sealed (4 groups + 9 sub-items, no AI-generated icons).

---

## Pending / open

- **Mobile flow validation**: user said "+" to proceed; mobile row built but not explicitly approved. May need iteration.
- **Icon swap decisions**: user has 39-icon comparison sheet but hasn't made any swap requests. Default current picks stand.
- **Toast / push notification frames**: not yet built. Spec mentions toasts but flow only covers in-app dropdown + page + mobile.
- **Settings page mobile (M5) consistency**: simplified layout — may need polish.
- **Cross-page consistency**: notification center is done. Other pages (Замовлення, Клієнти, Аналітика) not yet redesigned.

---

## Token to access Figma REST API

User shared `figd_tVAo-...` early in session. **Recommended action:** revoke and create new token, store in `~/.zshrc` as `FIGMA_TOKEN` env var. Scripts in `NextCRM-Designer/scripts/` read from env.

---

## Key git commits (NextCRM-Designer repo)

| Commit | What |
|--------|------|
| Initial dump | Design system mirror (47 pages) |
| Dashboard mirror | 24 product pages |
| design-skills knowledge base | 6 UX deep refs |
| Notification flow v3-v5 | Iterative mockup builds |
| Spec compliance round | Filter dropdown to unread only, bg highlight, auto-read |
| `318e630` | DESIGN.md + CLAUDE.md created |
| `64c8f91` | Mobile flow + A3.5 sidebar fix |
| `989d57b` | Sidebar density fix (HUG → fixed 40px) |
| `12c4c2f` | Real DS Logo applied to all 10 sidebars |
| `a0ebe2b` | Spec compliance: only unread + highlight + auto-read state |
| `af552fc` | Menu structure icon assignments documented |
| `b99cdbe` | Icon picker reference (13 slots × 3 candidates) |

---

## Resume checklist for next session

1. Read `MEMORY.md` index (3 design-skills files relevant to current task)
2. Read this file (`state-snapshot-2026-04-30.md`)
3. Read `DESIGN.md` and `CLAUDE.md` from NextCRM-Designer repo
4. Check Figma sections still exist on page `🟡 Центр сповіщень`:
   - `10885:5273` (Full Flow PC), `10898:5950` (Menu Structure), `10900:5324` (Icon Picker)
5. Ask user what to do next — likely candidates:
   - Approve mobile or request adjustments
   - Swap specific icons from picker
   - Start next page redesign (Замовлення / Клієнти / Аналітика)
   - Build toast/push notifications addendum
