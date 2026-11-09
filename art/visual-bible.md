# Identità visiva di BOT — direttiva per l'edizione illustrata

## Linguaggio grafico e qualità

Ogni capitolo termina con una **tavola iconica** in un linguaggio visivo coerente. Prima gli oggetti della storia: racchetta, cartellina, spalla riparata, sirena, pomodoro, orologio, lampada. Non sono poster generici. Il generatore riproducibile tools/artwork.py produce una copertina e 35 tavole con motivi editoriali stabili: un aggiornamento del PDF non cambia casualmente i tratti della scena.

Palette: blu notte #111F2C, ardesia #1C3444, avorio #F1EAD8, rame #DA9E5E, grigio azzurrato #89AEB8. Immagini di capitolo 16:9, copertina 2:3. Font del testo Liberation Serif e titoli Lato, tramite pacchetti liberi installati in build; mai incorporare file di font proprietari nel repository.

## Identità dei personaggi — ciò che non può cambiare

Le schede canoniche rimangono in characters/. Un dettaglio grafico non menzionato in quelle schede va considerato **proposta visiva**, non fatto narrativo.

**B-17 / Bi**: figura e proporzioni stabili della famiglia B; testa ovale, articolazioni meccaniche riconoscibili e spalla destra riparata con rivestimento differente **dopo** il capitolo 6. Non disegnare la riparazione prima dell'aggressione. Non disegnare lacrime su Bi nella scena finale.

**B-21**: stessa forma di base di B-17, ma è una diversa unità senza le sue memorie; **nessuna spalla riparata come quella di Bi**. L'eventuale codice identificativo deve rispettare la scena.

**Noah Carter**: postura concentrata, mani, quaderno di prove, lampada smontata. Non inventare una fisionomia diversa per ogni capitolo o attribuirgli come canoniche età e caratteristiche non dichiarate. Se appare un volto realistico, va fissato prima con una tavola approvata.

**Maya Bennett**: chiave d'ottone, documenti e gesto di stringere la chiave. Il volto, se necessario, deve provenire sempre da una stessa immagine di riferimento approvata. Non ridurre il personaggio a una figura generica che osserva Bi.

**Claire Foster**: prove, cartelle e responsabilità delle eccezioni. **Mei Lin**: verifiche di qualità e impianti. **Grace Walker**: presenza nella cura. **Helen Rivera**: pomodori e scelta di compagnia, mai ritratto passivo o stereotipato.

## Coerenza fra illustrazioni generate

1. Prima di scene realistiche creare una character sheet approvata per ciascun personaggio: fronte, profilo, tre quarti, proporzioni, indumenti ricorrenti e dettagli permanenti. Archiviarla con identificativo e versione sotto art/characters/.
2. Ogni nuova immagine con quel personaggio deve **riusare l'immagine-ancora**, non soltanto un prompt testuale. Confrontare anatomia, volto, capelli, dettagli della spalla e accessori contro l'ancora.
3. Registrare per ogni tavola capitolo, oggetto, personaggi presenti, riferimenti usati, versione e stato di revisione. Dove l'identità è essenziale, utilizzare ritocco, rig 2D/3D o una base unica; la sola generazione non garantisce identità perfetta.
4. Le tavole della prima edizione sono prevalentemente oggettuali e usano silhouette e forme **deterministiche**: il problema di cambiare faccia non si presenta. Possiamo aggiungere ritratti cinematografici più avanti, uno per volta, senza rompere la continuità.
5. **Nessuno spoiler iconografico**: non rivelare il progetto di sciopero prima del capitolo 33 o l'irreversibilità della fine di Bi prima del 35.

## Artefatti e verifica

`tools/artwork.py` genera una copertina e 35 tavole standard, poi applica gli override elencati in **`art/edition-assets.yml`**, dove ogni percorso è relativo a `art/`. L'override di copertina è `art/cover/bot-cover.png`, quello del capitolo 3 è `art/locations/valle-corta-sunset.png`. Altre immagini inserite in `art/` restano reference e non vengono pubblicate finché non sono collegate esplicitamente al capitolo adatto, per evitare spoiler o associazioni errate. `tools/build_docx.py` impagina mantenendo le proporzioni originali delle immagini. `tools/build.py` produce Markdown, EPUB illustrato, DOCX impaginato e archivio ZIP delle 36 immagini; la release converte il DOCX in PDF. `tools/check_edition.py` controlla che gli asset personalizzati siano presenti in ZIP, DOCX ed EPUB, oltre ai controlli su numero di immagini e pagine del PDF.

Controllo visivo obbligatorio: copertina, indice, apertura capitolo, tavola finale, ultimo paragrafo, caporali, accentate, numeri di pagina, assenza di testo tagliato, vedove/orfane e pagine bianche accidentali. Tutte le immagini devono essere coerenti con gli eventi del capitolo.

## Reference visive ancora da fissare — cast internazionale 2026-11-08

Le descrizioni e le origini in characters/malik-okafor.md, characters/anika-rao.md e characters/erik-solberg.md sono canoniche come profili narrativi; i volti non sono ancora approvati. Salvare future schede individuali con riferimenti stabili, rispettivamente in art/characters/malik-okafor.*, art/characters/anika-rao.*, art/characters/erik-solberg.*, scegliendo una sola estensione e aggiornando manifest e pipeline. Non usare ritratti stock di terzi come identità definitive né generare un volto differente per capitolo. L'origine culturale non determina stile, abiti, gesti o ruolo morale.
