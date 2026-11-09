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

La guida visiva si trova in art/visual-bible.md. **Le immagini personalizzate sotto `art/` non sono usate automaticamente in base al nome della cartella:** si collegano all'edizione tramite `art/edition-assets.yml`. La copertina `art/cover/bot-cover.png` sostituisce la copertina generata e `art/locations/valle-corta-sunset.png` sostituisce la tavola del capitolo 3 (dove viene introdotta Valle Corta). Gli altri 34 capitoli conservano le tavole generate. La stessa mappa alimenta EPUB, DOCX, PDF e ZIP illustrato, e i controlli verificano che le immagini originali siano incluse. Le tavole generate usano oggetti e silhouette riproducibili; per eventuali immagini realistiche di personaggi ricorrenti occorreranno reference sheet approvate e gli stessi asset di riferimento, non generazioni indipendenti. Il sistema è versionato insieme al manoscritto.

Per rigenerare l'edizione: installare le dipendenze Python in tools/requirements.txt e Pandoc, poi eseguire python tools/build.py. La conversione da DOCX a PDF viene eseguita nella pipeline GitHub tramite LibreOffice.

## Revisione corale v0.31.0

La nuova lettura di BOT rafforza la vita di ogni personaggio oltre il confronto sui robot: amici che non si vedono, acquisti rinviati, sport per principianti, turni, figli, conversazioni familiari banali e bisogni non dichiarati. Le modifiche sono state integrate in **34 scene** canoniche senza cambiare la struttura di 35 capitoli né il finale.

La guida alla caratterizzazione è in [`guidelines/personaggi-vita-privata-e-contraddizioni.md`](guidelines/personaggi-vita-privata-e-contraddizioni.md); il rapporto di revisione è in [`reviews/revisione-arco-corale-v0.31.0.md`](reviews/revisione-arco-corale-v0.31.0.md). Le schede `characters/`, lo stato e la timeline sono state aggiornate per preservare i desideri quotidiani nel lavoro successivo. Rimangono volutamente aperte alcune questioni morali e operative; la review non dichiara risolto ogni difetto letterario.

## Da Cyberdine industriale a software house — revisione v0.32.0

BOT resta un romanzo di 35 capitoli, ora ambientato dal primo capitolo in una Cyberdine che **vende software di integrazione, sviluppo, verifica e continuità**, non robot. Gli agenti AI lavorano prima dei robot fisici. B-17 taglia inizialmente l'erba del campus, passa alle commissioni e poi, grazie a un potenziamento che viene spiegato solo nel capitolo 10, comincia a contribuire ai test informatici. Gli sviluppatori imparano gradualmente a dialogare con agenti e robot e a esaminare il risultato senza scrivere tutto il codice; dopo l'uscita di Bi alcune dipendenze rimangono difficili da comprendere. La storia personale, l'azione collettiva di Bi e il finale restano quelli della versione precedente.

La [guida canonica allo scenario software](guidelines/cyberdine-software-evoluzione.md) definisce limiti tecnici, gerarchie delle autorizzazioni, settore aziendale e sequenza. La [review strutturale v0.32.0](reviews/revisione-cyberdine-v0.32.0.md) attraversa tutti i 35 capitoli e distingue le scene riscritte dalle parti conservate. I 37 file-scena interessati sono stati modificati direttamente nel romanzo, mantenendo il numero complessivo dei capitoli e delle scene. Vedere la release v0.32.0 per PDF, EPUB, DOCX e immagini.

## Edizione v0.33.0 — riscrittura della storia dall'agentico al robotico

La versione precedente aveva ridefinito il mestiere di Cyberdine. Questa edizione riscrive **21 scene narrative** per mostrare, non soltanto spiegare, l'evoluzione di Bi e del lavoro: prima il tagliaerba, poi la carta, poi le conversazioni e l'aiuto agli sviluppatori; dopo la sua uscita, le persone devono recuperare competenze di codice che hanno esercitato sempre meno. Nei capitoli 25, 27 e 30 gli effetti diventano economici, professionali e infine sistemici.

Sono state riscritte le quattro scene dei capitoli 1, 2 e 5, due scene del capitolo 3 e una ciascuna nei capitoli 4, 7, 8, 9, 25, 27 e 30. **Gli altri capitoli e le scene non elencate non vengono presentati come integralmente riscritti**: trama, dialoghi centrali e finale restano quelli canonici. Il documento [Riscrittura narrativa v0.33.0](reviews/riscrittura-narrativa-v0.33.0.md) documenta le scelte scena per scena; la [guida di Cyberdine](guidelines/cyberdine-software-evoluzione.md) contiene i vincoli tecnici e narrativi.
