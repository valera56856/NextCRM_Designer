---
name: Visual Design Checklist
description: Practical visual design rules to apply when creating mockups. Hierarchy, spacing, typography, color, density. Run through this checklist before declaring a design "done".
type: reference
originSessionId: 760c92ac-8a84-4d34-865f-7ab0d8a8baa2
---
# Visual Design — Working Checklist

## Hierarchy (most-violated rule)

Each screen has ONE primary action. Find it on the mockup. Now ask:
- Is its color the most saturated? (only ONE solid Blue 600 button per view)
- Is it visually heaviest? (largest, boldest, highest contrast)
- Does the eye land on it within 1 second?

If user has to hunt, the hierarchy is wrong.

**Levels:**
1. **Primary** — solid color, full weight (e.g. `Blue 600` fill, white text). One per view.
2. **Secondary** — outlined or low-saturation (e.g. white fill, `Gray 200` border, `Gray 700` text). Multiple OK.
3. **Tertiary** — text-only / link styling (e.g. `Blue 600` text, no background).
4. **Destructive** — `Red 600` only when the action is irreversible. Confirm modal required.

## Spacing — the 8-point grid

Use multiples of 4 (or 8 for larger gaps). Never random values.

| Use | Pixels |
|-----|--------|
| Gap inside a tight pill/badge | 4 |
| Gap between icon and text in a row | 8 |
| Padding inside cards | 12 / 16 |
| Vertical rhythm between rows | 12 |
| Section padding | 24 / 32 |
| Major dividers / page padding | 48 / 64 |

**8-point density tiers:**
- **Compact** (table rows, dropdowns): 8 / 12 paddings
- **Default** (cards, forms): 16 padding
- **Spacious** (marketing, empty states): 24 / 32 padding

## Typography

Consistent type scale. NextCRM tokens (from `tokens.css`):
- `12 / 14 / 16 / 18 / 20` — text
- `24 / 30 / 36 / 40 / 48` — display

**Roles, not sizes:**
| Role | Size | Weight |
|------|------|--------|
| Caption / metadata | 11–12 | Regular |
| Body | 14 | Regular |
| Body emphasis | 14 | Medium |
| Subhead | 16 | Bold |
| Section title | 20–24 | Bold |
| Page title | 30 | Bold |
| Display | 36+ | Bold |

**Line height** ≈ 1.4× for body, ≈ 1.2× for display.

**Weight discipline:**
- Use only Regular (400), Medium (500), Bold (700). Skip 300/600/800/900.
- Don't use Bold on body text — it's for titles only.

## Color

**60-30-10 rule** for any view:
- 60% neutral (whites, light grays — backgrounds, surfaces)
- 30% secondary (text colors, subtle borders)
- 10% accent (primary brand, CTA, highlights)

If accent color exceeds 10%, the eye gets fatigued and CTAs lose impact.

**Semantic mapping:**
| Meaning | NextCRM token | Hex |
|---------|---------------|-----|
| Primary action | `--blue-600` | `#1886FE` |
| Success | `--green-600` | `#10A957` |
| Warning | `--orange-700` | `#C54009` |
| Danger / error | `--red-600` | `#F10909` |
| Info | `--blue-100` background + `--blue-700` text | tinted |

**Backgrounds for icon chips** (light tint, dark icon):
- `--blue-50` bg + `--blue-600` icon
- `--green-100` bg + `--green-700` icon
- `--orange-100` bg + `--orange-700` icon
- `--red-50` bg + `--red-700` icon

This pairing always passes contrast.

## Contrast (WCAG)

Minimum AA targets:
- Body text: 4.5:1 against background
- Large text (18px+ or 14px Bold): 3:1
- UI elements (icons, borders next to interactive): 3:1

Quick reference:
- `Gray 700` (#525252) on white = 7.46:1 ✅
- `Gray 500` (#7C7C7C) on white = 4.6:1 ✅ (just passes)
- `Gray 400` (#989898) on white = 2.85:1 ❌ (only for disabled / decorative)

## Density choices (matters in CRM)

- **Lists & tables:** prefer dense (compact tier — 8/12). Users scan many rows.
- **Forms & onboarding:** spacious (16/24). Fewer fields per view.
- **Dashboards / cards:** default (16). Mix of read + scan.
- **Mobile:** larger touch targets (min 44×44pt). Compensate with vertical rhythm, not extra padding.

## Component states (don't ship a button with only "default")

For each interactive element, design ALL states:
- Default
- Hover (desktop only, slight darken / fill)
- Active / Pressed (more darken, micro-shrink optional)
- Focus (visible outline — accessibility)
- Disabled (50% opacity or `Gray 200` fill)
- Loading (spinner replaces label)

The NextCRM Button component set already defines these — find variants by `State=Hover`, `State=Active`, etc. and reuse.

## Density of decoration

Drop shadows: max 2 elevation levels per screen.
- Card / popover: subtle (16-24 blur, 0.08-0.12 alpha)
- Modal / dropdown: prominent (32 blur, 0.16 alpha)
- Don't shadow buttons, inputs, or list rows.

Borders: 1px is enough. 2px only for focus rings.
Radii: 4 / 8 / 12 / 999 (pill). Don't mix random values.

## Empty states (often forgotten)

Every list has 3 states. Design all 3.
1. **Default** (data) — what we usually mock
2. **Empty** (zero data) — illustration/icon + helpful copy + CTA to add data
3. **Error** (failed to load) — error icon + "Retry" button

Don't ship without all three.

## Responsive behaviour

For each view, decide breakpoints:
- Desktop: 1280+ (sidebar + content)
- Tablet: 768-1279 (sidebar collapsible / drawer)
- Mobile: <768 (bottom nav, full-screen modals replace dropdowns)

A "notification dropdown" on desktop becomes a "full-screen list" on mobile. Plan both.

## Final pass

Before declaring done, do this 60-second audit:
1. Squint test — can you see hierarchy at low resolution?
2. Greyscale test — does it work without color?
3. Empty state — drawn?
4. Error state — drawn?
5. Mobile — drawn?
6. Disabled / loading on primary action — drawn?
7. Borders & radii consistent? (4/8/12 only)
8. Spacings on the 4/8 grid?
9. One primary CTA per view?
10. Body text ≥ 4.5:1 contrast?
