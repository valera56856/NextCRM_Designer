---
name: Figma Plugin API Cookbook (use_figma)
description: Hard-won lessons for use_figma — auto-layout sizing, alignment enums, component import, text overrides. READ THIS BEFORE writing JS in use_figma.
type: reference
originSessionId: 760c92ac-8a84-4d34-865f-7ab0d8a8baa2
---
# Figma Plugin API — Cookbook for use_figma

## Mental model

The `use_figma` MCP tool runs JavaScript inside Figma's Plugin API context. You're not generating files — you're **scripting Figma itself**. Same APIs that real plugins use.

## The 10 gotchas that bit me

### 1. Alignment enums are `'MIN' | 'MAX' | 'CENTER'` — NOT `'START'/'END'`
```js
frame.counterAxisAlignItems = 'MIN';      // ✅ top-aligned
frame.counterAxisAlignItems = 'START';    // ❌ InvalidEnumValue
frame.primaryAxisAlignItems = 'SPACE_BETWEEN';  // ✅
```

### 2. New auto-layout frames default to 100×100 (visible bug if you forget)
After `figma.createFrame()` + `layoutMode = 'VERTICAL'`, the frame is **100×100 with FIXED sizing**. Children may render but the frame stays 100px wide/tall, clipping content. Always explicitly set sizing.

### 3. Set sizing AFTER appendChild
`layoutSizingHorizontal = 'FILL'` requires the frame to already be a **child of an auto-layout parent**. Order:
```js
parent.appendChild(child);          // 1) appendChild first
child.layoutSizingHorizontal = 'FILL';  // 2) then sizing
```
Same for `layoutGrow = 1`.

### 4. `'FILL'` requires parent's primary axis to be FIXED
Child can only `FILL` a primary axis dimension if parent has FIXED size on that axis. So:
- Phone frame: `setSize(phone, 375, 812)` → FIXED
- Then `setSize(child, 'FILL', 'FILL')` works inside phone ✅
- If phone is `'HUG'`/`'HUG'` → child FILL errors out ❌

### 5. Cross axis vs primary axis confusion
- VERTICAL frame: primary=vertical, cross=horizontal
- HORIZONTAL frame: primary=horizontal, cross=vertical
- `layoutSizingHorizontal` always means horizontal regardless of layoutMode
- `primaryAxisAlignItems` aligns along primary axis (justify-content)
- `counterAxisAlignItems` aligns along cross axis (align-items)

### 6. setProperties for component instance text overrides
```js
const inst = button.createInstance();
const props = inst.componentProperties || {};
const labelKey = Object.keys(props).find(k => k.toLowerCase().includes('label'));
if (labelKey) inst.setProperties({[labelKey]: 'Click me'});
else {
  // fallback: find text node and override directly
  const t = inst.findOne(n => n.type === 'TEXT');
  if (t) { t.fontName = {family:'Roboto', style:'Medium'}; t.characters = 'Click me'; }
}
```
Always wrap text override in try/catch — instances with weird structure throw.

### 7. Importing DS components by key
```js
const compSet = await figma.importComponentSetByKeyAsync('4af7bd61bebb20...');
// pick variant by name match
const primarySm = compSet.children.find(c => c.name.includes('Type=Primary, State=Enabled, Size=small, Style=Fill'));
const inst = primarySm.createInstance();
```
Use `importComponentByKeyAsync` for a single component (no variants). Keys live in `components.json` / `component_sets.json` REST endpoints.

### 8. Font loading is async and required
Before setting `text.characters` or `text.fontName`, load the font:
```js
await figma.loadFontAsync({family:'Roboto', style:'Regular'});
await figma.loadFontAsync({family:'Roboto', style:'Medium'});
await figma.loadFontAsync({family:'Roboto', style:'Bold'});
```
Inter quirk: style is `'Semi Bold'` (with space), not `'SemiBold'`.

