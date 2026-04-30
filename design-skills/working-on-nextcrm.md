---
name: Working on NextCRM (project-specific design playbook)
description: Concrete rules for designing inside NextCRM — DS file, Dashboard file, conventions used, where to find things. Read this BEFORE starting any design task on this project.
type: reference
originSessionId: 760c92ac-8a84-4d34-865f-7ab0d8a8baa2
---
# Working on NextCRM — Design Playbook

## Two Figma files

| File | Key | Purpose |
|------|-----|---------|
| **NextCRM Design System** | `H1Ngineb53cAIqPWdqD585` | Tokens, components (Button, Badge, Tags, etc.). Edit only when adding/refining DS components. |
| **NextCRM - Dashboard** | `NFCl7XHHO3xlUjE1Y2UUpg` | Actual product screens. CONSUMES components from DS. This is where mockups go. |

Both already mirrored locally:
- `~/.claude/.../memory/figma-ds/` — DS, 47 pages, all components catalogued
- `~/.claude/.../memory/figma-dashboard/` — Dashboard, 24 pages
- Both pushed to https://github.com/valera56856/NextCRM_Designer

## When user asks for a design

### Step 1: Read the relevant page memory
Open `figma-dashboard/pages/<page>.md` for the target page. It has:
- NodeId of the page (use as `nodeId` in Figma MCP calls)
- All sections / top-level frames with IDs
- Status (✅ done / 🟡 in-progress / 🔴 not-started)

### Step 2: Don't redesign what exists
If user says "design feature X on page Y" and page Y already has frames "X — view A" / "X — view B", screenshot those FIRST. Match the existing visual style. Only invent when nothing exists.

### Step 3: Use DS components
Components I've imported successfully:
- **Button / new** key `4af7bd61bebb20595ea64f8ed9f53cf7a11c3c76` — has `Type / State / Size / Style` variant axes (Primary/Success/Danger × Enabled/Hover/Active/Disabled/Focus/loading × small/medium × Fill/Outline/Ghost)
- **Tags** key `0e88e70b5ac17f4d01d5dce19bfec079ba01d7b2`
- **Badge-rounded** key `c063dcfd3933ac4622cb0410871314b8925c5295`
- **Mob - navbar** key `64e9a9aba55c2f7769cbb62fbe28df73245373ec`
- **Mob - tab** key `70bf0d47a6301cc11028513afdb1519eebd231d5`
- **Mob - navigationButton** key `7dbfca8308145d5fc4666faec3c08fe360c34de0`
- **Mob - nav_bar** key `3df2b6a6e797de4dc8609e028856ee3231de2460`

When importing Button, find specific variant by name match — e.g. `Type=Primary, State=Enabled, Size=small, Style=Fill`. See `figma-plugin-api-cookbook.md` for code.

### Step 4: Place mockup BELOW or BESIDE existing content
Pages have absolute coordinates. Find rightmost/bottom of existing content, place new SECTION clearly separated (≥200px gap). Name it `💠 <Feature> — Claude mockup vN`.

### Step 5: Ship 3 views minimum
For any feature, design at least:
1. **Default** state (with data)
2. **Empty** state (no data) — reassuring copy + CTA
3. **Mobile** version (375×812) — different layout, not just shrunk desktop

Add error state if applicable.

## Design tokens (for code generation)

