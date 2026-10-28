# How this repository was made (Angola)

This file is written by the build on 2026-10-28, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Diário da República de Angola, I Série, n.º 154 (16 August 2021), via the Government of Angola's legislation portal | <https://plataformacipra.gov.ao/public/ficheiros/arquivos/Gov_AngolaConstituição190102230948141675284494.pdf> | 2026-10-28 | Official text of the law (Imprensa Nacional). The portal states no licence. |
| Tribunal Constitucional de Angola, Constituição da República de Angola, Edição Especial Actualizada (2022) | <https://www.tribunalconstitucional.ao/media/d11gvf0z/edicao-especial-actualizada-2022.pdf> | 2026-10-28 | Official edition of the Tribunal Constitucional; no licence stated. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constituicao` | Constituição da República de Angola | 1 | 2021-08-16 to 2021-08-16 |

The build made 1 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futuro`: laws not yet in force on 2026-10-28.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 2 laws in the record.
- 1 tags.

## Dates

Each commit is dated at noon (Africa/Luanda) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Not applied as a general rule: every version is dated by the vigência clause of the law that made it. Lei n.º 18/21, art. 6.º: "A presente Lei de Revisão Constitucional entra em vigor à data da sua publicação" (Diário da República, I Série, n.º 154, 16 August 2021). Leis n.º 38/20 and 39/20: in force ninety days after publication (Diário da República, I Série, n.º 179, 11 November 2020), that is 9 February 2021. https://plataformacipra.gov.ao/public/ficheiros/arquivos/Gov_AngolaConstituição190102230948141675284494.pdf

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `9c42b9a8ab52ac980be6c85452126e9ddb271051982b3e588aeebca8cff285af` (217170 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

1 versions of 1 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Acts: the Constitution (published here), the Código Penal and the Código do Processo Penal (built, but held back from main). Lei n.º 22/11 (data protection) is published by the APD only as image scans: left out (no OCR).
- The Constitution has one version, 2021-08-16: the official republication ordered by Lei n.º 18/21 (art. 4.º), in force on publication (art. 6.º). It is credited to the publisher as the oldest version available, naming the Constitution of 2010 and Lei n.º 18/21. A 2010 version cannot be built: the Diário da República of 5 February 2010 is available only as a scan (no OCR), and Lei n.º 18/21 prints only the new wording of the provisions it changes ("1. […]" for kept paragraphs), so the 2010 wording of the altered provisions is not available as text.
- Cross-check: every article, the preamble, the three annexes and the approval formula were compared word for word with the Tribunal Constitucional's Edição Especial Actualizada (2022). They agree apart from five differences between the two editions, where the Diário da República's wording is kept: art. 36.º, n.º 3 lists the last item as "f)" (TC "e)"); art. 42.º, n.º 3, a) "proteção" (TC "protecção"); art. 173.º, n.º 1 "A requerimento do Presidente da Republica" (TC "O requerimento do Presidente da República"); art. 174.º, n.º 4 "extra-judicial" (TC "extrajudicial"); art. 242.º, n.º 2 "esetabelece" (TC "estabelece"). Article titles are in sentence case in the Gazette and in title case in the TC edition. Four words split across lines in the TC edition (arts. 16, 83, 95, 96) are artefacts of its text layer.
- Footnotes and their markers (7 pt and smaller) are left out; ordinal superscripts after body text ("n.os", "2.os") are kept. Line-end soft hyphens are joined; a hard hyphen at a line end is joined without the hyphen only when the whole word is printed elsewhere in the same Gazette, otherwise kept.
- Unit layout: one file per article (art-NNN, art-NNN-a for the articles added with a letter), the preamble, the three annexes and the approval formula; title, chapter and section headings are gathered in one file, estrutura, which names the article each heading precedes. The list of constituent legislators printed after the annexes is not law text and is left out.
- Typesetting is normalised once: NBSP to space, en dash to em dash, curly double quotes to « », the curly apostrophe to a straight one, runs of spaces collapsed.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (Claude Opus 5.5, claude-opus-5-5) wrote Lexifina's code, chose the sources and wrote the decisions. No model wrote, summarised or transformed legal text: the text is taken from the official PDFs by deterministic code.
