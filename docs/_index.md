---
name: NextCRM Figma Design System Index
description: Master index of NextCRM DS Figma file — all 47 pages, links to per-page markdown, asset catalogs
type: reference
originSessionId: 760c92ac-8a84-4d34-865f-7ab0d8a8baa2
---
# NextCRM Design System (Figma)

**File URL:** https://www.figma.com/design/H1Ngineb53cAIqPWdqD585/NextCRM-Design-System
**File Key:** `H1Ngineb53cAIqPWdqD585`
**Library Key:** `lk-b424958829321032d02eb237300bfcb3204bc53de4b95c86f2f754fff11ff6db927665ccf3c6ea9a1b985d296910034a9fc57a6bde61529f37e76b193e1cd270`
**Library Name:** `NextCRM Design System`
**Total components:** 2678 components, 145 component sets
**Last sync:** REST API depth=3, all 47 real pages saved

## Pages

| # | Page | Status | File |
|---|------|--------|------|
| 1 | Typography | — | [pages/typography.md](pages/typography.md) |
| 2 | Colors | — | [pages/colors.md](pages/colors.md) |
| 3 | Uploader | — | [pages/uploader.md](pages/uploader.md) |
| 4 | Data table | 🟡 in-progress | [pages/data-table.md](pages/data-table.md) |
| 5 | Alert | ✅ done | [pages/alert.md](pages/alert.md) |
| 6 | Avatar | ✅ done | [pages/avatar.md](pages/avatar.md) |
| 7 | Badge | ✅ done | [pages/badge.md](pages/badge.md) |
| 8 | Banner | ✅ done | [pages/banner.md](pages/banner.md) |
| 9 | Button | ✅ done | [pages/button.md](pages/button.md) |
| 10 | Breadcrumbs | ✅ done | [pages/breadcrumbs.md](pages/breadcrumbs.md) |
| 11 | Checkbox | ✅ done | [pages/checkbox.md](pages/checkbox.md) |
| 12 | Dashboard elements | ✅ done | [pages/dashboard-elements.md](pages/dashboard-elements.md) |
| 13 | Divider | ✅ done | [pages/divider.md](pages/divider.md) |
| 14 | Date / time picker | ✅ done | [pages/date-time-picker.md](pages/date-time-picker.md) |
| 15 | Icon | ✅ done | [pages/icon.md](pages/icon.md) |
| 16 | Input Number | ✅ done | [pages/input-number.md](pages/input-number.md) |
| 17 | Input / TextArea | ✅ done | [pages/input-textarea.md](pages/input-textarea.md) |
| 18 | Logo | ✅ done | [pages/logo.md](pages/logo.md) |
| 19 | Modal | ✅ done | [pages/modal.md](pages/modal.md) |
| 20 | Navbar | ✅ done | [pages/navbar.md](pages/navbar.md) |
| 21 | Notification | ✅ done | [pages/notification.md](pages/notification.md) |
| 22 | Overlay /  backdrop | ✅ done | [pages/overlay-backdrop.md](pages/overlay-backdrop.md) |
| 23 | Pagination | ✅ done | [pages/pagination.md](pages/pagination.md) |
| 24 | Radio | ✅ done | [pages/radio.md](pages/radio.md) |
| 25 | Scrollbar | ✅ done | [pages/scrollbar.md](pages/scrollbar.md) |
| 26 | Select | ✅ done | [pages/select.md](pages/select.md) |
| 27 | Skeleton | ✅ done | [pages/skeleton.md](pages/skeleton.md) |
| 28 | Spinner / Loader | ✅ done | [pages/spinner-loader.md](pages/spinner-loader.md) |
| 29 | Switch | ✅ done | [pages/switch.md](pages/switch.md) |
| 30 | Tabs | ✅ done | [pages/tabs.md](pages/tabs.md) |
| 31 | Toast | ✅ done | [pages/toast.md](pages/toast.md) |
| 32 | Toggle button | ✅ done | [pages/toggle-button.md](pages/toggle-button.md) |
| 33 | Tooltip | 🟢 done | [pages/tooltip.md](pages/tooltip.md) |
| 34 | Menu | 🟡 in-progress | [pages/menu.md](pages/menu.md) |
| 35 | Comment | 🔴 not-started | [pages/comment.md](pages/comment.md) |
| 36 | Dropdown menu | 🟡 in-progress | [pages/dropdown-menu.md](pages/dropdown-menu.md) |
| 37 | Empty state | 🔴 not-started | [pages/empty-state.md](pages/empty-state.md) |
| 38 | Form | 🔴 not-started | [pages/form.md](pages/form.md) |
| 39 | Filter | 🟡 in-progress | [pages/filter.md](pages/filter.md) |
| 40 | Popup | 🔴 not-started | [pages/popup.md](pages/popup.md) |
| 41 | Progress bar | 🔴 not-started | [pages/progress-bar.md](pages/progress-bar.md) |
| 42 | Progress indicator | 🔴 not-started | [pages/progress-indicator.md](pages/progress-indicator.md) |
| 43 | Progress tracker / Steps | 🔴 not-started | [pages/progress-tracker-steps.md](pages/progress-tracker-steps.md) |
| 44 | Range | 🔴 not-started | [pages/range.md](pages/range.md) |
| 45 | ?? ❖ Side navigation | — | [pages/side-navigation.md](pages/side-navigation.md) |
| 46 | Tag / Chip | 🟡 in-progress | [pages/tag-chip.md](pages/tag-chip.md) |
| 47 | Browser and OS previews | 🔴 not-started | [pages/browser-and-os-previews.md](pages/browser-and-os-previews.md) |

## Asset Catalogs
- [variables.md](variables.md) — colors, semantic, typography
- [components.md](components.md) — component-set names + keys
- [pages/](pages/) — per-page detailed structure

## Code Counterpart
Tokens: `src/components/ui/tokens.css` (header: "Design Tokens (from Figma)")
React UI: `src/components/ui/{Button,Input,Checkbox,Badge,Toggle,Spinner,Tag,CopyText,KPICard,ChartCard,MultiSelect,DateRangePicker}`

## How to use
When user asks for a design referencing a component or page:
1. Open `pages/<slug>.md` to see frame structure + variant names
2. Use NodeId from that file with `get_design_context` (fileKey + nodeId) for full details
3. Reuse `variables.md` token names in generated code
4. Cross-reference `components.md` for Code Connect mapping keys

## Re-sync
Raw JSON dumps persist in `figma-ds/raw/` (47 page JSONs + components/component_sets/styles, ~12MB).
To re-pull: set `FIGMA_TOKEN=figd_...` env var (NOT stored in this repo) and re-run the pipeline:
1. `python3 /tmp/figma-dump/fetch_pages.py` (regenerate raw JSON)
2. `python3 /tmp/figma-dump/build_memory_v2.py` (regenerate per-page MDs)

If `/tmp` was cleared, regen the scripts from this index — the logic is straightforward:
- `GET /v1/files/{key}?depth=1` → list pages
- `GET /v1/files/{key}/nodes?ids={pageId}&depth=3` → per page
- `GET /v1/files/{key}/component_sets` → catalog