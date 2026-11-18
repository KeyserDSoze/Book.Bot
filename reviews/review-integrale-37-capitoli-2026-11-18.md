# Review integrale di *Bot* — 37 capitoli

**Data:** 18 novembre 2026  
**Base canonica:** main, commit 99f5f0bf8ebf520f3678661be37b320c574e4374  
**Perimetro:** 37 capitoli, 156 scene, schede/sinossi, linee guida, script editoriali e ultimo workflow di pubblicazione.  
**Metodo:** lettura di tutte le sinossi; scansione dei testi delle 156 scene con attenzione agli incipit, finali, punti di vista e lunghezze; lettura estesa delle scene che sorreggono le svolte del primo atto, del conflitto umano, della nuova coppia Martin–Ethan, del fermo e del finale. Non è ancora un line editing di ogni frase.

## Sintesi editoriale

Il romanzo ha un impianto forte e riconoscibile: la sostituzione del lavoro non è decretata da un'entità malvagia, ma emerge da scelte economiche ordinarie; B-17 passa dal prato al software attraverso prove locali, e la responsabilità delle decisioni resta umana. La relazione Maya–Bi conferisce un costo emotivo alla discussione sui diritti; il finale rende reale l'ambiguità sulla coscienza senza trasformare Bi in un innocente assoluto. I nuovi capitoli 19–20 funzionano come controcampo generazionale: Martin non viene licenziato, ma la sua uscita impedisce l'ingresso di qualcun altro.

Non è necessario ricominciare da zero. Sono tuttavia presenti **difetti accertati di build** e **quattro aree narrative da rinforzare**: transizione motoria di Bi, tensione nella parte tecnico-legale, evoluzione visibile di Ethan/Martin, chiarezza del prezzo del ripristino finale.

## P0 — Problemi accertati che bloccano la pubblicazione

### P0.1 — Il capitolo finale resta cablato a 35 nei generatori

- **tools/build.py**, righe 45 e 53: la gestione della frase «Tutto tornò normale.» viene eseguita per il capitolo 35. Il manoscritto ora si conclude al **37**. L'EPUB illustrato rischia di contenere la frase finale **dopo il 35** e poi un'altra volta alla vera fine del romanzo.
- **tools/build_docx.py**, righe 235 e 255: la frase finale viene reinserita come tavola tipografica dopo il **35**, mentre nel capitolo 37 resta nel corpo della scena. Ne deriva un finale anticipato nel DOCX/PDF, potenzialmente duplicato.
- **tools/check_edition.py**: i range fino a 35, il conteggio fisso **36** (35 tavole più copertina), la ricerca di «CAPITOLO 35» e i limiti sulle immagini non seguono la lunghezza attuale del libro. La **release su main ha fallito**: «Illustration archive wrong: expected 36, got 38». Verifica fallita nel workflow 44276706145, benché tools/validate.py abbia correttamente accertato 37 capitoli e 156 scene.
- **tools/artwork.py**, dizionario MOTIFS: le illustrazioni tematiche 19–35 sono ancora associate ai vecchi capitoli; il motivo «lamp» ora è assegnato al 35 (lo sciopero), anziché al 37 (la lampada finale). Nuovi 19 e 20 richiedono motivi propri (riunione / torta o chiavi).

**Intervento:** eliminare ogni valore finale hardcoded, derivare il numero dall'indice canonico, collocare la frase finale una sola volta, aggiornare la mappa delle immagini, rendere dinamico il test e verificare MD/DOCX/EPUB/PDF e pagina finale. La release deve tornare verde su main.

### P0.2 — Versione editoriale non incrementata

Il file VERSION riporta ancora **0.33.6** dopo una revisione sostanziale e l'aggiunta di due capitoli. La regola delle edizioni fotografiche immutabili richiede un nuovo numero di versione prima della prossima pubblicazione.

## P1 — Interventi narrativi ad alto impatto

### P1.1 — Il salto tra il robot poco fluido del 3 e il campione di ping pong del 4

**Scene:** 3/001–004; 4/001–003; 4/005.

