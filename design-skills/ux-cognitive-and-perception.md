---
name: UX — Cognitive Foundations & Perception
description: How brains process UI. Hick's, Fitts's, Miller's laws. Gestalt principles. Cognitive biases. Apply these BEFORE choosing any layout or interaction.
type: reference
originSessionId: 760c92ac-8a84-4d34-865f-7ab0d8a8baa2
---
# UX — Cognitive Foundations & Perception

The user's brain is the bottleneck. Memorize these laws and your design intuition gets calibrated.

## The Five Laws

### 1. Hick's Law
**Decision time grows logarithmically with the number of choices.**

`Time = b × log₂(n + 1)`

Practical rules:
- **Menus**: ≤7 items per level. More = paralysis.
- **Filter pills**: ≤5 visible at once. Hide the rest behind "More".
- **Action buttons per view**: 1 primary + 2-3 secondary. More dilutes attention.
- **Form fields visible at once**: ≤7. Use multi-step or progressive disclosure beyond.
- **CRM specific**: Order action menu, status options, role permissions — bucket aggressively.

Anti-pattern: 12-item dropdown menus.
Cure: group by category with sub-menus, OR search-first interface.

### 2. Fitts's Law
**Time to hit a target = function of distance and size.**

`Time ∝ log₂(D/W + 1)` (D=distance, W=width)

Practical rules:
- **Touch targets ≥ 44pt** (iOS) / 48dp (Android). Below = miss-clicks.
- **Important buttons GROW.** Primary CTA always larger than secondary.
- **Edges are infinitely large** — corners and screen edges are easiest hit. Place high-frequency tools there (close button top-right, save bottom-right).
- **Gravity wells**: clicking near where the user just clicked is faster than clicking far away. Place related actions adjacent.
- **Mobile thumb zone**: bottom-center of phone is fastest reach. Bottom corners next. Top corners are agonizing — never put primary action there on mobile.

CRM application: bulk-action floating bar appears near the selection, not at the page header. Quick edit pencil is right next to the row, not in a deep menu.

### 3. Miller's Law (Working Memory)
**Working memory holds 7±2 items, more realistically 4±1 in modern recall.**

Practical rules:
- **Phone numbers chunked**: `+380 67 555 12 34` not `+380675551234`.
- **Wizard steps ≤ 5.** More feels endless.
- **Comparison views**: ≤4 columns side-by-side.
- **Confirmation modals**: state ONE consequence. Not three bullets.
- **Form sections**: ≤7 fields per section, then break.

CRM specific: order detail page should chunk: customer | items | shipping | payment | history. Five "rooms" beats one big wall of fields.

### 4. Doherty Threshold
**Productivity soars when system response < 400ms.**

Practical rules:
- **Optimistic UI**: render the change immediately, sync to backend in background. Bank apps do this for transfers — the balance updates before the API confirms.
- **Skeleton loaders < 1s, spinner < 5s, progress bar > 5s.**
- **Search results within 100ms** = "instant" feeling. Within 1s = "quick". Beyond 10s = abandon.
- **Hover preview** beats clicking through when stakes are low (linked records).

CRM specific: status change in a table row should toggle visually instantly even if API takes 2s. If sync fails, show a small "retry" inline — don't roll back without explanation.

### 5. Jakob's Law
**Users spend most of their time on OTHER products. They expect yours to work like those.**

Practical rules:
- **Don't reinvent navigation, search, login, settings, account menu.** Use industry conventions.
- **Logo top-left → home.** Always.
- **Magnifying glass = search.** Cog = settings. Bell = notifications. Don't be cute.
- **Save/cancel positions**: primary on right (Mac/web), primary on left (Windows). Pick one and stay consistent.
- **Esc closes modal. ⌘K opens command palette. /. opens search.**
- **Tables**: sortable columns click on header. Filter chips at top. Pagination bottom-right.

CRM specific: pattern-match against Salesforce, HubSpot, Pipedrive for what users expect. They've been trained for years.

## Gestalt Principles (Pattern Perception)

Brain auto-groups visual elements. Use this for free hierarchy.

### Proximity
**Close-together = related. Far apart = unrelated.**
- Field label sits NEXT to its input (4-8px), not floating 24px above.
- Action buttons cluster (8-12px gap). Different action groups separated (24-32px).
- List rows tight (12-16px), section breaks loose (32-48px).

### Similarity
**Same shape/color/size = same kind of thing.**
- All primary buttons identical. All secondary identical. Don't style buttons one-off.
- Status pills follow ONE shape (rounded rectangle), color encodes state.
- Avatar + name pattern repeated everywhere a person appears.

