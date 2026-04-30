---
name: Match the user's actual system, don't recreate generic
description: User said "не такой как у меня в системе + есть много пробелов в дизайне". Don't build approximations of dashboards — use the actual existing screens as base.
type: feedback
originSessionId: 760c92ac-8a84-4d34-865f-7ab0d8a8baa2
---
# Match the actual system — don't recreate generic dashboards

**Rule:** When showing a feature in dashboard context, USE THE ACTUAL EXISTING DASHBOARD, not a sketch of one.

**Why:** User said "Не такой как у меня в системе" — they have a real, polished CRM with established patterns. My recreations look like generic SaaS templates next to their actual product. The gap is immediately visible to the user.

## Concrete sins I committed in v3/v4

1. **Sidebar items had no icons** — text-only with bullet rectangles. Real NextCRM sidebar has line-icons next to each item (cart for Замовлення, chat for Чати, box for Склад, etc.).
2. **KPI cards generic 3-up grid** — real dashboard might have sparklines, trend arrows, different layout.
3. **Table looked like template, not their actual Замовлення page** — different column widths, different status pill styling, no row hover, no row actions.
4. **Top bar didn't match** — real one has different breadcrumb pattern, profile dropdown, possibly other affordances.
5. **No tertiary chrome** — secondary nav within page, filter rails, sort indicators.

## How to do it right next time

### Option A — Use an existing page as canvas
1. Read the relevant page from `figma-dashboard/pages/<page>.md`
2. Copy/instance an actual frame from there
3. Add ONLY the new feature (dropdown, modal, etc.) on top
4. Don't re-draw the dashboard — instance it

### Option B — Get screenshot, match exactly
1. Screenshot the existing page via `get_screenshot`
2. Match every detail: icons, spacing, type sizes, colors
3. Rebuild only if instancing isn't possible
4. Cross-check before declaring done

### Option C — Ask before drawing
If unsure how the existing system looks, ASK — show your sketch and say "is this close to your dashboard or wildly off?" Get a screenshot reference. Don't guess.

## Anti-pattern to avoid

❌ "I'll build a generic dashboard layout to show context" — generic IS the problem.
❌ Using bullet rectangles instead of real icons in nav.
❌ Inventing KPI card structure when their real cards are different.
❌ Approximate spacing when their tokens are exact.

## How to apply

When task involves "show feature X in app context":
1. First grab a screenshot of the actual relevant page (Замовлення / Дашборд / Аналітика).
2. Identify which existing frames/components to reuse.
3. Build the new feature in the EXACT visual language of that page.
4. If you can't match, say so explicitly — don't fake it.

The user can immediately tell when their system is being approximated vs reproduced. Approximation = visible gap = "не такой как у меня в системе".