### 9. Stroke directions need explicit weights
```js
frame.strokes = [{type:'SOLID', color:{r:0.94,g:0.94,b:0.94}}];
frame.strokeWeight = 1;        // master weight (required)
frame.strokeBottomWeight = 1;  // only bottom border
frame.strokeTopWeight = 0;
frame.strokeLeftWeight = 0;
frame.strokeRightWeight = 0;
```
Forgetting strokeWeight makes all sides 0 even if directional weights are set.

### 10. Effects (shadows) need full object
```js
frame.effects = [{
  type: 'DROP_SHADOW',
  visible: true,
  blendMode: 'NORMAL',
  color: {r:0, g:0, b:0, a:0.16},
  offset: {x:0, y:8},
  radius: 32,
  spread: 0,
}];
```
All seven keys required. Missing any → silent ignore or error.

## Reusable helpers (paste in every script)

```js
const c = (hex) => {
  const n = hex.replace('#','');
  return {r:parseInt(n.slice(0,2),16)/255, g:parseInt(n.slice(2,4),16)/255, b:parseInt(n.slice(4,6),16)/255};
};
const SOLID = (hex, a=1) => ({type:'SOLID', color:c(hex), opacity:a});

function aFrame(opts) {
  const f = figma.createFrame();
  f.layoutMode = opts.dir;
  f.itemSpacing = opts.gap || 0;
  f.paddingLeft = opts.pl || 0; f.paddingRight = opts.pr || 0;
  f.paddingTop = opts.pt || 0; f.paddingBottom = opts.pb || 0;
  f.fills = opts.fill ? [SOLID(opts.fill, opts.fillA)] : [];
  if (opts.radius != null) f.cornerRadius = opts.radius;
  if (opts.alignH) f.primaryAxisAlignItems = opts.alignH;
  if (opts.alignV) f.counterAxisAlignItems = opts.alignV;
  return f;
}

function setSize(f, h, v) {
  if (typeof h === 'number') { f.layoutSizingHorizontal = 'FIXED'; f.resize(h, f.height); }
  else f.layoutSizingHorizontal = h;  // 'HUG' | 'FILL'
  if (typeof v === 'number') { f.layoutSizingVertical = 'FIXED'; f.resize(f.width, v); }
  else f.layoutSizingVertical = v;
}

function txt({text='', size=14, style='Regular', color, lineHeight, letterSpacing, align, w}) {
  const t = figma.createText();
  t.fontName = {family:'Roboto', style};
  t.fontSize = size;
  t.characters = text;
  if (color) t.fills = [SOLID(color)];
  if (lineHeight) t.lineHeight = {value:lineHeight, unit:'PIXELS'};
  if (letterSpacing) t.letterSpacing = {value:letterSpacing, unit:'PERCENT'};
  if (align) t.textAlignHorizontal = align;
  if (w) t.resize(w, t.height);
  return t;
}
```

## Workflow that saves time

1. **Cleanup first.** Always start by removing your own previous output:
   ```js
   for (const child of page.children) {
     if (child.type === 'SECTION' && child.name?.includes('Claude mockup')) child.remove();
   }
   ```
   Otherwise debugging multiple iterations leaves zombie sections.

2. **Build minimum viable frame, screenshot, iterate.** Don't write 500 lines then find sizing was wrong on the whole tree.

3. **Use SECTION as your scratch container.** SECTION is a top-level container that holds frames at absolute positions — you don't need auto-layout for the outer scaffold.

4. **Get screenshot after every meaningful change.** `get_screenshot` with the section/frame ID confirms the visual.

5. **Don't trust hug sizing on text-heavy frames.** When a row contains long text + spacers + actions, hug-height gets weird. Set explicit width via `setSize(row, 'FILL', 'HUG')` or `setSize(row, 600, 'HUG')`.

## What I cannot do via Plugin API

- **Variables endpoint** (`/v1/files/{key}/variables/local`) needs `file_variables:read` scope — Enterprise plan only. Skip; read variable values from the design's actual fills instead.
- **Setting `figma.currentPage` directly** — use `await figma.setCurrentPageAsync(page)`.
- **Plugin data** (`getPluginData`/`setPluginData`) — not supported here, use `getSharedPluginData(namespace, key)` instead.
