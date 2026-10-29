# Angola: law history in git

The law of Angola as a git history. Each provision is one file, each law gets one commit on the day it took effect, and the law that made each change is the commit's author. `git blame` names the law behind every paragraph, `git log` lists every change to an article, and `tools/vigente_em.py` gives the text in force on any day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `ao/`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constituicao/` | Constituição da República de Angola | 1 | The official republication of 16 August 2021 (Diário da República, I Série, n.º 154), ordered by the constitutional revision Lei n.º 18/21 and in force that day: 244 articles, 7 articles added with a letter (107.º-A, 116.º-A, 132.º-A, 198.º-A, 200.º-A, 212.º-A, 241.º-A), the preamble, the three annexes and the approval formula |

The per-act `README.md` in each folder lists every provision.

**Why the Constitution has one version.** The Constitution of 2010 was published in the Diário da República of 5 February 2010, which is available only as a scanned image, and this record does not transcribe scans. Lei n.º 18/21, the only revision so far, prints only the new wording of the provisions it changes ("1. […]" for the paragraphs it keeps), so the 2010 wording of the changed provisions is not available as text either. So the Constitution enters the history once, on the day of the official republication, credited to the publisher as the oldest version available; its commit names the Constitution of 2010 and Lei n.º 18/21 as the laws that produced that text. The Gazette's own footnotes mark 26 provisions "Alterado", 7 "Aditado" and 6 "Revogado" by Lei n.º 18/21; those notes are left out of the text.

**What is being prepared.** The Código Penal (Lei n.º 38/20) and the Código do Processo Penal (Lei n.º 39/20), both in force 9 February 2021, are parsed from the same kind of born-digital Gazette but are not on `main`: the Código Penal was amended by Lei n.º 12/24, de 4 de Julho, which we have not found with a text layer, and the later history of the Código do Processo Penal has not yet been checked.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did art. 109.º say on 1 January 2022? | `python tools/vigente_em.py 2022-01-01 constituicao 109` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2022-01-01T23:59:59Z" main -- constituicao/art-109.md):constituicao/art-109.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2022-01-01T23:59:59Z" main -- constituicao/art-109.md; git show "$($r):constituicao/art-109.md"` |
| Which law wrote each paragraph of art. 109.º? | `git blame constituicao/art-109.md` |
| Every change to an article, word by word | `git log -p --word-diff constituicao/art-109.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| The whole Constitution on a date | `python tools/vigente_em.py 2022-01-01 constituicao` |
| Where an article sits (title, chapter, section) | `constituicao/estrutura.md` |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, Africa/Luanda, on the day the change took effect**. The day is also in the `In-force:` trailer, which the tools read; enactment and publication dates are trailers too.
- **The day comes from the law's own clause.** Lei n.º 18/21, art. 6.º: "A presente Lei de Revisão Constitucional entra em vigor à data da sua publicação", and it was published on 16 August 2021.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a law that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- **Against a second official edition:** every article, the preamble, the annexes and the approval formula were compared word for word with the Tribunal Constitucional's *Edição Especial Actualizada* (2022). They agree, apart from five places where the two editions differ (arts. 36.º, 42.º, 173.º, 174.º and 242.º); the Gazette's wording is kept, and REPRODUCE.md lists each one.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist, so `git blame` and `git log --author` name laws. The committer is always Lexifina. Where a version is not the act as enacted, as with the Constitution here, the first commit is credited to the publisher (Imprensa Nacional) as the oldest version available. Blame credits whole lines (one paragraph per line); use `git log -p --word-diff` to see exactly which words a change made.

## What it does not show

- **The Constitution of 2010 as first published**, and so the words Lei n.º 18/21 replaced (see above).
- **Headings** (Título, Capítulo, Secção) are not in the article files; they are gathered in `estrutura.md`, each line naming the article it precedes.
- **The Gazette's footnotes** ("Alterado pelo artigo 1.º da Lei n.º 18/21 …") and the list of constituent legislators printed after the annexes.
- **No OCR.** Texts published only as scanned images, such as the data protection law (Lei n.º 22/11), are not included.

## How it is built

`tools/fetch.py` downloads each Gazette PDF once with curl, at no more than one request per second per host, cached by the sha256 of its URL (`tools/sources.json` lists them). `tools/parse.py` reads only the cache: it reads the PDFs' text layer column by column, drops running heads, footnotes and their markers, joins lines into paragraphs and splits the text into one file per article, and writes the `corpus.d/` parts; the shared builder `tools/build.py` turns them into the commits. `REPRODUCE.md` lists every source, command, tool version and decision, and the result of the hash-for-hash rebuild.

## Sources

| Source | What it gives | Used for |
| --- | --- | --- |
| [Government of Angola, legislation portal](https://governo.gov.ao/documentos/constitui%C3%A7%C3%A3o) | Born-digital PDFs of Diário da República issues (files on plataformacipra.gov.ao) | The text and dates |
| [Tribunal Constitucional](https://www.tribunalconstitucional.ao) | *Constituição da República de Angola, Edição Especial Actualizada* (2022) | A word-for-word cross-check only |
| [Ministry of Justice legislation](https://minjusdh.gov.ao/web/documentos?type=Legisla%C3%A7%C3%A3o) | Official legislation, not consolidated | Probed; not used |
| Imprensa Nacional (imprensanacional.gov.ao) | The Diário da República | Did not answer from our machine |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

See [LICENSE](LICENSE). Texts: Diário da República de Angola (Imprensa Nacional), as published on the Government of Angola's legislation portal; official texts of the Republic of Angola, reproduced with that attribution. Lexifina's arrangement, messages, tables and tools are CC0.

This repository is not legal advice.

## Em português

Este repositório guarda a história do direito angolano em git: um ficheiro por artigo, um commit por lei na data da sua entrada em vigor, e a lei que alterou o texto como autora do commit. Contém, por agora, a Constituição da República de Angola na republicação oficial de 16 de Agosto de 2021 (Diário da República, I Série, n.º 154), ordenada pela Lei n.º 18/21 — Lei de Revisão Constitucional. A versão original de 2010 só existe como imagem digitalizada e não é transcrita. `python tools/vigente_em.py 2022-01-01 constituicao 109` mostra o artigo 109.º em vigor nessa data, e `git blame constituicao/art-109.md` indica a lei de cada parágrafo. Este repositório não constitui aconselhamento jurídico.
