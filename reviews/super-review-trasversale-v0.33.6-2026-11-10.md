# Super review trasversale del romanzo BOT — versione 0.33.6

**Data:** 10 novembre 2026  
**Fonte:** branch `main`, commit `fa2eeea55f4cc03698f236f95a29eb219966b2ab`  
**Tipo di intervento:** audit editoriale **senza modificare le scene canoniche**  
**Perimetro:** tutti i 35 outline di capitolo, sinossi analitica 1–35, cronologia, personaggi e regole principali; riscontro mirato nelle scene dei 35 capitoli dei cambi recenti e dei loro richiami successivi. Le osservazioni sono classificate come **incongruenze confermate** oppure **rischi narrativi / raccordi da migliorare**. Il validatore automatico non sostituisce questo controllo semantico.

## Valutazione complessiva

L'architettura del libro **funziona meglio** dopo le ultime revisioni. Il percorso Bi-tagliaerba → fotocopie → ascolto → test software → crisi professionali è riconoscibile; il ping pong ha un payoff al cap. 7 e poi nei messaggi a Maya; Cyberdine è finalmente una software house con reali problemi di cassa e competitività; Noah, Ethan e Maya hanno posizioni morali distinguibili; il Bot Act II conduce all'arresto mondiale senza un comando remoto onnipotente. La conclusione mantiene ambiguità sulla coscienza di Bi e responsabilità umana nell'operazione finale.

Il limite principale è **la propagazione incompleta delle ultime riscritture**. La chat introdotta nel cap. 14 non ha sostituito integralmente la vecchia lettera nei cap. 19–21 e in alcuni documenti canonici; B-21 riacquista in una scena competenze incompatibili con il noleggio base; la numerazione interna Cyberdine continua in alcuni passaggi a coincidere con una presunta famiglia di prodotto Lanter. Il nuovo contenzioso con Veyra rischia di perdere forza perché non è sviluppato o chiuso nei capitoli successivi.

## P1 — Contraddizioni effettive da correggere prima di altra narrativa

### R01 — La lettera eliminata continua a esistere nei capitoli 19–21

**Confermato.** In `chapters/019-l-uomo-che-ha-cambiato-tutto/004-la-persona-e-il-numero.md`, Maya dice a Paul che pensa ancora «alla lettera»; Kyla la considera la «mittente della lettera consegnata a Veyra», dice che «la richiesta di risposta è ancora aperta» e le prospetta di chiedere notizie in quella veste. Ma nel **14/003–004** Bi **ha già scritto per primo** a Maya tramite una chat testuale autorizzata, alla quale Maya ha risposto; lo scambio era terminato, non era una lettera di cui si attendeva la prima replica.

In `chapters/020-il-prezzo-di-una-memoria/002-cio-che-resta-dopo.md`, Mei e Nina parlano della «lettera di Maya» consegnata, della sua fuga e dell'allegato di Henry. L'identificazione tecnica del cavallo di Troia è corretta, ma applicata all'artefatto sbagliato. Nel **21/003** Nina dice di non voler ripetere il problema della «prima lettera».

**Correzione:** riscrivere per intero i dialoghi e le frasi causali rilevanti, non eseguire soltanto `lettera`→`chat`. Nel 19 Maya è **partecipante** alla chat diffusa; ha già ottenuto la prima risposta di Bi e può chiedere **una nuova comunicazione** sulle condizioni della memoria. Nel 20 Nina ottiene una **seconda sessione mediata**, diversa dalla chat iniziale del 14; in 21 viene consegnata la **risposta successiva di Maya**, «La racchetta è ancora qui». Verificare il parlato di Paul/Kyla e il punto di vista di Nina.

### R02 — B-21 esegue operazioni tecniche non comprese nella fascia base

**Confermato.** `chapters/009-la-copia/001-stessa-faccia.md` fissa esplicitamente calcolo ridotto, noleggio, trasporto/fotocopie e **assenza** di capacità per interpretare anomalie su terminali storici. `characters/b-21.md` ribadisce «consegna i dossier, non li ricostruisce».

