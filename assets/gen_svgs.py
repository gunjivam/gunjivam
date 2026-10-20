"""Generate the animated SVGs for the GitHub profile README."""
from xml.sax.saxutils import escape
import os

OUT = "/home/claude/github-profile/assets"
os.makedirs(OUT, exist_ok=True)
FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
CW = 9.0  # approx char width at 15px monospace

# ---------------------------------------------------------------- terminal
W, H = 760, 505
lines = [
    # (kind, text, color, start_time)
    ("cmd", "whoami", None, 0.6),
    ("out", "vamsi-avinash-gunji  ·  Senior DevOps Engineer / SRE @ Bank of America", "#e6edf3", None),
    ("cmd", "platform ls --clouds", None, None),
    ("out", "CLOUD       WHAT I RUN THERE", "#7d8590", None),
    ("out", "aws         EKS · EC2 · ROSA · IAM · CodePipeline · Artifactory", "#ff9e3d", None),
    ("out", "azure       AKS · Azure DevOps · Repos · cloud migration (-30% cost)", "#4aa8ff", None),
    ("out", "gcp         GKE · Rundeck automation · Terraform providers", "#5fd38d", None),
    ("out", "openshift   9+ clusters · 50+ apps · blue-green + A/B releases", "#ff6b6b", None),
    ("cmd", "terraform plan -target=module.certifications", None, None),
    ("out", '  + aws   = ["DevOps Engineer Pro", "Data Analytics Specialty"]', "#3fb950", None),
    ("out", '  + azure = ["DevOps Engineer Expert", "Administrator", "Data Scientist"]', "#3fb950", None),
    ("out", '  + cncf  = ["CKA", "CKAD", "CKS", "KCNA"]', "#3fb950", None),
    ("out", '  + hashi = ["Terraform Associate"]', "#3fb950", None),
    ("out", "Plan: 10 to add, 0 to change, 0 to destroy.", "#e6edf3", None),
    ("cmd", 'curl -s vamsiavinashgunji.com/contact', None, None),
    ("out", '{"open_to": "platform eng · multi-cloud · IaC · automation", "say": "hi 👋"}', "#d2a8ff", None),
]

parts = []
parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Animated terminal introducing Vamsi Avinash Gunji">')
parts.append(f"""<defs>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d1117"/><stop offset="1" stop-color="#111826"/></linearGradient>
</defs>
<style>
text{{font-family:{FONT};font-size:15px;white-space:pre}}
.p{{fill:#3fb950;font-weight:700}} .c{{fill:#79c0ff}} .t{{fill:#7d8590;font-size:13px}}
.cur{{fill:#e6edf3;animation:b 1s steps(1) infinite}} @keyframes b{{50%{{opacity:0}}}}
</style>
<rect width="{W}" height="{H}" rx="12" fill="url(#g)" stroke="#30363d"/>
<rect width="{W}" height="36" rx="12" fill="#161b22"/><rect y="24" width="{W}" height="12" fill="#161b22"/>
<circle cx="22" cy="18" r="6" fill="#ff5f57"/><circle cx="42" cy="18" r="6" fill="#febc2e"/><circle cx="62" cy="18" r="6" fill="#28c840"/>
<text x="{W/2}" y="23" text-anchor="middle" class="t">vamsi@platform: ~ — zsh</text>""")

y, t, x0 = 68, 0.6, 22
clip_id = 0
for kind, text, color, start in lines:
    if start is not None:
        t = start
    if kind == "cmd":
        prompt_w = 2 * CW  # "$ "
        n = len(text)
        typing = max(0.5, n * 0.045)
        clip_id += 1
        # stepped widths, one char at a time
        vals = ";".join(f"{i * CW:.1f}" for i in range(n + 1))
        parts.append(f'<g opacity="0"><set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/>'
                     f'<text x="{x0}" y="{y}" class="p">$</text></g>')
        parts.append(f'<clipPath id="k{clip_id}"><rect x="{x0 + prompt_w}" y="{y - 16}" height="22" width="0">'
                     f'<animate attributeName="width" values="{vals}" calcMode="discrete" begin="{t + 0.25:.2f}s" dur="{typing:.2f}s" fill="freeze"/></rect></clipPath>')
        parts.append(f'<text x="{x0 + prompt_w}" y="{y}" class="c" clip-path="url(#k{clip_id})">{escape(text)}</text>')
        t += 0.25 + typing + 0.35
    else:
        parts.append(f'<g opacity="0"><set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/>'
                     f'<text x="{x0}" y="{y}" fill="{color}">{escape(text)}</text></g>')
        t += 0.18
        if kind == "out" and lines.index((kind, text, color, start)) + 1 < len(lines) and \
                lines[lines.index((kind, text, color, start)) + 1][0] == "cmd":
            t += 0.5
    y += 26

# final prompt with blinking cursor
parts.append(f'<g opacity="0"><set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/>'
             f'<text x="{x0}" y="{y}" class="p">$</text><rect x="{x0 + 2*CW}" y="{y - 14}" width="9" height="18" class="cur"/></g>')
