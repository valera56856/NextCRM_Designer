---
name: UX — Mobile & Accessibility
description: Thumb zones, touch targets, gestures, mobile patterns. WCAG 2.2 AA standards, keyboard navigation, screen readers, color blindness. Both topics share a constraint mindset.
type: reference
originSessionId: 760c92ac-8a84-4d34-865f-7ab0d8a8baa2
---
# UX — Mobile & Accessibility

Both mobile and a11y are about designing under constraints. Constraints expose hidden assumptions in your interface.

## Mobile Patterns

### The thumb zone (Steven Hoober research)

When holding a phone in one hand, three zones:
- **Easy** (bottom-center, ~33%): natural thumb reach
- **OK** (middle, ~33%): slight stretch
- **Hard** (top-corners, ~33%): requires re-grip

**Implications for design:**
- Primary actions go BOTTOM, not top.
- Bottom tab bars > top nav bars on mobile.
- Floating action button (FAB) bottom-right is optimal.
- Top-right is the WORST spot for important actions (close button OK, send button BAD).
- Pull-to-refresh works because the gesture starts in the easy zone.

### Touch target sizing

**Minimums:**
- iOS: 44pt × 44pt (Apple HIG)
- Android: 48dp × 48dp (Material)
- Web: 48px × 48px (WCAG 2.5.5)

**Spacing between targets:** ≥ 8px to avoid mis-taps.

**Common violations:**
- Close (X) buttons in modals at 24px (too small).
- Sidebar toggles at 32px.
- Action icons in table rows at 28px.

If your design has small icons, expand the HIT AREA via padding even if the visual stays small. Click area > visual area is fine.

### Native gestures (mobile)

| Gesture | Convention | Common usage |
|---------|-----------|--------------|
| Tap | iOS/Android both | Click |
| Long press | Both | Selection mode, context menu |
| Swipe left/right | Both | Reveal actions on rows, pagination |
| Swipe up | iOS home indicator, Android nav | OS-level — don't conflict |
| Swipe down | iOS notification center | Pull-to-refresh OK in app body |
| Pinch | Both | Zoom (images, maps) |
| Two-finger pan | Both | Map pan |
| Edge swipe (left) | iOS back gesture | Don't overload |
| Drag | Both | Reorder lists, drag-drop |

**Rules:**
- Always provide a button alternative for gestures (discoverability).
- New users don't know gestures exist — show on first use.
- iOS edge-swipe to go back is sacred — don't break.

### Mobile chrome patterns

**Top bar:**
- Title centered or left.
- Back button (chevron-left) far left, 32px hit area.
- 1-2 action icons far right, 32px each.
- Don't overload — if 3+ actions, use overflow menu (•••).

**Bottom tab bar:**
- 4-5 tabs MAX. Beyond = overflow tab labelled "More".
- Active tab: filled icon + colored label OR top accent line.
- Inactive: outline icon + muted label.
- 24px icons + 10-11px label.
- Safe area: 24px+ bottom padding for home indicator.

**Floating action button (FAB):**
- One per screen. The single most-important action.
- Bottom-right (or bottom-center for iOS-feeling apps).
- 56px diameter, brand color, shadow.
- Pairs with bottom tab bar by sitting above it OR offset to right.

**Status bar:**
- Don't render fake status bars — let the OS handle it.
- Match status bar style to top bar (light background = dark icons).

### Mobile-specific UX swaps

| Desktop | Mobile equivalent |
|---------|-------------------|
| Sidebar nav | Bottom tab bar + hamburger drawer for less-used |
| Hover states | Press states (visible while finger is down) |
| Right-click menu | Long-press menu |
| Tooltips | Tap-to-expand inline |
| Multi-column layout | Single column, stacked |
| Dropdown popover | Bottom sheet OR full-screen modal |
| Inline edit | Dedicated edit screen |
| Search bar prominent | Search icon → opens overlay |
| Two-pane (list + detail) | Drilldown navigation |
| Keyboard shortcuts | n/a — design for touch |

### Bottom sheets vs modals

- **Bottom sheet**: slides up from bottom, partial-height. Allows context. iOS Action Sheet, Android Bottom Sheet.
- **Modal (center)**: covers full screen or central area. Heavier, blocks more.

**Use bottom sheet when:**
- Quick action with multiple options ("Share via…").
- Context still visible behind.
- iOS or modern Android conventions expected.

**Use modal when:**
- Critical confirmation.
- Multi-step input requiring focus.
- Truly modal (must complete or cancel).

### Pull-to-refresh

- Works on lists/feeds where data freshness matters.
- Uses spring animation: drag down → spinner appears → release → refresh → spinner disappears.
- Don't overload with other vertical gestures (would conflict).
- Show last-refreshed time after pull.

### Skeleton loaders on mobile

