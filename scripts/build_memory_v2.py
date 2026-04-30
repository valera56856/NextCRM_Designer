#!/usr/bin/env python3
"""V2: Recursively find component sets nested in SECTION/FRAME containers."""
import json, os, re

PAGES_DIR = "/Users/nextcrm/.claude/projects/-Users-nextcrm-Desktop-Projects-NextCRM/memory/figma-ds/raw"
MEM_DIR = "/Users/nextcrm/.claude/projects/-Users-nextcrm-Desktop-Projects-NextCRM/memory/figma-ds/pages"
FILE_KEY = "H1Ngineb53cAIqPWdqD585"

def slug(s):
    s = re.sub(r"[^\w\s\-]", "", s, flags=re.UNICODE).strip()
    s = re.sub(r"\s+", "-", s).lower()
    return s[:60] or "page"

def clean_name(s):
    return re.sub(r"^[✅🟡🟢🔴◆❖\s]+", "", s).strip()

def status_emoji(s):
    if "✅" in s: return "✅ done"
    if "🟢" in s: return "🟢 done"
    if "🟡" in s: return "🟡 in-progress"
    if "🔴" in s: return "🔴 not-started"
    return "—"

def find_component_sets(node, depth=0, path=""):
    """Recursively yield COMPONENT_SET nodes anywhere in the tree."""
    name = node.get("name","")
    cur_path = f"{path} → {name}" if path else name
    if node.get("type") == "COMPONENT_SET":
        yield {
            "name": name, "id": node.get("id"), "path": path or "(root)",
            "variants": [c.get("name","") for c in node.get("children", []) if c.get("type")=="COMPONENT"],
            "bbox": node.get("absoluteBoundingBox") or {},
        }
        return  # don't recurse into variants
    for c in node.get("children", []):
        yield from find_component_sets(c, depth+1, cur_path)

def find_sections(node, depth=0):
    """Yield top-level SECTION/FRAME containers (skip components themselves)."""
    if depth >= 1: return
    for c in node.get("children", []):
        t = c.get("type","")
        if t in ("SECTION","FRAME","GROUP"):
            yield c

def summarize_page(page_node, page_name, page_id, status):
    name_clean = clean_name(page_name)
    url = f"https://www.figma.com/design/{FILE_KEY}/?node-id={page_id.replace(':','-')}"
    lines = [
        "---",
        f"name: Figma Page — {name_clean}",
        f"description: NextCRM DS page \"{name_clean}\" — {status}. Component sets + variants extracted recursively from REST API.",
        "type: reference",
        "---",
        "",
        f"# {name_clean}",
        "",
        f"**URL:** {url}",
        f"**NodeId:** `{page_id}`",
        f"**Status:** {status}",
        "",
    ]
    children = page_node.get("children", [])
    if not children:
        lines.append("_Empty page — no content yet (red status)._")
        return "\n".join(lines)

    # Direct top-level structure
    sections = []
    for c in children:
        t = c.get("type","")
        nm = c.get("name","")
        nid = c.get("id","")
        bbox = c.get("absoluteBoundingBox") or {}
        w, h = bbox.get("width"), bbox.get("height")
        sz = f" {int(w)}×{int(h)}" if w and h else ""
        sections.append({"type": t, "name": nm, "id": nid, "size": sz, "node": c})

    lines.append(f"## Top-level structure ({len(sections)} containers)")
    for s in sections:
        lines.append(f"- **{s['name']}** ({s['type']}) `{s['id']}`{s['size']}")
    lines.append("")

    # All component sets, recursively
    all_sets = list(find_component_sets(page_node))
    if all_sets:
        lines.append(f"## Component Sets ({len(all_sets)})")
        lines.append("")
        for cs in all_sets:
            bbox = cs["bbox"]
            sz = f" {int(bbox['width'])}×{int(bbox['height'])}" if bbox.get('width') else ""
            lines.append(f"### {cs['name']}")
            lines.append(f"`{cs['id']}` — _{cs['path']}_{sz}")
            if cs["variants"]:
                lines.append(f"_{len(cs['variants'])} variants:_")
                for v in cs["variants"][:30]:
                    lines.append(f"- `{v}`")
                if len(cs["variants"]) > 30:
                    lines.append(f"- _+{len(cs['variants'])-30} more variants_")
            lines.append("")
    else:
        lines.append("## Component Sets")
        lines.append("_None found at depth=3._")
        lines.append("")

    return "\n".join(lines)

# Read manifest from raw dir's manifest if it exists, else rebuild
manifest_path = "/tmp/figma-dump/pages/_manifest.json"
with open(manifest_path) as f:
    manifest = json.load(f)

written = 0
for entry in manifest:
    pid = entry["id"]
    pname = entry["name"]
    fname = entry.get("file")
    status = status_emoji(pname)
    if not fname:
        continue
    fpath = os.path.join(PAGES_DIR, fname)
    if not os.path.exists(fpath) or os.path.getsize(fpath) < 100:
        md = summarize_page({"children": []}, pname, pid, status)
    else:
        with open(fpath) as f:
            data = json.load(f)
        page_node = data.get("nodes", {}).get(pid, {}).get("document", {})
        md = summarize_page(page_node, pname, pid, status)
    out_name = f"{slug(clean_name(pname))}.md"
    out_path = os.path.join(MEM_DIR, out_name)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md)
    written += 1

print(f"Rewrote {written} page MDs with recursive component_set extraction")
