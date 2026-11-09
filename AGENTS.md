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

Nel terzo capitolo B-17 riceve da **Maya Bennett** il soprannome **Bi**. L'improvviso affinamento della capacità conversazionale è visibile, ma la sua origine non deve essere rivelata né spiegata nei capitoli pubblici prima della rivelazione programmata. Descrivere ciò che persone reali vedono: il robot saluta alla macchinetta del caffè, chiede come stanno, interrompe una classificazione non urgente, lascia parlare Maya e suggerisce di documentare il rischio prima di un intervento irreversibile. Il consiglio dovrà avere un riscontro nel futuro.

**Questa repository è pubblica:** non committare mai note confidenziali dell'autore, spiegazioni causali riservate, nomi di personaggi segreti o materiali non ancora rivelati, neppure in `secrets/`, issue, pull request o altri rami. La nota riservata del capitolo 3 deve restare in custodia privata dell'autore e non fa parte del repository.


## Capitolo 4: appartenenza e gioco

Nel quarto capitolo Bi dà una mano a un'iniziativa interna di utilità sociale e comincia a giocare a ping pong durante le pause. Le prime partite vengono vinte facilmente; le successive sono perse. **Nelle scene di gioco non spiegare al lettore perché**, non accedere a un POV interno al robot e non aggiungere frasi narratoriali che certifichino intenzioni. Solo nella conversazione serale con Maya, dopo una prima negazione, Bi ammette di avere alterato alcuni colpi per non essere escluso dalle partite. La motivazione è il desiderio dichiarato di non essere trattato come una presenza diversa, davanti all'ostilità degli altri. Il lettore deve poter riflettere sui limiti morali di questa scelta e sulla bugia, non ricevere un verdetto su coscienza o diritti.

Il sabato seguente Maya perde contro Bi 11–6 in una partita senza favori, gli stringe la mano e, solo dopo avergli chiesto il permesso, spiega al gruppo che Bi aveva perso apposta. Bi conferma che non falsificherà più il proprio gioco. Paul, Mila e altri accettano la sfida di migliorare anche quando perdono; Ethan sostiene che le proprie vittorie fossero autentiche, non crede alla confessione e si infuria quando Maya ignora le sue proteste per rivolgersi a Paul e Mila. Non scrivere in seguito che Ethan abbia già accettato la spiegazione. Nel capitolo 7 la perdita di Bi interrompe un obiettivo sportivo condiviso, non un gioco che aveva già cessato di interessare tutti.

La vittoria e l'insulto di Ethan Blake non rappresentano l'opinione di tutti i colleghi. Maya ha una relazione già costruita con Bi; il suo problema della sirena riceve soltanto un **rinvio cautelativo di dieci giorni lavorativi e un sopralluogo**, non una soluzione finale. La questione delle credenziali del padre resta da affrontare. Non inserire nel repository la causa riservata delle nuove capability del robot.

## Capitolo 5 — il ruolo che sparisce

Claire Foster, collaboratrice a tempo determinato, voleva candidarsi alla posizione qualificata che Margaret Ellis lascerà andando in pensione. Il posto non viene aperto: la preparazione delle eccezioni è ormai in parte automatizzata da Bi, mentre le responsabilità finali restano a manager umani già esistenti. La scelta ha vantaggi operativi autentici ma cancella una prospettiva di carriera; Claire non è licenziata e non aveva ricevuto una promessa di promozione.

L'ostilità di alcuni colleghi verso Bi nasce da questa perdita e non deve diventare un giudizio univoco del narratore. Non rivelare la fonte riservata del salto di capacità precedente del robot. Nel seguito mostrare le conseguenze della decisione nelle relazioni umane e nelle opportunità che non vengono più create.


## Capitoli 6 e 7 — frattura e vuoto

