#!/usr/bin/env python3
"""NPClassifier coverage of the PlantMetWiki metabolites, restyled (same data as the plot of the notebook explore_npcs.ipynb).

  python make_npclassifier_figure.py   # writes npclassifier_coverage_styled.{svg,png}

Counts are the outputs of the notebook pilots/metabolomics_overlap/explore_npcs.ipynb (branch NPC_naming_metabolite of the community repository,
Liese van Ommeren, 20 November 2026): 2,974 PlantMetWiki metabolites with an InChIKey; 2,889 got a SMILES; 2,324, 2,178 and 1,953 got an
NPClassifier pathway, superclass and class.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).parent.parent
N = 2974
rows = [("InChIKey converted to SMILES", 2889, "#8c96a0"), ("NPClassifier pathway", 2324, "#1d4e6b"), ("NPClassifier superclass", 2178, "#1d4e6b"), ("NPClassifier class", 1953, "#1d4e6b")]
fig, ax = plt.subplots(figsize=(7.6, 3.2))
for i, (lab, v, col) in enumerate(rows):
    ax.barh(i, 100 * v / N, color=col, height=0.62)
    ax.text(100 * v / N + 1.2, i, f"{100 * v / N:.1f} %  ({v:,} of {N:,})", va="center", fontsize=9.5, color="#1f2933")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows]); ax.invert_yaxis()
ax.set_xlim(0, 145); ax.set_xticks([0, 20, 40, 60, 80, 100]); ax.set_xlabel("Share of the PlantMetWiki metabolites with an InChIKey (%)")
ax.spines[["top", "right"]].set_visible(False)
ax.set_title("Coverage of the NPClassifier levels in PlantMetWiki", loc="left", fontsize=11, fontweight="bold")
fig.tight_layout()
for ext in ("svg", "png"): fig.savefig(OUT / f"npclassifier_coverage_styled.{ext}", dpi=200, facecolor="white")
