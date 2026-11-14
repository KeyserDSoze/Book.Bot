---
type: scene
id: scene:001-benvenuti-in-cyberdine:002-le-cose-che-non-parlavano
chapter: chapter:001-benvenuti-in-cyberdine
number: 2
title: Le cose che non parlavano
canon: canon
pov: character:kyla
characters:
  - character:kyla
  - character:visitors
  - character:malik-okafor
  - character:noah-carter
  - character:gavin-shaw
  - character:b-17
locations:
  - location:cyberdine-campus
factions:
  - faction:cyberdine
  - faction:aruvhana
---

Malik aveva già riavviato il servizio tre volte quando Gavin entrò nel laboratorio.

«Quanto?»

«Non lo so.»

«Non è un orario, Malik.»

Sul monitor la prova di Bridgeglass era rossa. L'agente aveva preparato un adattatore che, dopo un timeout, interpretava una conferma ripetuta come un secondo ordine. Il terminale vecchio non sbagliava: era il software nuovo a leggere male ciò che tornava indietro. Il problema era proprio quello che la demo prometteva di evitare.

Una collega cercò il test mancante. Gavin scrisse a Kyla di rallentare la visita. Il telefono di Malik vibrava da dieci minuti; un junior aveva smesso di parlare e fissava la barra rossa del test. Gavin chiese ancora un orario. Malik gli rispose più forte del necessario: «Se mi chiedi ogni trenta secondi quando finisco, finisco dopo.» Nessuno rise.

Noah Carter comparve sulla soglia con un caffè ancora chiuso. Era arrivato tardi persino per il proprio lavoro, ma non per quella demo: non apparteneva al progetto Bridgeglass e nessuno lo aveva inserito nel calendario. Doveva occuparsi di un connettore per un altro cliente. Vide i monitor, poi Gavin.

«Bella mattinata», disse.

«Non abbiamo tempo per le battute», rispose Malik.

Noah appoggiò il caffè e si chinò sul monitor di Malik. Scorse i log del primo invio, poi quelli del tentativo successivo.

«Aspetta. Qui non è il terminale che duplica. Al retry cambiate l'identificatore del tentativo e lo state usando per riconoscere l'ordine. Guardate la chiave di idempotenza: deve restare legata all'operazione originale. Il resto non lo risolvete prima che arrivino.»

«Quindi sistemiamo quello?» chiese il junior.

«Dopo, con i test. Adesso il cliente è dietro quella porta.» Noah indicò il corridoio, dove si sentivano già le voci della delegazione. «Per la demo vi serve mostrare il percorso, non fingere che il terminale abbia risposto. Fate un mock. Dati finti, chiaramente separati. Niente chiamate alla macchina reale.»

Malik lo fissò. «È una demo tecnica. Non possiamo vendergli un giocattolo.»

«No, no, no», intervenne la collega, prima ancora che Noah finisse. «Non possiamo cambiare la demo a cinque minuti dall'incontro. Abbiamo promesso un terminale vero. E il mock non ha neanche passato la nostra revisione.»

«E soprattutto», aggiunse Malik, «tu non sei su questa commessa. Se il cliente scopre che gli stiamo mostrando dati inventati, quello che deve spiegarglielo sono io.»

Noah si raddrizzò. «Avete ragione su entrambe le cose. Non sono io a decidere cosa mostrare, e un mock non dimostra che Bridgeglass funziona. Ma fra cinque minuti avrete un bug aperto e nessuna schermata, oppure un flusso simulato che potete dichiarare per quello che è.»

«Kyla non ha autorizzato questa modifica», disse Daniel.

«Allora chiamala. Non mettete il mock al posto del collegamento reale di nascosto. Ditele cosa è rotto e fate scegliere a lei se mostrarlo.»

Malik scosse la testa. «E se insiste per il live?»

«Le fate vedere il test rosso. Il bug non sparisce se lo guardate in sei.»

«Basta», disse Daniel Reed. Non alzò la voce; fu il modo in cui chiuse il portatile a far tacere tutti. Era il project manager della commessa Aruvhana. Da due settimane vedeva le revisioni della proposta commerciale, il costo delle ore già bruciate e la data oltre la quale il cliente avrebbe confrontato Cyberdine con un altro fornitore. I tecnici vedevano il test rosso. Lui vedeva anche il contratto che poteva saltare.

«Malik, hai ragione: questa non è la demo che abbiamo promesso. E hai ragione anche tu sui controlli», disse alla collega. «Ma il terminale non sarà pronto quando entrano. Seguite Noah: mock isolato, dati sintetici, nessuna scrittura sul sistema reale. Io avviso Kyla e mi assumo la responsabilità della decisione. Se non autorizza, non lo mostriamo.»