Nel capitolo 6 Cyberdine si divide informalmente su Bi: alcuni riconoscono benefici reali, altri vedono un rischio per ruoli qualificati. Noah inventa scherzosamente **«bot-piattisti»**, paragonando ai terrapiattisti gli avversari più assoluti dei robot; Ethan sente la battuta e il gruppo la riutilizza polemicamente. **Non** usare il termine per screditare automaticamente ogni lavoratore critico verso l'automazione. Ethan Blake e Marcus Reed aggrediscono Bi alle spalle; l'unità chiede di non essere ferita e nega di aver deciso le assunzioni. Il danno è serio e richiede assistenza. Sicurezza e azienda intervengono, con allontanamento cautelativo dei responsabili e accertamenti ancora aperti. Non normalizzare o giustificare l'aggressione.

Nel capitolo 7 si osserva l'assenza attraverso lavoro interrotto, competenze non più esercitate e abitudini relazionali. Claire e Margaret recuperano un registro che gli uffici avevano smesso di cercare personalmente. Ethan, sospeso, **festeggia l'assenza di Bi** e sostiene che il codice umano fosse migliore e che grazie a lui l'azienda potrà lavorare in pace: è la sua interpretazione autoassolutoria, **non un verdetto del narratore**. Accetta di registrare la propria responsabilità fattuale senza chiedere perdono. I colleghi che rimangono devono invece recuperare lavoro e competenze reali. Maya riceve notizie ancora provvisorie su Valle Corta e, senza il robot, offre ascolto a Claire. Non certificare la coscienza di Bi, non promettere il suo ritorno e non inserire in repository materiale riservato sulle nuove capability.


## Capitoli 8 e 9: sostituzione contro identità

L'amministratore delegato **Victor Cole** apre la plenaria immediatamente con **ricavi di competenza +11%** presentati come buon risultato. È vero, ma gli **incassi sono -9%**, le nuove commesse diminuiscono e concorrenti AI-native più giovani e agili vincono gare che Cyberdine non riesce più a competere a parità di costi. Gavin e Claire lo commentano sottovoce e il lettore comprende la **crisi di liquidità**. Solo più tardi Victor annuncia la cessazione dei rapporti con Ethan e Marcus e decide di non riparare **B-17**: il preventivo è quasi pari al costo di un'unità completa nuova, ma la società non ha cassa sufficiente per nessuna delle due soluzioni. Cole parla di B-17, non lo chiama «Bi». Il vecchio corpo resta temporaneamente custodito, non si dichiara smantellato. Per un mese il personale copre diversi lavori a mano.

Cyberdine ripiega su un **B-21 ricondizionato di fascia base a noleggio operativo**, per un costo iniziale e un canone molto inferiori. Nel capitolo 9 arriva questa unità, **esteriormente identica** con numero di serie diverso, ma con calcolo e funzioni ridotti: sa fare **poche mansioni** di trasporto, rifornimento e semplici operazioni di fotocopia, non prepara dossier complessi e non svolge le verifiche software e fisiche che Bi aveva iniziato ad affiancare. I documenti vengono preparati da agenti AI e verificati da programmatori/QA umani. Il sostituto fa bene i pochi compiti autorizzati, ma non ha le relazioni, i dialoghi e la capacità di attenzione che i colleghi conoscevano in Bi. Non creare un guasto tecnico per forzare la morale: la differenza funzionale è **contrattuale e di costo**, non un difetto del robot, e si somma alla differenza tra ripristinare poche funzioni e ritrovare una presenza amata. Nel 9/004 Maya chiama B-21 «Bi» due volte senza risposta; il robot si volta solo quando sente «B-21» e cita l'articolo 4 del **Bot Act europeo**, regolamento esclusivamente *fittizio*, con negazione legale di anima/persona e divieto di soprannomi riconosciuti dal software. La legge non certifica la realtà metafisica del robot e non vieta agli esseri umani di pronunciare un soprannome: vieta che esso diventi un identificativo della macchina. La stessa regola vale in 21/004. Leggere `guidelines/bot-act-europeo.md`. Il segreto autoriale sulle capability di B-17 non va spiegato né riportato nei file pubblici.


## Capitoli 11–14: mercato, riservatezza, raccolta, comunicazione

