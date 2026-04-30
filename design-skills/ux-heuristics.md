---
name: UX Heuristics & Patterns
description: Concrete UX rules to apply when designing screens. Nielsen heuristics, common patterns, anti-patterns. Run through this when proposing or reviewing a design.
type: reference
originSessionId: 760c92ac-8a84-4d34-865f-7ab0d8a8baa2
---
# UX — Heuristics, Patterns, Anti-Patterns

## Nielsen's 10 — operationalized

Every screen review goes through these:

### 1. Visibility of system status
The user should always know what's happening.
- Loading? Show spinner / skeleton.
- Saved? Show toast for 3 sec.
- Synced 5 min ago? Show last-sync timestamp.
- 4 unread? Show badge count.

### 2. Match between system and real world
Use words from the user's domain, not engineering.
- "ТТН" ✅ (CRM users know this) — not "Tracking number"
- "Замовлення в обробці" ✅ — not "Order state: PROCESSING"
- Numbers: "₴2 450" ✅ — not "2450.00 UAH"

### 3. User control & freedom
Always provide an exit.
- Modal? Has X close button + click outside dismisses.
- Multi-step form? Has Back button.
- Destructive action? Show "Undo" toast for 5 sec.

### 4. Consistency & standards
Same visual = same behavior across the product.
- Blue button = primary action everywhere.
- Bell icon = notifications. Always.
- Never reinvent: dropdown caret, select chevron, search ⌕ — use industry conventions.

### 5. Error prevention > error messages
- Confirm destructive actions ("Delete order? This can't be undone").
- Disable submit until form is valid.
- Auto-save drafts so user can't lose work.

### 6. Recognition over recall
Don't ask user to remember things.
- Recent items in dropdowns
- Filter chips show what's currently filtered
- Breadcrumbs show where you are

### 7. Flexibility & efficiency
- Keyboard shortcuts for power users (⌘K for search, etc.)
- Bulk actions for repeating tasks
- Saved filters

### 8. Aesthetic & minimalist design
Every element competes for attention. Ruthlessly remove what doesn't help.
- "Nice to have" sidebar widget? Cut.
- Decorative gradient on a data table? Cut.
- 3 lines of helper text under input? 1 line.

### 9. Help users recognize, diagnose, recover from errors
Error messages must:
- State what went wrong (in plain language)
- Why it happened (if known)
- What to do now (specific action)

❌ "Validation failed"
✅ "Phone number must include country code, e.g. +380 67 555 1234"

### 10. Help & documentation
- Tooltips on non-obvious icons
- Empty states explain what the screen IS
- Inline guidance over external docs

## Common patterns by component

### Notification center (this project)
- Group by date (Today / Yesterday / Earlier)
- Unread = visual emphasis (background tint + dot)
- Most recent first
- Filter tabs: All / Unread / by category
- Mark all read action — visible
- "View all" link to full page when in dropdown
- Empty state with reassuring copy ("All caught up")

### List view (orders, products, customers)
- Sticky header on scroll
- Sortable columns (click header)
- Filter sidebar OR filter chips at top
- Pagination OR infinite scroll (not both)
- Bulk select with floating action bar
- Quick actions on hover (edit / delete)
- Empty state: "No items yet" + CTA to create

### Form
- Group related fields with light section headers
- Required fields marked (asterisk)
- Inline validation (validate on blur, show error below field)
- Submit button at bottom, disabled until valid
- Show progress for multi-step (1 of 3)
- Save draft automatically, restore on return

### Modal / dialog
- Title states the action ("Delete order #8421?")
- Body explains consequence
- Two buttons: cancel (text/secondary) + confirm (primary or destructive)
- Esc closes, click outside closes (unless destructive)
- Focus first input on open

### Table
- Don't paginate at 10 rows — use 25 / 50
- Sticky first column on horizontal scroll
- Empty cells: render `—`, not blank
- Numbers: right-aligned, monospace tabular numerals
- Dates: relative for recent ("2 хв тому"), absolute for older ("12 квітня")

### Dropdown / popover
- Width: hug content for menus, fixed for content-rich (notifications, profile)
- Anchor: align to trigger edge
- Max height: 400-600px, scroll inside
- Click outside dismisses
- Esc dismisses
- Arrow keys navigate (when keyboard accessible)

## Mobile-specific

### Touch targets
Min 44×44pt (Apple) / 48×48dp (Material). Spacing between buttons ≥ 8pt.

### Bottom nav
4-5 destinations max. Active tab highlighted.

### Top bar
- Back button on left (icon only)
- Title centered or left
- Action icons on right (max 2)
- Subtitle / count below title if needed

### Replacements (desktop → mobile)
- Sidebar nav → bottom tab bar + hamburger drawer
- Hover states → press-and-hold OR explicit "more" menu
- Right-click menus → swipe actions OR three-dot menu
- Multi-column layouts → single column, stacked
- Dropdown popover → full-screen modal OR bottom sheet
- Tooltips → inline helper text OR tap-to-expand

### Gestures
- Pull to refresh on lists
- Swipe to delete / archive
- Long press for selection mode
- Pinch to zoom on images

## Anti-patterns to refuse

1. **Modal in modal.** Never. Replace inner with inline section or new screen.
2. **Carousel as primary content.** Users skip them. If important, show all options.
3. **Hover-only interactions.** Mobile users can't hover. Add explicit tap path.
4. **Generic "Submit" / "Save" / "OK"** buttons. Use specific verbs: "Place order", "Save draft", "Got it".
5. **Disabled buttons without explanation.** If button is disabled, tooltip or inline text says why.
6. **Auto-playing video / audio.** Always opt-in.
7. **Required phone format with no example.** Show placeholder: `+380 67 555 1234`.
8. **Non-dismissable banners / cookies.** Provide X.
9. **Icon-only buttons with no label and no tooltip.** Either label or tooltip.
10. **Confirmation for non-destructive actions.** Saving a profile shouldn't need a "Are you sure?".

## Accessibility quick wins

- Every input has a `<label>`. Placeholder text is NOT a label.
- Every button has visible focus state.
- Color is never the only signal (status uses icon + text, not just dot color).
- Tab order matches visual order.
- Modals trap focus inside.
- Esc closes modals.
- Min font size: 12px for ANY text user reads (not pure decorative).
- Animation duration: ≤ 300ms; respect `prefers-reduced-motion`.

## Information architecture

When designing a new screen ask:
1. **What's the user's goal here?** One sentence. If you can't say it, the screen has no purpose.
2. **What action will they take?** That's the primary CTA.
3. **What do they need to see to decide that action?** That's the content.
4. **What can be deferred / hidden?** That's secondary nav, settings, advanced options.

Apply these and most "should this go here?" questions resolve themselves.

## When user feedback conflicts with heuristics

Heuristics are defaults. User research overrides. If real users in this product context (CRM operators, store owners) repeatedly request a non-standard pattern, listen — there might be domain reasons (workflow speed, established muscle memory) that beat the textbook rule.

But don't bend heuristics on assumption alone. Test first.