«No», disse Malik. Questa volta non abbassò lo sguardo. «È una scorciatoia. Avevamo detto che avremmo dimostrato l'integrazione, non un video interattivo. Così vendiamo qualcosa che oggi non funziona.»

«E se poi ci chiedono perché abbiamo cambiato i dati all'ultimo minuto?» aggiunse la collega. «Non abbiamo neanche completato la revisione del simulatore. Non è il modo corretto di lavorare.»

Daniel li lasciò finire. «Lo so. Ma Aruvhana non è venuta solo a vedere se un retry passa un test. Deve capire se vale la pena investire nella piattaforma. Se non riusciamo neppure a mostrare come dovrebbe funzionare, non arriveremo alla fase in cui possiamo sistemare il collegamento.»

«La fase in cui lo sistemiamo doveva essere prima di oggi», ribatté Malik.

«Sì», disse Daniel. «E non lo nasconderemo. Mostriamo il percorso con dati dichiaratamente sintetici, poi il difetto reale e il piano per risolverlo. Non vi sto chiedendo di dire che funziona. Vi sto chiedendo di non perdere la possibilità di venderlo prima di aver spiegato cosa stiamo costruendo.»

Malik guardò la collega. «Lo facciamo perché ce lo stai chiedendo tu. Ma sappi che non è quello che avremmo voluto fare. E non voglio che domani qualcuno dica che abbiamo validato questa integrazione.»

«Non lo dirà», rispose Daniel. «Metterò per iscritto che è stata una mia decisione e che il test live è fallito.»

«Allora registralo nel verbale della demo», disse la collega, ancora stizzita. «Non solo in una chat che sparisce.»

Daniel rimase a fissarla. Dal corridoio arrivò una risata dei visitatori. Guardò l'orologio, poi il monitor rosso. «Vi serve un'email? Va bene. Vi mando un'email.»

Aprì di scatto il portatile, che aveva appena chiuso, e cercò la conversazione della commessa. Sbagliò due volte a digitare il destinatario. «Così, almeno, siamo tutti tranquilli», borbottò, senza che nessuno gli rispondesse. Poi scrisse, leggendo quasi a voce alta mentre batteva sui tasti:

*Oggetto: Aruvhana / demo Bridgeglass — decisione operativa*

*Confermo che, per la dimostrazione di oggi, procediamo con dati mockati e un simulatore isolato, senza collegamento al terminale reale. Il test live è fallito e l'integrazione non è validata. La decisione è mia; il team tecnico ha segnalato le proprie riserve. Kyla deve approvare la presentazione al cliente, dichiarando esplicitamente che i dati sono sintetici. Daniel Reed.*

Premette **Invia**. Il suono della notifica arrivò sui portatili dei colleghi quasi nello stesso istante.

«Ecco. Adesso siete contenti?» disse Daniel. La voce gli uscì più aspra di quanto volesse. «Possiamo fare come dice Noah, per favore? Abbiamo il cliente dietro la porta.»

«Non è questione di essere contenti», rispose Malik, senza guardarlo. «È questione di sapere cosa stiamo mostrando.»

«Lo so, Malik.» Daniel si passò una mano sul viso. «Tu prepari il simulatore», disse alla collega. «Malik, tieni aperti i log e il test fallito. Quando ci chiederanno cosa funziona davvero, glielo faremo vedere. Senza abbellimenti.»

Noah aveva assistito allo scontro in silenzio, spostando il caffè lontano dalla tastiera. Non sorrise quando Daniel gli diede ragione. «Allora scrivigli così», disse alla collega.

Lei mise le dita sulla tastiera, mentre Noah dettava, senza neppure sedersi:

*Genera subito un mock isolato per la demo Bridgeglass. Usa solo dati sintetici: un ordine, la conferma del terminale, un timeout e il retry senza duplicazione. Mantieni le stesse schermate e lo stesso contratto API del flusso previsto, ma non collegarti al terminale reale. Mostra sempre MOCK — DATI SINTETICI. In parallelo analizza se la chiave di idempotenza cambia tra i tentativi e proponi un test riproducibile. Non modificare produzione e non dichiarare risolto il bug.*

«Invia», disse Malik.

L'agente iniziò a generare il simulatore. Daniel era alla porta, al telefono con Kyla: «Ancora cinque minuti. Falli passare dalla parete dei risultati.» La collega ricontrollava i campi di risposta; il junior continuava a chiedere se fosse abbastanza. Malik aveva le mani ferme sulla scrivania, ma la mascella serrata. Nessuno poteva permettersi di sbagliare un'altra volta.