### Closure
**Brain fills in incomplete shapes.**
- Dotted outlines work for "drop file here" zones.
- Stylized icons read as full objects (a triangle warning sign uses ~5 lines).
- Don't over-draw — minimal forms communicate clearer.

### Continuation
**Eye follows lines and curves.**
- Aligned columns are easier to scan than zig-zag.
- Tab indicators have a continuous underline = clear flow.
- Connector lines in flow diagrams beat arrows-everywhere.

### Common Region
**Things inside the same container = grouped.**
- Card boundaries communicate "this stuff belongs together".
- Sidebar boundary separates nav from content.
- Modal boundary screams "focus here, ignore behind".

### Figure-Ground
**Strong contrast separates focal element from background.**
- Modals dim the page behind them (overlay 50-60% black).
- Selected row darkens its fill or thickens its border.
- Focused input glows; others recede.

## Cognitive Biases That Affect UX

### Anchoring
First number seen biases all subsequent judgments.
- **Pricing tables**: show the highest tier first. Customers anchor to it, find middle "reasonable".
- Default values anchor too — pick smart defaults, not zero.

### Loss aversion
Losing $10 hurts ~2x more than gaining $10 feels good.
- **Confirm destructive actions**: "Delete order? This can't be undone."
- **Undo > confirmation** when feasible: faster and lower friction (Gmail's 5-second undo is better than "are you sure").
- Free trials end in loss framing: "Your access expires in 3 days" > "Upgrade to keep features".

### Default effect
People stick with defaults far more than chosen options.
- Pre-check the recommended option (organ donation rates triple in opt-out countries).
- Default sort, default filter, default view — design carefully.
- BUT: never pre-check legally meaningful consents (GDPR violation).

### Status quo bias
Users resist change. New features hide unless surfaced.
- **Onboarding tooltips** for new functionality. But MAX 1 per session.
- **What's new** modal sparingly — release notes, not feature popup spam.
- **Sunset old patterns gradually**: keep old way available while introducing new.

### Recency / Primacy
First and last items in a list are remembered better than middle.
- Most important nav item first or last.
- Important confirmation buttons LAST (right side typically).
- Quick filters: most-common first.

### Social proof
"100 people viewing this" / "23 reviews" boosts trust.
- Show usage indicators on shared resources ("Edited by Anna 2h ago").
- Activity feeds on dashboards build engagement.

### Zeigarnik effect
Brain remembers incomplete tasks better than completed ones.
- Progress bars create urgency to finish (LinkedIn profile completeness, onboarding checklists).
- "3 of 5 fields filled" is more compelling than "60%".
- BUT: don't fake-incomplete things to manipulate. Users notice.

### Peak-end rule
Memory of an experience is shaped by its peak and its end.
- Polish the success moments (animation when payment succeeds, confetti for milestones).
- Polish the EXIT (logout, delete account, export data) — these are emotional moments.
- One delightful microinteraction beats consistent meh.

## Mental Models

The user has a model of how your system works. Misalign at your peril.

**Find the mismatch:**
- "I clicked save but nothing happened" = no visible feedback = mental model says "click=action" but design says nothing.
- "Where do I find my orders?" = nav doesn't surface "Orders" prominently = navigation taxonomy mismatch.
- "Why can't I delete this?" = permission model not exposed = invisible state.

**Cures:**
- Visible feedback on every action.
- Use users' words for nav items (not internal jargon).
- Surface state visibly (disabled buttons, locked icons, "read-only" badges).
- Match real-world metaphors (folder, trash, draft, send).

## Three Levels of Processing (Don Norman)

Design needs to work at all three:

1. **Visceral** (gut reaction, <1s): Does it look trustworthy/professional/exciting?
2. **Behavioral** (using it): Does it feel responsive? Predictable? Smooth?
3. **Reflective** (after using): Did it solve my problem? Will I use it again?

CRM apps tend to over-index on behavioral and miss visceral. A clean professional aesthetic is itself a feature — operators trust the data more.

## Information Foraging

Users behave like animals foraging — they follow scent. "Information scent" = how clearly a link/button promises what's behind it.

- **Strong scent**: "Refunds last 30 days" → user knows exactly what's there.
- **Weak scent**: "Reports" → opaque.
- **No scent**: icon-only buttons without tooltips.

Apply: every interactive element should hint at its destination. Specific verbs > generic verbs. "Send invoice" > "Submit".

## When two principles conflict

- **Clarity > Consistency.** If a clearer pattern is slightly inconsistent with the rest, choose clarity.
- **Familiar > Original.** Boring patterns work. Save creativity for content, not navigation.
- **Visible > Hidden.** Hover-only and gesture-only interactions hurt discoverability.
- **Defaults > Configuration.** Most users never touch settings. Design for the unmodified state.
