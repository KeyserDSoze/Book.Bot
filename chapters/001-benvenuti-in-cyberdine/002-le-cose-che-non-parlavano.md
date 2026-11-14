---
type: scene
id: scene:001-benvenuti-in-cyberdine:002-le-cose-che-non-parlavano
chapter: chapter:001-benvenuti-in-cyberdine
number: 2
title: Le cose che non parlavano
canon: canon
pov: character:malik-okafor
characters:
  - character:malik-okafor
  - character:noah-carter
  - character:gavin-shaw
  - character:daniel-reed
  - character:elena-fischer
locations:
  - location:cyberdine-campus
factions:
  - faction:cyberdine
  - faction:aruvhana
---

Il primo ordine passava. Il secondo non avrebbe dovuto esistere.

Malik Okafor riaprì il log e ricominciò dall'alto. Il terminale di prova aveva confermato l'operazione prima che la rete si interrompesse. Alla riconnessione Bridgeglass avrebbe dovuto leggere quella conferma e fermarsi. Invece preparava una nuova esecuzione.

Il banco di prova la bloccava prima che raggiungesse la macchina. Sul monitor, però, il test era rosso da ventitré minuti.

«Non riavviare di nuovo il servizio», disse Elena Fischer. «Perdiamo la sequenza che ci serve.»

«Non lo sto riavviando.»

«Hai il comando aperto.»

Malik tolse le dita dalla tastiera. Aveva dormito forse due ore. Sul tavolo c'erano una barretta ancora incartata e quattro bicchieri di caffè, nessuno finito.

Daniel Reed arrivò con il telefono all'orecchio, chiuse la chiamata appena vide lo schermo.

«Kyla è davanti al laboratorio. Quanto ci serve?»

«Se vuoi un numero, dimmelo tu», rispose Malik.

«Non cominciare.»

«Siamo qui da quattro notti fino alle quattro. Non ricominciare tu con i minuti.»

Gavin Shaw, appoggiato allo stipite, guardava il calendario di Delivery sul proprio tablet. Aveva spostato due verifiche per liberare quella mattina e adesso un altro cliente chiedeva conto del ritardo.

«Mi serve sapere se devo richiamare i tecnici che avete tolto all'altra commessa», disse.

Elena allargò sul monitor due richieste consecutive. «No. Mi servono dieci minuti senza nessuno che chieda quanto manca.»

Daniel guardò la porta chiusa. «Non li abbiamo.»

Un ragazzo del team lesse la risposta dell'agente di sviluppo. «Propone di rigenerare l'adattatore con un controllo sul retry.»

«L'abbiamo già fatto», disse Elena. «Il test sintetico passava anche prima. È il terminale reale che non si comporta come il modello.»

«Quindi cosa gli chiediamo?»

Malik avrebbe voluto rispondere. Non riuscì a formulare una richiesta che non fosse una versione più stanca della precedente.

Noah Carter entrò con un caffè chiuso in mano e un cavo che spuntava dallo zaino.

«Chi ha occupato il banco che mi serviva?»

«Non è il tuo banco», disse Malik.

«Appunto. Dovrei essere a un altro piano.» Noah guardò le facce, poi lo schermo rosso. «Che succede?»

«La demo che hai sentito annunciare da tre settimane è morta», rispose Gavin.

Noah posò il caffè sul davanzale. Non chiese di prendere il controllo della tastiera. Si chinò sui log, seguì con un dito la prima conferma, poi la seconda richiesta.

«Questa è la stessa operazione?»

«Sì.»

«Perché ha un'altra chiave?»

Malik avvicinò il monitor. Nella prima riga c'era l'identificativo dell'ordine; nella successiva, dopo il timeout, un nuovo identificativo di tentativo.

Noah indicò i due valori. «State usando il numero del tentativo per decidere se l'ordine è già stato eseguito. Al retry cambia. Il sistema perde l'identità dell'operazione.»

Elena ingrandì la funzione. «Maledizione.»

«Possiamo correggerla?» chiese il ragazzo.

«Sì», rispose Malik. Poi guardò Daniel. «Non in cinque minuti. Va cambiata, provata con il terminale, e dobbiamo controllare che non rompa gli altri connettori.»

Daniel sbatté il palmo sul tavolo, una volta sola. «E allora cosa facciamo vedere ad Aruvhana?»

«Il problema», disse Elena.

«Ci hanno convocati per valutare un investimento, non per vederci debuggare», disse Gavin.

Noah si raddrizzò. «Fate un simulatore del percorso. Stesse schermate, dati sintetici, nessuna richiesta al terminale. Mostrate che cosa dovrebbe succedere, non dite che è successo davvero.»

