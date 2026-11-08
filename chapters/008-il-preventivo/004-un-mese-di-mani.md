---
type: scene
id: scene:008-il-preventivo:004-un-mese-di-mani
chapter: chapter:008-il-preventivo
number: 4
title: Un mese di mani
canon: canon
pov: character:irene-valli
characters:
  - character:irene-valli
  - character:mila-novak
  - character:elena-fischer
locations:
  - location:cyberdine-campus
factions:
  - faction:cyberdine
---

Il calendario degli incarichi temporanei si chiamava *Continuità assistita — fase transitoria*.

Irene aveva proposto di chiamarlo semplicemente *Le cose che dobbiamo tornare a fare*, ma Elena le aveva risposto che serviva un titolo utilizzabile nei documenti di progetto. Non c'era stata una discussione.

Sul calendario comparivano turni per il recupero degli originali, visite ai vecchi terminali, verifica delle regressioni che i simulatori non riproducevano e ricostruzione delle dipendenze software rimaste senza una persona di riferimento. Alcuni compiti appartenevano al personale di supporto; altri richiedevano sviluppatori.

Irene lesse il proprio nome accanto a una voce: **Martedì, 15:00–16:00 — validazione del percorso storico dei documenti e della funzione di conversione**.

Subito sotto compariva il corso sulle librerie legacy, rinviato per la seconda volta. Non mancavano le persone interessate; mancavano ore formalmente tolte alle consegne e attribuite alla formazione. Alla riunione avevano autorizzato il principio. Il budget esecutivo continuava a rimbalzare fra Delivery e HR.

Mila le si fermò accanto.

«Ti hanno dato una bella ora», disse.

«È un'ora senza altre riunioni. Per questo sembra bella.»

«Pensavo che gli agenti facessero quella parte.»

«La fanno. Ma quando il vecchio terminale restituisce un messaggio che non avevamo previsto, i test dicono ancora che va bene. Bisogna guardare il dispositivo e poi leggere il codice.»

«E perché non basta il nuovo robot?»

«Perché il nuovo robot non c'è ancora. E, quando arriverà, non avrà automaticamente le prove che Bi ha costruito insieme a noi.»

Irene aveva ripetuto quella frase così spesso da sentirla quasi estranea. Non era convinta che Bi fosse insostituibile. Era convinta che nessuno avesse messo in ordine ciò che lui aveva fatto: osservazioni, tentativi, casi scartati, piccoli adattamenti che i responsabili avevano accettato perché funzionavano. I log c'erano. Anche le patch. Mancava il filo che li teneva insieme.

Nel pomeriggio entrò nel laboratorio dei terminali vecchi. Un programmatore nuovo stava guardando una richiesta di correzione generata dall'agente.

«Questa patch elimina un controllo duplicato», disse. «I test sono verdi.»

«Quale controllo?»

L'uomo indicò una riga del confronto.

«Quello sulla seconda conferma.»

Irene ricordò il giorno in cui un programmatore aveva fatto spazio a Bi dietro la propria scrivania. Il robot aveva osservato una spia cambiare due volte; fino ad allora tutti avevano pensato che il terminale inviasse un solo messaggio.

«Sei sicuro che sia duplicato?»

«Lo dice l'agente.»

«Il codice cosa dice?»

L'uomo aprì il file. Il controllo era stato introdotto molti anni prima per un terminale che trasmetteva due stati simili con significati diversi. La nota era sintetica; non riportava un esempio completo.

«Non lo so», ammise.

«Allora proviamolo sul banco prima di togliere la condizione.»

Il test durò quarantatré minuti. Irene tenne il registro aperto mentre il programmatore cambiava i parametri nell'ambiente isolato. Non pubblicarono nulla. A un certo punto il terminale reale confermò una operazione e subito dopo inviò il messaggio che il simulatore classificava come ripetizione inutile.

Il programmatore si voltò verso Irene.

«Se togliamo questo, cancelliamo una informazione che serve alla riconciliazione.»

«Esatto.»

L'uomo si sedette. «Avrei firmato la patch.»

«Hai chiesto di provare il caso. Non l'hai firmata.»

«Perché tu conoscevi il problema.»

«Perché qualcun altro lo aveva trovato tempo fa e non l'avevamo scritto abbastanza bene.»

«Puoi insegnarmelo?», chiese lui.

Irene indicò il calendario. «È quello che sto cercando di fare da settimane. Per oggi hai ancora mezz'ora?»

L'uomo controllò il proprio turno. «Per oggi sì.»

Tornarono al codice. Irene chiese di allegare alla nuova prova la registrazione del terminale e una nota sulla funzione che traduceva i due stati. Il programmatore lesse il sorgente fino alla chiamata finale. Era una attività che avrebbe richiesto più tempo di un riepilogo automatico, ma gli serviva per spiegare il comportamento a chi sarebbe arrivato dopo.

Quando uscirono, la luce del corridoio aveva già cambiato colore.

Paolo li aspettava con un registro cartaceo sotto il braccio.

«Ho trovato la revisione», disse. «Era nell'archivio storico, non nel percorso che avevamo registrato.»

«Di nuovo?»

«Quella originale, questa volta.»

Irene controllò la fonte e inserì il riferimento nella procedura di continuità. Prima di confermare l'aggiornamento aggiunse due campi: **dove si trova l'originale senza il sistema** e **chi sa riprodurre il test senza usare il riepilogo dell'agente**.

«Questo diventerà un obbligo?», chiese Paolo.

«Lo proponiamo. Poi i responsabili decideranno.»

«Quindi non siamo proprio tornati indietro.»

«No. Stiamo cercando di non ripetere gli stessi errori quando torneremo ad automatizzare.»

Passando davanti all'ex ufficio di Adriana vide la nuova scritta *SALA DI APPOGGIO*. La responsabile era già andata in pensione. Aveva lasciato dietro di sé un quaderno pieno di riferimenti e un intero reparto abituato a chiedere alle macchine di raccoglierli.

Irene pensò al colloquio per la posizione senior che non si era mai svolto. Da settimane faceva una parte di quel lavoro, senza il titolo e senza una prospettiva garantita. Scoprire una vulnerabilità della riorganizzazione non avrebbe fatto ricomparire il posto. Non era neppure ciò che voleva: non desiderava che il progetto fallisse per avere ragione.

Alla macchinetta del caffè trovò un foglio scritto a mano: **SE FINITE I BICCHIERI, RIEMPITELI. SONO NEL DEPOSITO C.**

Sotto qualcuno aveva aggiunto: **NON SERVE UN ROBOT PER LEGGERLO.**

Irene sorrise appena. Aprì il vano, lo trovò quasi vuoto e prese nota di passare al deposito il giorno dopo.

Sul telefono arrivò una notifica del nuovo test. L'agente aveva incorporato la variante che lei e il programmatore avevano osservato, insieme al riferimento al codice originale. Il risultato era verde.

Non lo approvò subito.

Prima controllò che la registrazione del terminale reale fosse ancora accessibile a chi avrebbe dovuto fare la prossima revisione.