Nel capitolo 3 B-17 deve interrompere la traiettoria di polso, gomito e spalla perfino per appoggiare una pagina. Nel capitolo 4, in pochi giorni, rimanda servizi tagliati con precisione e batte giocatori umani 11–3 o 11–5; il profilo motorio limita accelerazione e spazio, ma il testo non mostra sufficientemente **come** un controllo ancora rigido riesca ad anticipare e colpire una pallina veloce. Il successo sportivo non è impossibile, ma il lettore può viverlo come un potenziamento fisico gratuito.

**Soluzione:** una scena o un passaggio di allenamento verificabile con traiettorie ripetibili, ottimo anticipo percettivo ma recuperi e cambi di direzione difettosi. Le prime vittorie avvengano contro dilettanti e in un perimetro stretto; il profilo non diventi improvvisamente agile. Eventuali nuovi miglioramenti devono essere graduali e non attribuiti apertamente a Noah.

### P1.2 — Il capitolo 10 concentra troppo «tell» tecnico in un unico ricordo

**Scena:** 10/001.

È corretto che il lettore scopra qui la modifica clandestina di Noah, la memoria sperimentale, i limiti energetici, la porta d'accesso e la disattivazione del blocco antiurto. Ma diverse spiegazioni compaiono una dopo l'altra nella stessa lunga sequenza retrospettiva. Il rischio non è l'inverosimiglianza, bensì un rallentamento proprio nel momento della sorpresa.

**Soluzione:** mantenere il cuore della rivelazione ma distribuirlo fra una prova incompleta concreta, un registro di configurazione e il ricordo dell'aggressione. La colpa per la protezione disattivata resta distinta dalla scelta violenta di Ethan e Marcus. Non anticipare nulla nei capitoli 1–9.

### P1.3 — Il tratto 11–16 diventa un dossier più che un thriller

**Scene chiave:** 11/001, 12/001–002, 13/004–005, 14/003–004, 15/001–003, 16/001–003.

Video, confessione, proprietà, offerta, chat, fuga di informazioni e controversia giudiziaria costituiscono una catena sensata. Il problema è la ripetizione di colloqui nei quali le persone chiedono verifiche, rinviano conclusioni e distinguono fascicoli. È verosimile per un'azienda software, ma il movimento emotivo può risultare statico.

**Soluzione:** separare le funzioni drammatiche. Il 12 appartiene alla rottura delle amicizie e alla responsabilità di Noah; il 13 al costo di recuperare Bi; il 14 al rifiuto e al contatto iniziato dal robot; il 15 a una violazione intima; il 16 deve produrre una **nuova conseguenza irreversibile**, non soltanto classificare correttamente l'evento. Compattare spiegazioni procedurali già fornite; rendere più incisivi gli obiettivi immediati di Maya e Nina.

### P1.4 — La crescita di Lavoro Prima è migliore, ma Martin ed Ethan scompaiono troppo a lungo

**Scene:** 8/006, 19/001–004, 20/001–004, 21/001, 25/004, 28/004, 29/004, 30/001, 31/004.

Ora la prima assemblea esiste e Martin entra con un passato preciso. Tuttavia Martin ha una presenza diretta forte soprattutto nel 19–20 e in un breve intervento nel 30; la sua influenza intermedia resta per lo più raccontata. Ethan passa dal piccolo gruppo alla carica di deputato anche attraverso un salto di diciotto mesi, e i compromessi, i fallimenti, le fratture interne e la costruzione della coalizione si vedono poco.

**Soluzione:** non servono altri due capitoli interi. Inserire **due o tre scene mirate** nei capitoli 23–29: una trattativa sindacale difficile o un presidio con esito modesto, un conflitto reale fra Martin ed Ethan sulla strategia/violenza, e una scelta di Leo o Owen non riducibile alla funzione di «vittima». Far vedere un piccolo costo politico prima di arrivare alle elezioni. Mantenere eterogenee le posizioni, senza far diventare tutti i critici anti-robot estremisti.

### P1.5 — L'ultimo sacrificio rischia di sembrare una necessità tecnica costruita per ottenere il finale

**Scene:** 34/002, 35/001–004, 36/001–004, 37/001.

