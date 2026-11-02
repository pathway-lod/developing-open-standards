#!/usr/bin/env python3
"""Version 2 of the questionnaire figure (v1 is kept: make_survey_figure.py): adds a panel with the themes of the questions
that respondents want to ask PlantMetWiki (survey_questions.csv). The panel is NOT linked to the ribbons: the answers are anonymous and
not matched to the respondents of the two other questions, and the themes are our grouping (a question can have two).

Flow figure of the partner questionnaire: what respondents use (entry point) -> what they want to find (goal).

  python make_survey_figure.py     # writes survey_entry_exit_v2.{svg,png}

Both questions were multiple choice. A ribbon between a data type and a goal is as wide as the number of respondents who ticked
both, so one respondent contributes to several ribbons. The height of a box is the sum of its ribbons; the label gives the
number of respondents who ticked the item.
"""
import csv
from collections import Counter
from itertools import product
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch, Rectangle
from matplotlib.path import Path as MPath

HERE = Path(__file__).parent
TABLES, OUT = HERE.parent / "tables", HERE.parent      # tables/ holds the answers, the figures go next to scripts/
INK, MUTED, RIBBON, BAR, SURFACE = "#1f2933", "#52606d", "#3b82a6", "#1d4e6b", "#ffffff"

rows = list(csv.DictReader(open(TABLES / "survey_responses.csv", newline="")))
split = lambda s: [x.strip() for x in s.split(";") if x.strip()]
resp = [(split(r["uses"]), split(r["goals"])) for r in rows]
uses_n = Counter(u for us, _ in resp for u in us)
goals_n = Counter(g for _, gs in resp for g in gs)
links = Counter((u, g) for us, gs in resp for u, g in product(us, gs))

short = {"Comparative pathway analysis across species": "Comparative pathway analysis\nacross species",
         "Orthology/homology (e.g. for gene/enzyme searches)": "Orthology / homology",
         "Metabolite annotations / Metabolomics": "Metabolomics",
         "BGCs (plant biosynthetic gene clusters)": "Biosynthetic gene clusters",
         "Finding regulatory relationships between genes and metabolites": "Regulatory relationships\ngenes - metabolites",
         "Connecting plant resilience to plant metabolism (and gene expression)": "Plant resilience\nand metabolism",
         "Finding/annotating metabolites": "Finding / annotating\nmetabolites",
         "Finding (candidate) genes": "Finding candidate genes",
         "transcriptional regulation": "Transcriptional regulation"}
lab = lambda s: short.get(s, s)

uses = sorted(uses_n, key=lambda k: (-uses_n[k], k))
goals = sorted(goals_n, key=lambda k: (-goals_n[k], k))
GAP = 1.2
def layout(order, side):
    y, pos = 0.0, {}
    for k in order:
        h = sum(w for (u, g), w in links.items() if (u if side == "L" else g) == k)
        pos[k] = (y, h); y += h + GAP
    return pos, y - GAP
L, hl = layout(uses, "L"); R, hr = layout(goals, "R")
H = max(hl, hr)
off = lambda pos, k: (H - (hl if pos is L else hr)) / 2
XL, XR, BW = 0.0, 10.0, 0.22

fig, ax = plt.subplots(figsize=(14.5, 7.2))
cl, cr = {k: L[k][0] + off(L, k) for k in L}, {k: R[k][0] + off(R, k) for k in R}
for u in uses:
    for g in goals:
        w = links.get((u, g), 0)
        if not w: continue
        y0, y1 = cl[u], cr[g]; cl[u] += w; cr[g] += w
        xa, xb, xm = XL + BW, XR, (XL + XR + BW) / 2
        verts = [(xa, y0), (xm, y0), (xm, y1), (xb, y1), (xb, y1 + w), (xm, y1 + w), (xm, y0 + w), (xa, y0 + w), (xa, y0)]
        codes = [MPath.MOVETO, MPath.CURVE4, MPath.CURVE4, MPath.CURVE4, MPath.LINETO, MPath.CURVE4, MPath.CURVE4, MPath.CURVE4, MPath.CLOSEPOLY]
        ax.add_patch(PathPatch(MPath(verts, codes), fc=RIBBON, ec=SURFACE, lw=0.8, alpha=0.42))