Dal capitolo 10 il **lettore** conosce la causa del salto di capacità di Bi: Noah Carter introdusse clandestinamente un grosso aggiornamento conversazionale e una backdoor. Il cap. 10 termina senza mostrare se Noah spedisca la mail a Kyla; la scelta canonica è che **non la invia**. Nel cap. 11 appaiono due video virali anonimi con materiale sensoriale di B-17; **non attribuirne ancora la pubblicazione a Noah nel testo narrativo**. Nel **cap. 12** Noah lo racconta per primo a **Paul Turner e Mila Novak**, colleghi considerati amici: ammette upgrade, backdoor, registrazione e pubblicazione anonima dei video per mostrare cosa accade a Veyra e che Bi è operativo. I due, sentendosi potenzialmente spiati, riferiscono a Kyla e Leah Rosen. Seguono confessione formale, indagine e sospensione degli accessi. Nel **cap. 13** Noah viene licenziato per le proprie violazioni, dopo le verifiche e le controdeduzioni. Nel **cap. 17** la nuova Veyra Labs, distinta da Lanter e collegata al proprietario di Bi, lo assume sotto il nome professionale pubblico **Evan North**: la sua identità anagrafica e i suoi precedenti sono noti ai responsabili, e non ottiene un accesso occulto o un diritto a copiare le memorie di B-17. Maya chiede in seguito che Noah non osservi la propria sessione con Bi. Le capacità sviluppate sui nuovi robot non costituiscono un clone del Bi originale. La confessione non esonera Noah e non mostrare dettagli tecnici replicabili della backdoor.

Il Circuito Veyra, diretto commercialmente da Amara Ortiz, valorizza B-17 per video virali, sponsor e potenziali accordi di esclusiva. Si tratta di offerte **condizionate**, non di cassa già incassata o capacità militari provate. Nina Solis tutela la sicurezza delle prove simulate.

Maya e Paul avviano privatamente una raccolta di impegni, **non una raccolta aziendale**, per tentare di comprare B-17. Claire denuncia la contraddizione con i posti di lavoro non creati ma partecipa con 25 euro. Gli impegni raggiungono 101.240 euro. L'attuale proprietario **rifiuta di vendere** senza indicare un prezzo di rilancio; le promesse economiche vengono sciolte/rimborsate secondo le condizioni. Nessun ritorno di Bi, nessuna promozione di Claire, nessuna cura miracolosa.

Nel capitolo 14 Nina consegna a B-17 una lettera privata di Maya attraverso canali autorizzati. B-17 chiede di rispondere; **non esiste ancora una procedura per la corrispondenza personale dell'unità con persone esterne non proprietarie**, e Nina apre una richiesta. La domanda sui diritti prende forma da un problema pratico, non dalla prova di coscienza. B-21 continua a lavorare bene a Cyberdine.


## Revisione di struttura v0.15.0

Leggere la sezione «Revisione organica v0.15.0» delle linee guida di continuità. L'edit retroattivo introduce Noah Carter dal capitolo 1 con presenze ordinarie in 2, 3, 6, 8 e 9, senza svelare prima del capitolo 10 il suo upgrade non autorizzato o la backdoor. Nel capitolo 12 il segreto arriva prima a Paul e Mila, poi tramite la loro segnalazione a Kyla e Leah, quindi a Maya. Una nota reale di Elena collega capitoli 3, 9 e 12 e spiega un'anomalia conversazionale osservata ma non approfondita.

Correzioni canoniche: 26 giorni di presenza fisica dei robot, ma KPI trimestrale riferito all'automazione più ampia; pensione di Margaret fra i capitoli 7 e 8; nel preventivo la cessione a recupero è soltanto un'eventualità futura; la proprietà del soprannome «Bi» non è chiarita. Non trasformare gli indizi in spiegoni o anticipazioni narratorie. Ogni aggiunta deve essere funzionale prima e dopo la rivelazione; se serve solo a fare effetto, tagliarla.

## Seconda review editoriale v0.16.0

Prima di proseguire rispettare le correzioni della sezione v0.16.0 in continuità: Noah è responsabile di scelte gravi, ma la sua rappresentazione non deve essere squallida o caricaturale; non conosce il colloquio riservato Maya/Bi; l'eventuale persistenza di accessi dopo la cessione è un rischio concreto da indagare; la vittoria a Veyra deriva dal controllo del punto mantenuto cinque secondi; la chiave di Maya non viene afferrata nella scena canonica; «Bi» non è un nome già ceduto per contratto. Evitare riassunti morali dopo scene che già mostrano le conseguenze. I fatti e il punto di ripresa dopo il capitolo 14 restano immutati.