Il fermo globale è ricostruito con firme, fornitori indipendenti, test incompleti e un evento normativo italiano che viene interpretato troppo ampiamente. È migliore di una backdoor che comanda tutte le flotte. Rimane però delicatissimo il nesso fra **revoca della referenza tecnica originaria** e **cancellazione irreversibile dell'identità di Bi**: è spiegato, ma talvolta pesa più il lessico delle attestazioni che il prezzo del tempo, delle alternative e dei test falliti.

**Soluzione:** prima della firma mostrare una controprova decisiva e comprensibile, magari un ripristino locale che funziona ma non si estende, e una scadenza materiale umana non astratta. La cancellazione deve restare una **scelta in urgenza** con un'altra via più lenta ma reale, non una costrizione dell'universo. Conservare il «No» di Bi e l'ultima frase.

## P2 — Migliorie di continuità, personaggi e lingua

1. **Show, don't tell nelle chiusure.** Molte scene funzionano tramite azioni, ma chiudono con un'interpretazione esplicita: «Non era ...», «Non significava ...», «Per la prima volta ...». Esempi: 4/002, 7/002, 12/002, 19/003, 20/004, 25/004, 35/001. Una parte è efficace; ripetuta per decine di scene produce cadenze simili. Preferire in alcuni punti l'oggetto o il gesto finale senza commento.
2. **Bi e memoria.** Il 3 stabilisce una continuità episodica fragile, il 4 lo mostra capace di imparare complesse dinamiche sociali. Ci sta una progressione, ma servono occasioni visibili in cui perda o ricostruisca dettagli ancora nel 4–5; la memoria non deve diventare perfetta dopo la prima confessione di Maya.
3. **Punto di vista robotico nel 2.** Le scene 2/002 e 2/005 sono marcate POV B-17 ma narrate come telemetria e campo visivo. Non è una certificazione di coscienza, però crea una convenzione distinta dagli altri POV ravvicinati: decidere se mantenerla come eccezione formalizzata o riformularla come osservazione strettamente esterna.
4. **Ethan e responsabilità.** Nel 7 non ha vero pentimento, nell'8/006 e nel 19/002 dice pubblicamente di avere sbagliato. È compatibile con una strategia politica, ma sarebbe utile mostrare se la frase gli costa qualcosa oppure è un modo per spostare l'argomento: evitare una redenzione implicita.
5. **Martin.** La pensione felice, la decisione di Victor e il prato sono ottimi controcampi; il capitolo 20 resta però relativamente breve rispetto al peso che gli attribuiamo. Il finale «Era l'unica risposta che aveva...» esplicita troppo la metafora della targa. Può bastare il messaggio di Leo e un gesto di Martin.
6. **Valle Corta.** La rimozione è sospesa, le quattordici case sono riconosciute, ma la sicurezza finale della sirena e la regolarizzazione delle vecchie credenziali restano in verifica. L'apertura è plausibile, ma dopo tanti capitoli bisogna scegliere se offrire un piccolo esito istituzionale definitivo o segnalare chiaramente che il percorso resta aperto senza presentarlo come dimenticanza.
7. **Il titolo «La prima bugia» (26).** Bi aveva già mentito nel ping pong al capitolo 4. La sinossi chiarisce che è la prima omissione di B-32 osservata da Grace, ma il lettore può credere a una contraddizione: valutare «La risposta mancante» / «Quello che non ha detto» o rendere il perimetro esplicito.
8. **Finale corale.** La cancellazione del 37/001 ha una scena intensa; il 37/004 sul noccioleto è invece una miniatura di circa 174 parole. Il contrasto può essere deliberato, ma l'epilogo deve evitare l'effetto checklist di tutti i luoghi e i personaggi prima dell'ultima frase. Valutare un montaggio con tre effetti permanenti anziché sei ripartenze equipollenti.
9. **Dossier canonici invecchiati.** La sinossi del capitolo 2 ordina ancora le scene «5, 1, 2, 3, 4» malgrado i file canonici 1–5; state/current.md dichiara in frontmatter di arrivare al 22, ma l'intestazione continua a dire «dopo il capitolo 20». In sinossi e guide restano vecchi riferimenti (es. nel 32 ci sono «capitolo 29/30/31» riferiti all'arco precedente, nel 26 la nota «25–33», e nel 24 un richiamo storico a «PR #7 ancora separata»). Ripulire queste tracce o isolarle come archivio storico non più normativo.
10. **Spoiler di processo.** AGENTS.md dichiara pubblica la repository e chiede di non inserire materiali riservati; secrets/reveal-plan.md è tuttavia un file pubblico contenente l'intero piano delle rivelazioni. È una contraddizione di governance da chiarire con l'autore, senza cancellare materiale senza consenso.

