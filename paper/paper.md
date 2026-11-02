---
title: 'BioHackEU26 report: Developing Open Standards for a Semantic Framework in Plant Specialized Metabolism'
title_short: 'BioHackEU26 #3: short title'
tags:
  - plant specialized metabolism 
  - knowledge graphs
  - pathways 
  - linked open data 
  - multi omics 
authors:
  - name: Elena Del Pup
    orcid: 0000-0002-9472-918X
    affiliation: 1
  - name: Denise Slenter
    orcid: 0000-0001-8449-1318
    affiliation: 2
  - name: Kumar Saurabh Singh
    orcid: 0000-0001-8352-5897
    affiliation: 2
affiliations:
  - name: Wageningen University & Research, Wageningen, NL
    ror: 04qw24q55
    index: 1
  - name: Maastricht University, Maastricht, NL
    ror: 02jz4aj89
    index: 2
date: 8 November 2026
cito-bibliography: paper.bib
event: BH26EU
biohackathon_name: "BioHackathon Europe 2026"
biohackathon_url:   "https://biohackathon-europe.org/"
biohackathon_location: "Barcelona, Spain, 2026"
group: Project 3
# URL to project git repo --- should contain the actual paper.md:
git_url: https://github.com/pathway-lod/developing-open-standards
# This is the short authors description that is used at the
# bottom of the generated paper (typically the first two authors):
authors_short: Elena Del Pup \emph{et al.}
---


# Introduction

