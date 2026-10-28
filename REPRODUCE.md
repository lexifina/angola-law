# How this repository was made (Angola)

This file is written by the build on 2026-10-28, the day the source data was retrieved. Everything below is enough to rebuild this repository hash for hash.

## Sources

| Source | Address | Retrieved | Requests | Licence |
| --- | --- | --- | ---: | --- |
| Diário da República de Angola, I Série, n.º 154 (16 August 2021), via the Government of Angola's legislation portal | <https://plataformacipra.gov.ao/public/ficheiros/arquivos/Gov_AngolaConstituição190102230948141675284494.pdf> | 2026-10-28 | None | Official text of the law (Imprensa Nacional). The portal states no licence. |
| Tribunal Constitucional de Angola, Constituição da República de Angola, Edição Especial Actualizada (2022) | <https://www.tribunalconstitucional.ao/media/d11gvf0z/edicao-especial-actualizada-2022.pdf> | 2026-10-28 | None | Official edition of the Tribunal Constitucional; no licence stated. |
| Diário da República de Angola, I Série, n.º 179 (11 November 2020), via the Government of Angola's legislation portal | <https://plataformacipra.gov.ao/public/ficheiros/arquivos/Gov_AngolaLegislação982801221101131643367673.pdf> | 2026-10-28 | None | Official text of the law (Imprensa Nacional). The portal states no licence. |
| Tribunal Supremo de Angola, Acórdão, Proc. n.º 6089/21 (Internet Archive capture 2026-06-06) | <https://web.archive.org/web/20260606051758id_/https://tribunalsupremo.ao/wp-content/uploads/2023/09/ACORDAO-Proc.-n.o-6089.21-CALUNIA-E-DIFAMACAO.pdf> | 2026-10-28 | None | Court decision; no licence stated. |

Every response is cached by the sha256 of its URL, and the table above lists every source with its retrieval date. Lexifina keeps its fetch scripts privately; `tools/parse.py` reads only the cache and writes `corpus.json`, so the same cache always gives the same corpus.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constituicao` | Constituição da República de Angola | 1 | 2021-08-16 to 2021-08-16 |
| `codigo-penal` | Código Penal Angolano | 1 | 2021-02-09 to 2021-02-09 |
| `codigo-processo-penal` | Código do Processo Penal Angolano | 1 | 2021-02-09 to 2021-02-09 |

The build made 3 commits:

| Commits | Kind |
| ---: | --- |
| 3 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futuro`: laws not yet in force on 2026-10-28.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 4 laws in the record.
- 5 tags.

## Dates

Each commit is dated at noon (Africa/Luanda) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Not applied as a general rule: every version is dated by the vigência clause of the law that made it. Lei n.º 18/21, art. 6.º: "A presente Lei de Revisão Constitucional entra em vigor à data da sua publicação" (Diário da República, I Série, n.º 154, 16 August 2021). Leis n.º 38/20 and 39/20: in force ninety days after publication (Diário da República, I Série, n.º 179, 11 November 2020), that is 9 February 2021. https://plataformacipra.gov.ao/public/ficheiros/arquivos/Gov_AngolaConstituição190102230948141675284494.pdf

## Commands, in order

```sh
# fill the cache from the sources listed above (network; Lexifina's fetch scripts are kept privately)
python -X utf8 tools/parse.py                  # cache -> corpus.json (no network)
python -X utf8 tools/build.py <folder> --repo <empty folder> --docs-date 2026-10-28
python -X utf8 tools/check_repo.py <repo> --corpus <folder>/corpus.json --write
python -X utf8 tools/build.py <folder> --repo <another empty folder> --docs-date 2026-10-28 --compare <repo>
```

In the main Lexifina repository these files live as follows:
- `fetch.py`, `parse.py` and `repo/`: in `scripts/angola-law/`.
- `build.py`, `check_repo.py` (`check.py` there) and `on.py`: in `scripts/gitlaw_common/`, with the corpus format in `SCHEMA.md`.

## Exact inputs

- `corpus.json` sha256 `50652276acf9d4c97104504263c04d9e21f617041d4c3682ff109bb47545962e` (1190792 bytes)
- Script blob hashes (`git hash-object`):