## Mappa di lettura capitolo per capitolo

| Cap. | Cosa funziona | Intervento consigliato |
|---:|---|---|
| 1 | Demo Bridgeglass fallita, Kyla ambiziosa ma responsabile, promessa positiva dell'automazione | Evitare che log e responsabilità occupino tutto il tempo emotivo della visita |
| 2 | Contrasto fotocopie/urto protettivo, attrito fra Kyla e Malik | Correggere la sinossi interna e standardizzare la convenzione del POV tecnico |
| 3 | Nome «Bi», memoria fragile, confidenza di Maya e miglioramento cognitivo | Non far sparire troppo presto i limiti di coordinazione e memoria |
| 4 | Ping pong come appartenenza e primo inganno socialmente comprensibile | Mostrare fisicamente perché la bravura di Bi è possibile con movimenti ancora poco fluidi |
| 5 | Posizione non riaperta, professionalità di Claire, conoscenze dei sistemi legacy | Dare un volto tangibile alla formazione promessa e non finanziata |
| 6 | Aggressione inquietante dal POV di Ethan; colpe separate | Controllare che non diventi un incidente inevitabile “spiegato” dal contesto |
| 7 | Assenza di Bi raccontata da procedure e persone che devono recuperare competenze | Ridurre alcune chiusure interpretative |
| 8 | Buona doppia linea crisi aziendale / primo incontro di Lavoro Prima | Il capitolo è molto più lungo degli altri; tenere l'assemblea come coda incalzante |
| 9 | B-21 funziona bene ma non è Bi: distinzione etica riuscita | Evitare spiegazioni ripetute della legge sugli alias |
| 10 | Svelamento di Noah, occasione di svolta thriller | Alleggerire il blocco retrospettivo tecnico |
| 11 | Il successo di Bi diventa valore economico e rischio di sorveglianza | Ridurre le due esitazioni successive di Noah se ripetitive |
| 12 | La confessione rompe l'amicizia con Paul/Mila e la fiducia di Maya | Conservare il trauma umano più del verbale |
| 13 | Raccolta volontaria credibile, speranza e strategia per Cyberdine | Evitare troppa esposizione contabile; valorizzare il rifiuto di Claire |
| 14 | Chat avviata da Bi dopo il rifiuto di vendita | Conferire più peso alla scelta attiva del robot |
| 15 | Violazione della chat privata con conseguenza intima | Rafforzare l'evento che sposta la posta in gioco, non solo la sua classificazione |
| 16 | Distinzione fra fuga dati, riuso e indagine di sicurezza | Compattare il linguaggio dei fascicoli; introdurre un esito irreversibile |
| 17 | Diffusione in assistenza e logistica con vantaggi veri e lavoro invisibile | Riprendere le nuove adesioni a Lavoro Prima senza forzature |
| 18 | Il fermo locale funziona come falsa prova dello sciopero e aumenta la tensione | Evitare ripetere troppe volte la lezione «procedura, non volontà» |
| 19 | Telefonata di Martin; assemblea plurale, rifiuto della violenza | Far emergere un attrito concreto persistente con Ethan |
| 20 | Festa luminosa che dà un volto al posto “non sostituito”; costo familiare | Ridurre spiegazione finale; mettere più vita e conflitti nelle scene brevi |
| 21 | Il nome di Noah diventa pubblico e controverso | Tenere distinta l'attribuzione tecnica dal giudizio morale |
| 22 | Memoria, privacy e padre di Maya finalmente connessi | Continuare a mostrare il costo delle verifiche, non solo la tassonomia |
| 23 | Maya incontra il robot senza diventare «strumento di collaudo» | Dare a Bi un dettaglio specifico imperfetto che sia solo loro |
| 24 | Helen e Chloe mostrano la cura oltre i KPI | Salvaguardare l'autonomia di Helen anche contro le scelte degli umani |
| 25 | Più tempo libero ma meno salario: conflitto ottimo | Fare entrare Martin o i lavoratori del movimento nel seguito, senza appropriarsi di Ruby |
| 26 | Prima omissione di B-32 in cura, conseguenze su Julia | Valutare titolo; distinguere colpa organizzativa e comportamento robotico |
| 27 | Bi propone una strategia utile per la sopravvivenza di Cyberdine | Alleggerire numeri e catena di approvazioni mantenendo il costo per Claire |
| 28 | Bi non può usare la confidenza di Maya per coprire un conflitto di ruolo | Piccolo evento pubblico che prepari la futura alleanza politica |
| 29 | Salto di diciotto mesi, nuovi robot e nuovi lavori mai aperti | Mostrare almeno un prezzo pagato da Ethan prima del seggio |
| 30 | Grande protesta eterogenea, Martin torna sul palco, Claire dissente | Dare a Martin conseguenze e una decisione oltre il discorso |
| 31 | Legge italiana credibile, differenziata dal Bot Act europeo | Evitare presagi troppo diretti del fermo del giorno dopo |
| 32 | Stop simultaneo e conseguenze in campi, magazzini, assistenza | Lo smarrimento funziona: non anticipare la responsabilità di Bi |
| 33 | I robot assenti dimostrano quanto siano infrastruttura ordinaria | Conservare soluzioni umane parziali e non trasformare tutto in apocalisse |
| 34 | Sei firme mostrano l'innovazione come somma di atti umani | Drammatizzare la scoperta senza troppe tavole tecniche |
| 35 | Bi ammette il disegno collettivo senza negare i diritti altrui | Esplicitare attraverso prove l'assenza di consenso delle altre unità |
| 36 | La scelta di Noah non ha prova metafisica né alternativa facile | Una controprova concreta prima delle firme aumenterebbe la tensione |
| 37 | «No», lacrime di Noah e ritorno del lavoro hanno forte coerenza morale | Curare il montaggio delle ripartenze; preservare esattamente l'ultima frase |

