# Design System — NextCRM

**Source of truth:** Figma file `H1Ngineb53cAIqPWdqD585` ([NextCRM Design System](https://www.figma.com/design/H1Ngineb53cAIqPWdqD585/NextCRM-Design-System)). 47 pages, 145 component sets, 2678 components published as a library.

This document consolidates the extracted system. For new work in Figma, instance components from the library. For code, reference CSS tokens that mirror these values.

## Product Context
- **What this is:** B2B SaaS CRM for Ukrainian e-commerce stores. Manages orders, customers, inventory, integrations (Nova Poshta, Prom.ua, WayForPay), team workflows.
- **Who it's for:** Store operators, managers, SaaS admins. Power users in the dashboard daily; non-technical operators.
- **Space/industry:** Multi-tenant CRM / e-commerce ops. Competes with KeyCRM, AmoCRM, Pipedrive.
- **Project type:** Data-dense web app (dashboard, tables, forms) + mobile companion (375×812 native patterns).

## Aesthetic Direction
- **Direction:** Industrial / Utilitarian — function-first, data-dense, professional. NOT playful, NOT marketing-flashy.
- **Decoration level:** Minimal. Typography and spacing carry the design. No decorative blobs, no purple gradients, no 3-column SaaS feature grids.
- **Mood:** Trustworthy software for serious work. Think Stripe Dashboard, Linear, KeyCRM — clean, dense, calm surface hierarchy.
- **Reference frame:** `Сповіщення — Швидкий перегляд` (`10686:5261`) in dashboard file `NFCl7XHHO3xlUjE1Y2UUpg` — the canonical example of how the system feels when assembled.

## Typography

**Font:** Roboto (Google Fonts). Loaded via `<link>` from Google. No fallback to Inter/system — that's the convergence trap.

**Scale (CSS tokens in `tokens.css`):**

| Token | Size | Use |
|-------|------|-----|
| `--text-50` | 11–12px | Caption, metadata, table micro |
| `--text-150` | 14px | Body, table cells, form fields |
| `--text-250` | 16px | Body emphasis, section labels |
| `--text-350` | 18px | Subheadings, modal titles |
| `--text-450` | 20px | Section titles |
| `--display-550` | 24px | Page titles, KPI numbers |
| `--display-650` | 30px | Hero subhead |
| `--display-750` | 36px | Major heading |
| `--display-850` | 40px | — |
| `--display-950` | 48px | Display |

**Line heights** match each size token (`--leading-50` … `--leading-950`).

**Weights:** Regular 400, Medium 500, Bold 700. Skip 300/600/800/900.

**Letter-spacing tokens** (`Letter spacing/50` … `/950`) for caps labels (e.g. `СЬОГОДНІ`, `СТАТУС`).

**Numbers:** `font-variant-numeric: tabular-nums` on money columns and tables.

**Curly quotes** `« »` for Ukrainian, ellipsis character `…` not three dots.

## Color

**Approach:** Restrained. Blue is primary. Green/Orange/Red/Indigo/Yellow are semantic only — never decorative.

**Primary scale (`Colors / Primary` set, 11 shades each):**

| Token | Hex | Use |
|-------|-----|-----|
| `--blue-50` | `#EDF9FF` | Tinted bg for blue icon chips, unread row highlight, hover |
| `--blue-100` | `#D8F0FF` | — |
| `--blue-200` | `#B9E6FF` | — |
| `--blue-300` | `#89D7FF` | — |
| `--blue-400` | `#51C0FF` | — |
| `--blue-500` | `#29A1FF` | — |
| `--blue-600` | `#1886FE` | **Primary CTA, active sidebar item, links** |
| `--blue-700` | `#0B6AEA` | Primary hover |
| `--blue-800` | `#1056BD` | — |
| `--blue-900` | `#144A94` | — |
| `--blue-950` | `#112E5A` | — |

**Semantic colors** (`Colors / Semantic` set):

| Role | Bg (chip) | Foreground | Hex |
|------|-----------|------------|-----|
| Critical / error | `#FFF0F0` | `#F10909` (red-600) | warning notifications, payment failures, destructive |
| Warning / system | `#FFF0E0` | `#C54009` (orange-700) | sync issues, low stock, system events |
| Success / confirmed | `#DBFDEA` | `#10A957` (green-600) | payment received, delivered, completed |
| Info / new | `#EDF9FF` | `#1886FE` (blue-600) | new orders, info banners |
| Indigo / payment | `#EFE9FE` | `#5E28D9` (indigo-700) | payment status, processing |
| Yellow / review | `#FEF3C7` | `#B45309` (yellow-800) | reviews, pending decisions |

**Neutrals (Gray scale):**

| Token | Hex | Use |
|-------|-----|-----|
| `--gray-50` | `#F6F6F6` | Page bg |
| `--gray-100` | `#F1F1F1` | Borders, dividers |
| `--gray-200` | `#DCDCDC` | Subtle borders, disabled bg |
| `--gray-400` | `#989898` | Disabled text, decorative only (fails 4.5:1) |
| `--gray-500` | `#7C7C7C` | Tertiary text, captions |
| `--gray-600` | `#656565` | Secondary text |
| `--gray-700` | `#525252` | Body secondary |
| `--gray-950` | `#292929` | Primary text on white |

**Color is never the only signal.** Status pills always pair color + label + icon.

## Spacing

**Base unit:** 4px / 8px hybrid grid. All paddings and gaps come from the token list.

| Token | Value | Use |
|-------|-------|-----|
| `--space-2` | 2 | Tight inline gaps (badge pill) |
| `--space-4` | 4 | Inside chips |
| `--space-6` | 6 | Tab pills, small button gaps |
| `--space-8` | 8 | Default chip padding, icon-text gap |
| `--space-12` | 12 | Card inner gap, between buttons |
| `--space-16` | 16 | Card padding, section padding |
| `--space-24` | 24 | Page padding, section break |
| `--space-32` | 32 | Major separation |
| `--space-48` | 48 | Hero / empty states |

**Density tier:** Default (52px row height for tables, 40px sidebar items, 16px card padding). Compact tier (32-40px row) for high-volume tables.

## Layout

**Approach:** Grid-disciplined. Sidebar 240px + content fills. No creative-editorial breaks for app screens. Hero/marketing layouts are out of scope (this is app UI).

**Breakpoints:** mobile 375 / tablet 768 / desktop 1024 / wide 1440.

**Border radius:**

| Token | Use |
|-------|-----|
| `--radius-4` | Tags, chips, status pills |
| `--radius-8` | Cards, inputs, buttons |
| `--radius-12` | Modals, popovers, drawers |
| `--radius-full` | Avatars, badges, dots |

NEVER uniform bubbly radius on everything (AI slop signal).

**Max content width:** 1440. Sidebar 240. Content area `calc(100% - 240px)`.

## Motion

**Approach:** Minimal-functional. Only transitions that aid comprehension.

**Easing:**
- Enter: `cubic-bezier(0, 0, 0.2, 1)` (ease-out)
- Exit: `cubic-bezier(0.4, 0, 1, 1)` (ease-in)
- Move: `cubic-bezier(0.4, 0, 0.2, 1)` (ease-in-out)

**Duration:**
- Micro (hover, button feedback): 50–100ms
- Short (dropdown, modal appear): 150–250ms
- Medium (page section transitions): 250–400ms

**Animate ONLY** `transform` and `opacity`. Never `width`/`height`/`top`/`left`.

**Respect `prefers-reduced-motion`** — disable non-essential animation.

## Components (live in Figma library)

Authoritative source: Figma file `H1Ngineb53cAIqPWdqD585`. Local catalog: [docs/components.md](docs/components.md). Key sets:

| Component | Library key | Variants |
|-----------|-------------|----------|
| Logo | `df41f5a13a1fc34dda0cf516ae99d5bb25007afe` | Default (blue) / Variant2 (white) |
| Button / new | `4af7bd61bebb20595ea64f8ed9f53cf7a11c3c76` | 198 variants (Type × State × Size × Style) |
| Tags | `0e88e70b5ac17f4d01d5dce19bfec079ba01d7b2` | — |
| Badge-rounded | `c063dcfd3933ac4622cb0410871314b8925c5295` | — |
| table-cell | `518beee8598c465aa9f198bdbe8c91c382cf2ef6` | — |
| Mob - navbar | `64e9a9aba55c2f7769cbb62fbe28df73245373ec` | mobile top nav |
| Mob - tab | `70bf0d47a6301cc11028513afdb1519eebd231d5` | mobile tab |
| Pop-up nav settings | `f3c3adf59fcd6608230011e64f02795db3d225d0` | — |

**Material icons** (sample of 31 with verified keys): `notifications`, `settings`, `warning`, `shopping_cart`, `shopping_bag`, `credit_card`, `chat`, `star`, `check_circle`, `chevron_right`, `chevron_left`, `keyboard_arrow_down`, `arrow_forward`, `close`, `more_horiz`, `search`, `filter_list`, `sync_problem`, `support_agent`, `category`, `warehouse`, `description`, `analytics`. Full key map in [design-skills/feedback-no-emoji-icons.md](design-skills/feedback-no-emoji-icons.md).

**Code mirror:** React UI in `src/components/ui/{Button,Input,Checkbox,Badge,Toggle,Spinner,Tag,CopyText,KPICard,ChartCard,MultiSelect,DateRangePicker}` with CSS tokens in `src/components/ui/tokens.css`. The header comment of tokens.css says "Design Tokens (from Figma)" — the React side is downstream of the Figma source.

## Anti-patterns (refuse, regardless of who asks)

1. **Emoji as icons** in product UI. Use real DS Material icons. ([feedback-no-emoji-icons.md](design-skills/feedback-no-emoji-icons.md))
2. **Generic dashboard recreation** when the actual NextCRM dashboard exists. Use real frames as base. ([feedback-match-existing-system.md](design-skills/feedback-match-existing-system.md))
3. **Purple/violet gradients** as decoration.
4. **3-column feature grid** with icons in colored circles.
5. **Centered everything** layouts.
6. **Inter / Roboto / Open Sans / Poppins / Space Grotesk** as a "safe" replacement font. Roboto IS our chosen font; using anything else is a regression.
7. **system-ui / -apple-system** as the primary display font.
8. **Bubbly uniform radius** on everything.
9. **Decorative blobs / wavy SVG dividers / floating circles**.
10. **Color as the only signal** for status.

## Companion docs

- [docs/_index.md](docs/_index.md) — full Figma DS extract, all 47 pages
- [docs/variables.md](docs/variables.md) — token catalog
- [docs/components.md](docs/components.md) — 145 component sets with library keys
- [dashboard/docs/_index.md](dashboard/docs/_index.md) — Dashboard file mirror, 24 product pages
- [design-skills/](design-skills/) — UX heuristics, cognitive foundations, mobile/a11y, SaaS patterns, project playbook
- [design-reviews/](design-reviews/) — per-feature design audit reports

## Decisions Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-04-30 | Initial DESIGN.md created | Consolidates the existing Figma DS (`H1Ngineb53cAIqPWdqD585`) and the design-skills knowledge base into a single canonical document. The Figma file remains the source of truth for components; this doc is the readable surface for AI agents and humans. |
| 2026-04-30 | Industrial/utilitarian aesthetic locked | Inferred from existing reference screens (dashboard tables, status pages, notification center). Matches CRM operator workflow — dense, calm, professional. Not marketing-style. |
| 2026-04-30 | Roboto as primary font | Already in Figma DS, already in `tokens.css`. Resist switching to Inter/Space Grotesk per anti-convergence directive. |
| 2026-04-30 | Blue 600 (#1886FE) as primary | Already established in DS. Single accent color per restrained palette principle. |
| 2026-04-30 | No emoji as icons rule | User feedback: "без тупих ємодзи". Real DS Material icons via Code Connect imports. |
| 2026-04-30 | Match-existing-system rule | User feedback: "не такой как у меня в системе". Use actual existing frames as base, never recreate generic dashboards. |