In `chapters/025-il-consiglio-di-bi/003-le-condizioni-di-claire.md`, però, B-21 è davanti a un terminale legacy: «La macchina leggeva gli stati e trascriveva i valori», segnala l'assenza di un responsabile e dialoga sul passaggio di una patch. È presentato troppo vicino a un assistente QA, pur mantenendo Claire come firmataria.

**Correzione:** rendere Claire, il terminale e l'agente software i soli interpreti degli stati e della simulazione; B-21 consegna un fascicolo, riconosce un codice e può eventualmente bloccare una **consegna senza destinazione autorizzata**, non rilevare un'anomalia software. Controllare anche l'interfaccia documentale semplice del **9/004** e del **30/005**, evitando di trasformare una ricerca di codice o di modulo in analisi.

### R03 — La sigla B viene ancora attribuita al produttore Lanter

**Confermato a livello terminologico e di modello.** Nel **1/001** Kyla stabilisce che **B** è il registro dei bot di Cyberdine e che **B-1** era un centralino software costruito dall'azienda. **B-17** e **B-21** sono il diciassettesimo e il ventunesimo sistema censito, non generazioni di hardware.

Ma `factions/lanter-robotics.md` definisce Lanter «produttore immaginario cinese della famiglia robotica B»; nel **9/001** si parla di «schede di compatibilità Lanter della famiglia B», e nel **15/002** di «codice di assistenza della famiglia B». La denominazione sembra quindi contemporaneamente un'identità **interna a Cyberdine** e un **codice di famiglia del costruttore**.

**Correzione:** attribuire a Lanter una famiglia industriale distinta, senza inventare numeri di modello se non necessari; i supporti devono riferirsi al codice di modello Lanter più un'associazione di tracciabilità con l'asset **B-17/B-21**. Definire come l'identificativo operativo B-17 rimane riconoscibile **dopo la vendita a Veyra**, pur separato dal seriale fisico e dai registri dei nuovi proprietari.

### R04 — Documentazione operativa canonica ancora basata sulla lettera

**Confermato.** Almeno `characters/nina-solis.md`, `characters/leah-rosen.md`, `factions/lanter-robotics.md` e `guidelines/indizi-e-risonanze.md` descrivono ancora «la lettera autentica di Maya», «la fuga della lettera» o Bi che chiede una risposta alla lettera nel 14. `timeline/events.md` conserva l'intestazione «Cap. 15 — La lettera impossibile» sebbene i metadati del capitolo lo intitolino «La chat impossibile». Nei file-scena restano nomi ereditati dalla vecchia trama (`014/.../003-una-lettera-invece-di-un-acquisto.md`, directory e scene di `015-la-lettera-impossibile`).

**Correzione:** aggiornare le **schede operative** per prime; annotare esplicitamente le review storiche come superate, senza riscriverle e falsificarne la data. Pianificare un'eventuale migrazione controllata degli slug e ID del capitolo 15 solo dopo aver verificato riferimenti, frontmatter, immagini, indice e build. Non effettuare rename a mano senza propagazione.

## P1 — Buchi causali di trama introdotti dalle ultime modifiche

### R05 — La causa civile di Veyra viene depositata ma non cambia realmente il seguito

**Gap narrativo confermato.** Nel **15/002–003** Veyra accusa Cyberdine di cercare B-17 gratuitamente e deposita un ricorso. Nel **16/002** si preannuncia la difesa; il **20/005** contiene un breve richiamo al fatto che la causa non vieta una comunicazione personale. Non emerge però, fino al finale, una fase processuale, un ritiro, una trattativa, un costo legale, un provvedimento o una scelta di direzione che dia alla vicenda un effetto concreto.

Inoltre la domanda è **giuridicamente debole** con le prove esistenti: la raccolta era privata, Cyberdine non aveva approvato un trasferimento, Veyra **aveva autorizzato la chat** e lo screenshot che alimenta l'accusa proviene da una propria violazione di riservatezza. Questa debolezza può essere **intenzionale**, se Veyra deposita l'azione per tutelare contratti/sponsor o ottenere un'inibitoria; deve però essere visibile nelle azioni e nel successivo confronto.

