# Design Audit — Notification Flow

**Date:** 2026-04-30
**Target:** Figma section `Notification Flow` on page `🟡 Центр сповіщень` (file `NFCl7XHHO3xlUjE1Y2UUpg`)
**Auditor:** Claude (Opus 4.7) using NextCRM design-skills checklist
**Mode:** Figma mockup audit (manual — `/design-review` skill is for live sites; this used the same checklist on a static design)

## Result

| Score | Before (v3) | After (v4) |
|-------|-------------|------------|
| **Design Score** | B+ | **A−** |
| **AI Slop Score** | A | A |
| Frames audited | 6 | 6 |
| Findings | 10 | 5 (fixed) + 5 (deferred) |

## Phase 1 — First Impression

### Desktop (Step 2 — Open dropdown)
The site communicates **competence** — clean, business-oriented, not clownish SaaS. Eye lands first on KPI numbers (`24` `1 845₴` `47`), then notification dropdown with color-coded icons, then sidebar. One word: **professional**.

⚠️ Hierarchy lied in v3: sidebar showed `Аналітика` highlighted but content was `Замовлення` — immediately signaled inconsistency.

### Mobile (Step 2 — Notifications list)
Communicates **mobile-native** feeling — top nav OK, bottom tab bar present, list compact. One word: **functional**.

⚠️ Big empty zone under last notification looked like clipped content, not intentional design.

## Findings Triage

### Fixed in v4

| # | Title | Impact | Category | Status |
|---|-------|--------|----------|--------|
| F1 | Action buttons missing on notification cards | HIGH | Interaction States | ✅ Fixed |
| F2 | Mobile: empty zone under list looks like a bug | HIGH | Spacing & Layout | ✅ Fixed |
| F3 | Sidebar active item didn't match content page | HIGH | Visual Hierarchy | ✅ Fixed |
| F4 | Table rows too tall for CRM density | HIGH | Spacing & Layout | ✅ Fixed |
| F6 | Sidebar dot indicator on inactive items adds noise | MEDIUM | Visual Hierarchy | ✅ Fixed |

### Deferred (medium / polish — for next pass)

| # | Title | Impact | Category | Why deferred |
|---|-------|--------|----------|--------------|
| F5 | KPI cards visually identical regardless of trend | MEDIUM | Visual Hierarchy | Needs user input on whether to bg-tint cards by trend (might create alarm fatigue) |
| F7 | Mobile time text borderline tap-friendly | MEDIUM | Typography | Half-fixed (11→12px); could go to 13px on the other states |
| F8 | Mobile tab chip clipping at right edge | MEDIUM | Responsive | Reduced 4 tabs→3 in v4; if tabs return to 4, need scroll affordance |
| F9 | Page header & KPI value share weight at 24px | POLISH | Typography | Minor; clear visual contrast via position |
| F10 | Date label contrast 3.7:1 — borderline | POLISH | Color & Contrast | Acceptable for non-text decoration per WCAG |

## Per-Category Grades (v4)

| Category | Grade | Notes |
|----------|-------|-------|
| Visual Hierarchy | **A−** | Sidebar matches content; action buttons restore the "user can act inline" affordance |
| Typography | B+ | Roboto, 3 weights, scale OK. Mobile time bumped to 12px. |
| Color & Contrast | B+ | 5 semantic colors, status pills color-coded |
| Spacing & Layout | B+ | Table density tightened; mobile list extended |
| Interaction States | A− | Action buttons restored; bell has hover state |
| Responsive | A− | Mobile patterns clean; no clipped tabs |
| Motion | n/a | Static mockup |
| Content & Microcopy | B+ | Real Ukrainian copy, specific labels |
| **AI Slop** | **A** | Real DS Material icons, no purple gradients, no SaaS clichés |
| Performance Feel | n/a | Static |

## Goodwill Reservoir Trajectory

Starting goodwill: 70/100

| Step | Action | Δ | Score |
|------|--------|---|-------|
| 1 | Login (assumed) | +5 obvious primary | 75 |
| 2 | See bell badge "4" | 0 (clear count) | 75 |
| 3 | Click bell → dropdown | +10 immediate, no lag | 85 |
| 4 | Read 4 unread | +5 categorized icons make scanning fast | 90 |
| 5 | Action button under "Нове замовлення" | +10 inline action, no context switch | 100 (capped) |
| 6 | Click "Постачання" | +5 specific verb (not "Click here") | 100 |
| 7 | "Прочитати все" → empty state | +5 reassuring "Все під контролем" | 100 |

