---
name: UX — Data Density (Tables, Forms, Dashboards)
description: How to design data-heavy interfaces. Tables, forms, dashboards, KPI cards, lists. Critical for CRM. Density vs scanability tradeoffs.
type: reference
originSessionId: 760c92ac-8a84-4d34-865f-7ab0d8a8baa2
---
# UX — Data Density

CRMs are data-heavy. The right density makes operators 3x faster. Wrong density slows them or hides errors.

## Density tiers

| Tier | Row height | Padding | Use case |
|------|-----------|---------|----------|
| **Compact** | 32-40px | 4-8px | Power-user tables (orders, transactions) — they want max rows visible. |
| **Default** | 44-52px | 12-16px | General lists, cards | 
| **Comfortable** | 56-72px | 16-24px | Marketing, low-frequency views |
| **Spacious** | 80px+ | 24-32px | Empty states, hero sections |

**Rule of thumb:** if user looks at ≥20 rows in a session, go compact. If <10, default is fine.

## Tables

The most-misdesigned UI in B2B. Here's the playbook.

### Anatomy
1. **Toolbar** (above): search, filter chips, sort, density toggle, column picker, bulk actions when selection active, "+ Create" CTA.
2. **Header row** (sticky): column labels, sortable indicators, resize handles.
3. **Body rows**: data, hover state, selection state, inline actions on hover.
4. **Footer**: pagination, total count, export.

### Column design
- **Number columns right-aligned, monospace tabular-nums.** "1 245 ₴" aligns visually so scanning differences is fast.
- **Text columns left-aligned.** Always.
- **Status columns center or left.** Color-coded pills.
- **Action columns right-aligned**, icon-only, hover-revealed (pencil/trash/more).
- **Avatar/photo columns**: 32×32px circle, far left.
- **Date columns**: relative for recent (`2 хв тому`), absolute for older (`30.04 14:08`).

### Column widths
- Don't auto-fit — users can't predict the layout.
- Set sensible defaults: ID 80px, name 200px, money 120px, status 120px, date 140px, actions 80px.
- Allow resize. Persist to user settings.
- Sticky first column on horizontal scroll (mobile / wide tables).

### Header behavior
- **Click to sort.** Single ↑/↓ arrow indicates sort direction.
- **Sort indicator** subtle when inactive, bold when active.
- **Multi-sort** (shift+click): power feature, hide from tooltip.
- **Resize**: cursor changes on header edge, drag to resize.

