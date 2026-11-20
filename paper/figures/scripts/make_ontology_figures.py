#!/usr/bin/env python3
"""Figures of the coverage of the requirements by ontology terms (static version of the charts of the specification dashboard).

  python make_ontology_figures.py   # reads tables/ontology_terms_snapshot.csv, writes ontology_terms_per_ontology.{svg,png} and ontology_coverage.{svg,png}

tables/ontology_terms_snapshot.csv is a copy of the columns row_id, req_id, use_case, role, curie, label, ontology, coverage and decision of
specification/ontology_terms.csv of the community repository (main branch, term table of 3 November 2026).

Figure 1: distinct terms per ontology, split by use case (a term used by several use cases counts once in each, as in the dashboard).
Figure 2: A) requirements by use case and status (covered = a primary term with exact coverage; partial = a primary term with partial coverage
or a stand-in; gap = neither), B) term rows by ontology and fit (exact, partial, no fit = local term of lodp:).
Rejected rows are not counted for the status of a requirement, as in the dashboard.
"""
import csv
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).parent
TABLES, OUT = HERE.parent / "tables", HERE.parent
INK, MUTED, SURFACE, BAND = "#1f2933", "#52606d", "#ffffff", "#eef2f6"
rows = list(csv.DictReader(open(TABLES / "ontology_terms_snapshot.csv", encoding="utf-8")))
UC = OrderedDict([("plantcyc", "PMN"), ("bgc", "BGC"), ("metabolomics", "MET"), ("paired_omics", "PO"), ("unsupervised", "UN"), ("transcriptomics", "TX"), ("common", "COM")])
UCCOL = {"PMN": "#0072B2", "BGC": "#E69F00", "MET": "#009E73", "PO": "#CC79A7", "UN": "#56B4E9", "TX": "#D55E00", "COM": "#8c96a0"}
STCOL = {"covered": "#0072B2", "partial": "#E69F00", "gap": "#D55E00"}
FITCOL = {"exact": "#0072B2", "partial": "#E69F00", "none": "#D55E00"}
LIGHT = {"#E69F00", "#56B4E9"}
tc = lambda c: INK if c in LIGHT else "white"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})

# ---- Figure 1: distinct terms per ontology, split by use case
per = defaultdict(lambda: defaultdict(set))
for r in rows:
    if r["curie"]: per[r["ontology"]][UC[r["use_case"]]].add(r["curie"])
tot = {o: len(set().union(*u.values())) for o, u in per.items()}
order = sorted(tot, key=lambda o: (-tot[o], o))
TOP = 12
top, rest = order[:TOP], order[TOP:]
fig, ax = plt.subplots(figsize=(8.2, 5.4))
labels = top + ["other"]
for yi, o in enumerate(labels):
    left = 0
    if o == "other":
        merged = defaultdict(set)
        for q in rest:
            for a, s in per[q].items(): merged[a] |= s
        data, total = merged, len({c for s in merged.values() for c in s})
        name = f"{len(rest)} other ontologies"
    else:
        data, total, name = per[o], tot[o], ("lodp (local)" if o == "lodp" else o)
    for a in UC.values():
        v = len(data.get(a, ()))
        if v:
            ax.barh(yi, v, left=left, color=UCCOL[a], edgecolor=SURFACE, linewidth=1, height=0.68)
            if v >= 4: ax.text(left + v / 2, yi, str(v), ha="center", va="center", fontsize=8.5, color=tc(UCCOL[a]))
            left += v
    ax.text(left + 0.8, yi, f"{total} distinct", va="center", fontsize=9, color=INK)
    labels[yi] = name
ax.set_yticks(range(len(labels))); ax.set_yticklabels(labels); ax.invert_yaxis()
ax.set_xlabel("Terms (counted per use case)"); ax.set_xlim(0, max(tot.values()) * 1.55)
ax.set_title("Terms of the specification per ontology, split by use case", loc="left", fontsize=11, fontweight="bold")
handles = [plt.Rectangle((0, 0), 1, 1, color=UCCOL[a]) for a in UC.values()]
ax.legend(handles, list(UC.values()), ncol=7, frameon=False, loc="upper center", bbox_to_anchor=(0.45, -0.13), fontsize=9, title="Use case", title_fontsize=9)
fig.tight_layout()
for ext in ("svg", "png"): fig.savefig(OUT / f"ontology_terms_per_ontology.{ext}", dpi=200, facecolor=SURFACE)
plt.close(fig)

