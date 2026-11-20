# Figures of the partner questionnaire

| Folder | Content |
|---|---|
| `scripts/` | Python scripts (matplotlib) that draw the figures from the tables: `make_survey_figure.py`, `make_survey_figure_v2.py`, `make_tools_figure.py` |
| `tables/` | The questionnaire answers, anonymised: `survey_responses.csv` (what respondents use, what they want to find), `survey_tools.csv` (bioinformatics tools), `survey_questions.csv` (questions to ask PlantMetWiki, with our theme) |
| this folder | The figures: `survey_entry_exit.*` (v1), `survey_entry_exit_v2.*` (adds the question themes), `survey_tools.*` |

Redraw: `python scripts/make_survey_figure_v2.py` (needs matplotlib).

**Update of 20 November 2026 (11 respondents).** The tables now hold the 11 respondents who filled in the extended questionnaire (goals, data, tools); 4 were added (r8 to r11). Two corrections to the earlier tables: the old r7 was identical to r6 in both tables and was removed (the old r8 is now r7), and the question about transcription factors, which had been merged into the answer a8, is now a separate answer (a9); `survey_questions.csv` has 13 answers with 17 questions. The respondent IDs of `survey_tools.csv` are assumed to match those of `survey_responses.csv` (checked by the order of the form rows). The answers in `survey_questions.csv` are anonymous and not linked to either. Free-text goals (improving cultivation conditions, stress responses) and data (knowledge graphs, mechanistic models, GEMs) are kept as separate items.

## Participants figure

`participants_expertise.*` (script `scripts/make_participants_figure.py`) shows the 11 participants of the BioHackathon project, their self-declared expertise and their working groups. Tables: `tables/participants.csv` (name, attendance), `tables/participants_expertise.csv` (expertise, participant) and `tables/working_groups.csv` (group, subgroup, participant). The tables hold names only (no email addresses). They were compiled from the planning notes of the project (updated 2026-11-20): "Sebastien" in the working-group list is Sebastian Beier (confirmed by the author).
