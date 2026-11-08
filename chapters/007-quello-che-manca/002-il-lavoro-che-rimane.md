---
type: scene
id: scene:007-quello-che-manca:002-il-lavoro-che-rimane
chapter: chapter:007-quello-che-manca
number: 2
title: Il lavoro che rimane
canon: canon
pov: character:claire-foster
characters:
  - character:claire-foster
  - character:margaret-ellis
  - character:olivia-hayes
  - character:paul-turner
locations:
  - location:cyberdine-campus
factions:
  - faction:cyberdine
---

La prima anomalia senza Bi arrivò alle undici e quattordici.

Claire Foster aveva davanti un registro di aggiornamenti software. Il sistema diceva che la revisione del cliente era stata completata. Il documento che avrebbe dovuto provarlo non era nella posizione indicata. In un secondo archivio, quello storico, la stessa revisione appariva con un numero diverso.

Aprì il ticket del reparto sviluppo.

*Connettore aggiornato. Test superati. Nessuna discrepanza critica.*

Non era una risposta sbagliata. Era la risposta a una domanda che Claire non stava facendo.

Chiese all'agente una ricostruzione delle fonti.

Ricevette una sintesi ordinata. Il modulo nuovo convertiva gli identificativi secondo la tabella in uso; quello vecchio conservava una mappatura precedente per compatibilità. Le due versioni sembravano riconciliabili.

«Sembrano», disse Claire allo schermo.

Un programmatore del team integrazioni le rispose alla chiamata.

«Hai visto il ticket?»

«Sì. Il risultato è verde.»

«Il documento vero non c'è.»

Il programmatore aprì la cronologia della patch. Era stata proposta dall'agente, controllata in revisione e verificata nei casi di prova che Bi aveva contribuito a costruire sul terminale fisico. La firma era valida; l'ambiente autorizzato aveva registrato tutto. Mancava il caso che si presentava ora: un documento registrato con un codice storico e consultato, dopo l'aggiornamento, da un modulo ancora più vecchio.

«Possiamo chiedere all'agente di cercarlo», disse lui.

«È quello che ho fatto.»

L'agente generò una nuova spiegazione, molto simile alla precedente.

Claire lo fissò. «Non ha trovato un'altra fonte. Ha formulato un'altra volta la stessa ipotesi.»

«Possiamo aumentare il contesto.»

«Sì. Ma prima apriamo la funzione che decide dove cercare.»

Il programmatore le mostrò la libreria. C'erano chiamate fra moduli di generazioni diverse, e una routine conteneva un riferimento a una convenzione che il team non usava da anni.

«Chi l'ha scritta?», chiese Claire.

«Non so. La cronologia più recente riguarda l'adattatore, non questo modulo. Possiamo cercare i commit vecchi.»

«Facciamolo.»

Un'ora prima avrebbero chiesto a Bi di mettere insieme il registro, il terminale e la spiegazione dei vecchi codici. Claire non stava scoprendo che le persone non potevano più svolgere quel lavoro. Stava scoprendo quanto fosse costoso ricostruire ogni dipendenza quando nessuna persona aveva attraversato l'intero percorso negli ultimi mesi.

Il collega trovò un commit antico, poi un commento che rimandava a un'appendice non più presente nel repository. Claire riconobbe il riferimento: era un registro cartaceo che Margaret Ellis le aveva mostrato durante la formazione.

«Il quaderno di bordo», disse.

«Quale?»

«Non è un file. L'abbiamo tenuto in archivio quando abbiamo sostituito il sistema delle revisioni.»

Il programmatore guardò l'orologio. Aveva una revisione da firmare nel pomeriggio e altre due patch in attesa.

«Posso seguirti in laboratorio dopo pranzo.»

«No. Vado a prendere il registro e poi torniamo sul codice. Ho bisogno che tu sappia spiegarmi la funzione, non di un'altra sintesi.»

Chiuse la chiamata e aprì il manuale.

Quarantasette pagine. Una nota rimandava alla vecchia appendice cartacea, senza indicare dove fosse conservata. Claire aveva scritto quella stessa osservazione nel mese di prova del nuovo archivio, poi si era fidata del fatto che Bi sapesse raggiungere gli originali.

Si alzò per andare da Margaret.

La responsabile stava svuotando un cassetto, a pochi giorni dalla pensione. Quando Claire le mostrò i due identificativi, non guardò il riepilogo.

«Sono entrambi sbagliati», disse.

«Tutti e due?»