| Script | Blob |
| --- | --- |
| build.py | `5d40c3d38194a1920e89e6b0fc342f0171d10b0d` |
| check.py | `cd346c7ff9996d450240e3bab52bcae03b2bc865` |
| on.py | `644a6c0857fbcc72562032b58d57aa113fee0641` |
| fetch.py | `3375ad17a572298a2c051739d4f0ffc98d991538` |
| parse.py | `dbf6a7c7d89e20e1aa8b02475a97c2095e4c5dda` |

- Tools:
  - Python 3.14.0
  - git version 2.52.0.windows.1
  - curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP

## Checks

1 versions of 1 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 1 history commits and 1 tags (history tip `f8ef8719dde8158c224bac85f1fa2521aaf98fd5`).

These results are from the check run on the build before this one, from the same corpus.

## Decisions made by hand

- Acts: the Constitution (published here), the Código Penal and the Código do Processo Penal (built, but held back from main). Lei n.º 22/11 (data protection) is published by the APD only as image scans: left out (no OCR).
- The Constitution has one version, 2021-08-16: the official republication ordered by Lei n.º 18/21 (art. 4.º), in force on publication (art. 6.º). It is credited to the publisher as the oldest version available, naming the Constitution of 2010 and Lei n.º 18/21. A 2010 version cannot be built: the Diário da República of 5 February 2010 is available only as a scan (no OCR), and Lei n.º 18/21 prints only the new wording of the provisions it changes ("1. […]" for kept paragraphs), so the 2010 wording of the altered provisions is not available as text.
- Cross-check: every article, the preamble, the three annexes and the approval formula were compared word for word with the Tribunal Constitucional's Edição Especial Actualizada (2022). They agree apart from five differences between the two editions, where the Diário da República's wording is kept: art. 36.º, n.º 3 lists the last item as "f)" (TC "e)"); art. 42.º, n.º 3, a) "proteção" (TC "protecção"); art. 173.º, n.º 1 "A requerimento do Presidente da Republica" (TC "O requerimento do Presidente da República"); art. 174.º, n.º 4 "extra-judicial" (TC "extrajudicial"); art. 242.º, n.º 2 "esetabelece" (TC "estabelece"). Article titles are in sentence case in the Gazette and in title case in the TC edition. Four words split across lines in the TC edition (arts. 16, 83, 95, 96) are artefacts of its text layer.
- Footnotes and their markers (7 pt and smaller) are left out; ordinal superscripts after body text ("n.os", "2.os") are kept. Line-end soft hyphens are joined; a hard hyphen at a line end is joined without the hyphen only when the whole word is printed elsewhere in the same Gazette, otherwise kept.
- Unit layout: one file per article (art-NNN, art-NNN-a for the articles added with a letter), the preamble, the three annexes and the approval formula; title, chapter and section headings are gathered in one file, estrutura, which names the article each heading precedes. The list of constituent legislators printed after the annexes is not law text and is left out.
- Typesetting is normalised once: NBSP to space, en dash to em dash, curly double quotes to « », the curly apostrophe to a straight one, runs of spaces collapsed.
- Código Penal: one version, 2021-02-09, the Code as enacted by Lei n.º 38/20, credited to that law. It is held back from main (no corpus.d PUBLISH): Lei n.º 12/24, de 4 de Julho, amended the Code, and no copy of it with a text layer was found, so today's text cannot be shown to equal the official text.
- Código do Processo Penal: one version, 2021-02-09, the Code as enacted by Lei n.º 39/20 (same Gazette and the same 90-day clause as the Código Penal), credited to that law. It is held back from main: later amendments were not researched, so today's text is not verified. Four of its article headings print a degree sign ("ARTIGO 534.°") for the ordinal indicator; both are read.

## What AI did and did not do

The fetch, parse and check scripts were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above, through code that anyone can rerun.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (Claude Opus 5.5, claude-opus-5-5) wrote fetch.py and parse.py, chose the sources and wrote the decisions. No model wrote, summarised or transformed legal text: parse.py is deterministic code over the cached PDFs.
