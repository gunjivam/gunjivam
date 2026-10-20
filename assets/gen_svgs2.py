"""Certification wall, languages card and LinkedIn card for the profile README."""
from xml.sax.saxutils import escape
OUT = "/home/claude/github-profile/assets"
FONT = "ui-sans-serif,-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
BASE = f"""<style>
.f{{font-family:{FONT}}} .m{{font-family:{MONO}}}
.in{{opacity:0;animation:up .5s ease-out forwards}}
@keyframes up{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:none}}}}
</style>"""

# ---------------------------------------------------------------- cert wall
vendors = {
    "AWS":       ("#ff9900", "#2a1d08"),
    "Microsoft": ("#2f9bff", "#0b1d33"),
    "CNCF":      ("#4c8dff", "#0f1a33"),
    "HashiCorp": ("#a57cff", "#1d1433"),
}
certs = [
    ("AWS", "DevOps Engineer", "Professional", "2022"),
    ("AWS", "Data Analytics", "Specialty", "2021"),
    ("Microsoft", "DevOps Engineer", "Expert", "2023"),
    ("Microsoft", "Azure Administrator", "Associate", "2023"),
    ("Microsoft", "Azure Data Scientist", "Associate", "2021"),
    ("CNCF", "CKA", "Kubernetes Admin", "2022"),
    ("CNCF", "CKAD", "App Developer", "2022"),
    ("CNCF", "CKS", "Security Specialist", "2023"),
    ("CNCF", "KCNA", "Cloud Native Associate", "2026"),
    ("HashiCorp", "Terraform", "Associate", "2023"),
]
W, cols, cw, ch, gap, top = 1000, 5, 180, 104, 10, 70
H = top + 2 * ch + gap + 26
x0 = (W - (cols * cw + (cols - 1) * gap)) / 2
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="10 certifications across AWS, Microsoft, CNCF and HashiCorp">', BASE]
s.append(f'<rect width="{W}" height="{H}" rx="12" fill="#0d1117" stroke="#30363d"/>')
s.append(f'<text x="24" y="40" class="f" fill="#e6edf3" font-size="18" font-weight="700">10 certifications</text>')
s.append(f'<text x="186" y="40" class="f" fill="#7d8590" font-size="14">· 4 vendors · multi-cloud by design</text>')
# vendor legend
lx = W - 24
for v in reversed(list(vendors)):
    n = sum(1 for c in certs if c[0] == v)
    label = f"{v} ×{n}"
    w = len(label) * 7.4 + 22
    lx -= w
    s.append(f'<circle cx="{lx + 6}" cy="35" r="5" fill="{vendors[v][0]}"/>'
             f'<text x="{lx + 16}" y="40" class="f" fill="#adbac7" font-size="13">{escape(label)}</text>')
    lx -= 10
for i, (v, title, sub, yr) in enumerate(certs):
    r, c = divmod(i, cols)
    x = x0 + c * (cw + gap)
    y = top + r * (ch + gap)
    accent, bg = vendors[v]
    big = len(title) <= 5  # acronyms (CKA etc.) get a big title
    s.append(f'<g class="in" style="animation-delay:{0.08 * i:.2f}s">')
    s.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="10" fill="{bg}" stroke="{accent}" stroke-opacity=".45"/>')
    s.append(f'<rect x="{x}" y="{y + 12}" width="4" height="{ch - 24}" rx="2" fill="{accent}"/>')
    s.append(f'<text x="{x + 16}" y="{y + 24}" class="m" fill="{accent}" font-size="11" font-weight="700" letter-spacing="1">{escape(v.upper())}</text>')
    s.append(f'<text x="{x + cw - 14}" y="{y + 24}" text-anchor="end" class="m" fill="#7d8590" font-size="11">{yr}</text>')
    if big:
        s.append(f'<text x="{x + 16}" y="{y + 60}" class="f" fill="#e6edf3" font-size="26" font-weight="800">{escape(title)}</text>')
    else:
        s.append(f'<text x="{x + 16}" y="{y + 56}" class="f" fill="#e6edf3" font-size="15" font-weight="700">{escape(title)}</text>')
    s.append(f'<text x="{x + 16}" y="{y + 82}" class="f" fill="#adbac7" font-size="{11.5 if len(sub) > 26 else 13}">{escape(sub)}</text>')
    s.append('</g>')