# ---- Figure 2: coverage
req = OrderedDict()
for r in rows:
    d = req.setdefault(r["req_id"], {"uc": UC[r["use_case"]], "rows": []}); d["rows"].append(r)
status = Counter()
for q, d in req.items():
    live = [r for r in d["rows"] if r["decision"] != "rejected"]
    if any(r["role"] == "primary" and r["coverage"] == "exact" for r in live): s = "covered"
    elif any(r["role"] in ("primary", "stand_in") for r in live): s = "partial"
    else: s = "gap"
    status[(d["uc"], s)] += 1
fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.9), gridspec_kw={"width_ratios": [1, 1.15]})
ax = axs[0]
ucs = list(UC.values()); ucs.sort(key=lambda a: -sum(status[(a, s)] for s in STCOL))
for yi, a in enumerate(ucs):
    left = 0
    for s in ("covered", "partial", "gap"):
        v = status[(a, s)]
        if v:
            ax.barh(yi, v, left=left, color=STCOL[s], edgecolor=SURFACE, linewidth=1, height=0.68)
            ax.text(left + v / 2, yi, str(v), ha="center", va="center", fontsize=9, color=tc(STCOL[s]), fontweight="bold")
            left += v
    ax.text(left + 0.6, yi, str(left), va="center", fontsize=9, color=INK)
ax.set_yticks(range(len(ucs))); ax.set_yticklabels(ucs); ax.invert_yaxis(); ax.set_xlabel("Requirements"); ax.set_xlim(0, 36)
ax.set_title("A. Requirements by use case", loc="left", fontsize=11, fontweight="bold")
ax.legend([plt.Rectangle((0, 0), 1, 1, color=STCOL[s]) for s in STCOL], ["covered", "partial", "gap"], frameon=False, loc="lower right", fontsize=9)
ax = axs[1]
fit = defaultdict(Counter)
for r in rows:
    if r["curie"]: fit[r["ontology"]][r["coverage"]] += 1
ords = sorted(fit, key=lambda o: (-sum(fit[o].values()), o))
shown, others = ords[:10], ords[10:]
names = [("lodp (local)" if o == "lodp" else o) for o in shown] + [f"{len(others)} other ontologies"]
cnts = [fit[o] for o in shown]
oc = Counter()
for o in others: oc.update(fit[o])
cnts.append(oc)
for yi, c in enumerate(cnts):
    left = 0
    for k in ("exact", "partial", "none"):
        v = c.get(k, 0)
        if v:
            ax.barh(yi, v, left=left, color=FITCOL[k], edgecolor=SURFACE, linewidth=1, height=0.68)
            if v >= 4: ax.text(left + v / 2, yi, str(v), ha="center", va="center", fontsize=9, color=tc(FITCOL[k]), fontweight="bold")
            left += v
    ax.text(left + 0.8, yi, str(left), va="center", fontsize=9, color=INK)
ax.set_yticks(range(len(names))); ax.set_yticklabels(names); ax.invert_yaxis(); ax.set_xlabel("Rows of the term table (candidate terms)"); ax.set_xlim(0, max(sum(c.values()) for c in cnts) * 1.15)
ax.set_title("B. Candidate terms by ontology and fit", loc="left", fontsize=11, fontweight="bold")
ax.legend([plt.Rectangle((0, 0), 1, 1, color=FITCOL[k]) for k in FITCOL], ["exact fit", "partial fit", "no fit (local term)"], frameon=False, loc="lower right", fontsize=9)
fig.tight_layout()
for ext in ("svg", "png"): fig.savefig(OUT / f"ontology_coverage.{ext}", dpi=200, facecolor=SURFACE)
print("requirements:", len(req), dict(Counter(s for (_, s) in [(k[0], k[1]) for k in status.elements()])))
print("per ontology distinct:", {o: tot[o] for o in order})
print("fit:", {o: dict(fit[o]) for o in ords[:11]})