- Critical on slow networks. Spinners feel broken on 3G.
- Skeleton matches actual content (avatar circle, title bar, body bar).
- Subtle shimmer: 1.5s loop, opacity 0.3-0.6.

### Network states

- **Offline**: detect, show banner "You're offline. Changes will sync."
- **Slow / 3G**: show skeleton longer, prefetch less.
- **Cellular vs WiFi**: don't auto-play video on cellular.
- **Data saver mode**: respect, reduce image quality.

### Safe areas

iPhone X+ has notch and home indicator. Use CSS env() vars:
```css
padding-top: env(safe-area-inset-top);
padding-bottom: env(safe-area-inset-bottom);
padding-left: env(safe-area-inset-left);  /* landscape */
padding-right: env(safe-area-inset-right);
```

Don't put interactive elements in safe area zones — they'll overlap OS UI.

### Forms on mobile

- **One field per screen** for complex forms (typeform pattern). Higher completion rates.
- **Auto-advance** to next field where possible.
- **Use HTML5 input types** for native keyboards: `tel`, `email`, `number`, `url`, `date`.
- **Autocomplete attributes**: `autocomplete="email"` etc. Lets browsers/keychains fill.
- **DON'T** auto-focus on mobile (pulls up keyboard immediately, jarring).
- **Submit button** ALWAYS visible (not below the fold).

### Mobile typography

- **Body 16px minimum** (iOS auto-zooms inputs <16px on focus, looks broken).
- **Headings 20-32px**.
- **Captions 12px floor**.
- Line-height 1.5 (more breathing room than desktop).
- Avoid all-caps for body — slow to read, suggests shouting.

### Mobile testing matrix

- iPhone SE (small, 375×667)
- iPhone 14 Pro (notch, 393×852)
- iPhone 14 Pro Max (huge, 430×932)
- Pixel 7 (Android, 412×915)
- iPad Mini (smallest tablet, 768×1024)

If it works on iPhone SE, it works everywhere.

---

## Accessibility (a11y)

Designing for users with disabilities makes the product better for EVERYONE. Captions help in noisy environments. Keyboard nav helps power users. High contrast helps in sunlight.

### WCAG 2.2 — the four principles (POUR)

1. **Perceivable** — info and UI must be presentable to users in ways they can perceive
2. **Operable** — UI must be operable (keyboard, voice, touch)
3. **Understandable** — info and operation must be understandable
4. **Robust** — content must be robust enough for assistive tech

### Conformance levels

| Level | Effort | Coverage |
|-------|--------|----------|
| **A** | Minimum | Catches major exclusions |
| **AA** | **The standard.** Required by ADA, EU, Canada, etc. | Most users covered |
| **AAA** | Premium | Usually only specific elements (close captions for live audio, etc.) |

**Target AA. Don't ship below A.**

### Color contrast

WCAG AA minimums:
- **Body text** (< 18px or < 14px bold): **4.5:1**
- **Large text** (≥ 18px or ≥ 14px bold): **3:1**
- **UI components** (buttons, form fields, icons): **3:1**
- **Focus indicators**: **3:1** against background

