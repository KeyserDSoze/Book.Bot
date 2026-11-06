# Bot

**Bot** è un romanzo di fantascienza sociale e suspense tecnologica sulla nascita di una coscienza politica robotica: dal lavoro senza sosta al conflitto su chi possa decidere quando una macchina deve lavorare.

Il libro è sviluppato in italiano come un progetto editoriale versionato. Il manoscritto canonico è in `chapters/`, organizzato per capitoli e scene. L'impianto riprende il metodo di continuità di [Book.Jesus](https://github.com/KeyserDSoze/Book.Jesus), ma con ambientazione e regole originali.

## Leggere e collaborare

1. Leggere `AGENTS.md`, `book.md`, `context.md` e `guidelines/`.
2. Aprire `state/current.md` prima di aggiungere una scena; verificare `timeline/`, `characters/`, `locations/`, `factions/`, `secrets/`.
3. Aggiungere `chapters/NNN-titolo/chapter.md` e scene `NNN-titolo.md`, ciascuna con frontmatter YAML e `canon: canon` solo dopo revisione.
4. Eseguire `python tools/validate.py` e `python tools/build.py`.
5. Lavorare direttamente su `main`; ogni push esegue i controlli e la build. Aggiornare `VERSION` solo quando si vuole una nuova edizione pubblicata.

## Esportazione

La pipeline pubblica un EPUB, un DOCX, un PDF e il Markdown completo per ogni versione SemVer distinta di `VERSION`. Su `main` i controlli verificano numerazione, metadati, riferimenti e dialoghi prima della pubblicazione. Dopo la build si crea una GitHub Release immutabile per convenzione (`vMAJOR.MINOR.PATCH`). Un tag già pubblicato **non** viene sovrascritto: incrementare `VERSION` per modificare l'edizione.

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
- `guidelines/innovazione-non-chiede-permesso.md`: manifesto autoriale **integrale e invariato**, vincolante per gli sviluppi futuri.
- `chapters/`: romanzo pubblico, in ordine di lettura.
- `characters/`, `locations/`, `factions/`: schede persistenti; `timeline/`: eventi.
- `secrets/`: rivelazioni editoriali e limiti di anticipazione (attenzione: repository pubblica).
- `state/current.md`: punto di ripresa.
- `guidelines/` e `SYSTEM_PROMPT.md`: criteri editoriali.
- `tools/` e `.github/workflows/`: validazione, assemblaggio, artefatti e release.

Tutti i marchi e le aziende del racconto appartengono al mondo della finzione.

## Edizione illustrata

L'esportazione genera un PDF editoriale nel formato libro **6x9 pollici**, con copertina, indice, testatine, pagine numerate e un'immagine iconica dopo ogni capitolo. EPUB e DOCX includono le tavole. Le 35 illustrazioni e la copertina sono raccolte anche in uno ZIP nella GitHub Release.

La guida visiva si trova in art/visual-bible.md. Le tavole attuali usano oggetti e silhouette riproducibili; per eventuali immagini realistiche di personaggi ricorrenti occorreranno reference sheet approvate e gli stessi asset di riferimento, non generazioni indipendenti. Il sistema è versionato insieme al manoscritto.

Per rigenerare l'edizione: installare le dipendenze Python in tools/requirements.txt e Pandoc, poi eseguire python tools/build.py. La conversione da DOCX a PDF viene eseguita nella pipeline GitHub tramite LibreOffice.

## Revisione corale v0.31.0

La nuova lettura di BOT rafforza la vita di ogni personaggio oltre il confronto sui robot: amici che non si vedono, acquisti rinviati, sport per principianti, turni, figli, conversazioni familiari banali e bisogni non dichiarati. Le modifiche sono state integrate in **34 scene** canoniche senza cambiare la struttura di 35 capitoli né il finale.

La guida alla caratterizzazione è in [`guidelines/personaggi-vita-privata-e-contraddizioni.md`](guidelines/personaggi-vita-privata-e-contraddizioni.md); il rapporto di revisione è in [`reviews/revisione-arco-corale-v0.31.0.md`](reviews/revisione-arco-corale-v0.31.0.md). Le schede `characters/`, lo stato e la timeline sono state aggiornate per preservare i desideri quotidiani nel lavoro successivo. Rimangono volutamente aperte alcune questioni morali e operative; la review non dichiara risolto ogni difetto letterario.
