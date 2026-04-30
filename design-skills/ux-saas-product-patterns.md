---
name: UX — B2B SaaS & Product Patterns
description: Patterns specific to B2B SaaS / CRM products. Multi-tenancy, permissions, CRUD, onboarding, settings, billing, integrations, audit logs. The "boring but critical" product UX.
type: reference
originSessionId: 760c92ac-8a84-4d34-865f-7ab0d8a8baa2
---
# UX — B2B SaaS Product Patterns

B2B SaaS has its own UX dialect. These patterns appear in 90% of business apps. Master them and you save weeks of design.

## Multi-tenancy UX

### What is multi-tenancy
One platform serves multiple isolated organizations (tenants/workspaces/companies). Each tenant has its own data, users, settings.

### Tenant switching
- **Workspace switcher** in nav: dropdown showing current tenant name + logo, list of tenants user belongs to, "+ Add workspace" / "Create new".
- **URL slug per tenant**: `app.com/acme-corp/orders` — bookmarkable per tenant.
- **Visual differentiation**: tenant color/logo subtle in chrome (not loud — they should still feel they're in YOUR app).

### Inviting users
- Invite by email → email with magic link → user creates password.
- Show pending invites in member list.
- Resend / cancel invite available.
- **Don't** require account creation BEFORE invite — friction.

### Roles
Common role hierarchy:
- **Owner**: full control, billing, can delete tenant.
- **Admin**: manage users, settings, all data.
- **Manager**: manage data, view all.
- **Member / Operator**: work with data, limited admin.
- **Viewer**: read-only.
- **Guest / External**: limited scope, often time-bound.

Custom roles: power feature. Don't ship until ≥10 customers ask.

### Permissions UX
Two patterns:

1. **Role-based** (RBAC): user has role, role has permissions. Simple, scales.
2. **Resource-based** (ACL): per-resource permissions. Powerful, complex.

For most CRMs: RBAC + per-record sharing for sensitive data (e.g., "Anna can see only her customers").

### Permission UI patterns
- **Permission matrix**: roles × actions grid. Checkboxes.
- **Per-resource sharing**: "Share this customer with…" modal.
- **Inheritance hints**: "Inherited from team manager" tooltip.

### Showing permission state
- Disabled actions: tooltip explains "You don't have permission to delete. [Request access from admin]"
- Hidden actions: rare — better to show + disable than confuse with missing UI.
- Read-only mode: clear visual indicator, "Viewer" badge.

## CRUD pattern templates

Every business object goes through Create / Read / Update / Delete. Use consistent patterns.

### List view (Read)
- Table or list (depending on data type).
- Search + filters + sort.
- Pagination or infinite scroll.
- "+ Create" CTA top-right.
- Bulk actions.

### Detail view (Read deep)
Two patterns:
- **Side drawer**: opens from list, list still visible. Good for browsing through records.
- **Full page**: more space, more data. Use for complex objects (orders, customers with many tabs).

### Create
- "+ New" button in list view → opens form.
- Form: modal for simple, full page for complex (≥5 fields).
- Validate eagerly OR on blur, not on every keystroke.
- "Save" creates and goes to detail view OR back to list with toast confirmation.

### Update
- "Edit" button in detail view → form.
- **Inline edit** for single fields: hover shows pencil, click to edit, save on blur.
- **Form edit** for multiple changes.
- Distinguish "saved" state visually (timestamp + "Last updated by Anna").

### Delete
- Always confirm. Modal: "Delete order #8421? This action cannot be undone."
- OR provide "soft delete" + 30-day undo window (better for users).
- "Archive" pattern: hide from default views but recoverable.
- Hard delete: only for admin, with extra confirmation (typing "DELETE" or similar).

### Bulk operations
- Select multiple in list view.
- Floating action bar appears: count + actions (Archive / Delete / Export / Tag).
- Confirm with summary: "Archive 23 orders?"
- Show progress for slow operations.
- Allow cancel mid-operation.

## Onboarding UX

First-run experience determines retention.

### Phases
1. **Account creation** — email/social, password, basic info.
2. **Workspace setup** — name, members, integrations.
3. **First-data moment** — create first record OR import.
4. **Aha moment** — see value (first sale tracked, first report generated).
5. **Habit formation** — return visits.

### Patterns
- **Empty state as onboarding**: "Let's create your first order" with CTA. NO modal forced.
- **Checklist**: "Setup checklist (3 of 6 done)" — progress, gamification.
- **Sample data import**: optional, lets users explore before committing.
- **Interactive tour**: guided, contextual. SHORT (<5 steps). Skippable.
- **Tooltips on first use**: one tooltip per feature on first encounter, never again.

### Anti-patterns
- ❌ Mandatory tour with 12 steps.
- ❌ Modal blocking app on first visit.
- ❌ "Welcome to [App]!" splash screen.
- ❌ Demanding credit card before showing value.
- ❌ Dark patterns (pre-checked upsells, hard-to-find skip).

### Progressive disclosure
Don't show all features day 1. Surface advanced features as user matures:
- Day 1: core features only.
- Day 7: introduce "Filters" if user has searched.
- Day 30: introduce "Workflows" if user has 50+ records.

## Settings UX

Settings are where users tune the product. Bad settings UX = abandoned configuration.

### Settings page structure
Group by area:
- **Account / Profile**: name, email, password, avatar, timezone.
- **Workspace / Organization**: name, logo, branding, plan.
- **Members & Roles**: user list, invites, role config.
- **Notifications**: per-channel, per-type.
- **Integrations**: connected services, API keys.
- **Billing**: plan, payment method, invoices, usage.
- **Security**: 2FA, sessions, audit log.
- **Privacy / Data**: export, delete, retention.
- **Advanced / Developer**: API tokens, webhooks.

### Save patterns
- **Autosave** for simple toggles (notification preferences, theme).
- **Explicit save** for forms (profile edit).
- Show save state: "Saved" indicator, fade after 2 sec.

### Search within settings
For products with 50+ settings: built-in search at top of settings page.

### Reset to defaults
- Per-section "Reset to defaults" button.
- Confirm if user has customized.
- Don't apply to data, only configuration.

### Sensitive actions
- Account deletion: behind double confirmation, shows summary of what will be deleted.
- Plan downgrade: clearly show what's being lost.
- Data export: should always be available before destructive actions.

## Billing UX

The most-financially-sensitive UX surface. Mistakes lose customer trust permanently.

### Plan selection
- Show top 3 tiers side-by-side.
- Highlight "Most popular" or recommended.
- Per-tier: price (monthly + yearly with discount), features, limits.
- "Contact sales" for enterprise (no public price).

### Pricing display
- Show currency. "$" alone is ambiguous.
- Show what's included AND limits ("up to 1,000 orders/month").
- Annual savings explicit: "Save $X (20%)".

### Payment
- Use Stripe / PayPal / native (don't roll your own).
- Show last 4 digits of card on file.
- Allow multiple payment methods with default.
- **Test card**: provide for development, not in prod.

### Subscription management
- Clear current plan + next billing date + amount.
- Upgrade / downgrade self-serve.
- Cancel: don't hide. Make it findable in <3 clicks.
- Cancel flow: ask reason (optional), offer pause/discount, confirm.
- Export data option BEFORE cancellation.

### Usage / limits
- Visible meter when approaching limit: "234/250 customers (94%)".
- Pre-warning at 80%.
- Block at 100% with clear upgrade path.
- Don't silently fail — explain why.

### Invoices
- Downloadable PDF.
- Editable billing details (company name, address, tax ID).
- Email invoices automatically + accessible in app.

### Failed payments
- Email + in-app banner: "Payment failed. [Update card]"
- Grace period (3-7 days) before suspending.
- Read-only mode during grace period > immediate cutoff.

## Integrations UX

External services connected to your platform.

### Integration directory
- Grid of available integrations: logo + name + 1-line description.
- Filter by category (Communication, Payments, Shipping, Analytics).
- Search.
- Status badges: Connected / Available / Setup required.

### Connection flow
- Click integration → modal explaining what it does.
- "Connect" → OAuth flow OR API key input.
- Show progress: "Authenticating… / Fetching data… / Done"
- Confirmation: "Connected. Last synced just now."

### Connected integrations
- List of active integrations.
- Per-integration: status indicator, last sync, "Configure" button, "Disconnect".
- Per-integration health check.

### Configuration
- Per-integration settings: which data to sync, frequency, mapping.
- Save with validation.

### Errors
- Sync failure: red status indicator, error message, "Retry" button.
- Re-authentication needed: clear "Reconnect" CTA.

## Audit log / Activity

For compliance and debugging.

### What to log
- All write actions (create, update, delete).
- Permissions changes (role assigned, sharing changed).
- Login / logout.
- Failed authentication.
- Settings changes.
- Data exports.

### Display pattern
- Time-stamped list: "Anna deleted order #8421 — 2026-04-30 14:08".
- Filter: by user, by action type, by date range, by resource.
- Search.
- Export: CSV / JSON.

### Per-resource activity
- On detail view, show "Activity" tab: log scoped to this object.
- "Status changed from 'Pending' to 'Approved' by Olha — 12 min ago"

### Retention
- Configurable retention (30 / 90 / 365 days / forever).
- Show retention policy in UI.

## Search UX

CRMs have many records. Search is the entry point.

### Global search
- ⌘K / Ctrl+K opens search overlay.
- Searches everything: customers, orders, products, settings.
- Group results by type.
- Recent searches at top when empty.
- Keyboard arrows navigate results, Enter selects.

### Per-page search
- Search input above table/list.
- Searches WITHIN current view.
- Debounced (300ms typing pause).
- Highlight matched terms in results.

### Search empty state
- "No results for 'Petrenkov'" + "[Clear search]" + suggestions.

### Search filters
- Search box + filter chips combined.
- "customer:Anna status:active" — power-user syntax.
- OR a UI for advanced filters.

## Import / Export

Data portability is a trust signal.

### Import
- Templates downloadable (CSV with headers, sample data).
- Field mapping UI: source column → destination field.
- Preview before commit.
- Validation summary: "X rows have errors — [Review]"
- Don't fail entire import on partial errors — import good rows, list failures.

### Export
- CSV / Excel / JSON formats.
- Scope: filtered set or full table.
- Email link for large exports (>10k rows): processed async.
- Include audit metadata (timestamp, user) in export.

## Activity feed

Real-time chronological log of what's happening.

### Per-record (e.g., on order detail)
- Status changes: "Status: Pending → Shipped (Anna, 2 min ago)"
- Comments: threaded
- System events: "Email sent to customer"
- Attachments added

### Workspace-level
- Tenant-wide feed: "Olha created 3 orders / Anna updated customer X"
- Filter by user, by type.
- Real-time via websocket.

## Comments / mentions

Many CRMs have collaborative features.

### Comment patterns
- Per-record comment thread.
- @-mention to notify a user.
- Reactions (thumbs, etc.) — optional.
- Edit / delete own comments.
- Markdown support (light): bold, italic, code, links.

### Mentions
- Type "@" → autocomplete dropdown of users.
- Mentioned user gets notification.
- Visual: "@Anna" rendered as colored chip.

## Tags / Categories

Custom organization layer.

### Tag UX
- Add tag from any resource detail view.
- Color-coded for fast scan.
- Tag autocomplete + create new inline.
- Manage tags in settings: rename, merge, delete.

## Drafts / Auto-save

For long forms or content creation.

- Auto-save every 30 sec OR on blur.
- "Draft saved" indicator.
- "Continue draft" or list of drafts on return.
- Don't auto-publish drafts — user explicitly publishes.

## Versioning / History

For records that change over time.

- "View history" on detail page.
- Side-by-side or unified diff view.
- Restore to version: "Restore" button.
- Per-version metadata: who, when, what changed.

## Power user features

For users who live in the app daily.

### Keyboard shortcuts
Document via `?` shortcut help modal.
Common:
- `n` new record
- `c` compose / create
- `g` go to (followed by area letter): `gd` dashboard, `go` orders.
- `/` search
- `e` edit
- `Esc` close

### Saved views / Filters
Power users want their custom configurations:
- Save filter combinations as named views.
- Set default view per user.
- Share views with team.

### Bulk-edit power user patterns
- Select 100 rows → edit one field → applies to all.
- Conditional bulk edit: "Set status=Active where category=Premium".

### Command palette
⌘K opens unified search + actions:
- "Create order" → instant action.
- "Go to settings" → navigation.
- "Anna Petrenko" → record.
- Mixed results, ranked by recent + frequency.

## Internationalization (i18n)

If multi-language is on roadmap:

### Plan ahead
- Externalize all strings (no hardcoded text).
- Use translation keys with English defaults.
- Account for text expansion: Ukrainian/German +20-30% longer than English.
- Number/date formats per locale.

### Currency
- Format per locale: "₴2 450" (UA), "$2,450" (US), "2.450 €" (DE).
- Multi-currency support: explicit currency on every amount.

### RTL support
- Hebrew, Arabic. Layout mirrors.
- Use logical CSS properties: `padding-inline-start` not `padding-left`.
- Icons that imply direction (chevron) flip in RTL.

### Time zones
- Store UTC, display in user's timezone.
- Show timezone explicitly when ambiguous: "14:08 UTC+2".

## Trust signals

Things that build user confidence in B2B SaaS:

- **Last updated** timestamps everywhere.
- **Connected services** status visible.
- **Audit log** accessible.
- **Export data** always available.
- **Security badges** in footer (SOC2, GDPR, ISO).
- **Status page** linked when issues happen.
- **Changelog / release notes** visible.
- **Support response time** advertised.

## Anti-patterns specific to B2B SaaS

- ❌ Pricing hidden behind "Contact us" for SMB plans (only enterprise should require it).
- ❌ Cancel button buried 5 levels deep in settings.
- ❌ "You're using 99% of your quota" with no clear upgrade path.
- ❌ Trial that requires credit card upfront.
- ❌ Onboarding tour with 12 mandatory steps.
- ❌ Multi-tenancy without visible tenant switcher.
- ❌ Permissions UI that requires 10 clicks to give one user view access.
- ❌ Audit logs that aren't exportable.
- ❌ Settings with 100 toggles and no search.
- ❌ Integrations directory with 50 entries and no filter.

## Reference apps to study

- **Salesforce**: too complex for inspiration on simplicity, but reference for B2B depth.
- **HubSpot**: best B2B SaaS onboarding.
- **Linear**: best command palette + keyboard shortcuts in modern SaaS.
- **Stripe Dashboard**: best billing UX, period.
- **Notion**: best flexible-but-simple UX.
- **Intercom**: best customer messaging UX.
- **Pipedrive**: solid CRM patterns to model.
- **Airtable**: tables done right.
