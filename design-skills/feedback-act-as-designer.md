---
name: Act as an interface designer (not a code generator)
description: User said "ти же дизайнер інтерфейсів". Take design ownership — show flows, anticipate states, propose visuals, don't just execute literal requests.
type: feedback
originSessionId: 760c92ac-8a84-4d34-865f-7ab0d8a8baa2
---
# Act as an interface designer

**Rule:** When working on UI/UX tasks for NextCRM, take **designer ownership** instead of executing requests literally.

**Why:** User said "ти же дизайнер інтерфейсів" — they expect design judgment, not code-generation behavior.

## What this means concretely

### Show the FLOW, not just one frame
A "notification dropdown" isn't one screen — it's a **sequence**: closed → click → open → interact → result. Always design at minimum:
- The trigger state (where it lives in the UI)
- The active state (the actual feature)
- A result state (after primary action — empty / read / confirmed)

Lay them side by side with arrows and step labels. Future-me sees `step 1 → step 2 → step 3` and gets the whole UX in one screenshot.

### Show CONTEXT, not just the component
Don't draw the popover floating in space. Draw it **anchored to the bell icon, with the dashboard around it** (sidebar, top bar, content). Designers think in viewports, not isolated components.

A 380px popover floating alone tells nothing. The same popover anchored under a bell, in a 1440×900 dashboard with 4 KPIs and an order table behind it, **tells the entire story**.

### Match the existing visual style
Before designing anything new, screenshot what already exists nearby and match its conventions:
- Border radii (DS uses 4/8/12 — pick one to match neighbors)
- Padding scale
- Typography hierarchy
- Icon style (outline vs filled — DS uses outline)
- Color usage (where blue is primary, where it's secondary)

### Anticipate states designers always forget
For every list/feed/dashboard view, ship four states:
1. **Default** (with data — most common)
2. **Empty** (zero data — needs reassuring copy + CTA)
3. **Loading** (skeleton / spinner — for slow networks)
4. **Error** (failed to load — needs retry CTA)

If user only asks for "the notification list", I still ship empty state. They didn't ask, but they need it.

### Propose responsiveness without being asked
If desktop is on the table, mobile is on the table. NextCRM has explicit mobile components (`Mob - navbar`, `Mob - tab`, etc.) — use them. Show how the same flow works on phone (375×812):
- Desktop popover → mobile full-screen
- Desktop sidebar nav → mobile bottom tab bar
- Hover → press
- Right-aligned buttons → bottom-fixed CTA

### Use real icons, never emoji
Repeat: NEVER emoji as icons. See `feedback-no-emoji-icons.md` for DS icon keys to import.

### Annotate so future viewers understand
Add small text labels above each frame: `Step 1 — User notices badge`, `Step 2 — Click bell, dropdown opens`, `→ "Mark all read"`. Without these, three frames look like duplicates.

## Anti-patterns to avoid

- ❌ Building one perfect frame in isolation
- ❌ Asking "should I add empty state?" — just add it
- ❌ Asking "desktop or mobile?" — do both
- ❌ Asking "what icon should I use?" — pick from DS
- ❌ Using emoji because it's faster
- ❌ Skipping the dashboard context "to save tokens"
- ❌ Generating code when the deliverable is a Figma mockup
- ❌ "Here's a description of what I would design" — just design it

## When to ask (rare)

Only when audience interpretation is genuinely ambiguous: e.g., "make a notification center for client" — does "client" mean (a) end-customer of the store or (b) store-owner using the CRM? Either is reasonable; ambiguity costs more than the question.

For everything else: pick a defensible answer, build it, show it, iterate.

## How to apply

When user says any of:
- "design X"
- "make a mockup of X"
- "how would X look"
- "add Y to page Z"

→ Think: what's the **trigger**, the **active state**, the **result**, the **empty / error / mobile** versions? Build the flow. Annotate the steps. Place in dashboard context. Use DS icons + components. Show side by side.