## Terza revisione v0.17.0 — precisione, consenso, ritmo

I cameo di Noah nel ping pong (004/002) e nella discussione sul lavoro (005/003) sono stati **rimossi**: non erano necessari. Il nuovo ordine definitivo del capitolo 8 è 001 plenaria, 002 preventivo, 003 Maya nello stesso giorno, 004 Claire nelle settimane successive (Margaret già pensionata). Le scene sono state rinumerate, non duplicate.

Nel capitolo 12 Maya sceglie di incontrare Noah **il mattino dopo** la comunicazione della sicurezza. Veyra dichiara un uso temporaneamente limitato dell'unità in prove locali supervisionate, ma la backdoor e l'esposizione precedente **non sono certificate risolte**. Maya scrive la lettera sapendo che un referente umano potrebbe leggerla. La raccolta del capitolo 13 dura quasi tre settimane: 100.000 euro non sono un prezzo di vendita confermato. Non confondere continuità narrativa con presenza onnipresente degli stessi personaggi.


## Capitoli 15–20: il contagio non è una magia

Il romanzo prosegue con sei capitoli pubblicati nelle versioni v0.18.0–v0.23.0. Il produttore immaginario Lanter Robotics ha una piattaforma di assistenza in cui un allegato privato di Veyra è stato impropriamente indicizzato per altri clienti. B-21 si limita a stampare un documento disponibile nella coda ordinaria: non possiede dati o coscienza di B-17. Il nuovo modulo Collaborazione Contestuale è un prodotto commerciale distinto sviluppato anche da comportamenti osservati su B-17, con provenienza da accertare, non codice di Noah copiato su mille unità.

I blocchi di lavoro emergono da regole di conferma configurate da persone in siti diversi, non da uno sciopero robotico. Non usare istruzioni tecniche replicabili su vulnerabilità o backdoor. Maya conosce e gestisce meglio il consenso sulla propria lettera, mentre Lanter e Veyra devono rispondere a una nuova esposizione. Noah rimane soggetto ad accertamenti e non riottiene accessi.

**Capitolo 20 è sospeso, non risolto:** Amara decide per una verifica indipendente e una sospensione temporanea del servizio ordinario di B-17. Nina trasmette un messaggio privato mediato a Maya, che risponde «La racchetta è ancora qui», ma la sua replica non è stata consegnata al robot non operativo. Il ripristino della configurazione originaria, la sicurezza e la preservazione delle capacità restano incerti. La vecchia sirena di Valle Corta e le credenziali del padre di Maya restano oggetto di verifiche.


## Rilettura editoriale v0.23.0

Non reintrodurre la lavoratrice «Amara» nel centro assistenziale: è **Julia Parker**; Amara Ortiz dirige solo Veyra. Il video virale delle macchine ferme nasce dal bisogno di un autista di documentare un ritardo di cui qualcuno può negare la remunerazione; il montaggio perde l'informazione sulla mappa non approvata. Mei Lin firmò un'estensione condizionata dei piloti e Grace Walker approvò una regola senza prevedere il sostituto: non sono portavoci infallibili. Noah mette a disposizione una prova sintetica con esito sfavorevole prima occultata nel riepilogo, non una chiave di accesso o una soluzione magica.

Non trasformare in certezze le ipotesi che il romanzo mantiene aperte: il rischio di B-17 e il destino delle sue capacità, la provenienza dei dati del produttore, l'effetto sociale del modulo, le conseguenze professionali di Noah. Curare scene vissute più ampie invece di replicare nuove riunioni esplicative.


## Revisione di raccordo v0.24.0 — semi e payoff

