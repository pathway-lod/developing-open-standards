#!/usr/bin/env python3
"""Participants of the BioHackathon project: expertise (rows) of each participant (columns) and the working group(s) they joined.

  python make_participants_figure.py     # reads tables/participants*.csv and tables/working_groups.csv, writes participants_expertise.{svg,png}

A dot means that the participant listed the expertise in the planning document. The letters above the names mark the working groups
(T terms, P pilots, R results) the participant joined. Expertise is self-declared; participants who are not in a working group were project coordinators or advisers.
"""
import csv
from collections import Counter, defaultdict
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).parent
TABLES, OUT = HERE.parent / "tables", HERE.parent
INK, MUTED, DOT, BAND, SURFACE = "#1f2933", "#52606d", "#1d4e6b", "#eef2f6", "#ffffff"

people = list(csv.DictReader(open(TABLES / "participants.csv", encoding="utf-8")))
exp = defaultdict(set)
for r in csv.DictReader(open(TABLES / "participants_expertise.csv", encoding="utf-8")): exp[r["expertise"]].add(r["participant"])
grp = defaultdict(set)
for r in csv.DictReader(open(TABLES / "working_groups.csv", encoding="utf-8")): grp[r["participant"].replace(" (partly)", "")].add(r["group"])
LETTER = {"Terms": "T", "Pilots": "P", "Results": "R"}

THEMES = [("Semantic technologies", ["RDF", "SPARQL", "Ontologies", "Shape constraints (SHACL/ShEx)", "Evidence and provenance modelling"]),
          ("Plant omics and chemistry", ["Multi-omics", "Transcriptomics", "Metabolomics", "MS annotations", "Plant specialized metabolism", "Chemical identifiers and structures", "Statistics"]),
          ("Engineering and community", ["Web development", "GitHub Actions and CI/CD", "FAIR data and research data management", "Governance and community curation"])]
# columns: by working group (Terms, Pilots, Results, none), then alphabetical
def key(p):
    g = grp.get(p["participant"], set()); return (min([list(LETTER).index(x) for x in g]) if g else 9, p["participant"])
people.sort(key=key)
cols = {p["participant"]: i for i, p in enumerate(people)}
rows, y, theme_y = [], 1.3, []
for t, es in THEMES:
    theme_y.append((t, y, y + len(es) - 1))
    for e in sorted(es, key=lambda e: (-len(exp[e]), e)): rows.append((e, y)); y += 1
    y += 1.5
fig, ax = plt.subplots(figsize=(11, 7.6))
for t, y0, y1 in theme_y:
    if theme_y.index((t, y0, y1)) % 2 == 0: ax.axhspan(y0 - 0.5, y1 + 0.5, color=BAND, zorder=0)
for e, yv in rows:
    ax.text(-0.8, yv, e, ha="right", va="center", fontsize=10, color=INK)
    for n in exp[e]: ax.scatter(cols[n], yv, s=150, color=DOT, edgecolor=SURFACE, linewidth=1.5, zorder=3)
    ax.text(len(people) - 0.2, yv, str(len(exp[e])), ha="left", va="center", fontsize=10, color=INK)
for t, y0, y1 in theme_y:
    ax.text(-8.6, y0 - 0.95, t, ha="left", va="center", fontsize=9.5, color=MUTED, fontweight="bold")
for p in people:
    n, i = p["participant"], cols[p["participant"]]
    ax.text(i, -1.6, n, rotation=55, ha="left", va="bottom", fontsize=9.5, color=MUTED if "remote" in p["attendance"] else INK, style="italic" if "remote" in p["attendance"] else "normal", rotation_mode="anchor")
    letters = " ".join(LETTER[g] for g in LETTER if g in grp.get(n, set()))
    ax.text(i, -0.95, letters or "–", ha="center", va="center", fontsize=9.5, color=MUTED, fontweight="bold")
ax.text(-0.8, -0.95, "Working group", ha="right", va="center", fontsize=9.5, color=MUTED, fontweight="bold")
ax.text(len(people) - 0.2, -0.95, "People", ha="left", va="center", fontsize=9.5, color=MUTED, fontweight="bold")
ax.text(-8.6, rows[-1][1] + 2.2, "T = terms, P = pilots, R = results (visualisation, ranking and scoring). Italic grey names: remote participants.",
        ha="left", fontsize=8.5, color=MUTED)
ax.set_xlim(-8.7, len(people) + 0.6); ax.set_ylim(rows[-1][1] + 3.2, -4.8); ax.axis("off")
fig.patch.set_facecolor(SURFACE)
for ext in ("svg", "png"): fig.savefig(OUT / f"participants_expertise.{ext}", dpi=200, bbox_inches="tight", facecolor=SURFACE)
c = Counter(g for p in people for g in grp.get(p["participant"], set()))
print(len(people), "participants;", dict(c)); print({e: len(exp[e]) for e, _ in rows})
