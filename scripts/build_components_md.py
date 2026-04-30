#!/usr/bin/env python3
"""Rebuild components.md with full list from REST API."""
import json, os
from collections import defaultdict

with open('/tmp/figma-dump/component_sets.json') as f:
    sets = json.load(f).get('meta', {}).get('component_sets', [])
with open('/tmp/figma-dump/components.json') as f:
    comps = json.load(f).get('meta', {}).get('components', [])

# Bucket sets by their containing page (containing_frame.containingStateGroup or pageId)
sets_by_page = defaultdict(list)
for s in sets:
    page_id = s.get('containing_frame', {}).get('pageId') or s.get('containing_frame', {}).get('nodeId') or 'unknown'
    page_name = s.get('containing_frame', {}).get('pageName') or '—'
    sets_by_page[(page_id, page_name)].append(s)

# Same for loose components (only ones not part of a set — i.e. component_set_id is None)
loose = [c for c in comps if not c.get('component_set_id')]
loose_by_page = defaultdict(list)
for c in loose:
    page_id = c.get('containing_frame', {}).get('pageId') or 'unknown'
    page_name = c.get('containing_frame', {}).get('pageName') or '—'
    loose_by_page[(page_id, page_name)].append(c)

lines = [
    '---',
    'name: NextCRM Figma Components Full Catalog',
    'description: Full published-component catalog of NextCRM DS — 145 component sets + 2678 components, grouped by page',
    'type: reference',
    '---',
    '',
    '# Components — Full Catalog',
    '',
    f'**File Key:** `H1Ngineb53cAIqPWdqD585`',
    f'**Library Key:** `lk-b424958829321032d02eb237300bfcb3204bc53de4b95c86f2f754fff11ff6db927665ccf3c6ea9a1b985d296910034a9fc57a6bde61529f37e76b193e1cd270`',
    f'**Totals:** {len(sets)} component sets, {len(comps)} components ({len(loose)} loose, {len(comps)-len(loose)} variants)',
    '',
    '## Component Sets by Page',
    '',
]

# Sort pages: those with most sets first, but keep predictable ordering
sorted_pages = sorted(sets_by_page.items(), key=lambda x: (-len(x[1]), x[0][1]))
for (pid, pname), items in sorted_pages:
    if not items: continue
    lines.append(f'### {pname}  `{pid}`')
    lines.append('')
    for s in sorted(items, key=lambda x: x.get('name','')):
        nm = s.get('name','')
        nid = s.get('node_id','')
        key = s.get('key','')
        desc = (s.get('description') or '').strip().replace('\n',' ')
        desc_short = (desc[:80] + '…') if len(desc) > 80 else desc
        lines.append(f"- **{nm}** — node `{nid}`, key `{key}`" + (f" — _{desc_short}_" if desc else ""))
    lines.append('')

# Loose components, only show pages that have non-icon stuff
lines.append('## Loose (non-set) Components by Page')
lines.append('')
sorted_loose = sorted(loose_by_page.items(), key=lambda x: (-len(x[1]), x[0][1]))
for (pid, pname), items in sorted_loose:
    if not items: continue
    lines.append(f'### {pname}  `{pid}`  — {len(items)} components')
    # Show only first 30 names, the rest are typically icon variants
    names = [c.get('name','') for c in items]
    for n in names[:30]:
        lines.append(f'- `{n}`')
    if len(names) > 30:
        lines.append(f'- _+{len(names)-30} more (likely icons/glyphs)_')
    lines.append('')

OUT = '/Users/nextcrm/.claude/projects/-Users-nextcrm-Desktop-Projects-NextCRM/memory/figma-ds/components.md'
with open(OUT, 'w') as f:
    f.write('\n'.join(lines))
print(f'Wrote {OUT} ({len(lines)} lines)')
