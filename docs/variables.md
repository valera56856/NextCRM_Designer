---
name: NextCRM Figma Variables
description: All design tokens (variables) from the NextCRM Design System Figma library — colors, semantic, typography
type: reference
originSessionId: 760c92ac-8a84-4d34-865f-7ab0d8a8baa2
---
# Variables (NextCRM Design System)

`fileKey: H1Ngineb53cAIqPWdqD585`

## Variable Collections

### Colors / Primary
Variable set key: `a8b022c566405e3472ed76b0ad21b3f82c5266d1`

- `Primary / 0` … `Primary / 1000`
- `Blue / 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950`

(Code mirror in `tokens.css`:)
```
--blue-50: #EDF9FF;   --blue-500: #29A1FF;
--blue-100: #D8F0FF;  --blue-600: #1886FE;
--blue-200: #B9E6FF;  --blue-700: #0B6AEA;
--blue-300: #89D7FF;  --blue-800: #1056BD;
--blue-400: #51C0FF;  --blue-900: #144A94;
                       --blue-950: #112E5A;
```

Other primitive scales (mirrored in tokens.css, expected to also exist as Figma variables on other pages):
- Gray, Red, Green, Orange, Yellow, Indigo, Neutral — each with shades 50–950

### Colors / Semantic
Variable set key: `da89d206ca63467ccd782960c3db1eaa56970cb7`

Button states:
- `Button/primary/{enabled, hover, active, disabled, On colour}`
- `Button/secondary/{hover, active}`
- `Button/tertiary/{default, hover, active}`
- `Button/hyperlink/{default, hover, active}`
- `Button/Overlay`

Text:
- `Text/Primary`

(More semantic tokens almost certainly exist — surface, border, icon, etc. — and will be added when their pages are explored.)

### Typography Primary
Variable set key: `b86aeba9b92406f61c998a6121984ebd6210224f`

- `Letter spacing/50` … `Letter spacing/950` (FLOAT)

(Code mirror in `tokens.css`:)
```
Sizes: --text-50 (12px), --text-150 (14px), --text-250 (16px),
       --text-350 (18px), --text-450 (20px),
       --display-550 (24px), --display-650 (30px),
       --display-750 (36px), --display-850 (40px), --display-950 (48px)

Line heights: --leading-50 (18) ... --leading-950 (60)

Weights: regular 400, medium 500, semibold 600, bold 700

Font: 'Roboto', system-ui, sans-serif
```

### Spacing & Radius (from code, expected in Figma as variables)
- Spacing: 0, 2, 4, 6, 8, 10, 12, 16, 20, 24, 32, 40, 48
- Radius: 4, 8, 12, full (9999)

## How to reference in design-to-code

When generating React from Figma context, replace raw hex / px values with the corresponding CSS variable from `tokens.css`. Example:
- Figma fill `Blue / 600` → `var(--blue-600)`
- Figma `Button/primary/hover` → semantic class on Button component (do not inline)