«Sì. State chiedendo al sistema nuovo di decidere se un documento ha lo stesso significato di uno che il sistema vecchio chiamava in un altro modo.»

«Come facciamo a saperlo?»

Margaret indicò il riferimento di archivio.

«Andiamo a cercare la persona che aveva tenuto il registro. Prima di chiedere al programma di interpretarci il passato, dobbiamo sapere cosa c'è scritto.»

Il custode dell'archivio rispose al telefono. Conservava ancora il quaderno, ma non avrebbe consegnato l'originale senza registrare l'accesso. Claire e Margaret lo raggiunsero al piano inferiore.

Il registro era più piccolo di quanto Claire ricordasse. Aveva una copertina rigida e pagine segnate a matita. A metà una riga collegava il vecchio numero al nuovo e spiegava il motivo della variazione: una classe di documenti non poteva essere riclassificata con la stessa regola degli altri, perché la prima approvazione conservava valore anche dopo l'annullamento di una richiesta successiva.

Claire fotografò la pagina nel modo consentito e tornò in laboratorio. Il programmatore aveva aperto il codice originale.

«Ecco dov'era», disse lui, indicando una condizione scritta anni prima. «Questa funzione non traduce soltanto il codice. Decide quale approvazione rimane valida quando ce ne sono due.»

«E il test dell'agente?»

«Prova la conversione. Non prova quel significato.»

Claire sentì insieme sollievo e irritazione. Non c'era stato un malfunzionamento spettacolare. Il programma aveva fatto ciò che il team aveva verificato. Nessuno aveva chiesto di controllare la ragione per cui una vecchia condizione era ancora nella libreria.

Il programmatore preparò una prova di regressione specifica, poi lesse lui stesso la funzione prima di proporre la correzione. Claire controllò che la nuova prova riportasse la fonte originale e il percorso per recuperarla senza il sistema automatico.

Non autorizzarono il rilascio quel pomeriggio. Era necessario verificare un altro cliente che usava la stessa libreria.

Olivia entrò nella stanza poco prima delle cinque. Gavin l'aveva chiamata due volte per sapere quando il suo team avrebbe potuto chiudere la pratica. Lei gli aveva risposto che un rilascio poteva aspettare finché anche il cliente più vecchio fosse stato controllato. Per non lasciare la squadra ferma senza sapere perché, aveva già avvisato supporto e commerciale del ritardo.

«Avete risolto?»

«Abbiamo capito cosa non sappiamo ancora», rispose Claire. «E abbiamo trovato il codice che fa la differenza.»

Olivia lesse la nota. Aveva un nuovo campo: **Fonte originale e persone in grado di ricostruire il comportamento in assenza dell'agente**.

«Questa non era nella procedura», osservò.

Claire attese il consueto «non è di nostra competenza». Olivia invece scrisse nel registro la dipendenza dal reparto sviluppo, dalla conservazione degli originali e dal supporto cliente. «Se manca una delle tre cose, voglio che l'eccezione resti aperta anche se ogni team ha chiuso il proprio ticket», disse.

«Dovrebbe esserci.»

Olivia non promise un nuovo ruolo senior. Approvò l'inserimento del campo nella proposta di revisione e chiese che venisse provato su almeno un'altra eccezione prima di renderlo obbligatorio.

Quando Claire tornò alla scrivania, l'agente aveva già predisposto un riepilogo del lavoro svolto. Era ben scritto, corretto in quasi tutti i punti. Non diceva che avevano passato l'intero pomeriggio a cercare una donna prossima alla pensione e un quaderno di carta.

Claire aggiunse una frase alla fine: *La funzione era presente. La conoscenza necessaria a interpretarla non era più distribuita fra i team.*

Rilesse le parole, poi le cancellò. Suonavano come una diagnosi definitiva su persone che avevano soltanto avuto troppo poco tempo.

Scrisse invece: *Da ripetere con un team che non ha partecipato al ripristino, usando le fonti documentate oggi.*

Era una verifica. Non una lezione.

Prima di uscire rimise il quaderno nel contenitore destinato all'archivio. Margaret era già tornata a casa. Le aveva lasciato un messaggio: *Non dimenticare di far leggere la funzione a qualcuno che non l'ha mai vista.*

Claire lo copiò nella propria lista del giorno dopo.

Sul monitor apparvero altri tre ticket pronti per l'approvazione. Li lasciò in attesa fino alla mattina.

Per una volta non era il sistema a dover aspettare una persona. Era una persona a decidere che il sistema poteva aspettare.