s.append("</svg>")
open(f"{OUT}/certs.svg", "w").write("\n".join(s))

# ---------------------------------------------------------------- languages I actually write
langs = [
    ("Python", "#3572A5", "automation, tooling, ops scripts", 5),
    ("HCL", "#844FBA", "Terraform modules & wrappers", 5),
    ("YAML", "#cb171e", "Kubernetes, Ansible, pipelines", 5),
    ("Bash", "#89e051", "glue for everything", 5),
    ("Groovy", "#4298b8", "Jenkinsfiles & shared libraries", 4),
    ("Go", "#00ADD8", "CLIs & Kubernetes tooling", 3),
    ("Java", "#b07219", "where it all started", 4),
    ("SQL", "#e38c00", "MySQL · PostgreSQL", 3),
]
W, rh, top = 1000, 40, 66
H = top + ((len(langs) + 1) // 2) * rh + 18
colw = (W - 48) / 2
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Languages I write day to day">', BASE]
s.append(f'<rect width="{W}" height="{H}" rx="12" fill="#0d1117" stroke="#30363d"/>')
s.append(f'<text x="24" y="40" class="f" fill="#e6edf3" font-size="18" font-weight="700">What I actually write</text>')
s.append(f'<text x="226" y="40" class="f" fill="#7d8590" font-size="14">· at work, not just in public repos</text>')
for i, (name, col, desc, lvl) in enumerate(langs):
    c, r = divmod(i, (len(langs) + 1) // 2)
    x = 24 + c * colw
    y = top + r * rh
    s.append(f'<g class="in" style="animation-delay:{0.07 * i:.2f}s">')
    s.append(f'<circle cx="{x + 7}" cy="{y + 12}" r="6" fill="{col}"/>')
    s.append(f'<text x="{x + 22}" y="{y + 17}" class="f" fill="#e6edf3" font-size="15" font-weight="700">{escape(name)}</text>')
    s.append(f'<text x="{x + 96}" y="{y + 17}" class="f" fill="#8b949e" font-size="13">{escape(desc)}</text>')
    for k in range(5):
        s.append(f'<rect x="{x + colw - 90 + k * 15}" y="{y + 6}" width="11" height="11" rx="2.5" fill="{col if k < lvl else "#21262d"}"/>')
    s.append('</g>')
s.append("</svg>")
open(f"{OUT}/languages.svg", "w").write("\n".join(s))

# ---------------------------------------------------------------- LinkedIn card
W, H = 1000, 150
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Connect on LinkedIn: 12+ recommendations, 10 certifications, 7+ years">', BASE]
s.append('<defs><linearGradient id="lg" x1="0" x2="1"><stop offset="0" stop-color="#0a2540"/><stop offset="1" stop-color="#0d1117"/></linearGradient></defs>')
s.append(f'<rect width="{W}" height="{H}" rx="12" fill="url(#lg)" stroke="#1f6feb" stroke-opacity=".5"/>')
s.append(f'<text x="28" y="48" class="f" fill="#e6edf3" font-size="22" font-weight="800">Vamsi Avinash Gunji</text>')
s.append(f'<text x="28" y="74" class="f" fill="#9fb3c8" font-size="14">Senior DevOps Engineer · SRE · AWS · Azure · GCP · OpenShift · Terraform</text>')
stats = [("12+", "recommendations"), ("10", "certifications"), ("7+ yrs", "in production"), ("7", "companies")]
for i, (n, l) in enumerate(stats):
    x = 28 + i * 150
    s.append(f'<g class="in" style="animation-delay:{0.1 * i:.1f}s"><text x="{x}" y="116" class="f" fill="#58a6ff" font-size="24" font-weight="800">{n}</text>'
             f'<text x="{x}" y="134" class="f" fill="#8b949e" font-size="12">{l}</text></g>')
bx, bw = W - 230, 200
s.append(f'<rect x="{bx}" y="{H/2 - 22}" width="{bw}" height="44" rx="22" fill="#0a66c2"/>')
s.append(f'<text x="{bx + bw/2}" y="{H/2 + 5}" text-anchor="middle" class="f" fill="#fff" font-size="15" font-weight="700">Connect on LinkedIn →</text>')
s.append("</svg>")
open(f"{OUT}/linkedin.svg", "w").write("\n".join(s))
print("ok")