CSS tokens live in user's repo at `src/components/ui/tokens.css`. When writing code, never use raw hex — always reference variable. Map:
- `Blue 600` (#1886FE) → `var(--blue-600)` — primary action
- `Blue 50` (#EDF9FF) → tinted background for blue-icon chips
- `Gray 200` (#DCDCDC) → borders, dividers
- `Gray 700` (#525252) → secondary text
- `Gray 950` (#292929) → primary text
- `Green 600` (#10A957) → success
- `Orange 700` (#C54009) → warning text on orange-100 chip
- `Red 600` (#F10909) → danger / unread badge

Spacing: `--space-{0,2,4,6,8,10,12,16,20,24,32,40,48}`. Stick to these.

Typography: Roboto. Sizes 11–48 from token list. Never custom sizes.

## Conventions noticed in existing screens

### Sidebar nav (desktop)
- Width 278px when expanded, 56px collapsed
- Items: icon + label, 12px gap
- Active: blue-50 background + blue-600 text + 3px left accent
- Hover: gray-100 background
- Sub-items indented 24px

### Top bar (desktop)
- 52px tall, white background, gray-200 bottom border
- Left: breadcrumbs in gray-700, separator `/` in gray-400
- Right: search (⌘K), bell with red dot, avatar dropdown

### Page content area
- 32px padding from sidebar/top bar edges
- Page title: 24px Bold gray-950, 32px below top bar
- Section between content blocks: 24px gap

### Tables (existing in Замовлення, Товари, Клієнти)
- Row height ~52px (compact)
- Header: 12px Medium gray-500 uppercase, gray-50 bg
- Hover row: gray-50
- Selected row: blue-50
- Status pills inline (Tags component)

### Cards (KPI on dashboard)
- White bg, 12px radius, 1px gray-200 border
- 20-24px padding
- Light shadow on hover only

### Mobile patterns (existing in Mob - components)
- Status bar at top (system clock, signal, battery)
- App top nav: back button (28px), title, action icon (28px)
- Bottom tab bar: 4-5 items, 24px+24px safe area at bottom
- Cards: less padding (12px), full width with 16px page margins

## Gotchas specific to this project

### Ukrainian text is longer than English
Ukrainian translations average 15-20% longer. Layout must accommodate:
- "Settings" → "Налаштування" (1.5x)
- "Order" → "Замовлення" (1.6x)
- "Notifications" → "Сповіщення" (1.0x)

For nav labels and buttons, allocate 20% more horizontal space than English designs.

### Existing notification center is for SaaS staff (multi-tenant)
The current "Сповіщення — Швидкий перегляд" / "Сповіщення — Центр сповіщень" frames on page `🟡 Центр сповіщень` are designed for **the SaaS team** that monitors all client stores (multiple tenant badges: Nova Poshta, TechStart UA, BeautyPro, etc.).

When user says "клієнт" / "client" — they mean the **store owner using the CRM** (single-tenant view). No multi-store badges.

### Use DS Button via importComponentSetByKeyAsync
Don't reinvent button styles in mockups — import the real Button component. Variant naming pattern: `Type=<Primary|Success|Danger>, State=<Enabled|...>, Size=<small|medium>, Style=<Fill|Outline|Ghost>`.

### Currency format: ₴ on right, space, no decimals for round
- "2 450 ₴" ✅
- "1 890,50 ₴" (when fractional) ✅
- "$2,450" or "2450 UAH" ❌

### Date format
- Recent (< 24h): relative — "2 хв тому", "1 год тому"
- Yesterday: "вчора, 18:42"
- This week: weekday name — "пн, 14:08" or absolute time
- Older: "26 квітня" (no year if current year)

## When to ask vs proceed

**Just do it (auto mode default):**
- Layout choice (drawer vs popover vs page) — pick based on existing pattern
- Specific copy for empty states / placeholders — make it match brand voice
- Color tinting choices that follow DS — apply rules from visual checklist
- Whether to include error state — yes, always

**Ask once:**
- Audience interpretation when ambiguous ("client" = end-customer or store-owner?)
- Major scope expansion ("should we also add the settings page for this?")
- When existing design conflicts with what I'd recommend (do they want to align with existing or break new?)

## Output expectations

Every design task ends with:
1. Section in Figma named `💠 <Feature> — Claude mockup vN`
2. At least 3 views (default / empty / mobile)
3. Use DS components where they exist
4. Brief text summary in chat with: what I made, what node IDs, what tradeoffs, what to refine

Don't generate React/CSS code unless explicitly asked. The Figma mockup is the deliverable.
