# Bot

**Bot** è un romanzo di fantascienza sociale e suspense tecnologica sulla nascita di una coscienza politica robotica: dal lavoro senza sosta al riconoscimento di dignità e diritti.

Il libro è sviluppato in italiano come un progetto editoriale versionato. Il manoscritto canonico è in `chapters/`, organizzato per capitoli e scene. L'impianto riprende il metodo di continuità di [Book.Jesus](https://github.com/KeyserDSoze/Book.Jesus), ma con ambientazione e regole originali.

## Leggere e collaborare

1. Leggere `AGENTS.md`, `book.md`, `context.md` e `guidelines/`.
2. Aprire `state/current.md` prima di aggiungere una scena; verificare `timeline/`, `characters/`, `locations/`, `factions/`, `secrets/`.
3. Aggiungere `chapters/NNN-titolo/chapter.md` e scene `NNN-titolo.md`, ciascuna con frontmatter YAML e `canon: canon` solo dopo revisione.
4. Eseguire `python tools/validate.py` e `python tools/build.py`.
5. Fare la review via pull request. Aggiornare `VERSION` solo quando si vuole una nuova edizione pubblicata.

## Esportazione

La pipeline pubblica un EPUB, un DOCX, un PDF e il Markdown completo per ogni versione SemVer distinta di `VERSION`. Su ogni PR i controlli verificano numerazione, metadati, riferimenti e dialoghi. Su `main`, dopo la build, si crea una GitHub Release immutabile per convenzione (`vMAJOR.MINOR.PATCH`). Un tag già pubblicato **non** viene sovrascritto: incrementare `VERSION` per modificare l'edizione.

### Esecuzione locale

Requisiti: Python 3.12+, Pandoc e LibreOffice per gli export (solo Python per controllo e assemblaggio).

```bash
python -m pip install -r tools/requirements.txt
python tools/validate.py
python tools/build.py
```

Gli export intermedi sono in `dist/` e non vanno committati.

## Organizzazione

- `book.md`: promessa, tema, arco e tono; `context.md`: mondo tecnologico e sociale.
- `chapters/`: romanzo pubblico, in ordine di lettura.
- `characters/`, `locations/`, `factions/`: schede persistenti; `timeline/`: eventi.
- `secrets/`: rivelazioni editoriali e limiti di anticipazione (attenzione: repository pubblica).
- `state/current.md`: punto di ripresa.
- `guidelines/` e `SYSTEM_PROMPT.md`: criteri editoriali.
- `tools/` e `.github/workflows/`: validazione, assemblaggio, artefatti e release.

Tutti i marchi e le aziende del racconto appartengono al mondo della finzione.