Sul monitor apparve il flusso simulato, finalmente verde. In un pannello separato rimase il test reale, rosso.

«Quello è un film», disse Malik.

«Esatto», rispose Noah. «Non una prova. Il problema potrebbe essere nella chiave: domani lo dimostrate sul terminale, non oggi davanti a loro.»

«Non abbiamo domani se oggi salta il contratto», disse Daniel.

Noah riprese il caffè. «Allora spiegategli bene cosa stanno guardando.» Era già diretto alla propria commessa quando Daniel lo richiamò. «Noah, grazie.»

Lui alzò una mano senza voltarsi. Non aveva salvato la demo. Aveva soltanto dato al team qualcosa da mostrare e un punto preciso da cui ripartire.

Quando Kyla entrò con i visitatori, il laboratorio dei sistemi vecchi aveva un difetto che Kyla non riusciva a far sistemare: odorava di plastica calda anche quando tutte le apparecchiature erano spente.

Leïa entrò e si fermò davanti a un terminale beige. Sotto lo schermo c'era un lettore che accettava tessere magnetiche di un formato fuori commercio.

«Questo lo usavamo nella sede di mio padre», disse.

«Probabilmente il vostro era più nuovo», rispose Kyla. «Questo è arrivato con il suo manuale originale. Mancano soltanto tre pagine, quelle che spiegano la procedura d'errore.»

Sahir si chinò sul pannello. «E voi vendete software per tenerlo in vita?»

«Per permettergli di parlare con il resto. Non siamo antiquari.»

Dietro il vetro Malik Okafor, sviluppatore del gruppo integrazioni, aveva aperte due finestre. A sinistra una richiesta del cliente: *riconciliare i risultati del registro locale senza ripetere le operazioni già confermate*. A destra una proposta di codice prodotta da un agente, accompagnata dal confronto con la versione precedente.

«Il nostro lavoro è sempre stato scrivere interfacce», spiegò Kyla. «Chi sviluppa un sistema nuovo di solito non vuole conoscere il passato di tutti gli altri. Noi facciamo in modo che una macchina costruita vent'anni fa e un servizio appena installato non si scambino promesse che non possono mantenere.»

«E quanto vi costava?»

«Alcune commesse richiedevano mesi e squadre intere. Gli agenti di sviluppo hanno cambiato quel lavoro. Oggi preparano adattatori, test, documentazione tecnica. Questo non significa che la versione pronta sia automaticamente quella giusta.»

Dall'altra parte del vetro Malik fermò il cursore su una riga evidenziata. Sul monitor arrivò un messaggio del responsabile Delivery: *Ci serve il via libera entro le dodici. Se slitta, avvisatemi adesso.* Malik lo lesse senza rispondere. Indicò a una collega il punto sullo schermo; lei scorse fino a una funzione precedente, poi scosse la testa. L'agente aveva usato un modo elegante per evitare un controllo duplicato. La funzione più vecchia, però, esisteva proprio perché in certe condizioni un doppio messaggio non doveva essere trattato come una doppia operazione.

«Perché non accettano la proposta?», chiese Leïa.

«Hanno trovato un caso che manca nella prova», rispose Kyla. «La consegna è a mezzogiorno. Se il cliente non può aspettare, voglio che lo dicano prima, non dopo il rilascio.»

La porta si aprì per lasciar passare un tecnico con un vassoio protetto. Portava una tastiera di ricambio e una tessera di prova. Prima di avvicinarsi al banco chiese che la macchina fosse messa nello stato consentito. Nessuno aveva fretta di saltare quel passaggio.

Sahir indicò una spia arancione.

«Perché qui c'è ancora un pulsante fisico? Se siete bravi a scrivere connettori, perché non leggete direttamente il segnale?»

«Perché il costruttore non ha mai previsto una interfaccia per quel segnale. E perché sostituire il controllo costerebbe più del servizio che il cliente ci chiede. Possiamo installare sensori, realizzare un adattatore, oppure usare una procedura verificata che legge il pannello e agisce sui comandi consentiti. Dipende dal rischio, dalle autorizzazioni e da chi deve rispondere di quell'azione.»

Un robot si avvicinò al banco con un contenitore piatto. Non era B-17. Appoggiò il contenitore sulla striscia segnata, attese la conferma di un operatore e tornò verso la porta.

«Per questo avete comprato corpi», disse Leïa.