**Final: 100/100 ✅** — healthy reservoir, no friction points identified.

## Trunk Test (per page)

### Desktop (open state)
1. Site? `NextCRM` brand top-left ✅
2. Page? `Замовлення` breadcrumb + page title ✅
3. Sections? Sidebar nav visible with current section highlighted ✅
4. Options? "+ Нове замовлення" + Filter + bell ✅
5. Where? Sidebar `Замовлення` active ✅
6. Search? Top bar `Пошук ⌘K` ✅
**PASS (6/6)**

### Mobile (notifications view)
1. Site? Bottom NextCRM-style nav ✅
2. Page? `Сповіщення` title prominent ✅
3. Sections? Tabs visible ✅
4. Options? Each notification tappable ✅
5. Where? Active `Сповіщення` in bottom bar ✅
6. Search? Missing (acceptable for notif list)
**PASS (5/6)**

## Hard Rules Check

Universal:
- ✅ Define CSS variables for color (using NextCRM tokens)
- ✅ No default font stacks (Roboto, real typeface)
- ✅ One job per section
- ✅ Cards earn their existence (notification cards = the interaction)
- ✅ Body text >=16px or proper hierarchy
- ✅ Visible labels (no placeholder-as-label)

Litmus checks:
1. Brand/product unmistakable in first screen? **YES** (NextCRM mark + sidebar)
2. One strong visual anchor? **YES** (KPI row)
3. Page understandable by scanning headlines? **YES**
4. Each section has one job? **YES**
5. Are cards actually necessary? **YES** (notif card = the interaction unit)
6. Does motion improve hierarchy? n/a (static)
7. Would design feel premium with all decorative shadows removed? **YES** (shadows are functional — popover elevation, not ornament)

**All 7 PASS.**

## Output

**Figma section:** `10875:5236` — `Notification Flow — Claude mockup v4 (post design-review)`
**Frames:**
- Desktop: `10875:5241` (closed), `10875:5400` (open), `10875:5667` (empty)
- Mobile: `10875:5852` (dashboard), `10875:5922` (notifications), `10875:6066` (empty)

**Predecessors deleted:** v1 (10863:5139), v2 (10865:5139), v3 (10867:5139, 10872:5197) all cleaned up.

## Recommendations for next iteration

1. **F5 — KPI trend tinting** (medium): consider faint green/red bg on cards with positive/negative deltas. Start with subtle (5% saturation) — alarm fatigue risk if too saturated.
2. **F7 — Mobile time legibility** (medium): bump time to 13px on all mobile rows for thumb-distance readability.
3. **F8 — Tab overflow indicator** (medium): if mobile gets 4+ filter tabs, add "..." or fade-edge to signal scrollability.
4. **Add tablet breakpoint** (768): both desktop and mobile defined; tablet needs design (sidebar collapsible, dropdown becomes drawer).
5. **Add settings page** (next feature): user clicked "Налаштувати сповіщення" in the empty state — that page doesn't exist yet.

## v5 → v5+context (post-feedback)

User feedback: "Не такой как у меня в системе + есть много пробелов в дизайне"

### What changed
1. Dropped my generic dashboard recreation
2. Built compact dropdown matching the existing "Швидкий перегляд" reference exactly:
   - 372w, no tabs, no date groups
   - "06" badge format (not "4")
   - Red warning-triangles for errors, orange for system events
   - Inline "Прочитати" link as text-link, not button
   - Unread indicator as small blue dot (not full-card tint)
3. Added "Real interface context" frame (1440×900):
   - NEXT/CRM red-accent brand mark
   - Real sidebar with line icons per item (shopping_cart, chat, category, warehouse, description, analytics, settings, support_agent)
   - Expandable items with keyboard_arrow_down chevrons
   - Active state: blue bg + chevron + badge
   - Top bar: breadcrumb + bell + avatar with dropdown chevron
   - Status filter tabs with counts (Всі/Нові/У роботі/Доставка/Завершені)
   - Real Замовлення table with status pills
   - Dropdown overlay anchored under bell

### Final score
**A** (was A− at v4) — visual language now matches user's existing system.

