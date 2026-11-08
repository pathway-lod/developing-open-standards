# Figures of the partner questionnaire

| Folder | Content |
|---|---|
| `scripts/` | Python scripts (matplotlib) that draw the figures from the tables: `make_survey_figure.py`, `make_survey_figure_v2.py`, `make_tools_figure.py` |
| `tables/` | The questionnaire answers, anonymised: `survey_responses.csv` (what respondents use, what they want to find), `survey_tools.csv` (bioinformatics tools), `survey_questions.csv` (questions to ask PlantMetWiki, with our theme) |
| this folder | The figures: `survey_entry_exit.*` (v1), `survey_entry_exit_v2.*` (adds the question themes), `survey_tools.*` |

Redraw: `python scripts/make_survey_figure_v2.py` (needs matplotlib).

The respondent IDs r1-r8 of `survey_tools.csv` are assumed to match those of `survey_responses.csv` (to be confirmed). The answers in `survey_questions.csv` are anonymous and not linked to either.