Plant specialized metabolites are a major source of innovative pharmaceuticals, novel foods, and biobased natural products. However, resolving the metabolic pathways that biosynthesize these compounds remains a key scientific challenge, as plant biosynthetic genes are often genomically dispersed and duplicated, resulting in highly branched, diversified, and promiscuous underlying metabolic networks. Additionally, knowledge of plant metabolic pathways remains scattered across disconnected resources, with limited interoperable annotations, and valuable experimental multi-omics datasets remain siloed and underused. To address these gaps, we developed the Linked Open Data knowledge graph PlantMetWiki (<https://plantmetwiki.bioinformatics.nl/>) [@citesAsDataSource:DelPup2026PlantMetWiki], the first semantically enriched knowledge base for querying experimentally validated pathway information for plant biosynthetic reactions, including predictions of biosynthetic gene clusters. Still, researchers lack an open, standardized, and reusable AI-ready format for integrating new datasets with community knowledge in the form of a Minimum Information Standard (MIS). Additionally, there is no framework to apply such a MIS to systematically link computational evidence from bioinformatics tools and paired plant transcriptomics-metabolomics datasets to predict or validate pathway-level knowledge.

## Background

Plant specialized metabolites are a major source of pharmaceuticals, food ingredients, crop protection compounds, and bio-based products [@citesAsAuthority:Huang2023]. Discovery of plant natural products depends on resolving the enzymatic routes that produce them, yet the biosynthesis of the majority remains uncharacterized [@citesAsAuthority:Owen2026]. The obstacle is that plant pathways resist reconstruction from any single data modality: extensive genome duplication distributes pathway genes across large, paralog-rich families that are only partially clustered, the enzymes they encode are catalytically promiscuous, and the resulting networks are highly branched and biosynthesis enzymes are shared with primary metabolism [@citesAsAuthority:Ji2024].

Metabolomics, transcriptomics, and genome sequencing are now generating promising data that can be integrated with dedicated multi-omics analysis pipelines to address this gap [@citesAsAuthority:Wolters2024]. However, this evidence accumulates in domain-specific resources and individual publications that each capture one complementary facet of metabolism, such as enzymatic reactions, metabolite structures, or genomic context [@citesAsAuthority:Singh2022], and that are often curated to different standards and incompatible identifiers. Pathway resources such as the Plant Metabolic Network [@citesAsAuthority:Hawkins2025] are by design restricted to experimentally validated knowledge, and provide no mechanism for recording computational predictions, the evidence supporting them, or their confidence. Predictions are therefore published as static supplementary tables rather than as traceable assertions that can be compared across tools and revised with novel experimental evidence.

To make curated pathway knowledge reusable and machine-actionable, I developed PlantMetWiki [@citesAsDataSource:DelPup2026PlantMetWiki], a semantically enriched and queryable knowledge graph dedicated to plant biosynthetic pathways, integrating experimentally validated pathway information across hundreds of plant taxa with existing ontologies, harmonized chemical annotations, and crosslinks to biosynthetic gene clusters predicted by plantiSMASH [@citesAsDataSource:DelPup2026plantiSMASH]. PlantMetWiki provides a foundation for FAIR data representation and reuse, but there is no open, standardized format for adding new experimental datasets to this curated pool, and no framework for linking computational evidence from bioinformatics tools and from paired transcriptomics-metabolomics experiments. Extending curated knowledge with traceable predictions requires a shared representation of entities, relations, evidence types, provenance, and confidence, and an evaluative framework that the field currently lacks.

During the proposed scientific exchange, I will address this through collaboration with researchers involved in the MetaboLinkAI project at ETH Zurich, which develops FAIR and AI-ready metabolomics workflows based on knowledge graphs, federated data integration, graph machine learning, and large language models. The project will provide me with direct access to state-of-the-art developments in semantic interoperability standards, AI-assisted discovery methods, and metabolomics knowledge representation, and to (part of) the multi-omics communities whose involvement any adopted standard requires.

The work will deliver a community-supported validation schema for aligning and integrating multi-omics datasets, and an evidence-based scoring method for predictions from multi-omics pipelines, interoperable with existing standards. Together, these render plant pathway knowledge FAIR and AI-ready, representing curated pathways, omics evidence, and scored predictions in a single machine-actionable graph. In the future, our proposed workflow will be capable of supporting scalable community annotation, enabling AI-assisted discovery of plant specialized metabolic pathways through graph-based prioritization of candidate pathway components and the generation of experimentally testable biosynthetic hypotheses.

## Objectives

As part of the BioHackathon Europe 2026, in this project we aim to:

1. Co-develop a community-supported Minimum Information Standard (MIS) for predicted plant pathway knowledge representation;
2. Design validation schemas to integrate experimental multi-omics datasets and predictions in alignment with the MIS;
3. Establish methods to align pathway-related predictions across bioinformatics pipelines, and approaches for scoring and prioritization of these predictions based on evidence strength, provenance, and community-defined criteria.

The project expands the plant metabolism knowledge graph PlantMetWiki with predictions from (multi-)omics plant knowledge coming from the community, which requires community-supported standards with feedback from the plant science community. We build an *evidence model* that says, for any prediction or experimental result attached to a PlantMetWiki pathway, enzyme, gene or metabolite, why it is believed (a typed evidence statement), where it comes from (tool, version, input data) and how strongly it is anchored in the knowledge graph. Users can then filter the graph by the kind of support behind a statement. The terms come from existing ontologies wherever possible; what no ontology provides is collected as candidates for new terms. These outcomes will enable scalable community annotation of pathway information, improved integration of multi-omics data, prioritization of candidate pathway components, and more reproducible and transparent bioinformatics analyses.

# Implementation

All work is open and lives in the repository [pathway-lod/lod-pathways-community](https://github.com/pathway-lod/lod-pathways-community): the specification, the discussion workflow, the validation shapes, the pilots and the generated outputs.

## Questionnaire to core laboratories

To ground the requirements in how the data are used, we interviewed six core laboratories that generate paired plant omics data, with a questionnaire. It asked for the key research question or goal of each laboratory, what they use to answer it (data types and analyses), which bioinformatics tools they use, and what they would like to ask a knowledge graph such as PlantMetWiki. All four questions allowed several answers. The answers are anonymised and kept in the repository together with the scripts that draw the figures (`paper/figures/`).

All six laboratories start from transcriptomics and all six want to find candidate genes; five want to reconstruct pathways, three to find enzymes and three to find or annotate metabolites (Figure \ref{figureSurvey}). Orthology and comparative pathway analysis are the next most common starting points (five and four laboratories), and metabolomics is used by two. The tools reflect the same picture (Figure \ref{figureTools}): OrthoFinder is named by five laboratories, SIRIUS, MZmine, DESeq and plantiSMASH by four each, and paired-omics tools (MEANtools, mixOmics, an in-house tool) by only two. Nine answers to the question of what to ask PlantMetWiki contained 14 questions. Most ask for genes or enzymes of a pathway or reaction step, or for comparisons of pathways and orthologs across species; others ask for routes to a compound, for genes linked to a trait or stress, for the physical clustering of genes, and for compounds (novel products, bioactivity, chlorinated products). We use these questions as test cases for the evidence model. They also show needs that the specification does not yet cover, in particular orthology, transcription factors and traits.

![Questionnaire to six core laboratories: what they use (entry point) and what they want to find (goal). Ribbon width is the number of laboratories that ticked both, the number in brackets the laboratories that ticked the item. The right panel groups the 14 questions that the laboratories want to ask PlantMetWiki into themes (our grouping; the answers are anonymous and not linked to the laboratories on the left). \label{figureSurvey}](./figures/survey_entry_exit_v2.png)

![Bioinformatics tools named by the six laboratories, grouped by use. A dot marks a laboratory that named the tool. \label{figureTools}](./figures/survey_tools.png){ width=70% }

## The evidence model

Every prediction or experimental result is modelled in the same way, so that predictions of different kinds can be queried together. A *claim* (the prediction or result) has evidence (`sio:SIO_000772`), an evidence node typed with a class of the Evidence and Conclusion Ontology (ECO) and carrying the scores of the tool; the evidence was generated by a *run* (software, version, input data) following PROV-O; and the claim is anchored in an existing PlantMetWiki node (pathway or metabolite) with an *anchor tier* that records how strongly it is tied to the knowledge graph (for example, a gene-level link is stronger than a link only through an EC number).

```mermaid
flowchart LR
  CL["claim<br/>(prediction or result)"] -- "has evidence" --> EV["evidence node<br/>typed with an ECO class,<br/>plus tool scores"]
  EV -- "prov:wasGeneratedBy" --> RUN["run<br/>software, version, input data"]
  CL -- "anchored in / to<br/>(with an anchor tier)" --> PMW["existing PlantMetWiki node<br/>pathway or metabolite"]
```

## Use cases to support

The use cases are the kinds of predictions and data that we want PlantMetWiki to be able to hold. Each has an acronym that is also the prefix of its requirement IDs in the specification (for example `PO-03` is the third requirement of the paired omics use case).

Table: Use cases supported by the framework, with the pilot dataset used to test each. Cases 5 and 6 are emphasised in our working list.

| # | Use case | Specification | Test data | Pilot |
| --- | --- | --- | --- | --- |
| 1 | New pathway from the literature | not yet a use case of its own | Ipecac alkaloid biosynthesis in two evolutionarily distant plants (Colinas et al.) | `pilots/ipecac_overlap` |
| 2 | PlantCyc (PMN) inferred enzyme function | PMN | PlantCyc evidence codes on PlantMetWiki nodes | `shape_constraints/rdf/plantcyc.ttl` |
| 3 | plantiSMASH-predicted biosynthetic gene clusters (BGCs) | BGC | plantiSMASH 2.0 precalculated database, about 30,400 BGCs in 430 genomes | `pilots/plantismash_overlap` |
| 4 | Transcriptomics | TX | covered inside the paired data of cases 1 and 6 | no separate pilot |
| 5 | **Metabolomics** | MET | Brassicaceae metabolic fingerprinting (Wolters et al. 2026) | `pilots/metabolomics_overlap` |
| 6 | **Paired omics** (transcript-metabolite associations) | PO | Tomato data of the MEANtools paper [@citesAsDataSource:Singh2025MEANtools] | `pilots/meantools_overlap` |
| 7 | "Unsupervised" graph neural network (GNN) predictions of conversion steps | UN | none yet | none |

## Working groups

The work is organised in four groups, which correspond to the sections of the Results:

1. **Terms.** Discuss and curate the proposed terms and the gaps in the specification, and identify the terms to propose to an existing ontology.
2. **Pilots.** Test the alignment of the use case datasets with PlantMetWiki.
3. **Visualization and extraction of results.** Show what the aligned data say, and rank or score predictions.
4. **Submission system (optional).** Build and test an automated way to submit, integrate and approve new predictions, with decentralised governance.

## The pipeline

The work follows six steps, each with its own folder and documentation in the repository.

Table: The six steps of the pipeline.

| Step | What happens | Where |
| --- | --- | --- |
| 1. Use cases | Choose the kinds of predictions and experimental data to align with PlantMetWiki, and what each needs to say | `specification/` |
| 2. Specification | For each use case: the requirements (what must be said), the candidate ontology terms and the gaps. One row per requirement and term in a table (`ontology_terms.csv`, the source of truth), the text in `SPECIFICATION.md`. Term IDs and labels are checked against the EBI Ontology Lookup Service (OLS) | `specification/` |
| 3. Community discussion | The table is shown as a web dashboard; discussion happens in GitHub issues; maintainers' labels turn decisions into pull requests (see below) | `.github/`, dashboard |
| 4. Shape constraints | The chosen terms become SHACL shapes that say what a statement must contain before it is added to the knowledge graph. Problems are either rejected (violations) or flagged (warnings) | `shape_constraints/` |
| 5. Pilots | Each use case is tried on a real dataset | `pilots/` |
| 6. Outputs | RDF (Turtle) validated against the shapes, a sample graph, a local placeholder vocabulary (`lodp:`) for terms that no ontology provides, and the terms to propose to larger ontologies | `shape_constraints/rdf/`, `examples/` |

## The specification dashboard: how terms are discussed and approved

The specification is shown as an interactive dashboard at <https://pathway-lod.github.io/lod-pathways-community/>. It lists every requirement with its status, decision, owner and candidate terms, with filters by use case, decision, owner, action and ontology, and charts of the number of terms per ontology and of the coverage. Anyone can take part:

1. **Find a requirement** with the search box or the filters, and select its ID to see the candidate terms.
2. **Start a discussion** with the buttons on the requirement. They open a GitHub issue form that is already filled in: *ask a question*, *suggest a term*, or *propose a new requirement*. Issues carry the label `ontology-terms` and the requirement ID in the title (for example `[PMN-03]`).
3. **Take a requirement on** by ticking the volunteering box of the form, or ask a maintainer to assign the issue.
4. **Maintainers decide with labels.** `decision:agreed`, `decision:rejected`, `decision:proposed` or `decision:open` on an issue makes a GitHub Action open a pull request that changes the `decision` of that requirement in the table. The label `accept-term` on a term suggestion adds the term as a new row (its label and IRI are looked up in OLS) and `decision:rejected` marks only that suggested term as rejected.
5. **Review and merge.** Nothing reaches the main branch without a reviewed pull request. Only people with triage or write access can set labels, so only they can trigger a change. The issue text is read as data and is checked against the lists of the specification.
6. **The dashboard is regenerated** from the table when a pull request is merged, and the checks on every pull request keep the generated files and the table in sync.

Terms that no ontology provides are rows of the same table, with the action `local_term` while a local placeholder is used and `request_term` when a term should be proposed to an existing ontology such as ECO, STATO, PSI-MS or EDAM.

# Results

## 1. Discussion and curation of proposed and gap terms

At the time of writing the specification has seven use cases and 119 requirements, described by 188 rows of candidate terms (TODO: update the numbers before submission; they are generated from `ontology_terms.csv`). Of these rows, 75 are a primary term, 37 an alternative, 18 a stand-in, 49 a local term and 9 mark a gap where no term exists. Most requirements still wait for a decision (104 rows proposed, 82 open, 2 rejected). The dashboard makes these numbers current, and is the place where co-authors and the wider community discuss and approve the terms.

**Terms to propose to an existing ontology.** Seven requirements are marked `request_term`: for these we have searched OLS and found no suitable term, and we intend to propose one to an existing ontology (for example EDAM, ECO, STATO or PSI-MS) instead of keeping a local term. An example is metabolite-transcript correlation evidence, for which `ECO:0007590` is only the closest term. TODO: list the final terms to propose, the ontology and the status of each request.

## 2. Test alignment of use case datasets (pilots)

Each pilot checks how much of a real dataset can be aligned with PlantMetWiki, and what evidence is available. TODO: add the headline numbers of the first three pilots from their READMEs.

- **Metabolomics** (`pilots/metabolomics_overlap`): LC-MS/MS annotations of 14 Brassicaceae species (Wolters et al. 2026) matched to PlantMetWiki metabolites on the first InChIKey block, with six evidence tiers from the GNPS library match to MS2Query analogues; the three annotation tools are combined in a consensus (agreement of three tools counts 1.0, two tools 0.5).
- **Paired omics** (`pilots/meantools_overlap`): gene-metabolite associations of MEANtools [@usesMethodIn:Singh2025MEANtools] functional clusters in tomato, with genes mapped to PlantMetWiki pathways in three tiers (locus, UniProt, EC) and metabolite features by exact mass (MS1 only), compared against a chance background.
- **BGC predictions** (`pilots/plantismash_overlap`): plantiSMASH 2.0 [@citesAsDataSource:DelPup2026plantiSMASH] clusters in 430 genomes linked to PlantMetWiki genes and pathways in three tiers.
- **New pathway from the literature** (`pilots/ipecac_overlap`): the paired ipecac alkaloid data (Colinas et al.). Of the 12 metabolites of the paper, 6 are in PlantMetWiki (secologanin exactly; three with a protonation difference only; two on the connectivity level only) and 6 are absent, among them all those of the acid route. The pathway of emetine biosynthesis (PWY-7135) has 8 conversions, of which 5 are linked to a UniProt enzyme, one only to a PlantCyc monomer, and two to no enzyme. The cloned *Carapichea* genes are 94-98% identical to enzymes already in this pathway, the *Alangium* genes at most 46%. The heterologous expression and infiltration experiments give reaction evidence for the step without an enzyme and for new acid-route compounds (75 comparisons, 41 with a higher product level). The study is targeted metabolomics of known compounds, so it tests reaction-level evidence and not spectral matching.

Pilots on the other use cases (PMN, TX, UN) are still WIP.

## 3. Ranking and Scoring of Predictions 

The pilots already rank evidence in tiers (for example `gene_direct` over `gene_uniprot` over `gene_ec`, and the six tiers of the metabolite annotations) and the consensus of three annotation tools gives a score between 0 and 1. A scoring framework that ranks candidate pathway components by evidence strength, completeness, provenance and reproducibility, and its benchmark against the experimentally validated pathways of PlantMetWiki, is still to be defined (TODO).

## 4. Submission system (optional)

The discussion workflow of the specification (issue forms, labels and Actions that open pull requests) is already an automated, reviewed way to approve *terms*. TODO: test an automated system to submit, validate (against the SHACL shapes) and approve new *predictions*; a design note and a local test of Nanodash, a tool for publishing signed nanopublications, are being explored for this.

**Governance.** We aim to improve decentralised governance: who may propose, who may approve, and how decisions are traced. Today only people with triage or write access to the repository can approve, and every change passes a reviewed pull request. TODO: describe the governance model agreed by the community.

# Discussion

...

## Acknowledgements
We thank Nicola Zamboni and Adriano Rutz for the supervision of Elena Del Pup during the preparation of the BioHackathon and the writing of this report. 
...

# References

```{=latex}
\AtEndDocument{%
```

# Appendices

## Appendix A: Original project plan (from the proposal)

The plan consists of three interconnected work packages corresponding to the project objectives. The BioHackathon Europe 2026 (9 - 14 November 2026, Barcelona) extends this work to a broader international community.

### Community requirements and draft semantic framework (Objective 1)

The first month establishes what a minimum information specification for predicted plant biosynthetic pathway knowledge must contain. Requirements will be collected through a structured questionnaire, disseminated to an identified list of stakeholders across European institutions, and through targeted interviews with researchers in metabolomics, plant biology, semantic web technologies, and the relevant ELIXIR communities. Questions will cover data modalities in routine use, metadata that is recorded in practice, analytical workflows, predictive tools, and datasets available for reuse.

In parallel, existing ontologies, controlled vocabularies, and interoperability resources will be reviewed, including WikiPathways [@usesMethodIn:Zdouc2025], BridgeDb [@usesMethodIn:Rutz2026], Identifiers.org, and the Ontology Lookup Service. A gap analysis will identify concepts that no current vocabulary expresses to describe evidence, provenance, and confidence, and will document where existing terms can be reused. The specification will follow the structure of MIBiG [@citesAsDataSource:Singh2025MEANtools] and MITE [@citesForInformation:Sansone2019], which are already familiar to the natural product community, while being built directly on a machine-actionable RDF-based model.

In parallel, I will participate in the meetings of the MetaboLinkAI project and present PlantMetWiki [@citesAsDataSource:DelPup2026PlantMetWiki] and the project objectives to partners to identify synergies with existing tools and involve them in the standard development process. Together with the host laboratory, I will select one paired transcriptomics-metabolomics dataset as the proof-of-concept for Months 2 and 3, prioritizing a species for which PlantMetWiki already holds curated pathways, so that predictions can later be assessed against known biology.

Expected outputs: stakeholder requirements report; gap analysis of existing vocabularies; draft minimum information specification expressed as an RDF data model; selected proof-of-concept dataset.

### Prototype validation schema (Objective 2)

The second month implements and tests the specification to prototype an end-to-end workflow connecting pathway knowledge, metabolomics data, transcriptomics evidence, and computational predictions within a common semantic framework. Semantic data shapes (SHACL or ShEx) will be written to encode the required metadata, provenance, quality criteria, and interoperability constraints, giving machine-actionable validation of multi-omics datasets (transcriptomics and metabolomics).

The selected transcriptomics-metabolomics dataset will be transformed into a semantically enriched representation and linked to pathway entities in PlantMetWiki following Linked Open Data principles and the FAIR guiding principles [@citesForInformation:Agrawal2024]. Achieving this requires resolving identifier mismatches, provenance modeling, and vocabulary alignment between resources, which will be supported by the expertise of the Zamboni Lab and MetaboLinkAI partners.

Interactions with MetaboLinkAI researchers and collaborators from the ELIXIR BioHackathon project "Developing Open Standards for a Semantic Framework in Plant Specialized Metabolism" (9 - 14 November 2026 in Barcelona) will keep the schema aligned with parallel developments in federated querying, semantic enrichment, and FAIRification workflows, and will ensure that what is prototyped here is what the community will later be asked to adopt.

Expected outputs: validation schema implementing the specification; tested end-to-end FAIR integration workflow; semantically enriched proof-of-concept dataset; demonstration of interoperable querying across PlantMetWiki and multi-omics-supported predictions.

### Evidence integration, benchmarking, and dissemination (Objective 3)

The final month focuses on integrating computational predictions and experimental evidence into a unified framework for pathway prioritization and hypothesis generation. Predictions for the proof-of-concept species by plantiSMASH [@citesAsDataSource:DelPup2026plantiSMASH] and MEANtools [@citesForInformation:vanIersel2010] will be mapped to a common semantic representation and aligned with experimental observations.

A scoring framework will be defined to rank candidate pathway components by evidence strength, completeness, provenance, and reproducibility. Its performance will be benchmarked using the experimentally validated pathways already curated in PlantMetWiki as ground truth. This provides an objective measure of whether evidence-based scoring adds discriminative power, and yields a prioritised list of candidate components that are well supported but not yet experimentally described, which are of direct interest for follow-up work in both laboratories.

The resulting workflows, standards, and validation approaches will be reviewed with collaborators from MetaboLinkAI, ELIXIR, and WikiPathways, released openly and registered on FAIRsharing [@citesAsAuthority:Wilkinson2016] to maximize visibility, reuse, and long-term sustainability. The ELIXIR BioHackathon in Barcelona (9-14 November 2026) will extend the outreach to a broader international community to refine, test, and adopt them, beyond the duration of the fellowship.

Expected outputs: benchmarked scoring scheme; prioritized candidate pathway components for the proof-of-concept species; openly released specification, schemas, and workflows.

The three packages are sequential but independently deliverable: the specification and gap analysis stand alone as a community contribution even if integration proves more complex than anticipated, and the validation schema is useful independently of the scoring results. Overall, the work will contribute towards establishing a FAIR and interoperable framework for integrating experimentally validated pathway knowledge, multi-omics evidence, and computational predictions, enabling more reproducible and scalable discovery of plant specialized metabolic pathways.

```{=latex}
}
```
