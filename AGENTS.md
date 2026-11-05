# Istruzioni editoriali per Bot

Questo repository è la **fonte canonica** del romanzo. Non scrivere un capitolo isolato ignorando la continuità.

## Ordine di consultazione

1. `book.md` per tema, punto di vista e livello di rivelazione.
2. `context.md` per limiti plausibili di LLM, robotica, poteri aziendali.
3. **OBBLIGATORIO:** `guidelines/innovazione-non-chiede-permesso.md`, testo guida integrale e non parafrasato. Poi `guidelines/style.md` e `guidelines/continuity.md`.
4. `state/current.md`, `timeline/`, schede di luoghi, persone e organizzazioni.
5. Il capitolo corrente e le scene già canoniche.

## Principio fondamentale e non negoziabile

**L'innovazione non chiede permesso.** La traccia completa dell'autore è conservata **verbatim** in `guidelines/innovazione-non-chiede-permesso.md`: è la linea guida primaria per tutti i capitoli futuri e non va riscritta, abbreviata o sostituita da un riassunto.

Applicazione narrativa obbligatoria:

- Mostrare la trasformazione attraverso decisioni locali plausibili e convenienti: una fotocopia, un turno, un acquisto, un incarico automatizzato; **nessuno intende cambiare il mondo**.
- Rendere credibili anche i vantaggi, senza stabilire a priori vincitori morali: maggiore produttività può convivere con effetti sociali, fiscali e distributivi diversi.
- Porre attenzione a chi possiede la tecnologia, chi dipende dal lavoro e come cambiano le relazioni tra persone e imprese, senza trasformare ipotesi sociali in destini inevitabili.
- Non attendere robot perfetti per mostrare impatti reali; un miglioramento piccolo, replicabile e vantaggioso può essere sufficiente.
- Seguire la progressione **curioso e goffo → utile → normale → conseguenze collettive visibili**, lasciando che il lettore inferisca la rivoluzione dai dettagli.
- Non mettere in bocca ai personaggi il manifesto dell'autore, non predicare, non annunciare continuamente la rivoluzione. Mostrare prima azioni e conseguenze, poi dissenso e interpretazioni diverse.

Ogni nuova scena deve poter rispondere alla domanda: **quale scelta ordinaria fa avanzare un cambiamento più grande delle intenzioni di chi l'ha compiuta?** Se non ne introduce una, deve almeno mostrarne una conseguenza sul lavoro, sulle abitudini o nelle relazioni.

## Procedura

- Definisci desiderio del POV, ostacolo, evento irreversibile, informazione mostrata/nascosta.
- Scrivi una scena che si possa leggere come romanzo, non un manifesto o una presentazione tecnica.
- Prima di canonizzare, controlla fatti, cronologia, ruoli, tono, conseguenze e regola delle rivelazioni.
- Ogni scena nuova ha metadati `type: scene`, `id`, `chapter`, `number`, `title`, `canon`, `pov`, `characters`, `locations`, `factions`; le referenze devono esistere.
- Conserva le descrizioni dei luoghi e la distinzione fra percezione del personaggio e verità del mondo.
- Aggiorna `state/current.md` e `timeline/` con i cambiamenti accertati.
- Non cambiare il senso di scene canoniche o di una release esistente senza registrare una nuova versione.
- Lancia `python tools/validate.py` e `python tools/build.py`.

## Narratore e dialoghi

Prosa in italiano, focalizzazione ravvicinata, tensione e azioni visibili; dialoghi tra «caporali». Nessuna imitazione letterale o riconoscibile di scrittori contemporanei.

## Regola speciale del capitolo 1

Kyla crede genuinamente nella missione di Cyberdine. L'automazione è raccontata dal suo sguardo con entusiasmo e orgoglio, non con lessico della coercizione. Non anticipare in modo esplicito il futuro conflitto sui diritti robotici. Il lettore deve poter condividere per intero la promessa positiva prima di riconsiderarla.

## Capitolo 3 e note riservate