parts.append("</svg>")
assert y + 20 < H, y
open(f"{OUT}/terminal.svg", "w").write("\n".join(parts))

# ---------------------------------------------------------------- pipeline
stages = [
    ("2016", "Seton Hall", "BS CS + Math"),
    ("2019", "Clarivate", "SWE → DevOps"),
    ("2022", "Farmers", "DevOps · ROSA"),
    ("2022", "Home Depot", "SRE II"),
    ("2023", "State Street", "Platform Eng"),
    ("2023", "PwC", "DevOps"),
    ("2023", "Bank of America", "DevOps"),
    ("2025", "Goldman Sachs", "Sr. DevOps"),
    ("now", "Bank of America", "Sr. DevOps / SRE"),
]
W, H = 1000, 220
x_start, x_end, cy = 70, 925, 110
step = (x_end - x_start) / (len(stages) - 1)
p = []
p.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Career shown as a deployment pipeline from 2016 to now">')
p.append(f"""<style>
text{{font-family:{FONT}}}
.yr{{fill:#7d8590;font-size:12px}} .co{{fill:#e6edf3;font-size:13px;font-weight:700}} .ro{{fill:#8b949e;font-size:11.5px}}
.hd{{fill:#e6edf3;font-size:14px;font-weight:700}} .sub{{fill:#7d8590;font-size:12px}}
.ring{{transform-box:fill-box;transform-origin:center;animation:pulse 2s ease-out infinite}}
@keyframes pulse{{0%{{opacity:.8;transform:scale(1)}}100%{{opacity:0;transform:scale(2.2)}}}}
</style>
<rect width="{W}" height="{H}" rx="12" fill="#0d1117" stroke="#30363d"/>
<text x="24" y="34" class="hd">career.pipeline</text>
<text x="160" y="34" class="sub">#9 · main · triggered by curiosity in 2016</text>
<text x="{W-24}" y="34" text-anchor="end" class="sub" opacity="0">deployed ✔<set attributeName="opacity" to="1" begin="{len(stages)*0.55:.2f}s" fill="freeze"/><animate attributeName="fill" values="#7d8590;#3fb950" begin="{len(stages)*0.55:.2f}s" dur="0.4s" fill="freeze"/></text>
<line x1="{x_start}" y1="{cy}" x2="{x_end}" y2="{cy}" stroke="#30363d" stroke-width="4" stroke-linecap="round"/>
<line x1="{x_start}" y1="{cy}" x2="{x_start}" y2="{cy}" stroke="#238636" stroke-width="4" stroke-linecap="round">
<animate attributeName="x2" from="{x_start}" to="{x_end}" begin="0.3s" dur="{(len(stages)-1)*0.55:.2f}s" fill="freeze"/></line>""")
for i, (yr, co, ro) in enumerate(stages):
    x = x_start + i * step
    t = 0.3 + i * 0.55
    last = i == len(stages) - 1
    if last:
        p.append(f'<circle cx="{x}" cy="{cy}" r="15" fill="#3fb950" class="ring" opacity="0"/>')
    p.append(f'<circle cx="{x}" cy="{cy}" r="15" fill="#161b22" stroke="#30363d" stroke-width="3">'
             f'<set attributeName="stroke" to="{"#3fb950" if last else "#238636"}" begin="{t:.2f}s" fill="freeze"/>'
             f'<set attributeName="fill" to="{"#0f2e1a" if last else "#238636"}" begin="{t:.2f}s" fill="freeze"/></circle>')
    glyph = "▶" if last else "✓"
    p.append(f'<text x="{x}" y="{cy + 5}" text-anchor="middle" fill="#fff" font-size="{12 if last else 14}" opacity="0">{glyph}'
             f'<set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/></text>')
    p.append(f'<text x="{x}" y="{cy - 30}" text-anchor="middle" class="yr">{yr}</text>')
    words = co.split(" ")
    if len(co) > 12 and len(words) > 1:
        a = " ".join(words[:-1]); b = words[-1]
        p.append(f'<text x="{x}" y="{cy + 42}" text-anchor="middle" class="co">{escape(a)}</text>')
        p.append(f'<text x="{x}" y="{cy + 58}" text-anchor="middle" class="co">{escape(b)}</text>')
        ry = cy + 76
    else:
        p.append(f'<text x="{x}" y="{cy + 42}" text-anchor="middle" class="co">{escape(co)}</text>')
        ry = cy + 60
    p.append(f'<text x="{x}" y="{ry}" text-anchor="middle" class="ro">{escape(ro)}</text>')
# travelling packet, loops forever after the first run
p.append(f'<circle r="5" fill="#79c0ff"><animateMotion path="M{x_start},{cy} L{x_end},{cy}" dur="4s" begin="{len(stages)*0.55:.2f}s" repeatCount="indefinite"/>'
         f'<animate attributeName="opacity" values="0;1;1;0" dur="4s" begin="{len(stages)*0.55:.2f}s" repeatCount="indefinite"/></circle>')
p.append("</svg>")
open(f"{OUT}/pipeline.svg", "w").write("\n".join(p))
print("ok")
