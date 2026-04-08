#!/usr/bin/env python3
import argparse
import html
import json
from pathlib import Path


def render_command(cmd: dict) -> str:
    params = cmd.get("params", [])
    examples = cmd.get("examples", [])
    params_rows = "".join(
        f"<tr><td>{html.escape(str(p.get('name', '')))}</td>"
        f"<td>{'yes' if p.get('required') else 'no'}</td>"
        f"<td>{html.escape(str(p.get('default', '')))}</td>"
        f"<td>{html.escape(str(p.get('description', '')))}</td></tr>"
        for p in params
    ) or "<tr><td colspan='4'>No parameters documented.</td></tr>"
    example_blocks = "".join(
        f"<pre><code>{html.escape(ex)}</code></pre>" for ex in examples
    ) or "<p>No examples documented.</p>"
    return f"""
    <section class="command-card" id="{html.escape(cmd.get('name', ''))}">
      <h2>{html.escape(cmd.get('name', ''))}</h2>
      <p class="meta">{html.escape(cmd.get('kind', ''))} · {html.escape(cmd.get('feature', ''))}</p>
      <p>{html.escape(cmd.get('summary', ''))}</p>
      <p><strong>Risk:</strong> {html.escape(cmd.get('risk', 'unknown'))}</p>
      <p><strong>Source:</strong> {html.escape(cmd.get('source_file', ''))} {html.escape(cmd.get('source_symbol', ''))}</p>
      <h3>Parameters</h3>
      <table>
        <thead><tr><th>Name</th><th>Required</th><th>Default</th><th>Description</th></tr></thead>
        <tbody>{params_rows}</tbody>
      </table>
      <h3>Examples</h3>
      {example_blocks}
    </section>
    """


def render_page(data: dict) -> str:
    nav = "".join(
        f"<li><a href='#{html.escape(cmd.get('name', ''))}'>{html.escape(cmd.get('name', ''))}</a></li>"
        for cmd in data.get("commands", [])
    )
    cards = "".join(render_command(cmd) for cmd in data.get("commands", []))
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(data.get('project', 'Codee Commands'))}</title>
  <style>
    :root {{ --bg:#f4f1ea; --ink:#1e1d1a; --muted:#686457; --card:#fffdf8; --line:#d7d0c1; --accent:#6e7f5b; }}
    body {{ margin:0; font:16px/1.5 Georgia, serif; color:var(--ink); background:linear-gradient(180deg,#f7f4ee, #ece6d9); }}
    .wrap {{ max-width:1200px; margin:0 auto; padding:32px 20px 80px; }}
    .hero {{ display:grid; gap:8px; margin-bottom:28px; }}
    .layout {{ display:grid; grid-template-columns:280px 1fr; gap:24px; }}
    .sidebar, .command-card {{ background:var(--card); border:1px solid var(--line); border-radius:18px; }}
    .sidebar {{ padding:18px; position:sticky; top:20px; height:fit-content; }}
    .command-card {{ padding:22px; margin-bottom:18px; }}
    .meta {{ color:var(--muted); }}
    ul {{ margin:0; padding-left:18px; }}
    a {{ color:var(--accent); text-decoration:none; }}
    table {{ width:100%; border-collapse:collapse; margin:12px 0; }}
    th, td {{ border-top:1px solid var(--line); padding:8px; text-align:left; vertical-align:top; }}
    pre {{ overflow:auto; background:#f1ede3; padding:12px; border-radius:12px; }}
    @media (max-width: 900px) {{ .layout {{ grid-template-columns:1fr; }} .sidebar {{ position:static; }} }}
  </style>
</head>
<body>
  <div class="wrap">
    <header class="hero">
      <h1>{html.escape(data.get('project', 'Command Manual'))}</h1>
      <div class="meta">Version {html.escape(data.get('version', 'unknown'))} · Updated {html.escape(data.get('updated_at', 'unknown'))}</div>
      <p>Operational command handbook for quick lookup of command purpose, parameters, examples, and risks.</p>
    </header>
    <div class="layout">
      <aside class="sidebar">
        <h2>Commands</h2>
        <ul>{nav}</ul>
      </aside>
      <main>{cards}</main>
    </div>
  </div>
</body>
</html>"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Render command catalog JSON to an HTML handbook.")
    parser.add_argument("input", help="Path to command catalog JSON")
    parser.add_argument("output", help="Output HTML file path")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    data = json.loads(input_path.read_text(encoding="utf-8"))
    output_path.write_text(render_page(data), encoding="utf-8")
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