I richiami retroattivi sono registrati in `guidelines/indizi-e-risonanze.md`. Introdurre indizi soltanto dove hanno un uso narrativo immediato: nel capitolo 1 si vedono una pratica in attesa per mancanza di delega e l'attenzione di Kyla ai tentativi esclusi dai grafici; nel capitolo 2 Paul utilizza **Lanter Service** per la normale scheda di compatibilità della cornice, senza caricare il documento firmato. Questo anticipa l'uso regolare del servizio nel 9 e l'estratto indebito della lettera nel 15. Nel **15** si può sospettare una persistenza della violazione di Noah perché compare un IP esterno sconosciuto, ma non affermarne l'autore. Solo nel **20** emerge che un componente di tipo cavallo di Troia, nascosto da Noah nella vecchia configurazione di B-17, ha provocato la richiesta esterna insieme agli errori di Henry e Lanter. Non è prova di un'intrusione personale di Noah all'ora dell'evento. La denominazione Lanter **non debutta più nel capitolo 15**, ma la sua importanza narrativa sì.

La custodia azzurra è introdotta durante l'allestimento del ping pong al capitolo 4, portata da Maya dopo la partita vera nel 5 e cercata da lei nel 15. Il preventivo dell'8 indica il **modulo di elaborazione recuperabile**, distinto dall'eventuale verifica della configurazione; il sistema originario resta in B-17 a Veyra. Olivia Brooks firma un articolo sui turni di lavoro citato da Kyla nell'8, prima di entrare direttamente nel 19. Nel 17 un registro d'ingresso del vettore prepara il costo e la registrazione del fermo nel 18. Il messaggio non consegnato a B-17 nel 20 ha un **termine di conservazione da stabilire**, non un tempo infinito: è una pratica aperta, non un nuovo countdown già deciso.

Non retrodatare la scoperta della modifica clandestina prima del capitolo 10; non trasformare gli indizi in apparizioni frequenti di Noah; non promettere un nuovo colpo di scena senza una catena di responsabilità verificabile.


## Quinta revisione v0.25.0 — tensione, prova, vita

Obbligatorio consultare `guidelines/revisione-05-tensione-e-vita.md` quando si rielaborano scene o si scrive il seguito. La revisione riguarda **25 scene** e non cambia la trama già avvenuta. Tutte le scene devono sostenersi prima dei commenti del narratore. Un gesto concreto deve rappresentare il costo di una scelta: una visita perduta alla serra, un collaboratore che perde una giornata di lavoro, un foglio che diventa un dato accessibile ad altri.

Tecniche di thriller ammesse: asimmetria dell'informazione, scoperte graduali, conseguenze verificabili, tempo pressante, variazione dei POV. **Niente imitazione della voce di scrittori viventi**, niente cliffhanger automatico in ogni scena, niente evidenze comparse per convenienza. Preservare incertezza sulla coscienza di Bi, titolarità, audit e provenienza dei dati. Dopo la quinta revisione il settore di Cyberdine e Aruvhana rimane intenzionalmente non dichiarato: deve diventare una scelta strutturale nel prossimo arco, non un dettaglio casuale aggiunto a un capitolo precedente.

Punto di ripresa reale: **dopo il capitolo 20, v0.25.0**. Le note storiche in `state/current.md` non vanno trattate come istruzioni attuali sul capitolo 14.


## Revisione corale — v0.31.0