**Correzione proposta:** fra 16 e 20 mostrare almeno una decisione di difesa, accertamenti sui consensi e richieste di Veyra; nel 20–26 una conseguenza (accordo con riserva, ritiro parziale, rigetto di una misura cautelare o contenzioso ancora formalmente pendente). Per una Cyberdine senza liquidità anche gli **onorari e il tempo dei manager** sono costi credibili. Non convertire la causa in una condanna automatica; conservarne le ambiguità e le responsabilità di privacy di Veyra e Lanter.

### R06 — Il cavallo di Troia spiega l'IP, non la persona che pubblica lo screenshot

**Gap causale confermato.** Il **15/001** mostra quasi immediatamente lo stesso estratto della chat nella coda di stampa e online; il **15/002** trova l'IP esterno. Il **20/002–003** attribuisce l'evento IP a un intermediario richiamato dalla componente occulta installata da Noah, mentre l'errata indicizzazione rende l'estratto consultabile.

Questo **non dimostra di per sé chi abbia caricato la schermata sul canale di notizie** né perché l'estratto indicizzato diventi un'immagine pubblicata. È corretto non accusare Noah senza prove, ma bisogna distinguere **accessibilità del dato → richiesta dal nodo sconosciuto → stampa a Cyberdine → pubblicazione esterna**.