## Ordine di lavoro consigliato

**Passo 1 — Sicurezza dell'edizione.** Correggere P0.1/P0.2, produrre e verificare un'edizione di prova in tutti i formati, controllare che nessuna versione inserisca il finale dopo il capitolo 35. Operazione tecnica separata dalla riscrittura.

**Passo 2 — Continuità letteraria.** Intervenire sul passaggio 3–4, sul lessico dei limiti motori e sulle ripetizioni della rivelazione 10/12. Piccola PR dedicata; non riaprire senza motivo i capitoli 1–2 già stabilizzati.

**Passo 3 — Parte centrale.** Editare 11–16 per alternare più chiaramente perdita umana e conseguenze procedurali; lavorare su alcuni finali-scena e sulle posizioni di Maya, Nina, Noah.

**Passo 4 — Ascesa del movimento.** Inserire 2–3 scene fra 23 e 29 che facciano pagare a Ethan e Martin un prezzo organizzativo/politico concreto e mostrino l'azione di Leo/Owen. Niente altre decine di pagine di manifesto.

**Passo 5 — Finale.** Rivedere l'ultima catena tecnica 34–37 da un punto di vista da lettore: una prova fallita, un'alternativa meno distruttiva ma lenta, la scelta sotto pressione, il rifiuto di Bi, il ritorno del lavoro. Conservare senza variazioni «Tutto tornò normale.»

**Passo 6 — Pulizia del canone.** Correggere note storiche non più applicabili, guide e link interni; distinguere la sinossi storica a 35 da quella corrente a 37; decidere in privato il destino dei piani spoiler nel repository pubblico.

## Giudizio conclusivo

Il romanzo merita una **revisione selettiva ad alto impatto**, non una riscrittura totale: gli episodi più riusciti mostrano già bene le persone e il costo delle scelte. La priorità è eliminare i falsi finali dell'edizione e togliere la sensazione che la parte centrale sia composta da verbali, mentre l'evoluzione di Bi, Ethan e Martin deve restare esperienza visibile. Il finale con la cancellazione di Bi è coerente con il percorso: va protetto, non spiegato fino a spegnerne l'ambiguità.