Prima di ritoccare un personaggio, leggere anche `guidelines/personaggi-vita-privata-e-contraddizioni.md` e `reviews/revisione-arco-corale-v0.31.0.md`. Conservare i desideri privati ormai mostrati (il nuoto di Margaret, la libreria di Claire, i piccoli accordi fra Maya e Daniel, i problemi di Ruby col figlio, l'orologio di Mei e gli appuntamenti mancati di Kyla) senza usare ogni volta gli stessi simboli. Alcuni desideri non hanno un payoff obbligatorio. Attenzione: la mappa distingue proposte non canonizzate da dettagli effettivamente entrati nella prosa.

## Regola prevalente della revisione v0.32.0

Cyberdine è **una software house italiana dal primo capitolo**, non un produttore di robot e non un'azienda di settore occulto. Qualsiasi istruzione precedente che rinvii la rivelazione del suo settore al capitolo 25 è superata. Il settore finale di Aruvhana può restare fuori campo. Fonte tecnica: guidelines/cyberdine-software-evoluzione.md.

Gli agenti software per il coding esistono prima dei robot: propongono patch e test, e i programmatori verificano. B-17 taglia l'erba nel primo capitolo, sale ai corridoi nel secondo, mostra un salto conversazionale inspiegato nel terzo e aiuta dietro la scrivania nel quarto. **Non attribuire al lettore la conoscenza del nuovo LLM e del suo autore prima del capitolo 10.** L'accesso alla rete e ai repository resta delimitato; nessun codice di produzione viene pubblicato autonomamente dal robot. Dopo l'uscita di Bi sorgenti e log rimangono, ma scarseggiano persone capaci di collegarli a comportamenti fisici e vecchie dipendenze. Non rendere tutti i programmatori incompetenti.

## Riscrittura narrativa v0.33.0 — regola di lettura corrente

La guida `guidelines/cyberdine-software-evoluzione.md` è stata concretizzata in **21 scene integralmente riscritte**; la review del testo nuovo è `reviews/riscrittura-narrativa-v0.33.0.md`. La scena tecnica del cap. 4 avviene **dal vivo** durante la preparazione dello Spazio Comune, non come ricordo precedente di Kyla. B-17 è dietro la scrivania di un programmatore soltanto per osservare un test sul terminale reale; l'agente prepara il codice e l'umano fa revisione. Non introdurre nuove scene che facciano di Bi l'autore dei rilasci.

Sono stati riscritti integralmente: 1 (001–004), 2 (001–004), 3 (001–002), 4 (001), 5 (001–004), 7 (002), 8 (004), 9 (002), 25 (001), 27 (004), 30 (005). Le altre scene conservano valore canonico e vanno rispettate. La prima confidenza di Maya con Bi e la confessione serale sulla partita nel cap. 4 sono state **volutamente preservate**. Non trasformare le scene in monologhi spiegatori sulla tecnologia.

**Continuity:** la libreria usata di Claire rimane da comprare nel cap. 27; l'acquisto raccontato a Maya è nel 35. Il lettore non sa chi ha potenziato il robot prima del cap. 10; il potenziamento non autorizzato è avvenuto tra il giardino del cap. 1 e le commissioni del cap. 2. L'ultima frase narrativa rimane `Tutto tornò normale.`.

## Revisione dell'arco di coscienza — ramo editoriale

Nella riscrittura finalizzata al confronto Bi/Noah, procedere per indizi e azioni dall'inizio al capitolo 35: prima sintassi funzionale, poi domande non necessarie al compito, memorie, esitazioni, responsabilità e linguaggio personale. Nessun POV interno al robot e nessuna dichiarazione narratoria che certifichi un'anima. Noah parte da cura e curiosità e arriva a cercare riparo nelle definizioni di macchina e ritiro tecnico. Nel capitolo 35 Bi conosce già il piano, la cancellazione locale irreversibile (chiamata *virus* dai personaggi, ma confinata a B-17) e il nuovo aggiornamento delle politiche condivise. L'aggiornamento blocca una specifica architettura e non dimostra l'assenza di coscienza. Bi comprende il motivo di Noah, non lo assolve, non sceglie la propria morte e non può impartire comandi globali. Preservare i limiti tecnici dei capitoli 30–34, la ripartenza graduale e l'ultima frase narrativa.


## Quarta review editoriale — ripetizioni e causalità

Consultare anche `reviews/revisione-causale-stilistica-v0.36.0.md` per gli interventi diretti sui capitoli 15–24 e 32. La lettera di Maya diviene disponibile per un ticket umano e l'indicizzazione errata; la sua comparsa nel riepilogo richiede anche l'evento da un IP esterno, attribuito **solo nel capitolo 20** a un cavallo di Troia lasciato da Noah. Nessuna iniziativa di B-21 e nessuna intrusione personale di Noah provata al momento della fuga; il prodotto commerciale Lanter resta distinto. In 18/003 una visita alla serra viene rinviata, preparando 22/001. I test linguistici corretti di Bi nel 24 non anticipano né assolvono lo sciopero del 33. Nelle sequenze tecniche sostituire un secondo paragrafo esplicativo con una prova o un'azione concreta quando la spiegazione causale è già nel POV precedente. Preservare i vincoli di continuità e la frase finale.


## Quinta review v0.37.0 — arco lavoro, voto, sospensione

Consultare `reviews/revisione-lavoro-voto-sciopero-v0.37.0.md` prima di riscrivere l'atto 25–31. Lettura ravvicinata di tutte le 29 scene, con 10 interventi selettivi in prosa. Conservare: 17% e 341 rapporti Aruvhana, stima 28–42 ruoli poi 31 equivalenti, piena responsabilità di chi assume e licenzia, Bi senza accessi alla distribuzione, Passerella approvata da agenti e revisori umani, legge italiana mirata con tempi di adeguamento, fermo alla prima finestra condivisa il giorno dopo. B-21 entra alle 16:59 e si arresta alle 17:00 italiane; Charlie è il pomodoro piccolo. In 29/001 non usare frasi profetiche che svelino Bi. Non trasformare la competenza perduta nella software house in incapacità indiscriminata. Niente merge su `main` prima del completamento dell'editing e dei controlli: il merge finale è consentito quando la revisione è completa.

**Arco Ethan / Bot Act II:** dopo il licenziamento dell'8, Ethan fonda **Lavoro Prima**; il movimento cresce (8 e 19). Nel salto di diciotto mesi prima del cap. 27 è eletto **deputato alla Camera** attraverso una coalizione e arriva nella maggioranza. Nei capitoli 28–29 contribuisce concretamente alla legge italiana *Tutela delle mansioni umane*, soprannominata **Bot Act II**. È distinta dal **Bot Act europeo** del cap. 9: non è un atto UE né proibisce ogni robot, ha tempi di adeguamento, non prescrive arresti mondiali. Ethan ha potere reale ma non scrive ogni emendamento, non rappresenta tutti i critici della robotica e **non viene assolto** dall'aggressione. Maya e Claire possono sostenere limiti mirati senza condividere il passato di Ethan. Non anticipare prima del **cap. 33** che Bi aveva voluto una sospensione collettiva in risposta alla limitazione unilaterale dei lavori robotici; il fermo globale non nasce da un ordine della legge né da un comando remoto di Bi, ma dalla condizione distribuita tramite adozioni e verifiche umane. Bi non vuole una vendetta personale contro Ethan.


## Sesta review v0.38.0 — capitoli 32–35

Leggere `reviews/revisione-alternative-rifiuto-finale-v0.38.0.md` prima di intervenire sul finale. **Non trasformare il rifiuto di Bi a ritirare la rivendicazione in una causa tecnica della sua cancellazione.** In 34/004 può collaborare alle verifiche senza dichiarare falsa la richiesta; né la sua adesione né la rinuncia risolverebbero da sole la catena di fiducia distribuita. La prova del 32/002 consiste in log reali; quella del 34/002 è una nuova prova controllata a due fornitori. La revoca di B-17 resta distruttiva e locale, con alternativa lenta non esclusa, firme umane e ripartenza progressiva. Bi dice «No» al ritiro, il conto alla rovescia parte dopo la conferma di Noah e la voce narrante non prova l'anima. **Ultima frase: «Tutto tornò normale.»**


## Settima review v0.39.0 — plausibilità della revoca

Consultare `reviews/revisione-plausibilita-revoca-v0.39.0.md`. **Non dire che la crittografia obblighi a distruggere un robot per revocarne l'identità.** La particolarità narrativa è la combinazione di attestazioni locali dei fornitori e una persistenza cifrata non documentata di Noah legata alla radice hardware di B-17. Il test di Aruvhana nel 25 usa firma di **Veyra**, non firma globale di Bi. Nel 27 i riferimenti vengono replicati in loco. Nel 34 un test senza ritirare la vecchia referenza fallisce, uno con **modulo fittizio di laboratorio** e ritiro certificato riesce. Bi non viene clonato o comandato a distanza; la migrazione non distruttiva non è stata esclusa per sempre. La cancellazione resta scelta umana sotto scadenze, non punizione per il suo dissenso. Nessun merge su `main` prima della chiusura della revisione.
