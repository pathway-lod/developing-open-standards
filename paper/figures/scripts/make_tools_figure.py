#!/usr/bin/env python3
"""Bubble plot of the bioinformatics tools named in the partner questionnaire.

  python make_tools_figure.py     # reads tables/survey_tools.csv, writes survey_tools.{svg,png}

One row per tool, grouped by what it is used for. A bubble in a respondent column means that respondent named the tool;
the last column sums the respondents (bubble area and number). The groups are ours, the answers are the respondents'.
Spelling was normalised (planitSMASH -> plantiSMASH, DEseq -> DESeq, Uniprot -> UniProt, MEMEsuite and MEME -> MEME suite,
"Kallisto-Sleuth / mixOmics" split in two). The tools were split on ";" in survey_tools.csv, so commas inside brackets stay.
"""
import csv
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).parent
TABLES, OUT = HERE.parent / "tables", HERE.parent      # tables/ holds the answers, the figures go next to scripts/
INK, MUTED, BUBBLE, BAND, SURFACE = "#1f2933", "#52606d", "#1d4e6b", "#eef2f6", "#ffffff"

GROUPS = [
    ("Metabolomics", ["SIRIUS", "MZmine", "GNPS"]),
    ("Orthology", ["OrthoFinder", "SonicParanoid"]),
    ("Gene clusters", ["plantiSMASH"]),
    ("Paired omics", ["MEANtools", "mixOmics", "Own paired-omics tool"]),
    ("Expression and statistics", ["DESeq", "Kallisto-Sleuth", "Genie3", "Pearson correlation", "z-score", "Self-organizing maps"]),
    ("Annotation, motifs, visualisation", ["Cytoscape", "ShinyGO", "GoMapMan", "UniProt", "MEME suite"]),
    ("Not classified", ["SKM"]),
]
RENAME = {"planitSMASH": "plantiSMASH", "Making our own tool for paired omics": "Own paired-omics tool",
          "self organizing maps": "Self-organizing maps", "Uniprot": "UniProt", "MEMEsuite": "MEME suite", "MEME": "MEME suite"}

def parse(cell):
    out = []
    for part in cell.split(";"):
        name = part.split("(")[0].strip()
        out += [x.strip() for x in name.split(" / ")]
    return [RENAME.get(n, n) for n in out if n]

rows = list(csv.DictReader(open(TABLES / "survey_tools.csv", newline="")))
used = {r["respondent"]: set(parse(r["tools"])) for r in rows}
resp = sorted(used)
total = Counter(t for s in used.values() for t in s)
known = {t for _, ts in GROUPS for t in ts}
assert set(total) <= known, set(total) - known

order = [(g, t) for g, ts in GROUPS for t in sorted(ts, key=lambda t: (-total[t], t))]
fig, ax = plt.subplots(figsize=(8.2, 0.34 * len(order) + 1.6))
y = {}
yy, last = 0, None
for g, t in order:
    if g != last and last is not None: yy += 0.6
    y[t] = yy; yy += 1; last = g
# alternating group bands and group labels
for i, (g, ts) in enumerate(GROUPS):
    y0, y1 = y[ts[0] if False else min(ts, key=lambda t: y[t])], y[max(ts, key=lambda t: y[t])]
    if i % 2 == 0: ax.axhspan(y0 - 0.5, y1 + 0.5, color=BAND, zorder=0)
    ax.text(-8.3, (y0 + y1) / 2, g.replace(" and ", " and\n").replace("motifs, ", "motifs,\n").replace("Gene clusters", "Gene\nclusters"), ha="left", va="center", fontsize=9.5, color=MUTED, fontweight="bold")
xs = {r: i for i, r in enumerate(resp)}; XT = len(resp) + 0.6
for t, yv in y.items():
    ax.text(-0.45, yv, t, ha="right", va="center", fontsize=10, color=INK)
    for r in resp:
        if t in used[r]: ax.scatter(xs[r], yv, s=110, color=BUBBLE, edgecolor=SURFACE, linewidth=1.5, zorder=3)
    ax.scatter(XT, yv, s=110 * total[t], color=BUBBLE, alpha=0.45, edgecolor=BUBBLE, linewidth=1, zorder=3)
    ax.text(XT + 0.55, yv, str(total[t]), ha="left", va="center", fontsize=10, color=INK)
for r in resp: ax.text(xs[r], -1.2, r, ha="center", fontsize=9.5, color=MUTED)
ax.text(XT, -1.2, "Respondents\n(total)", ha="center", va="center", fontsize=9.5, color=MUTED, fontweight="bold")
ax.set_xlim(-8.4, XT + 1.2); ax.set_ylim(yy + 0.2, -2.2); ax.axis("off")
fig.patch.set_facecolor(SURFACE)
for ext in ("svg", "png"):
    fig.savefig(OUT / f"survey_tools.{ext}", dpi=200, bbox_inches="tight", facecolor=SURFACE)
print(len(resp), "respondents,", len(total), "tools"); print(total.most_common())
