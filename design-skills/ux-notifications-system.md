---
name: UX — Notifications System (Deep)
description: Comprehensive notification UX. Channels, severity levels, batching, preferences, do-not-disturb, anti-spam. Critical for CRM with high event volume.
type: reference
originSessionId: 760c92ac-8a84-4d34-865f-7ab0d8a8baa2
---
# UX — Notification Systems

Notifications are the highest-friction UX surface. Every notification is a tax on attention. Design them like rationed currency.

## The 4 channels

| Channel | When | Latency | Persistence |
|---------|------|---------|-------------|
| **Toast (in-app)** | User is in app, transient confirmation | 0 | 3-5 sec |
| **In-app inbox** | User is in app, async events to act on later | seconds | Until read/dismissed |
| **Push (mobile/desktop)** | User outside app, time-sensitive | seconds | OS-controlled |
| **Email** | Anything important, official record | minutes | Forever |
| **SMS** | Truly urgent, low-volume | seconds | Phone log |
| **Browser push (web)** | User in browser, opted-in | seconds | OS-controlled |

A single event can fire multiple channels. Decide policy per event type.

## Severity levels

| Level | Color | Channel default | Example |
|-------|-------|-----------------|---------|
| **Critical** | Red | Push + In-app + Email | Payment failed, account suspended, security alert |
| **Warning** | Orange | In-app + Email (digest) | Low stock, integration error, sync delay |
| **Info** | Blue | In-app only | New order, message received, report ready |
| **Success** | Green | Toast (transient) | Saved, sent, completed |

Don't conflate severity with novelty. "New" doesn't mean "urgent".

## Information architecture for notifications