NextCRM contrast quick check:
- `Gray-700` (#525252) on white = 7.46:1 ✅
- `Gray-500` (#7C7C7C) on white = 4.6:1 ✅ (barely)
- `Gray-400` (#989898) on white = 2.85:1 ❌ (only for disabled / decorative)
- `Blue-600` (#1886FE) on white = 3.5:1 ✅ for large/UI, ❌ for body
- `Blue-700` (#0B6AEA) on white = 4.8:1 ✅ body too

**Tools:** Chrome DevTools color picker shows ratio. Stark plugin in Figma. WebAIM contrast checker.

### Color is never the only signal

Wrong: red dot indicates error.
Right: red dot + warning icon + "Sync failed" text.

8% of men are red-green colorblind. Design as if grayscale — does it still communicate?

### Keyboard navigation

Every interactive element must be:
1. **Reachable** via Tab.
2. **Operable** via Enter/Space.
3. **Visible** when focused (focus ring).

**Tab order**: matches visual order. No surprises (jumping right then back to left).

**Skip links**: hidden until focused, jump past nav: `[Skip to main content]`. Critical for screen reader and keyboard users.

**Focus traps in modals**: when modal open, Tab cycles WITHIN modal only. Esc closes.

**Focus restoration**: when modal closes, return focus to triggering element.

**Custom focus rings**: 2-3px outline, accent color, ≥3:1 contrast. Material default works.

```css
:focus-visible {
  outline: 2px solid var(--blue-600);
  outline-offset: 2px;
}
```

`:focus-visible` (not `:focus`) — shows ring only for keyboard users, not after mouse click.

### Keyboard shortcuts

For power users:
- ⌘K / Ctrl+K: command palette / search.
- / : search.
- ? : show all shortcuts.
- Esc: close modal / cancel.
- Enter: submit / confirm.
- Tab / Shift+Tab: navigate.

CRM-specific:
- `n` to create new (record, order).
- `c` to compose (message).
- `gd` to go to dashboard.

Document in a shortcut help modal accessible via `?`.

### Screen readers

Most-common: VoiceOver (Mac/iOS), NVDA (Windows free), JAWS (Windows commercial), TalkBack (Android).

**Semantic HTML wins:**
- `<button>` not `<div onClick>`.
- `<a href>` not `<span onClick>`.
- `<form>`, `<label for>`, `<input>`.
- `<nav>`, `<main>`, `<aside>`, `<header>`, `<footer>` — landmarks help screen reader users navigate.
- `<h1>` to `<h6>` in proper hierarchy (don't skip levels).

**ARIA when semantic HTML isn't enough:**
- `aria-label` for icon-only buttons: `<button aria-label="Close"><Icon /></button>`
- `aria-describedby` for tooltips and helper text linked to fields.
- `role="alert"` on toast notifications (announced immediately).
- `role="dialog"` + `aria-modal="true"` on modals.
- `aria-live="polite"` for non-urgent updates ("Saved").
- `aria-live="assertive"` for urgent ("Error").
- `aria-hidden="true"` for decorative elements.

**Label everything:**
- Form fields → `<label>`.
- Icon buttons → `aria-label`.
- Tables → `<caption>` or `aria-label`.
- Images → `alt=""` (empty for decorative, descriptive for meaningful).

**Test:** Tab through entire app with eyes closed, listening to VoiceOver. If you can't operate it, neither can a blind user.

### Forms accessibility

- **Labels visible**, not placeholder-as-label.
- **Required indicator**: asterisk + `aria-required="true"`.
- **Error linked**: `aria-describedby` on input pointing to error text id.
- **Inline errors**: not just color — text + icon.
- **Field grouping**: `<fieldset>` + `<legend>` for related radio groups.
- **Auto-completing fields**: `autocomplete="email"`, `autocomplete="tel"`, `autocomplete="given-name"`, etc.

### Tables accessibility

- `<table>` with `<thead>`, `<tbody>`.
- `<th>` for column headers, with `scope="col"`.
- `<caption>` describing the table.
- Avoid layout tables (use CSS Grid).

### Color blindness

Types:
- **Protanopia** (red blindness): avoid red/green pairs.
- **Deuteranopia** (green blindness): same.
- **Tritanopia** (blue-yellow blindness): less common.
- **Monochromacy**: rare; design for grayscale.

**Test:** apply grayscale filter — does the UI still communicate? Use Chrome DevTools Rendering panel "Emulate vision deficiencies".

### Reduced motion

`@media (prefers-reduced-motion: reduce)` → kill non-essential animation.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

Vestibular disorders cause nausea from parallax/zoom animations. Respect.

### Cognitive accessibility

Often overlooked:
- **Plain language**: 8th-grade reading level for general apps.
- **Predictable behavior**: same action → same result.
- **No time limits** unless safety-critical (banking session timeout). Or extendable.
- **Undo** for everything reversible.
- **Forgiving forms**: accept various phone formats, normalize on save.
- **Avoid jargon**: "Logout" not "End session". "Customers" not "Counterparties".

### Auditory accessibility

- **Captions** on videos.
- **Transcripts** for audio.
- **Visual alerts** alongside any sound (chime + popup, never chime alone).

### Motor / dexterity

- **Touch targets** large.
- **Don't require precise gestures** (3-finger swipe is hostile to motor-impaired users).
- **Allow time** — don't auto-close important dialogs after 5 seconds.

### Testing accessibility

- **axe DevTools** browser extension: catches ~30% of issues automatically.
- **Lighthouse** in Chrome DevTools.
- **Keyboard-only testing**: unplug mouse, navigate.
- **Screen reader testing**: turn on VoiceOver, listen.
- **Zoom testing**: zoom browser to 200% — does UI break?
- **Color blindness simulator** in Chrome DevTools.

### Accessibility quick wins (high impact, low effort)

1. Set `lang="uk"` on `<html>`.
2. Add `<title>` per page.
3. Use semantic HTML throughout.
4. Add `alt=""` to all images.
5. Visible focus rings (`:focus-visible`).
6. Color contrast meets 4.5:1 for body text.
7. All form fields have visible labels.
8. Skip-to-main-content link at page top.
9. Modal traps focus, Esc closes.
10. Respect `prefers-reduced-motion`.

These cover ~80% of common a11y issues.

## When mobile and a11y conflict (rare)

- **Touch target ≥ 44pt** can fight with **dense data tables**: solution = expand hit area without expanding visual area.
- **Color contrast** can fight with **brand subtlety**: solution = darken text/UI just for active state, keep brand decorative elements lighter.
- **Reduced motion** can fight with **delight animations**: solution = disable purely decorative motion, keep functional motion (slide-in cards stay functional, just shorter).

When in doubt: a11y wins.
