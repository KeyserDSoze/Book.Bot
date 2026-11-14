---
type: scene
id: scene:001-benvenuti-in-cyberdine:002-le-cose-che-non-parlavano
chapter: chapter:001-benvenuti-in-cyberdine
number: 2
title: Le cose che non parlavano
canon: canon
pov: character:malik-okafor
characters:
  - character:kyla
  - character:visitors
  - character:malik-okafor
  - character:noah-carter
  - character:gavin-shaw
  - character:daniel-reed
  - character:b-17
locations:
  - location:cyberdine-campus
factions:
  - faction:cyberdine
  - faction:aruvhana
---

Malik aveva già riavviato il servizio tre volte. Sul monitor la prova di Bridgeglass era rossa. Dopo un timeout, l'adattatore generato con l'aiuto dell'agente trattava la conferma ritrasmessa come un nuovo ordine: proprio il caso che Cyberdine avrebbe dovuto dimostrare di saper prevenire.

«Quanto manca?» chiese Daniel Reed.

«Non lo so», rispose Malik.

«Non è una risposta che posso dare a Kyla.»

«E io non posso inventarmi un test passato.»

La collega accanto a Malik confrontava due registri; un junior aveva smesso di parlare. Gavin, responsabile delle consegne, aveva già avvertito Kyla che la demo era rossa e ora cercava di capire quali altre attività stessero saltando. Il laboratorio era pieno di notifiche e nessuno aveva il coraggio di chiudere una finestra.

Noah Carter comparve sulla soglia con un caffè in mano. Era arrivato tardi per la propria commessa, non per Bridgeglass: su quel progetto non lavorava e nessuno lo aveva convocato.

«Avete una faccia terribile.»

«Allora non fermarti a guardarla», sbottò Malik.

Noah guardò i due tentativi nei log. «Qui state usando l'identificatore del retry come chiave dell'operazione. Al secondo tentativo cambia. Non è il terminale a duplicare: siete voi che non riconoscete più lo stesso ordine.»

«Quindi lo correggiamo», disse il junior.

«Lo correggete e lo testate, dopo. Adesso non ci riuscite in cinque minuti. Fate un mock isolato. Dati sintetici, nessuna chiamata alla macchina reale. Almeno fate vedere il flusso.»

«No, no», intervenne la collega. «Non cambiamo la demo all'ultimo. Il simulatore non è validato.»

«E non sei nemmeno su questa commessa», aggiunse Malik. «Se domani salta fuori che abbiamo mostrato dati inventati, la responsabilità è nostra.»

Noah appoggiò il caffè. «Avete ragione. Un mock non prova che il collegamento funzioni. Ma la delegazione è qui e il prodotto va spiegato. Dichiarate che è una simulazione, non toccate il terminale e conservate il test fallito.»

«Basta», disse Daniel. Aveva ascoltato fino a quel momento con il telefono in mano. «Malik, so cosa abbiamo promesso. Ma se non mostriamo nemmeno il percorso di Bridgeglass, Aruvhana non avrà alcuna ragione per finanziarne il completamento. Seguite Noah. Io avviso Kyla.»

«Lo facciamo perché ce lo stai ordinando», disse Malik, più forte. «Non perché sia il modo giusto di dimostrare un'integrazione.»

«E lo voglio per iscritto», disse la collega. «Nessuno deve scrivere che l'abbiamo validata.»

Daniel si voltò di scatto. «Vi serve un'email? Bene. Vi mando un'email.»

Aprì il portatile, selezionò subito i destinatari, mise Kyla in copia e digitò senza esitazioni:

*Oggetto: Aruvhana — decisione operativa demo Bridgeglass*

*Confermo che oggi mostreremo un flusso simulato con dati sintetici, senza collegamento al terminale reale. Il test live è fallito e l'integrazione non è validata. Il team tecnico ha espresso riserve. Mi assumo la responsabilità operativa della scelta. Kyla dovrà approvare la modalità di presentazione al cliente.*

Premette *Invia*.

«Ecco. Adesso siete contenti? Possiamo fare come dice Noah? Il cliente è già in azienda.»

«Non è questione di essere contenti», rispose Malik. «È questione di cosa gli facciamo credere.»

«Lo so», disse Daniel, senza abbassare lo sguardo. «E non vi chiedo di mentire. Vi chiedo di preparare qualcosa che possiamo mostrare dichiarando i limiti.»

Noah indicò la finestra dell'agente. «Scrivi così.»

*Genera un mock isolato della demo Bridgeglass con dati sintetici: creazione ordine, conferma, timeout e retry senza duplicazione. Mantieni le schermate previste, ma disabilita ogni collegamento al terminale. Etichetta l'ambiente MOCK — DATI SINTETICI. Non dichiarare risolto il bug. Separatamente proponi un test per verificare la chiave di idempotenza tra tentativi.*

La collega inviò il prompt. L'agente produsse il primo flusso, ma una schermata non caricò. Malik imprecò sottovoce. Il junior cercò il campo mancante; Daniel camminava avanti e indietro, poi si fermò per non dare agli altri un motivo in più di innervosirsi. Noah indicò una discrepanza tra due nomi di proprietà. La collega la corresse e rilanciò.

Finalmente il percorso sintetico diventò verde. Accanto, il test reale rimase rosso.

«È una rappresentazione», disse Malik. «Non una prova.»

«Esatto», rispose Noah. «Adesso sapete anche da dove cominciare domani.»

Daniel controllò personalmente le etichette, la separazione dal terminale e il materiale da consegnare ai visitatori. Poi scrisse a Kyla: *Simulazione pronta. Nessun dato reale, nessun collegamento live. Possiamo riceverli quando autorizzi. Ti spiego tutto prima di iniziare.*

Noah recuperò il caffè e tornò alla propria commessa. Nessuno lo applaudì. Il team era riuscito a preparare una demo; non aveva risolto il problema che la demo avrebbe dovuto dimostrare.
