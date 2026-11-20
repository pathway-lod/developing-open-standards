"""Draw the evidence-to-score schema (figureScoring) for the gene example.
Run: python make_scoring_figure.py   (needs matplotlib); writes ../scoring_schema.png/.svg"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

out = os.path.join(os.path.dirname(__file__), "..")
fig, ax = plt.subplots(figsize=(11, 5.2))
ax.set_xlim(0, 120); ax.set_ylim(0, 56); ax.axis("off")

def box(x, y, w, h, text, fc, ec="#444", fs=8.5, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3,rounding_size=1.2",
                                fc=fc, ec=ec, lw=1))
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=fs,
            fontweight="bold" if bold else "normal")

def arrow(x1, y1, x2, y2, label=None, ls="-"):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color="#555", lw=1, linestyle=ls))
    if label:
        ax.text((x1+x2)/2, (y1+y2)/2 + 1.2, label, ha="center", fontsize=8, color="#222")

for x, t in [(1, "1  Evidence tiers\n(one query each, incl. federated services)"),
             (48, "2  Families\n(non-independent tiers)"),
             (70, "3  Noisy-OR"), (94, "4  Ranked list")]:
    ax.text(x, 55, t, fontsize=9, fontweight="bold", va="top")

tiers = [("gene in a PlantMetWiki pathway", "0.90", 40),
         ("gene + BGC partner in pathway", "0.70", 33),
         ("two genes in the same BGC", "0.30", 26),
         ("co-expressed with a pathway gene", "0.50", 17),
         ("ortholog of a pathway gene", "0.50", 8)]
for name, w, y in tiers:
    box(1, y, 42, 5, f"{name}  (w = {w})", "#e8f0fb")
fam = [("membership\nstrongest tier only", 29, 14, "#fdf1d6", "0.90"),
       ("omics", 15.5, 7, "#fdf1d6", "0.50"),
       ("sequence", 6.5, 7, "#fdf1d6", "0.50")]
box(48, 29, 16, 14, "membership\nstrongest tier\nonly", "#fdf1d6")
box(48, 15.5, 16, 7, "omics", "#fdf1d6")
box(48, 6.5, 16, 7, "sequence", "#fdf1d6")
for y in (42.5, 35.5, 28.5): arrow(43.3, y, 47.7, 36 if y > 25 else 36)
arrow(43.3, 19.5, 47.7, 19)
arrow(43.3, 10.5, 47.7, 10)

ax.add_patch(Circle((76, 24.5), 7.5, fc="#e5f3e5", ec="#444", lw=1))
ax.text(76, 24.5, "1 − ∏(1 − w)", ha="center", va="center", fontsize=9, fontweight="bold")
arrow(64.3, 36, 69.5, 28.5, "0.90")
arrow(64.3, 19, 68.6, 22, "0.50")
arrow(64.3, 10, 69.5, 19.5, "0.50")
box(88, 17, 29, 15, "score\n1 − 0.10 × 0.50 × 0.50\n= 0.975\n\n+ tiers passed,\nas metadata", "#fbe9e7", fs=8.5)
arrow(83.6, 24.5, 87.7, 24.5)
ax.text(55, 1, "Weights are drafts. Only the strongest tier of a family counts; "
        "a further independent family can only raise the score.",
        ha="center", fontsize=8, style="italic", color="#444")
fig.savefig(os.path.join(out, "scoring_schema.png"), dpi=200, bbox_inches="tight")
fig.savefig(os.path.join(out, "scoring_schema.svg"), bbox_inches="tight")