«Assolutamente no», rispose Elena. «Un mock fatto in corsa, senza revisione, con la delegazione dietro la porta?»

«È il nostro lavoro che ci metti in mano», disse Malik. «Se passa per una prova reale, chi firma siamo noi. Tu domani sei di nuovo sull'altra commessa.»

«Non firmo io», disse Noah. «Per questo non vi sto dicendo di farlo di nascosto. Il test rosso resta. Lo mostrate se ve lo chiedono. Ma se entrano adesso non avete neanche il flusso da spiegare.»

«Ci avevano promesso una macchina collegata», disse Elena. «Non un film.»

«Avete ragione tutti», disse Daniel.

Nessuno gli prestò attenzione. Malik aveva già girato lo schermo verso Noah.

«Certo che è facile, quando non hai passato quattro notti a rimediare ai cambi di perimetro. Avevamo detto che non potevamo mostrare tutte le casistiche. È stato promesso comunque.»

«Malik.»

«E adesso volete che un agente ci costruisca una bella bugia verde.»

«Malik, basta!»

Daniel questa volta alzò davvero la voce. Il ragazzo tolse le mani dalla tastiera.

«Non abbiamo il tempo di rifare la storia delle ultime due settimane», disse il project manager. «Il terminale oggi non è pronto. Possiamo perdere la trattativa senza neppure mostrare il prodotto, oppure preparare un percorso simulato e dichiarare esattamente cos'è. Seguite Noah. Io rispondo della decisione.»

«È una scorciatoia», disse Elena.

«È una scelta commerciale con un limite tecnico scritto nero su bianco. Non ti sto chiedendo di validarla.»

«Allora lo voglio nero su bianco davvero», disse Malik. «Non voglio sentir dire domani che il team ha consegnato la demo funzionante.»

Daniel aprì di scatto il portatile. «Vi serve un'email? Va bene. Vi mando un'email.»

Selezionò la distribuzione interna della commessa. Controllò i destinatari, aggiunse Kyla in copia e scrisse mentre gli altri guardavano l'ora.

*Oggetto: Aruvhana — decisione operativa sulla demo Bridgeglass*

*Il collegamento live ha fallito la verifica del retry e non è validato. Autorizzo la preparazione di un simulatore isolato con soli dati sintetici e nessuna operazione sul terminale reale. Il team tecnico ha espresso riserve e non approva l'integrazione. Mi assumo la responsabilità di questa scelta. La presentazione al cliente richiede il consenso di Kyla e la dichiarazione esplicita che il flusso è simulato. Il test fallito rimane disponibile.*

Firmò. Inviò. Sul portatile di Malik arrivò subito la notifica.

«Ecco», disse Daniel. «Adesso possiamo lavorare?»

Malik non rispose. Spostò il proprio computer per fare spazio a Elena.

Noah indicò la finestra dell'agente. «Chiedigli una cosa per volta. Prima il percorso, poi l'aspetto. Scrivi.»

Dettò il compito: un ordine sintetico, la conferma simulata, il timeout e un secondo tentativo che non generasse un nuovo ordine. Ambiente separato. Nessuna chiamata al terminale. Etichetta permanente *MOCK — DATI SINTETICI*. In un ticket distinto, diagnosi della chiave di idempotenza e test da ripetere sul banco vero.

L'agente generò la prima versione. All'avvio la pagina della conferma rimase vuota.

«Campo sbagliato», disse Elena. «La risposta del nostro contratto API non si chiama così.»

Il ragazzo corresse la mappatura. Malik controllò la configurazione di rete e staccò il collegamento di prova dal simulatore. Elena rilanciò il percorso, una volta. Poi una seconda, cambiando l'ordine degli eventi.

Sul monitor comparvero quattro passaggi verdi. A fianco restò aperto il test rosso.

Daniel non sorrise. Lesse la scritta *MOCK — DATI SINTETICI*, verificò che fosse visibile anche nella schermata finale e chiamò Kyla. Lei non rispose; stava parlando con i visitatori.

Le scrisse: *Simulatore pronto, isolato, verificato per la sola presentazione. Il live resta fallito. Ho bisogno del tuo via libera prima dell'ingresso. Ti spiego tutto di persona.*

Noah recuperò il caffè ormai tiepido.

«Allora io vado a lavorare davvero», disse.

Malik lo guardò allontanarsi. Avrebbe voluto ringraziarlo, ma il monitor rosso era ancora acceso e, oltre la parete, sentiva ridere uno dei clienti.