«Per una parte del lavoro. Un agente software non può inserire una vecchia tessera in un lettore. E, se le nostre simulazioni sbagliano, qualcuno deve andare a guardare ciò che il terminale ha fatto davvero.»

Kyla li portò al monitor della dimostrazione. Il cruscotto Bridgeglass visualizzò un ordine, l'invio al terminale e la conferma. Per un istante parve perfetto.

Sahir non guardava l'animazione. Guardava un identificatore in basso a destra.

«Questi dati li state leggendo adesso dalla macchina?»

Kyla cercò Malik con gli occhi. Lui non fece cenno di sì.

«No», disse. «La risposta del terminale è simulata. Il collegamento reale ha un difetto che stiamo isolando.»

«Quindi non avete appena dimostrato il prodotto che volete venderci.»

Il silenzio fu abbastanza lungo perché Daniel smettesse di digitare. Leïa posò la penna. Anika, fino a quel momento immobile, chiese: «Da quanto lo sapete?»

«Da prima del vostro ingresso», rispose Kyla. Non avrebbe attribuito il ritardo al cliente o al terminale. «Avremmo dovuto dirvelo prima di avviare il flusso.»

Sahir indicò il verde sullo schermo. «Allora spegnete la simulazione. Voglio vedere dove fallisce davvero.»

Malik chiuse il mock e riaprì i log. Sul terminale di prova il primo ordine risultava confermato; al nuovo tentativo, il software proponeva di elaborarlo di nuovo. Non lo lasciò eseguire. Mostrò il controllo che lo bloccava e spiegò quale test mancava.

Anika guardò Kyla. «Il mock mi mostra cosa vorreste vendere. Questo errore mi dice cosa devo chiedervi prima di comprarlo.»

Kyla li portò quindi a un'altra schermata, con tre pratiche di prova già predisposte, distinguendo i dati sintetici dai risultati verificati. La tensione non si sciolse. Il cliente era rimasto, ma non per ammirare la demo.

Tre pratiche di censimento dei clienti erano ferme in attesa di un controllo. L'agente aveva segnalato campi incoerenti, suggerito correzioni e preparato una modifica ai controlli futuri. Sotto comparivano i test riusciti e quelli esclusi perché non c'erano dati sufficienti.

«Quattro giorni per individuare i controlli che arrivavano troppo tardi», spiegò. «Prima ce ne servivano molti di più. La squadra ha accettato due suggerimenti e ne ha respinto uno.»

«Perché respingerlo, se risparmiava più tempo?»

Kyla chiamò la cronologia. Comparve una nota dell'addetta alla qualità: *il caso elimina un passaggio che serve per una classe di documenti ancora validi*. La proposta era rimasta in prova.

«Perché quel documento non aveva letto il nostro piano commerciale», rispose Kyla. «Continuava a essere valido anche se il software lo giudicava scomodo.»

Leïa rise. Sahir non rise; stava leggendo le motivazioni, una per una.

«Quanti sviluppatori scrivono ancora tutto il codice?», chiese.

«Non saprei dare una percentuale unica. Dipende dalla commessa. Qualcuno lavora sulle architetture e decide le prove, qualcuno entra nelle librerie più vecchie quando l'agente non basta. Soprattutto, vorrei che nessuno smettesse di saperci entrare.»

Non era una frase prevista dalla presentazione. Le sfuggì mentre osservava la collega dietro il vetro che aveva appena trovato la funzione dimenticata.

Leïa indicò un riquadro di approvazione vuoto.

«Questa operazione non parte?»

«Manca la firma della persona delegata. Non la sostituisce una frase del modello, e non la sostituisce il fatto che il test sia verde.»

Kyla aspettò che leggessero il campo. Per una volta i visitatori ebbero pazienza con una schermata che non si aggiornava.

Uscendo dal laboratorio incrociarono B-17. Veniva dal giardino con un contenitore di guanti e una forbice da potatura nel vano protetto. Sul ginocchio metallico aveva una macchia verde.

«Lui non sa niente di quelle librerie?», domandò Sahir.

«Oggi ha soprattutto dei cespugli da finire», rispose Kyla.

B-17 attraversò il corridoio senza voltarsi. Dietro di lui una porta si chiuse con il piccolo rumore di una serratura in funzione.

Noah, davanti al vecchio varco che stavano ancora riparando, aveva ottenuto finalmente una apertura corretta. Non celebrò. Chiese all'addetto di ripetere l'operazione, questa volta senza il suo intervento.

Kyla lo osservò per un istante prima di seguire gli ospiti.
