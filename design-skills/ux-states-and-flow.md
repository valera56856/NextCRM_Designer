---
name: UX — States, Feedback, and Flow
description: Loading, error, empty, success states. Toast vs banner vs modal. Microinteractions. Optimistic UI. Error recovery. The full lifecycle of every interaction.
type: reference
originSessionId: 760c92ac-8a84-4d34-865f-7ab0d8a8baa2
---
# UX — States, Feedback, and Flow

The difference between a polished product and a brittle one is how it handles non-happy paths.

## The 8 states every component has

For each interactive element, design ALL of these:

1. **Default** (rest)
2. **Hover** (desktop only — pointer over)
3. **Focus** (keyboard navigation, accessibility)
4. **Active / Pressed** (mid-click)
5. **Selected** (toggle is on, item is chosen)
6. **Disabled** (not currently usable)
7. **Loading** (waiting for response)
8. **Error** (something went wrong)

**Plus context-dependent:**
- Empty (list with no items)
- Read-only (data exists but can't be edited)
- Stale (data is old, refresh available)

## Loading states — picking the right one

| Pattern | When to use | When NOT |
|---------|-------------|----------|
| **Skeleton** | Layout known, data <2s | Quick async (<200ms) — flicker |
| **Spinner** | Quick async, action button | Long waits (>5s) — feels stuck |
| **Progress bar** | >5s, known duration | Unknown duration |
| **Indeterminate progress** | >5s, unknown duration | Quick |
| **Optimistic UI** | Low-risk action with predictable result | Destructive or transactional |
| **Streaming** | Chat, AI responses, logs | Static data |

### Skeleton best practices
- Match real content's exact layout.
- Subtle shimmer animation (300ms loop, low opacity).
- Show ≥3 skeleton items so user knows it's a list.
- Replace with real content piece-by-piece (don't wait for everything).

### Spinner best practices
- Use sparingly. Inside buttons after click. Inside cards while loading their data.
- 16-24px size, accent color.
- Don't overlap with the click target — disable the button during load.
- Pair with status text for waits >2s: "Saving…" / "Processing payment…"

### Progress bar best practices
- Show actual percentage if known.
- Show stage if multi-stage: "Uploading 3/10 files".
- Update at least every 500ms — frozen progress = "is it stuck?"
- Allow cancel for >10s operations.

### Optimistic UI patterns
- Click "Mark as read" → instant visual change → background API call.
- Click "Like" → counter increments instantly.
- If API fails: show subtle error toast, revert visually, offer "retry".
- DON'T optimistic-update for: payments, sends, deletes, anything irreversible.

## Empty states — the most-skipped state

Every list/table/feed has an empty state. NEVER ship without it.

### Anatomy
1. **Visual** (illustration or icon, decorative — set the tone)
2. **Headline** (1 line, warm tone): "No notifications yet"
3. **Description** (1-2 lines, what this place is for): "When you get a new order or message, it'll appear here."
4. **Primary action** (CTA to populate): "+ Create your first order"
5. **Secondary**: link to docs, video, sample data import

### Tone
- Warm but not saccharine. "Все під контролем" beats "Looks like there's nothing here!".
- Specific to the context. "No customers yet" + "Add your first customer" beats generic "No data".
- Avoid emoji unless brand-aligned (not in B2B CRM).

### Distinct empty states
- **Brand new account / first-time user**: onboarding-style. "Welcome! Let's get you set up."
- **Filtered to nothing**: "No orders match these filters. [Clear filters]"
- **Search miss**: "No results for 'Petrenkov'. [Try fewer keywords]" + suggestions.
- **Achievement / Done**: "All caught up. ✓"
- **Resource not yet created**: regular onboarding empty state.

### Anti-patterns
- ❌ Empty state showing 0 in a table with full chrome (looks broken).
- ❌ "No data" or "No items" — uninformative.
- ❌ Empty state that doesn't suggest what to do next.
- ❌ Generic stock illustration of magnifying glass on a folder.

## Error states — recovery first

The error UX is more important than the success UX. Errors happen; recovery defines the experience.

### Error message anatomy
1. **What happened** (plain language): "Couldn't save your changes."
2. **Why** (if known): "Your session expired."
3. **What to do now** (specific): "[Sign in again] and we'll restore your work."

❌ "Validation failed" / "Error code 422" / "Something went wrong"
✅ "Please enter a valid Ukrainian phone number, e.g. +380 67 555 1234"

### Error placement
- **Field-level**: inline below the field (form validation).
- **Section-level**: banner above the section.
- **Page-level**: full banner at top OR replace content with error state.
- **Toast**: only for transient errors that don't block work ("Saved offline. Will sync when online.").

### Error recovery actions
- **Retry button** for network/transient errors.
- **Edit/correct** for validation.
- **Contact support** for unrecoverable.
- **Undo** for actions that succeeded but user regrets.

### Specific error patterns

**Network error / offline:**
- Banner: "You're offline. Changes will sync when reconnected."
- Disable actions that need network; queue what you can.
- Show last-synced timestamp.

**Permission denied:**
- "You don't have permission to delete orders. [Request access from admin]"
- Don't hide the action — show it disabled with tooltip explaining.

**Server error (5xx):**
- Apologize. "Sorry, our servers are having trouble. We're on it."
- Retry button.
- Status page link if available.

**Validation error:**
- Inline, specific, with example of correct format.

**Conflict (someone else edited):**
- "Anna edited this 30 sec ago. [View their changes] / [Overwrite] / [Merge]"
- Don't silently overwrite.

**Rate limit:**
- "Too many requests. Wait 30 sec and try again."
- Show countdown.

## Success states — celebrate completion

Success feedback closes the loop. Without it, users wonder "did it work?"

### Toast (default for most success)
- Bottom-right (Mac) or top-right (Windows). Pick one consistently.
- Auto-dismiss 3-5 sec. User can dismiss earlier.
- Don't stack >3 — collapse to "+5 more".
- Include action when relevant: "Order created. [View] / [Undo]"

### Inline success
- After form save: "Saved" indicator near the form, fade after 2 sec.
- After inline edit: green check briefly, fade.

### Modal success
- Major events: payment received, account created, integration connected.
- Includes next-step CTAs: "What's next?"
- User-dismissed (no auto-close).

### Animation for delight
- Subtle — don't block work.
- Confetti for milestones (first order shipped, 100 customers reached). Sparingly.
- Check-circle drawing animation for success confirmation (300ms).

## Feedback patterns — when to use which

| Pattern | Severity | Duration | Example |
|---------|----------|----------|---------|
| **Inline message** | Field-level | Persistent | Form validation error |
| **Toast / Snackbar** | Low | Auto-dismiss 3-5s | "Saved", "Sent" |
| **Banner** | Medium | Persistent until acted | "Your trial expires in 3 days" |
| **Alert dialog** | High | Modal, blocking | "Delete order? This can't be undone." |
| **Status indicator** | Ambient | Always visible | "● Connected" / "● Offline" |
| **Notification** | Async event | User reads on demand | "New order received" |

### Toast vs Banner
- **Toast**: temporary acknowledgment of an action just taken. "Saved." Goes away.
- **Banner**: persistent state needing attention. "Trial expires in 3 days." Stays until resolved.

### Banner vs Modal
- **Banner**: informational, doesn't block. "We've updated our terms — review."
- **Modal**: requires decision before proceeding. "Confirm delete?"

### Modal best practices
- One question or task per modal. No "modal in a modal".
- Title states the action: "Delete order #8421?"
- Body explains consequence: "This action can't be undone."
- Two buttons: cancel (secondary) + confirm (primary or destructive).
- Confirm is destructive-colored if action is destructive (red).
- Esc closes. Click outside closes UNLESS destructive (then explicit close required).
- Focus first input on open (or primary action if no input).
- Trap focus inside (don't let tab go outside the modal).

## Microinteractions

Small animated feedback that makes the interface feel alive.

### What deserves a microinteraction
- **State change**: toggle flips, checkbox checks, switch slides.
- **Critical action confirmation**: payment success animation, error shake.
- **Discovery**: subtle pulse on a new feature for 1 cycle.
- **Status update**: live counter ticking, progress bar moving.

### Animation principles (12 from Disney, applied to UI)

1. **Squash & stretch**: button compresses on press (98% scale), bounces back.
2. **Anticipation**: tooltip grows from origin, doesn't just appear.
3. **Staging**: enter major elements first, decorative later.
4. **Follow-through**: dropdown items slightly overshoot then settle.
5. **Slow in / slow out** (easing): everything natural.
6. **Arcs**: floating action button moves on a curve, not straight line.
7. **Secondary action**: icon flips while text fades.
8. **Timing**: 200-300ms for most. 50-100ms for micro. >500ms only for major scene transitions.
9. **Exaggeration**: error shake is 6-8px, not 2px (otherwise feels glitchy).
10. **Solid drawing**: rendered in 3D space if possible (subtle shadows during motion).
11. **Appeal**: easing curves matter — `cubic-bezier(0.4, 0, 0.2, 1)` is the Material default for a reason.
12. **Straight ahead vs pose to pose**: most UI = pose-to-pose (start state → end state, system fills in).

### Easing functions cheat sheet
- **ease-out** (decelerate): things ENTERING the screen. `cubic-bezier(0, 0, 0.2, 1)`. Most natural.
- **ease-in** (accelerate): things LEAVING the screen. `cubic-bezier(0.4, 0, 1, 1)`.
- **ease-in-out**: things MOVING within the screen. `cubic-bezier(0.4, 0, 0.2, 1)`.
- **linear**: progress bars, infinite loaders only.
- **spring** (overshoot): playful contexts. Use sparingly.

### Animation duration guide
- 50-100ms: hover state, tooltip appear, button click feedback
- 150-200ms: dropdown open, modal appear
- 250-350ms: page section transitions
- 400-500ms: full page transitions (rare in apps)
- >500ms: special moments only (success celebrations, onboarding)

### Performance
- Animate ONLY `transform` and `opacity`. Never `width`, `height`, `top`, `left` — they trigger layout recalc.
- 60fps target. If choppy, simplify.
- Respect `prefers-reduced-motion`: disable non-essential animation.

## Optimistic UI deep dive

Pattern: show the result before the server confirms.

### When it works
- **Toggle states** (mark as read, like, follow).
- **Reorderable lists** (drag-drop).
- **Inline edits** of simple fields.
- **Adding to a list** (new comment, new item).

### When it doesn't
- **Payments** — never optimistic.
- **Sends** (email, SMS) — show "Sending…"
- **Deletes** — confirm first, OR provide undo window.
- **Conflicts** likely — show real server response.

### Failure handling
- Subtle toast: "Couldn't save. [Retry]"
- Revert visual to pre-action state.
- Offer manual retry.
- DON'T pop a modal — would interrupt flow.

### Conflict resolution
- If your optimistic update conflicts with another user's change:
- Show: "Anna also edited this. [Use Anna's] / [Use yours] / [Merge]"
- Default to safer option (don't auto-overwrite).

## Confirmation patterns

### When to confirm
- Destructive: delete, archive, unsubscribe, cancel-trial.
- Public: post, send, publish.
- Expensive: place order, charge card, run report.
- Irreversible: anything that can't be undone with 2 clicks.

### When NOT to confirm
- Routine: save, edit, mark-read, navigate.
- Reversible with quick undo: archive (restorable).
- Common actions that confirm-fatigue users.

### Better than confirmation: undo
For most actions, "[Saved] [Undo]" toast for 5s beats a modal.

### Confirm modal anatomy
- **Title**: action stated as question. "Delete this order?"
- **Body**: consequence in plain words. "This will permanently remove order #8421 and all its history."
- **Optional**: typing confirmation for very destructive ("type 'DELETE' to confirm") — for nuclear actions only (delete account, drop database).
- **Buttons**: Cancel (text or secondary) + Delete (destructive red).

## Status indicators (ambient feedback)

Always-visible state that helps users navigate.

- **Connection**: ● Online / ● Offline / ⟳ Reconnecting
- **Last save**: "Saved" / "Saving…" / "Unsaved changes"
- **Last sync**: "Synced 2 min ago" / "Last sync failed [Retry]"
- **Active integrations**: green dot per service, tooltip with status

Don't make these visually loud. They're ambient. Tiny, edge of view.

## Flow design — chaining states

A flow is a sequence of state transitions. Map them all.

### Example: "Place an order" flow
1. Click "+ New order" → modal opens (loading state if needed)
2. Customer step → autocomplete loads (loading), validation runs (eager? lazy?)
3. Items step → product search (loading per query)
4. Shipping step → address validation (background async)
5. Review step → all data summarized
6. Submit → progress (multi-step API)
7. Success → confirmation modal with "View order" / "Create another"
8. Error → field highlighted with specific message + recovery path

For each transition, ask:
- What does the user see?
- What can go wrong?
- How do they recover?
- How do they go back?

## Flow design anti-patterns

- ❌ Form that loses data on browser back button
- ❌ Multi-step form without progress indicator
- ❌ Modal trap (user can't escape without completing)
- ❌ Submit button that doesn't disable during submit (double-submit risk)
- ❌ Success page with no "next" action
- ❌ Error page with no recovery path
- ❌ "Are you sure?" for routine actions (confirm fatigue)
- ❌ Loading state that lasts >10s with no progress indication