for k, (y, h) in L.items():
    y += off(L, k); ax.add_patch(Rectangle((XL, y), BW, h, fc=BAR, ec="none"))
    ax.text(XL - 0.15, y + h / 2, f"{lab(k)}  ({uses_n[k]})", ha="right", va="center", fontsize=10, color=INK)
for k, (y, h) in R.items():
    y += off(R, k); ax.add_patch(Rectangle((XR, y), BW, h, fc=BAR, ec="none"))
    ax.text(XR + BW + 0.15, y + h / 2, f"{lab(k)}  ({goals_n[k]})", ha="left", va="center", fontsize=10, color=INK)
ax.text(XL + BW, -1.7, "Entry point: what respondents use", ha="right", fontsize=11.5, fontweight="bold", color=INK)
ax.text(XR, -1.7, "Goal: what they want to find", ha="left", fontsize=11.5, fontweight="bold", color=INK)
ax.text((XL + XR) / 2 - 1, H + 4.0, f"n = {len(resp)} respondents. Ribbon width = respondents who ticked both; (n) = respondents who ticked the item.",
        ha="center", fontsize=9, color=MUTED)

THEMES = [("genes_enzymes", "Genes or enzymes for a\npathway or reaction step"), ("species_orthologs", "Comparing species,\northologs"),
          ("compounds", "Questions about compounds\n(novel products, bioactivity,\nstructures)"), ("routes", "Routes to a compound"),
          ("trait_regulation", "Genes linked to a trait,\nstress or regulator"), ("genomic_context", "Genomic context\n(physical clustering)")]
qs = list(csv.DictReader(open(TABLES / "survey_questions.csv", newline="")))
tn = Counter(t for q in qs for t in q["theme"].split(";"))
nans, nq = len({q["answer"] for q in qs}), len(qs)
XP, SC, PB = XR + 8.6, 1.0, "#8a5a00"
ax.text(XP, -1.7, "Questions to ask PlantMetWiki", ha="left", fontsize=11.5, fontweight="bold", color=INK)
ax.text(XP, 0.6, f"{nq} questions in {nans} answers, not linked to the ribbons", ha="left", fontsize=8.5, color=MUTED)
step = (H - 6.0) / (len(THEMES) - 1)
for i, (key, label) in enumerate(sorted(THEMES, key=lambda t: -tn[t[0]])):
    yc = 4.2 + i * step
    ax.text(XP, yc, label, ha="left", va="center", fontsize=9.5, color=INK)
    ax.add_patch(Rectangle((XP + 6.2, yc - 1.5), tn[key] * SC, 3.0, fc=PB, ec="none"))
    ax.text(XP + 6.2 + tn[key] * SC + 0.15, yc, str(tn[key]), ha="left", va="center", fontsize=10, color=INK)
ax.text(XP, H + 4.0, "Themes are our grouping; a question can fall under two (counts add up to more than 14).", ha="left", fontsize=8.5, color=MUTED)
ax.set_xlim(-3.6, XR + 21); ax.set_ylim(-2.6, H + 5.0); ax.invert_yaxis(); ax.axis("off")
fig.patch.set_facecolor(SURFACE)
for ext in ("svg", "png"):
    fig.savefig(OUT / f"survey_entry_exit_v2.{ext}", dpi=200, bbox_inches="tight", facecolor=SURFACE)
print(len(resp), "respondents;", len(uses), "inputs;", len(goals), "goals")
for k in uses: print(" use ", uses_n[k], k)
for k in goals: print(" goal", goals_n[k], k)