### Row interactions
- **Hover state**: subtle bg darken (gray-50). Reveals action icons.
- **Click row**: navigates to detail OR opens side drawer (NOT a modal — modals don't allow comparison).
- **Click checkbox**: enters selection mode — toolbar morphs into bulk-action bar.
- **Right-click**: context menu (advanced; mobile users won't have this).
- **Inline edit**: double-click cell to edit. Save on blur or Enter. Esc cancels.

### Empty cells
- Render `—` (em dash), not blank.
- "Not provided" for fields that should have data.
- Don't use `null` or `N/A` — feels engineery.

### Pagination vs infinite scroll
- **Pagination** when users need to know "how many" (data integrity, audit, exports).
- **Infinite scroll** when users browse (social feeds, search results).
- **Hybrid**: load 50 at a time, show "Load 50 more" button + total count.

### Empty state
NEVER render an empty table. Replace with:
- Illustration or icon (decorative)
- One sentence explaining what this view IS
- Primary CTA to add the first item ("+ Створити перше замовлення")
- Optional: link to docs or sample data import

### Error state
- Banner above table: "Не вдалось завантажити (network error). [Повторити]"
- Don't blank the screen. If stale data exists, keep showing it with a stale indicator.

### Density toggle
Some tables benefit from user-controlled density:
- Dropdown with 3 options: Compact / Default / Comfortable
- Persist per-table per-user
- Default to most useful for that view (transactions = compact, customers = default)

### Filter UX
- **Chip pattern**: filters render as removable chips above the table. "Status: Active ✕"
- **Filter sidebar** for many facets (>5 categories of filters).
- **Filter modal** for casual one-time filtering.
- **Saved filters / Views**: power feature, allow naming "My open orders".

### Bulk actions
- Checkbox column far-left (master checkbox in header).
- Selection count anchors a floating action bar: "5 selected" + actions: Archive, Export, Delete.
- Position floating bar at bottom (Mac convention) or top (Windows convention) — pick one.
- Esc deselects everything.

## Forms

Forms are conversations. The user has something to say; the system listens.

### Field groupings
- Group related fields under a section header.
- Section spacing: 32-48px between groups.
- Within group: 16-24px between fields.

### Labels
- **Always visible.** Above the field for scannability, NOT placeholder-as-label (placeholder disappears when typing — kills error recovery).
- **Top-aligned labels** read fastest (research consensus).
- **Required mark**: asterisk after label `Email *` OR mark optional fields `Phone (optional)`. Pick one. Don't do both.
- **Field width matches expected input.** Phone field shouldn't be 600px wide. Postal code shouldn't be full-width.

### Placeholder text
- For format hint only: `+380 67 555 1234`
- NEVER as the only label.
- Color: `gray-500` (4-5:1 contrast minimum).

### Validation
- **Validate on blur, not on every keystroke.** Eager validation feels naggy.
- **Error message inline below field**, not at top of form.
- Error message format: what's wrong + how to fix. "Email must be in format `name@example.com`" beats "Invalid email".
- **Color + icon + text** — don't rely on color alone (colorblind users).
- **Success state on blur** for password strength meters, username availability checks.

### Smart defaults
- Country/timezone from IP.
- Currency from locale.
- Date today.
- Recently-used values pre-filled.
- Dramatically reduce field count via inference.

### Input types
- Use HTML5 input types: `email`, `tel`, `url`, `number`, `date`, `time`. Mobile keyboards adapt.
- **Date pickers**: provide both typed-in and calendar-pick options.
- **Phone**: format as user types (mask). Accept paste with various formats.
- **Currency**: right-align value, currency symbol fixed left/right per locale (₴ on right in UA).
- **File upload**: drag-drop zone + button. Show preview after upload.

### Autosave vs explicit save
- **Autosave** for long forms, drafts, settings. Show "Saved" indicator.
- **Explicit save** for transactional commits (place order, send invoice) — user must consciously trigger.
- Hybrid: autosave drafts, explicit Save+Submit at end.

### Multi-step forms
- ≤5 steps. Beyond = user abandonment spike.
- **Visible progress** at top: "Step 2 of 4 — Customer info".
- **Allow back navigation** without losing data.
- **Save draft** after each step.
- **Show summary** before final submit ("Review and confirm").

### Field ordering
- Easy → hard. Most-known → least-known. Builds momentum.
- Group by user mental model, not DB schema.
- Required first, optional last (within a section).

### Error recovery
- After failed submit, focus jumps to FIRST error field.
- Error summary at top: "3 fields need attention" + jump links.
- Preserve all entered values. Never blank a form on error.

### Cancel/exit
- "Cancel" or "Discard" button — clearly secondary styling.
- Confirm if there are unsaved changes: "You have unsaved changes. Discard them?"
- Esc key triggers cancel in modals.

## Dashboards

Dashboards answer "What should I pay attention to?"

### KPI selection
**Show ≤6 top-level KPIs above the fold.** More = visual noise, no focal point.

Each KPI needs:
- **Metric label** (small, gray): "Сьогодні замовлень"
- **Big number** (24-32px bold): "47"
- **Trend indicator**: "+8% від вчора" with green/red color
- **Optional**: tiny sparkline (last 30 days)

Skip "engagement" KPIs (page views, session duration) for B2B CRMs. Show actionable: orders, revenue, conversion, alerts.

### Chart types
- **Line**: trends over time (single metric).
- **Bar**: comparison across categories.
- **Stacked bar**: category breakdown over time.
- **Pie**: ≤4 segments. Beyond = use bar.
- **Area**: cumulative trends.
- **Sparkline**: tiny inline trend, no axes — just the shape.
- **Heatmap**: 2D pattern (hours × days for activity).
- **Geo map**: spatial data only.

### Time range picker
- **Presets**: Today, 7 days, 30 days, This month, Last month, This year, Custom.
- **Compare to previous period** as a toggle (built-in compounding insight).
- **Persist last selection** per user per dashboard.

### Drill-down
- Click a KPI → go to filtered list view (e.g., click "47 orders today" → orders list filtered to today).
- Click a chart segment → go to detail view.
- Always provide a way back (breadcrumb).

### Real-time vs cached
- **Real-time**: payments, alerts, support tickets — minutes matter.
- **Hourly refresh**: most dashboards. Show "Updated 14 minutes ago" indicator.
- **Daily**: business reporting, financial summaries.

### Customization
- Power feature: drag-drop widgets, save layouts.
- Don't ship until you have ≥10 default users — observe what they want first.
- Reset-to-default option always available.

### Empty/zero states
- New tenant with no data: show explanatory illustration + "Create your first order" CTA.
- Specific metric at zero: don't hide. Show "0" honestly. "0 errors today" is a positive signal.

### Mobile dashboards
- Stack vertically. KPIs full-width.
- Charts: simplified (drop axis labels, smaller).
- Hide secondary cards behind tabs or "see all" link.
- DON'T show 12 cards with 2-column grid on mobile — too dense to read.

## Lists (non-table)

When data isn't tabular but is repeating: customers, conversations, notifications.

### List item anatomy
- **Avatar/icon** left.
- **Title** (Medium weight): primary identifier.
- **Description** (Regular, muted): one line of context.
- **Metadata** right: time, count, status.
- **Action affordance**: chevron, arrow, or implicit row-click.

### Hierarchy patterns
- **Flat list**: no nesting.
- **Grouped list**: section headers (e.g., "Today / Yesterday / This week").
- **Tree list**: indented, expandable. Use sparingly — comprehension cost.

### Selection
- Single-select: row highlights, no checkbox.
- Multi-select: checkboxes. Use sparingly — confuses users vs tables where it's expected.

### Pagination patterns
- Show first 10-20.
- "Load more" button vs scroll-trigger: "Load more" gives user control.
- Infinite scroll only when browsing is the goal.

## Card grids

When items are visual / non-tabular (products, projects, dashboards).

- **3-4 columns desktop, 2 tablet, 1 mobile.**
- Equal aspect ratio for visual rhythm.
- Hover: lift + shadow (2-3px translateY, soft shadow).
- Card content hierarchy: image → title → metadata → CTA.

## Anti-patterns to refuse

- ❌ Tables with 12+ columns and no horizontal scroll affordance.
- ❌ Forms with 30+ fields on one screen.
- ❌ Dashboards that show 15 KPIs (none of them stand out).
- ❌ Pagination in a screen that has 8 items total (just show them all).
- ❌ Sorting that resets when you navigate away and back.
- ❌ Filters that don't show in the URL (can't share or bookmark).
- ❌ Inline edit that loses data on Esc without warning.
- ❌ "Delete" without confirmation OR undo (always one or the other).
- ❌ Empty state showing the table chrome (header, pagination) — looks broken.

## Decision rules

- **Table vs list**: structured comparable data → table. Repeating non-tabular items → list. People → list. Orders → table.
- **Modal vs side drawer vs inline**: 
  - Quick edit (1 field) → inline.
  - Detail view (read + light edit) → side drawer.
  - New record creation → modal OR full page.
  - Confirmation → modal.
- **Dropdown vs radio vs toggle**:
  - Boolean → toggle.
  - 2-3 options visible → radio.
  - 4+ options OR space-constrained → dropdown.
  - Multi-select → checkbox group OR multi-select dropdown.