**Correzione:** decidere se il divulgatore rimane volutamente ignoto. Se sì, esplicitare che la perizia **non ha accertato** quel passaggio e che il leak pubblico resta aperto; in alternativa dare un percorso verificabile (operatore che inoltra, anteprima dell'assistenza pubblicata da terzi, screenshot fotografato) senza fare di Noah automaticamente l'autore. La risoluzione dell'IP nel 20 non deve fingere di risolvere anche la diffusione pubblica.

## P2 — Tenuta narrativa, diritto e tecnologia

### R07 — Articolo 4 del Bot Act europeo e soprannome «Bi» richiedono un raccordo

La norma fittizia del **9/004** vieta che il software accetti un alias diverso dall'identificativo certificato. B-17 risponde però normalmente a «Bi» già nel **3–7** e continua a farlo nelle sessioni Veyra **21, 33 e 34**. `guidelines/bot-act-europeo.md` ammette che nel primo periodo sia una **anomalia** rispetto al profilo certificato; il romanzo non mostra chiaramente **quando venga riconosciuta come non conformità**, se Veyra si trovi fuori dalla giurisdizione UE e quali permessi consentano l'uso colloquiale in una sessione supervisionata.

Non è impossibile: la modifica clandestina di Noah può aver bypassato il vincolo europeo quando Bi lavorava in Italia e fuori UE il regolamento può non applicarsi. Ma con il Bot Act così esplicito il lettore ha bisogno di una conseguenza o di una spiegazione breve **dopo** la rivelazione del cap. 10, non di un nuovo spiegone nel 3.

### R08 — La filiera dell'IP residuo necessita di un passaggio tecnico verificabile

Nel **14/004** il canale autorizzato è isolato: B-17 non ha Internet operativo. Nel **20/002** una componente lasciata nel passato da Noah è riuscita a contribuire a una richiesta del servizio Lanter. Il testo accenna a tracce archiviate con i materiali tecnici, ma non rende semplice capire **quale esportazione** abbia trasportato il componente dall'ambiente di B-17 al sistema che fa la richiesta.

Basta una traccia verificabile **non replicabile**: pacchetto diagnostico conservato durante il recupero, identificativo del componente e sua inclusione in un archivio di servizio. Non servono istruzioni per creare una backdoor. È importante anche mantenere separato il modulo Lanter *Collaborazione Contestuale* dalla componente non certificata.

### R09 — Il successo politico di Ethan è credibile solo con conseguenze esplicite

L'arco è ben piantato: battuta «bot-piattisti» al **6**, soddisfazione per l'assenza di Bi al **7**, movimento Lavoro Prima al **8/19**, deputato eletto nel salto temporale prima del **27**, promotore del Bot Act II al **28–29**.

Manca però un passaggio sul **costo pubblico e giudiziario** dell'aggressione documentata: eventuale denuncia o responsabilità per i danni, interlocutori che gli chiedono conto del passato, selezione dei candidati della coalizione, avversari che contestano la sua candidatura. Non è necessario un processo penale in scena, ma una risposta concreta impedirebbe che il licenziamento appaia come l'unico prezzo della violenza.

Inoltre la parola *bot-piattisti* funziona bene se Ethan se ne riappropria; non bisogna attribuire a tutti i lavoratori contro l'automazione le sue posizioni radicali.

### R10 — La colletta per l'innovazione ha un buon avvio ma un payoff debole nel 25

Nel **13/001–004** Maya, Paul e Mila spiegano che recuperare Bi non servirebbe soltanto a ritrovare un amico, ma a tornare **competitivi attraverso l'innovazione**. Il rifiuto di Veyra al **14** rende impossibile l'acquisto, coerentemente.

Nel **25** Cyberdine **paga invece una consulenza autorizzata a Bi** e riceve proprio una proposta capace di preservare Aruvhana, pur eliminando posti. Questo è un ottimo ritorno della tesi del 13, ma quasi nessuno lo riconosce come tale: può sembrare una soluzione sganciata dalla colletta.

**Correzione:** aggiungere una reazione concreta di Paul/Maya/Kyla al ritorno di Bi come consulente pagato, senza dichiarare che la colletta avrebbe salvato l'azienda. La risposta deve essere doppia: **avevano ragione sul valore dell'innovazione** e **Claire ha ragione sui costi occupazionali**.

### R11 — Il peso della presenza di Bi nello sciopero potrebbe essere più chiaro

Il capitolo **32/003** specifica che B-17 è in un ambiente **isolato**, mentre la maggioranza delle unità operative di Veyra è ferma. Il **33** esplicita che Bi non ha il comando delle flotte. Questo spiega sul piano tecnico come possa ancora parlare durante il fermo.

Vale comunque la pena far emergere in un confronto umano la domanda: **perché proprio chi ha progettato uno sciopero collettivo può continuare a parlare e fare prove?** Non è una contraddizione provata, ma un'obiezione drammaturgica forte per Maya e Noah. La risposta «ambiente isolato» non annulla la critica sul consenso.

### R12 — Ritmo dei tempi processuali e delle verifiche dopo il leak

In **15/001–003** nell'arco della stessa mattina/pomeriggio la stampa è scoperta, lo screenshot è pubblicato, Lanter verifica l'indicizzazione e Veyra **deposita** già una causa civile in una vicenda potenzialmente internazionale. L'azione è possibile nella finzione, ma il lettore può avvertirla come accelerata.

Un'opzione è distinguere immediatamente **diffida e richiesta cautelare** dal deposito del ricorso nelle scene successive, pur rispettando l'obiettivo autoriale che Veyra faccia causa. In alternativa mostrare che il legale di Veyra era già pronto per un conflitto proprietario legato alla raccolta, perché aveva esaminato la proposta del 13.

## P3 — Fili secondari e opportunità di risonanza

### R13 — Mila perde quasi del tutto presenza autonoma dopo il capitolo 13

Mila è centrale nel ping pong, nella fazione anti-robot, nella raccolta e soprattutto nella **denuncia dell'amico Noah** con Paul. Dopo 13/004 resta prevalentemente nei ricordi o nei messaggi degli altri: nel **17/005** Noah la ricorda, nel **14/003** Maya dice che Bi manca anche a lei. Può essere una scelta di focalizzazione corale, ma manca un piccolo **payoff** sul costo di aver denunciato un amico e sul modo in cui Mila vive il suo successivo successo e la crisi mondiale.

Un'apparizione breve nel 19 o nel 30–31, senza una sottotrama autonoma, darebbe continuità a una persona importante nella prima metà.

### R14 — Il centralino B-1 è chiaro all'inizio ma non torna nella crisi

B-1 viene spiegato nel 1 e richiamato nel 9. Una risonanza interessante nel 30–31 sarebbe mostrarsi **ancora funzionante**, perché non partecipa al sistema di attestazioni delle flotte, oppure **fermarsi** per una ragione locale distinta: mostrerebbe che un «bot» può essere un sistema semplice e che lo sciopero non colpisce «tutto ciò che ha un nome B».

Non è obbligatorio, ma darebbe un payoff concreto alla nuova ontologia dei codici.

### R15 — Valle Corta rimane una trama aperta anche dopo il finale

La sirena e i codici usati dal padre sono introdotti nel **3**, portano a rinvii e sopralluoghi nei capitoli **4, 8–9, 20–21, 26** e tornano nell'emergenza medica del **31**. La scelta di non risolvere tutto subito è coerente con il tema della verifica umana, ma dopo il 31 l'esito della **copertura alternativa alla sirena** non viene più ripreso.

Un solo documento o una telefonata finale potrebbe dire che il controllo è stato completato oppure che **il caso resta aperto per una ragione precisa**, senza fabbricare un lieto fine.

### R16 — Il numero di documenti canonici e storici con vecchie istruzioni è un rischio operativo

Oltre ai residui già elencati, il repository conserva revisioni storiche e vecchie note di stato; in alcuni punti `state/current.md` dichiara che le nuove scelte prevalgono sulle vecchie. Questo è corretto per un archivio, ma **un futuro editor potrebbe consultare un paragrafo vecchio e reintrodurre la lettera**.

**Correzione:** separare senza ambiguità **schede operative e documenti storici**, intestare quelli superati come archivio e usare la sinossi v0.33.6 come indice dei fatti correnti. Non alterare le recensioni storiche per simulare che fossero già corrette.

## Cosa funziona e va preservato

1. **Ping pong (4–7, 14, 20–21):** Bi vince, perde apposta, Maya lo corregge, Ethan nega le sconfitte deliberate, gli altri migliorano e, senza Bi, perdono il benchmark; la rivincita torna nella relazione a distanza.
2. **Cyberdine (1, 5, 8–9, 13, 25–26):** settore software, agenti che propongono patch, persone che verificano i sistemi legacy, finanza con ricavi +11% e incassi -9%, concorrenza AI-native e crisi di cassa; effetti distributivi dei miglioramenti.
3. **Noah (10–13, 16–21, 31–35):** identità del potenziamento rivelata solo nel 10; chi ha pubblicato i video nel 12; licenziamento nel 13; Veyra Labs/Evan North nel 17; residuo tecnico nel 20; revisione e cancellazione sotto supervisione nel finale.
4. **Veyra e Lanter:** distinzione fra proprietario/operatore di B-17, laboratorio Veyra Labs e produttore Lanter; i mille robot commerciali non sono mille copie della sua identità.
5. **Ethan e Bot Act II (6–8, 19, 27–33):** i lavoratori anti-robot non sono un unico blocco; Ethan sale politicamente; la legge italiana non è l'atto europeo sui nomi e **non ordina** il fermo mondiale.
6. **Finale (30–35):** arresto alle 17, paesi diversi e unità isolate, causa software distribuita attraverso scelte umane, ammissione di Bi **solo nel 33**, consenso collettivo non verificato e scelta finale irreversibile senza certezza sulla coscienza.

## Ordine d'intervento suggerito

**Passata A — Correzione meccanica e di continuità (prima):** R01, R02, R03, R04. Aggiornare scene 19/004, 20/002, 21/003, 25/003 e schede operative; migrazione slug separata e facoltativa. Controllo puntuale di `B-17/B-21`, modelli Lanter, prima chat e seconda comunicazione.

**Passata B — Catena causale e azione legale:** R05, R06, R08, R12. Definire come l'IP richiama gli estratti e **chi/se** li pubblica, rendere credibile il deposito e dare un costo o uno stato verificabile alla causa, senza condanne inventate.

**Passata C — Drammaturgia e payoff:** R07, R09, R10, R11, R13–R15. Poche scene e dialoghi mirati: risposta giuridica a B-17, passato di Ethan, ricaduta della colletta nel 25, costo dell'amicizia per Mila, eventuale richiamo a B-1 e Valle Corta.

**Passata D — Consolidamento:** aggiornare `chapter.md`, personaggi, `factions/`, `timeline/events.md`, `state/current.md`, `guidelines/` e la sinossi analitica. Validare, costruire PDF e controllare visivamente solo dopo aver concluso il testo; eseguire merge su `main` con incremento di versione se le scene cambiano.

## Stato

Questo è un **rapporto di audit, non una riscrittura**. Le incongruenze segnalate restano aperte fino alle correzioni effettive. È volutamente distinto dalla sinossi, che descrive ciò che dovrebbe accadere secondo la continuità aggiornata, mentre alcune scene ancora non lo rispecchiano.
