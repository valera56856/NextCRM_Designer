---
name: Don't use emoji as icons in mockups
description: User explicitly requested no emoji as icons. Use real SVG/component icons from the DS instead.
type: feedback
originSessionId: 760c92ac-8a84-4d34-865f-7ab0d8a8baa2
---
# No emoji as icons — use real DS icons

**Rule:** Never use emoji characters (🛒 🔔 📦 ⚠ 💳 ★ etc.) as icons in Figma mockups or generated UI.

**Why:** User said "без тупих ємодзи" — emojis look unprofessional, render inconsistently across OS/font, don't follow the design system, and break visual consistency. Real designs use uniform stroke/fill icons.

**How to apply:**

The NextCRM Design System (`H1Ngineb53cAIqPWdqD585`) has hundreds of Material-style icons published as components. ALWAYS import these via `figma.importComponentByKeyAsync(key)` instead of inline emoji.

Common icons needed for notifications:
- `shopping_cart` / `shopping_bag` — orders
- `warning` / `warning_amber` — alerts
- `inventory_2` / `package_2` — shipping/delivery
- `credit_card` / `payments` — payments
- `chat_bubble` / `chat` / `comment` / `message` — messages
- `star` / `star_border` — reviews
- `notifications` / `notifications_active` — bell
- `check` / `check_circle` — success
- `error` / `error_outline` — errors
- `sync_problem` / `sync` — sync issues
- `settings` — settings gear
- `close` — X dismiss
- `arrow_forward` / `arrow_back` — navigation arrows
- `chevron_right` / `chevron_left` / `chevron_down` — chevrons
- `more_horiz` / `more_vert` — kebab menus
- `filter_list` — filter
- `search` — search

To find a specific icon's component key, query the file's `components.json` for the icon name (lowercase, underscored).

**Before:** `txt({text:'🛒', size:14})`  ❌
**After:** `(await figma.importComponentByKeyAsync(SHOPPING_CART_KEY)).createInstance()` ✅

**Helper to add to scripts:**
```js
async function dsIcon(name, color, size=20) {
  const COMPONENT_KEY_MAP = { /* preload from components.json */ };
  const key = COMPONENT_KEY_MAP[name];
  if (!key) throw new Error('Unknown icon: ' + name);
  const comp = await figma.importComponentByKeyAsync(key);
  const inst = comp.createInstance();
  inst.resize(size, size);
  // override stroke color via findOne(VECTOR) -> strokes
  const vec = inst.findOne(n => n.type === 'VECTOR');
  if (vec) vec.strokes = [{type:'SOLID', color: hexToRgb(color)}];
  return inst;
}
```

## Pre-resolved DS icon keys (from components.json — verified)

```
arrow_back: 2ddd30755e12dba9b8bfac63c20498156e543c62
arrow_forward: a2605a4c74088b8a2fc2bcc0e0bd3302c13c9429
call_made: 8b8257855ff76fb21927b03eb1d792599af0700d
chat: 50728d7af62be3dd1a2efb91f2192b35f302de81
chat_bubble: cb10beb2009b22237591cfd569be7f24b881fbb1
check: 01b95483e48f25bf35ec08f0d7340307d000ef55
check_circle: 29c1f7a96db3738ae6e5b052a2d86aca828c355b
chevron_left: ba0ccdb15515dd8c7d6b6b9665d3637f36877f2f
chevron_right: c8fb1dac5848bfceb4a04f126a6ee837854b828f
close: 592378985f0dbd0f94215e914c963218929c88e1
comment: 3b845d6562eb21dc995572cd5a6e8abedea64522
credit_card: 56d2dc90a8fa4de67328aab19c5558477aeaad5b
error: 97401a338cf48f11b1ad309d609a047a323203a0
expand_more: 6125c81bb26e1289b51da7e4ce508b0654f78c90
filter_list: dcda6eb7c22790030dbce3ab7563acea9bb94f8a
keyboard_arrow_down: f8f69ac2a97f4b7dcd51920cd06f6216c2fe49ec
message: 200bbdd320094477669bc2db9d36f62d7379356c
more_horiz: b8884870eb32ad5f0995fcfa23e29a459552e5b2
more_vert: 29d4982d6a36daed7eed2bb5accc75480826171d
notifications: 369438428a6f975abd7bba3968cc02f172a860c0
notifications_active: 3c7a67cfdb362dd19b8d1237eef8c862b733f96d
payments: d06c39c1637d71cc7412ecfacf38c930202e50cc
search: f97da6426f15b2314cb75e2b1203106e18561b3b
settings: dc6555f86557e51c530ae396c7a3f2427570976b
shopping_bag: 9d5d4ce19edc137a92a2a068a78f7558a513577c
shopping_cart: ce523a27c4cb24965a8daa0074274a83b5f47ef1
star: f16535f69ff76c665f202dd079b46a7e9f4cd78e
star_border: 795c40b8ad180ce60a5be159f093178b29a3e072
sync: a0ecabeaf31cd4edd663609e8e3e876626f016e4
sync_problem: a4b536b9102ec328dcdcf0da3a17b05c98a57a64
warning: 361fc006addb4cf3cea332c88c1d352bb9fc930a
```
