# Angola: law history in git


The law of Angola as a git history: one file per provision, one commit per version on the day it took effect, and the act that made each change as the commit's author. `git blame` names the act behind every paragraph; `git log` lists every change to an article; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Angola's national law, which global-law reads at `angola/national/acts/`.

**What is in it now:** the Constitution (Constituição da República de Angola), in one version: the official republication of 16 August 2021 ordered by the constitutional revision Lei n.º 18/21, with its articles 1.º to 244.º and the 7 added with a letter (such as 107.º-A), the preamble, the three annexes and the approval formula. [`constituicao/README.md`](constituicao/README.md) lists every provision.

Each provision is one file in `constituicao/` (`art-076.md` is Article 76, Direito ao trabalho; `art-107-a.md` is Article 107-A); the headings (Título, Capítulo, Secção) are gathered in [`constituicao/estrutura.md`](constituicao/estrutura.md), each naming the article it precedes.

The text is in Portuguese, as the Diário da República prints it. An English translation is not part of this record.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to Article 76 of the Constitution (the right to work) | `git log -p --word-diff -- constituicao/art-076.md` |
| Which act wrote each paragraph of Article 76? | `git blame constituicao/art-076.md` |
| Every version of Article 76, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- constituicao/art-076.md` |
| Article 76 as in force on 1 January 2022 | `python tools/vigente_em.py 2022-01-01 constituicao 76` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Angolan law](https://global-law.lexifina.com/v1/try_claude?country=angola)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=angola)**: the same question in ChatGPT.
- **[Search Angolan law on our site](https://lexifina.com/law?country=angola&q=f%C3%A9rias)**: a search for "férias" (annual leave), with each provision's text and its versions, no account needed.
- **[Developer REST API](https://global-law.lexifina.com/v1/search_law?query=f%C3%A9rias&jurisdiction=angola)**: the same search as JSON, with no key. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in Portuguese or in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add angola/national/acts
python3 tools/law.py show 2026-01-01 angola/national/acts/constituicao/art-076.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, Africa/Luanda, on the day the version took effect, and carries it in its `In-force:` trailer:

- the day comes from the in-force clause of the law that made the version: Lei n.º 18/21, artigo 6.º, puts the revision in force on its publication, 16 August 2021;
- `tools/vigente_em.py` picks the version by that trailer, not by the commit date.

The one version is credited to the publisher, Imprensa Nacional (Diário da República de Angola), as the oldest version available, and its commit names the Constitution of 2010 and Lei n.º 18/21 as the laws that produced the text. A later change will be credited to the law that made it; the committer is always Lexifina.

## How it is checked

- `tools/check_repo.py` reads every version back from git on the day it took effect and on the day before, and both must match the corpus: 0 mismatches. The results are in [`REPRODUCE.md`](REPRODUCE.md).
- Every article, the preamble, the annexes and the approval formula were compared word for word with the Tribunal Constitucional's *Edição Especial Actualizada* (2022). They agree apart from five places where the two editions differ (artigos 36.º, 42.º, 173.º, 174.º and 242.º); the Gazette's wording is kept, and `REPRODUCE.md` lists each one.
- History is append-only: no merge commits, no commit dated in the future, and every commit's trailers parse.

## What it does not show

- **The Constitution of 2010 as first published**, and so the words Lei n.º 18/21 replaced. The Diário da República of 5 February 2010 is available only as a scanned image, which this record does not transcribe, and Lei n.º 18/21 prints only the new wording of the provisions it changes.
- **Any other act yet.** The Código Penal (Lei n.º 38/20) and the Código do Processo Penal (Lei n.º 39/20) are built on the `preview` branch but held back from `main`: the Código Penal was amended by Lei n.º 12/24, not found with a text layer, and the later history of the Código do Processo Penal is not yet checked. Texts published only as scans, such as the data protection law (Lei n.º 22/11), are not included.
- **The Gazette's footnotes**, which mark 26 provisions "Alterado", 7 "Aditado" and 6 "Revogado" by Lei n.º 18/21, and the list of constituent legislators printed after the annexes.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [Government of Angola, legislation portal](https://governo.gov.ao/documentos/constitui%C3%A7%C3%A3o) | Official journal: Diário da República, I Série (Imprensa Nacional), born-digital PDFs | no, the issue as published | The text and its dates, from I Série n.º 154, 16 August 2021 |
| [Tribunal Constitucional](https://www.tribunalconstitucional.ao) | Official edition: *Constituição da República de Angola, Edição Especial Actualizada* (2022) | no | A word-for-word cross-check only |

## Licence

See [`LICENSE`](LICENSE). The texts are official legal texts of the Republic of Angola from the Diário da República (Imprensa Nacional), reproduced with that attribution; the portal publishes no licence for them. The history, commit messages, tables and tools are CC0 1.0.

No AI model wrote, translated or corrected legal text, and none runs when the history is built; the scripts were written by an AI model (see [`REPRODUCE.md`](REPRODUCE.md)).

## Em português

Este repositório guarda a história do direito angolano em git: um ficheiro por disposição, um commit por versão no dia em que entrou em vigor e, como autor do commit, o ato que fez cada alteração. Contém, por agora, a Constituição da República de Angola na republicação oficial de 16 de Agosto de 2021 (Diário da República, I Série, n.º 154), ordenada pela Lei n.º 18/21; a versão original de 2010 só existe como imagem digitalizada e não é transcrita. `python tools/vigente_em.py 2022-01-01 constituicao 76` mostra o artigo 76.º em vigor nessa data, e `git blame constituicao/art-076.md` indica o ato de cada parágrafo.

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