### The notification object
Every notification has:
- **id**: unique
- **type**: category (order_new, payment_failed, message_received, sync_error, ...)
- **severity**: critical / warning / info / success
- **title**: ≤ 60 chars, scannable
- **body**: 1-2 lines context
- **action**: optional CTA (mark as read, view, retry)
- **timestamp**: when it occurred
- **read**: boolean
- **source**: who/what triggered it (user, system, integration)
- **resource**: what it refers to (order #, customer, product)
- **deep_link**: where clicking takes you

### Center vs Inbox vs Feed
- **Center / Dropdown** (header bell): top 5-10 recent. For glanceable awareness.
- **Full Inbox** (dedicated page): full history, filters, bulk actions.
- **Activity Feed** (sidebar widget): real-time log, ambient awareness, sometimes per-resource (order activity).

CRMs often need all three.

## The dropdown center

This is the bell icon, top bar, popover.

### Dimensions
- 360-440px wide.
- Max-height ~480-640px, internal scroll if more items.
- Anchored under bell, right-aligned.

### Header
- Title: "Сповіщення" or "Notifications".
- Unread badge: red pill, format `06` (with leading zero) or `4` — match brand.
- Settings icon (gear): jumps to notification preferences.
- Optional: filter tabs (All / Unread / by category) — only if user volume justifies.
- Optional: "Mark all read" — link, not a button.

### Body
- List of notification rows.
- Date grouping if many: TODAY / YESTERDAY / EARLIER.
- Each row: icon + title + body + time + (optional) inline action + unread dot.
- Empty state when zero unread: "Все під контролем".

### Footer
- "View all" → link to full inbox page.
- Optional: "Notification settings" link.

### Notification row
```
[icon-32] Title (Medium 13)               2 хв тому ●
          Body description (Regular 12)
          [Inline action link]
```

- **Icon**: category-coded, 32×32 in tinted circle.
- **Title**: bold/medium for unread, regular for read.
- **Body**: ONE line, truncated with `…`. If user wants more, they click.
- **Time**: small, muted, top-right.
- **Unread indicator**: small blue dot (8px) right of time.
- **Inline action**: text-link style ("Прочитати"). Only on items where user can act WITHOUT navigating away.

### Behaviors
- Click row → mark as read + navigate to deep link.
- Click action link → action without navigation.
- Hover → slight bg darken.
- Right-click (desktop power feature) → options menu (mark unread, mute this type, snooze).

## The full inbox page

When user clicks "View all" or has too many to manage in dropdown.

### Layout
- Filter sidebar OR filter chips at top: category, severity, date range, read status.
- Bulk action toolbar when items selected: Mark read, Archive, Delete.
- List view (denser than dropdown): icon + title + body + time + status pill.
- Pagination or infinite scroll.

### Filters
- Critical only
- Unread only  
- Last 7 / 30 / custom range
- By type: Orders / Payments / System / Messages
- By source: User actions / System events / Integrations

### Saved views
Power feature: "My critical alerts" / "This week's payments" / "Stuck syncs".

## Notification batching

The biggest UX difference between annoying and useful notification systems.

### Batching strategies

**Real-time**: every event fires individually. Use ONLY for critical (payment fail, security).

**Throttled**: same-type events within a window collapse into one. "5 new orders in last hour" instead of 5 separate notifications.

**Digest**: scheduled summary. "Daily digest: 47 orders, 3 sync warnings, 2 customer messages". Common for email.

**Smart batching**: ML-decided based on importance and user behavior. Out of scope for most CRMs.

### Per-type batching policy

| Event type | Real-time | Throttled | Digest |
|-----------|-----------|-----------|--------|
| Critical (payment fail, security) | ✅ | | |
| New order | When low volume | Above 10/hour | |
| New customer message | ✅ | | |
| Sync error | First instance | Repeats | |
| Activity feed (low priority) | | | ✅ |
| Reports ready | ✅ | | |

### Throttling UX
"You have 12 new orders" + chevron to expand individual ones. Don't hide them entirely.

## Notification preferences

This is where users tune the system to their workflow.

### Preference page anatomy
- Group by event type (not channel).
- Per type: which channels (in-app / email / push / SMS).
- Per type: severity threshold ("only critical").
- Per type: batching ("real-time" / "hourly" / "daily digest" / "off").

### UI pattern
```
ORDERS
    New order placed                [✓] In-app  [✓] Email  [ ] Push
    Order status changed            [✓] In-app  [ ] Email  [ ] Push
    Payment received                [✓] In-app  [✓] Email  [✓] Push

INVENTORY
    Low stock alert                 [✓] In-app  [✓] Email  [ ] Push
    ...
```

### Smart defaults
- New users: critical-only on push, all in-app, daily email digest.
- Users with many notifications: auto-suggest reducing channels.

### Quick mute
- "Mute this type for 1 hour / today / this week / forever" from each notification.
- "Snooze all notifications for 1 hour" — focus mode.

### Do not disturb
- Schedule (e.g., 18:00-09:00 weekdays, all weekend).
- Vacation mode (date range).
- Critical bypass: critical notifications still arrive during DND. (User opts in/out.)

## Anti-spam principles

### The 1-2-3 rule
- **1 notification per event.** Same order place, payment received, shipped — that's 3 events, OK.
- **2 channels max** for non-critical. If it's in-app + email + push, you're spamming.
- **3 day mute** suggested when user dismisses 3 same-type notifications without acting.

### Smart silence
- Don't notify for actions the user just performed (they know they did it).
- Don't notify for changes only the actor would care about.
- Don't notify on weekends / off-hours unless critical.

### Frequency caps
- Per type per hour: ≤5.
- Total per day: ≤30 in-app, ≤5 email, ≤3 push.
- Beyond cap: roll up into digest.

## Onboarding for notifications

First-run experience matters.

### Initial setup
- Don't pre-enable all channels. Ask.
- Wizard: "Which events are most important to you?" (orders, payments, customer messages, system).
- Show example notifications during setup so users know what to expect.

### Permission prompts
- Browser push: never ask on first visit. Wait for value moment ("You missed 3 orders today — want push notifications?").
- Email: opt-in, easy unsubscribe.
- SMS: only with explicit opt-in (regulated).

## Mobile-specific patterns

### Push notifications
- Title: 50 chars max (truncated past 60 on most devices).
- Body: 110-180 chars max.
- Actionable: include action buttons when useful ("View" / "Dismiss").
- Group by category in OS notification center.
- Quiet hours respected (silent mode).

### In-app on mobile
- Bell icon top-right, badge with count.
- Tap → full-screen list (not dropdown — too cramped).
- Pull-to-refresh.
- Swipe left = archive, swipe right = mark read (or vice versa, be consistent).

### Mobile-specific event handling
- Receiving a push during foreground → show in-app banner instead of OS notification (since user is here).
- Tapping push → deep-link to relevant screen, not just app home.

## CRM-specific notification taxonomy

For NextCRM, here are common event types and recommended channels:

### Critical (always notify)
- `payment.failed` → Push + In-app + Email
- `security.suspicious_login` → Push + Email
- `subscription.expired` → Email + In-app banner
- `sync.repeated_failure` (3+ times) → Push + In-app

### Warning (notify by default, mutable)
- `inventory.low_stock` → In-app + Email digest
- `sync.timeout` → In-app
- `order.delivery_delayed` → In-app + Email
- `customer.complaint_received` → Push + In-app

### Info (notify in-app, mutable)
- `order.placed` → In-app
- `order.status_changed` → In-app (only for managed roles)
- `customer.message_received` → Push (operator) + In-app
- `report.ready` → In-app
- `integration.connected` → In-app

### Internal (digest only)
- `team.action_taken` → Daily digest
- `usage.milestone_reached` → Weekly digest

## Notification UX checklist

Before shipping a notification system:

- [ ] Each event mapped to channels and severity
- [ ] Batching rules per type
- [ ] User preferences page covering all event types
- [ ] DND / quiet hours
- [ ] Mute-this-type from any notification
- [ ] Smart defaults for new users
- [ ] Empty state for "all caught up"
- [ ] Mark-all-read action (with undo if heavy)
- [ ] Deep links work from every notification
- [ ] Mobile push has actionable buttons where useful
- [ ] Email digest format tested
- [ ] Critical notifications bypass DND (opt-in)
- [ ] Frequency caps prevent spam
- [ ] Test with high-volume tenant (1000+ events/day)
- [ ] Accessibility: screen reader announces new notifications

## Anti-patterns

- ❌ Same event firing toast + push + email (triple-spam).
- ❌ Notifications without deep links (user has no way to act).
- ❌ Generic notifications: "Something happened in your account".
- ❌ Notifications as marketing (badge count for upsells).
- ❌ Forcing all-or-nothing (user can't tune which types).
- ❌ Loud animations / sounds for non-critical events.
- ❌ Critical alerts mixed with low-priority in same view (signal-to-noise crash).
- ❌ Email digest with 200 items, no grouping.
- ❌ Browser push prompted before first user action.

## Reference apps to study

- **Slack**: best-in-class notification preferences UX. Per-channel, keyword-based, schedules.
- **Linear**: minimal, focused inbox. Notifications as todos.
- **GitHub**: noisy by default but with extensive controls. Inbox-style.
- **Stripe Dashboard**: critical-only by default. Excellent batching.
- **Intercom**: real-time customer messages with sound + badge + push.

When unsure about a pattern, check what these apps do.