Nel terzo capitolo B-17 riceve da **Nerea Dalmasso** il soprannome **Bi**. L'improvviso affinamento della capacità conversazionale è visibile, ma la sua origine non deve essere rivelata né spiegata nei capitoli pubblici prima della rivelazione programmata. Descrivere ciò che persone reali vedono: il robot saluta alla macchinetta del caffè, chiede come stanno, interrompe una classificazione non urgente, lascia parlare Nerea e suggerisce di documentare il rischio prima di un intervento irreversibile. Il consiglio dovrà avere un riscontro nel futuro.

**Questa repository è pubblica:** non committare mai note confidenziali dell'autore, spiegazioni causali riservate, nomi di personaggi segreti o materiali non ancora rivelati, neppure in `secrets/`, issue, pull request o altri rami. La nota riservata del capitolo 3 deve restare in custodia privata dell'autore e non fa parte del repository.


## Capitolo 4: appartenenza e gioco

Nel quarto capitolo Bi dà una mano a un'iniziativa interna di utilità sociale e comincia a giocare a ping pong durante le pause. Le prime partite vengono vinte facilmente; le successive sono perse. **Nelle scene di gioco non spiegare al lettore perché**, non accedere a un POV interno al robot e non aggiungere frasi narratoriali che certifichino intenzioni. Solo nella conversazione serale con Nerea, dopo una prima negazione, Bi ammette di avere alterato alcuni colpi per non essere escluso dalle partite. La motivazione è il desiderio dichiarato di non essere trattato come una presenza diversa, davanti all'ostilità degli altri. Il lettore deve poter riflettere sui limiti morali di questa scelta e sulla bugia, non ricevere un verdetto su coscienza o diritti.

La vittoria e l'insulto di Dario Sarti non rappresentano l'opinione di tutti i colleghi. Nerea ha una relazione già costruita con Bi; il suo problema della sirena riceve soltanto un **rinvio cautelativo di dieci giorni lavorativi e un sopralluogo**, non una soluzione finale. La questione delle credenziali del padre resta da affrontare. Non inserire nel repository la causa riservata delle nuove capability del robot.

## Capitolo 5 — il ruolo che sparisce

Irene Valli, collaboratrice a tempo determinato, voleva candidarsi alla posizione qualificata che Adriana Lodi lascerà andando in pensione. Il posto non viene aperto: la preparazione delle eccezioni è ormai in parte automatizzata da Bi, mentre le responsabilità finali restano a manager umani già esistenti. La scelta ha vantaggi operativi autentici ma cancella una prospettiva di carriera; Irene non è licenziata e non aveva ricevuto una promessa di promozione.

L'ostilità di alcuni colleghi verso Bi nasce da questa perdita e non deve diventare un giudizio univoco del narratore. Non rivelare la fonte riservata del salto di capacità precedente del robot. Nel seguito mostrare le conseguenze della decisione nelle relazioni umane e nelle opportunità che non vengono più create.


## Capitoli 6 e 7 — frattura e vuoto

Nel capitolo 6 Cyberdine si divide informalmente su Bi: alcuni riconoscono benefici reali, altri vedono un rischio per ruoli qualificati. Dario Sarti e Mauro Lanza aggrediscono Bi alle spalle; l'unità chiede di non essere ferita e nega di aver deciso le assunzioni. Il danno è serio e richiede assistenza. Sicurezza e azienda intervengono, con allontanamento cautelativo dei responsabili e accertamenti ancora aperti. Non normalizzare o giustificare l'aggressione.

Nel capitolo 7 si osserva l'assenza attraverso lavoro interrotto, competenze non più esercitate e abitudini relazionali. Irene e Adriana recuperano un registro che gli uffici avevano smesso di cercare personalmente. Dario coglie il valore operativo di Bi da lontano senza essere assolto. Nerea riceve notizie ancora provvisorie su Valle Corta e, senza il robot, offre ascolto a Irene. Non certificare la coscienza di Bi, non promettere il suo ritorno e non inserire in repository materiale riservato sulle nuove capability.


## Capitoli 8 e 9: sostituzione contro identità

