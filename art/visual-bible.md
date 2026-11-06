# Identità visiva di BOT — direttiva per l'edizione illustrata

## Linguaggio grafico e qualità

Ogni capitolo termina con una **tavola iconica** in un linguaggio visivo coerente. Prima gli oggetti della storia: racchetta, cartellina, spalla riparata, sirena, pomodoro, orologio, lampada. Non sono poster generici. Il generatore riproducibile tools/artwork.py produce una copertina e 35 tavole con motivi editoriali stabili: un aggiornamento del PDF non cambia casualmente i tratti della scena.

Palette: blu notte #111F2C, ardesia #1C3444, avorio #F1EAD8, rame #DA9E5E, grigio azzurrato #89AEB8. Immagini di capitolo 16:9, copertina 2:3. Font del testo Liberation Serif e titoli Lato, tramite pacchetti liberi installati in build; mai incorporare file di font proprietari nel repository.

## Identità dei personaggi — ciò che non può cambiare

Le schede canoniche rimangono in characters/. Un dettaglio grafico non menzionato in quelle schede va considerato **proposta visiva**, non fatto narrativo.

**B-17 / Bi**: figura e proporzioni stabili della famiglia B; testa ovale, articolazioni meccaniche riconoscibili e spalla destra riparata con rivestimento differente **dopo** il capitolo 6. Non disegnare la riparazione prima dell'aggressione. Non disegnare lacrime su Bi nella scena finale.

**B-21**: stessa forma di base di B-17, ma è una diversa unità senza le sue memorie; **nessuna spalla riparata come quella di Bi**. L'eventuale codice identificativo deve rispettare la scena.

**Nico Valenti**: postura concentrata, mani, quaderno di prove, lampada smontata. Non inventare una fisionomia diversa per ogni capitolo o attribuirgli come canoniche età e caratteristiche non dichiarate. Se appare un volto realistico, va fissato prima con una tavola approvata.

**Nerea Dalmasso**: chiave d'ottone, documenti e gesto di stringere la chiave. Il volto, se necessario, deve provenire sempre da una stessa immagine di riferimento approvata. Non ridurre il personaggio a una figura generica che osserva Bi.

**Irene Valli**: prove, cartelle e responsabilità delle eccezioni. **Mei Lin**: verifiche di qualità e impianti. **Ada Serri**: presenza nella cura. **Teresa Marin**: pomodori e scelta di compagnia, mai ritratto passivo o stereotipato.

## Coerenza fra illustrazioni generate

1. Prima di scene realistiche creare una character sheet approvata per ciascun personaggio: fronte, profilo, tre quarti, proporzioni, indumenti ricorrenti e dettagli permanenti. Archiviarla con identificativo e versione sotto art/characters/.
2. Ogni nuova immagine con quel personaggio deve **riusare l'immagine-ancora**, non soltanto un prompt testuale. Confrontare anatomia, volto, capelli, dettagli della spalla e accessori contro l'ancora.
3. Registrare per ogni tavola capitolo, oggetto, personaggi presenti, riferimenti usati, versione e stato di revisione. Dove l'identità è essenziale, utilizzare ritocco, rig 2D/3D o una base unica; la sola generazione non garantisce identità perfetta.
4. Le tavole della prima edizione sono prevalentemente oggettuali e usano silhouette e forme **deterministiche**: il problema di cambiare faccia non si presenta. Possiamo aggiungere ritratti cinematografici più avanti, uno per volta, senza rompere la continuità.
5. **Nessuno spoiler iconografico**: non rivelare il progetto di sciopero prima del capitolo 33 o l'irreversibilità della fine di Bi prima del 35.

## Artefatti e verifica

tools/artwork.py genera cover.png e chapter-001.png ... chapter-035.png. tools/build_docx.py realizza il libro 6x9 pollici con copertina, indice, giustificazione, margini, testatine, pagine numerate e tavola a fine capitolo. tools/build.py produce Markdown, EPUB illustrato, DOCX impaginato e archivio ZIP delle 36 immagini. La release converte il nuovo DOCX in PDF.

Controllo visivo obbligatorio: copertina, indice, apertura capitolo, tavola finale, ultimo paragrafo, caporali, accentate, numeri di pagina, assenza di testo tagliato, vedove/orfane e pagine bianche accidentali. Tutte le immagini devono essere coerenti con gli eventi del capitolo.
