# NextCRM Designer

Local mirror and machine-readable extract of the **NextCRM Design System** Figma file, built so AI agents (and humans) can reference tokens, components, and per-page structure without re-querying Figma every time.

## Source

- **Figma file:** [NextCRM Design System](https://www.figma.com/design/H1Ngineb53cAIqPWdqD585/NextCRM-Design-System)
- **File key:** `H1Ngineb53cAIqPWdqD585`
- **Library key:** `lk-b424958829321032d02eb237300bfcb3204bc53de4b95c86f2f754fff11ff6db927665ccf3c6ea9a1b985d296910034a9fc57a6bde61529f37e76b193e1cd270`

## Structure

```
docs/                    Human-readable markdown summaries
├── _index.md            Master index — all 47 pages with links
├── components.md        Full catalog: 145 component sets + 2678 components
├── variables.md         Color, semantic, typography token reference
└── pages/               One file per Figma page
    ├── button.md        Button page — 6 component sets, 198 variants
    ├── modal.md         Modal page — 5 component sets
    ├── select.md        Select page — 8 component sets
    └── ...44 more

raw/                     Source-of-truth JSON dumps from Figma REST API
├── 01-typography.json   per-page subtree (depth=3)
├── ...46 more
├── components.json      published components catalog
├── component_sets.json  published component sets catalog
└── styles.json          published styles catalog

scripts/                 Re-sync pipeline (Python 3, stdlib only)
├── fetch_pages.py       Pull all pages via Figma REST API
├── build_memory_v2.py   Convert raw JSON → markdown summaries
└── build_components_md.py  Build components.md catalog
```

## Stats

- **58 pages** in source file (47 with content, 11 separators/cover/archive — skipped)
- **30 components** marked done (✅), 6 in progress (🟡), 11 not started (🔴)
- **145 component sets**, **2678 components** published in library
- **12 MB** total (mostly raw JSON)

## How to re-sync

```bash
# 1. Get a Figma personal access token (Settings → Security → Generate)
#    Scope needed: file_content:read
export FIGMA_TOKEN="figd_..."

# 2. Re-pull all pages
python3 scripts/fetch_pages.py

# 3. Rebuild markdown
python3 scripts/build_memory_v2.py
python3 scripts/build_components_md.py
```

The pipeline is incremental — it skips already-cached page JSONs.

## How AI agents use this

Tell your agent: *"Use the design system in NextCRM-Designer to build screen X"*. The agent should:

1. Read `docs/_index.md` for the page list
2. Open `docs/pages/<component>.md` to see the component set, variants, node IDs
3. Cross-reference `docs/variables.md` for tokens
4. Use `docs/components.md` for Code Connect mapping keys
5. (Optional) Re-fetch deeper detail via Figma MCP `get_design_context` with `fileKey` + `nodeId`

## Token security

**Never commit `FIGMA_TOKEN`.** It's in `.gitignore` patterns. The scripts read it from env only — the repo contains zero credentials.

If a token is ever exposed (chat, gist, screenshot), revoke it immediately at https://www.figma.com/settings → Security → Personal access tokens.

## Code mirror

The React/CSS implementation lives in a separate repo. CSS tokens at `src/components/ui/tokens.css` are derived from this Figma file (header comment: `Design Tokens (from Figma)`).