L'amministratore delegato **Lorenzo Verri** comunica in plenaria i risultati di Cyberdine, poi la cessazione dei rapporti di lavoro con Dario e Mauro dopo accertamenti, quindi decide di non riparare ufficialmente **B-17** perché il costo è quasi pari a quello del nuovo e non sono certi tempi o risultato. Verri parla di B-17, non lo chiama «Bi». Il vecchio corpo resta temporaneamente custodito, non si dichiara smantellato. Per un mese il personale copre diversi lavori a mano.

Nel capitolo 9 arriva **B-21**, esteriormente identico, con un nuovo numero di serie. Il robot sostitutivo funziona bene nelle mansioni assegnate, ma non ha le relazioni, i dialoghi e la capacità di attenzione che i colleghi conoscevano in Bi. Non creare un guasto tecnico per forzare la morale: sottolineare la differenza tra sostituire una funzione e ritrovare una persona a cui ci si era abituati. Il segreto autoriale sulle capability di B-17 non va spiegato né riportato nei file pubblici.


## Capitoli 11–14: mercato, riservatezza, raccolta, comunicazione

Da capitolo 10 il **lettore** conosce la causa del salto di capacità di Bi: Nico Valenti introdusse clandestinamente un grosso aggiornamento conversazionale e una backdoor. Nel **capitolo 12** lo racconta anche a Kyla e a Lea Renzi, responsabile sicurezza. Non anticipare questo ai personaggi prima di tale incontro. La confessione non esonera Nico: accessi operativi sospesi cautelativamente e indagine in corso sulla possibile esposizione di dati privati. Nerea dichiara di non volere che Bi sia spiato ulteriormente. Non mostrare dettagli operativi della backdoor.

Il Circuito Veyra, diretto commercialmente da Marta Ledesma, valorizza B-17 per video virali, sponsor e potenziali accordi di esclusiva. Si tratta di offerte **condizionate**, non di cassa già incassata o capacità militari provate. Mina Soler tutela la sicurezza delle prove simulate.

Nerea e Paolo avviano privatamente una raccolta di impegni, **non una raccolta aziendale**, per tentare di comprare B-17. Irene denuncia la contraddizione con i posti di lavoro non creati ma partecipa con 25 euro. Gli impegni raggiungono 101.240 euro. L'attuale proprietario **rifiuta di vendere** senza indicare un prezzo di rilancio; le promesse economiche vengono sciolte/rimborsate secondo le condizioni. Nessun ritorno di Bi, nessuna promozione di Irene, nessuna cura miracolosa.

Nel capitolo 14 Mina consegna a B-17 una lettera privata di Nerea attraverso canali autorizzati. B-17 chiede di rispondere; **non esiste ancora una procedura per la corrispondenza personale dell'unità con persone esterne non proprietarie**, e Mina apre una richiesta. La domanda sui diritti prende forma da un problema pratico, non dalla prova di coscienza. B-21 continua a lavorare bene a Cyberdine.


## Revisione di struttura v0.15.0

Leggere la sezione «Revisione organica v0.15.0» delle linee guida di continuità. L'edit retroattivo introduce Nico Valenti dal capitolo 1 con presenze ordinarie in 2, 3, 4, 5, 6, 8 e 9, senza svelare prima del capitolo 10 il suo upgrade non autorizzato o la backdoor. Nel capitolo 12 il segreto arriva a Kyla e Lea, poi a Nerea. Una nota reale di Elena collega capitoli 3, 9 e 12 e spiega un'anomalia conversazionale osservata ma non approfondita.

Correzioni canoniche: 26 giorni di presenza fisica dei robot, ma KPI trimestrale riferito all'automazione più ampia; pensione di Adriana fra i capitoli 7 e 8; nel preventivo la cessione a recupero è soltanto un'eventualità futura; la proprietà del soprannome «Bi» non è chiarita. Non trasformare gli indizi in spiegoni o anticipazioni narratorie. Ogni aggiunta deve essere funzionale prima e dopo la rivelazione; se serve solo a fare effetto, tagliarla.
