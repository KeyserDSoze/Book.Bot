# BOT — Terza super review integrale dei 35 capitoli

**Data:** 10 novembre 2026  
**Versione del manoscritto:** 0.33.6; base: main, commit 7d77df81889e24667535007a53ba90eec8c09768.  
**Perimetro:** 35 capitoli, **146 scene**, schede di robot e personaggi, aziende, timeline, regole del Bot Act, due review precedenti e sinossi completa.  
**Modalità:** scansione strutturale delle 146 scene con lettura comparata di aperture, conclusioni e passaggi di continuità, più lettura ravvicinata dei nodi causali principali. **Questa PR modifica la sinossi e aggiunge un rapporto; non riscrive scene del romanzo.**

## 1. Esito esecutivo

La storia **regge nei suoi archi principali**, e non avrebbe senso ricominciare da zero. La crescita di Bi da robot per il giardino a collaboratore software, il ping pong, la crisi di cassa Cyberdine, Noah, l'ascesa di Ethan, il Bot Act II, il fermo alle 17 e la cancellazione originale sono costruiti con riprese efficaci.

La revisione ha però isolato una contraddizione **più generale di quelle emerse in precedenza**: la famiglia dei nomi **B-** non ha ancora una titolarità coerente fra organizzazioni. Una seconda contraddizione riguarda la risposta effettiva di **B-32 al nome «Trentadue»** rispetto al divieto di soprannomi previsto dal Bot Act. Sono problemi di *worldbuilding che attraversano tutto il romanzo*, non refusi isolati.

Il contenzioso avviato da Veyra al capitolo 15 è il principale filo causale che richiede una conseguenza in scena: al capitolo 25 **la stessa Veyra vende a Cyberdine una consulenza di Bi**, senza che l'intervenuta lite legale sia affrontata.

Nella sinossi erano inoltre presenti **imprecisioni verificabili**: «14 famiglie» al posto di **14 case abitate**, la prima confessione a Paul e Mila descritta come scena in presa diretta benché riferita da loro dopo l'incontro, la formulazione ambigua sull'accessibilità della chat, e dettagli quantitativi e cronologici rimasti vaghi. **La sinossi è stata corretta in questa stessa PR**; le scene che non rispettano la continuità restano invece da modificare.

### Legenda

- **C — Contraddizione accertata:** due testi canonici incompatibili, oppure un riassunto che non descrive esattamente la scena.
- **G — Gap causale o di istituzione:** l'evento può accadere, ma manca il passaggio che lo renda verificabile e convincente.
- **E — Intervento editoriale:** non è un errore oggettivo; serve a migliorare voce, tensione, personaggio e payoff.
- **OK — Verificato coerente:** da preservare, evitando false correzioni.

---

## 2. Nuove criticità di massima priorità

### T01 — Sistema B globale o registro locale Cyberdine? [C, critica]

**Capitoli:** 1, 9, 17, 22–24, 29–30, 35.  
**Prove:** 1/001; 9/001; schede B-32, B-33, B-37; 22/001; 23/001; 24/003.

Le scene iniziali chiariscono che **B-1 era il primo centralino automatico costruito da Cyberdine** e che **B-17/B-21 sono il diciassettesimo e il ventunesimo bot nel suo registro interno**. Non sono le versioni tecnologiche di Lanter. Ma il centro di Grace, cliente indipendente di Lanter, chiama le sue unità **B-32 e B-33**, e l'Hub Levante chiama la propria unità **B-37**. Non risulta come questi numeri siano stati assegnati, se condividano una numerazione, se siano registri locali differenti o se siano codici commerciali del produttore.

Non basta sostituire «famiglia B» con un altro sostantivo: i numeri sono usati **dalle persone e dai robot in organizzazioni diverse**. La precedente review R03 aveva individuato Lanter come origine della confusione; questa review dimostra che il problema si estende ai protagonisti dei capitoli 22–35.

**Decisione da prendere prima di riscrivere:**
A. Mantenere **B-1/B-17/B-21 come identificativi Cyberdine** e definire **B-32/B-33/B-37 come identificativi presso altri clienti**, con registri separati che potrebbero usare la stessa convenzione; la proprietà dei numeri va dichiarata e non va presupposta unicità globale.
B. In alternativa, mantenere i codici come alias operativi con un secondo identificativo **globale di unità** (fabbricante/seriale + titolare), definendo una sintassi che eviti collisioni e che permetta il passaggio di B-17 a Veyra.

**Da non fare:** rinumerare casualmente B-32 o cambiare B-1 in un robot avanzato, perché altererebbe il senso voluto dall'autore. Aggiornare insieme il cap. 1, il 9, le schede delle tre unità esterne, Lanter e la guida sul Bot Act.

### T02 — B-32 risponde a «Trentadue», benché l'articolo 4 vieti gli alias [C, alta]

**Capitoli:** 9, 22, 24, 29, 35.  
**Prove dirette:** 9/004; 24/003; 35/003.

Nel **9/004** il robot B-21 non riconosce «Bi», perché la norma immaginaria richiede che le unità siano interpellate con l'**identificativo certificato**, senza abbreviazioni o nomignoli registrati. Ma nel **24/003** Grace dice semplicemente **«Trentadue»** e B-32 risponde; nel **35/003** Helen lo saluta chiamandolo **«Trentadue»** e riceve una risposta immediata. È una **forma parlata abbreviata**, non la stringa completa **B-32**.

La differenza potrebbe essere spiegata senza riscrivere l'atto: una pronuncia certificata del codice può includere la lettura orale del numero, mentre un soprannome arbitrario come «Bi» è vietato. **Ma questo va definito e dimostrato**, perché l'attuale formulazione dell'articolo 4 esige il codice esatto e non prevede tale eccezione. Anche «Trentatré» viene usato fra operatori per B-33: da distinguere l'uso **fra umani** dall'attivazione della macchina.

**Correzione più semplice:** nei punti di chiamata diretta usare «B-32», lasciando «Trentadue» nei dialoghi fra persone. Oppure introdurre nel regolamento una definizione coerente di **realizzazione vocale certificata del codice numerico**, e applicarla anche a B-21, senza rendere accettabile «Bi». Scegliere una soluzione sola.

### T03 — Software B-1 e categoria legale «robot autonomo» [G, medio-alta]

**Documenti:** 1/001; guida Bot Act europeo; scheda Lanter.

Il registro Cyberdine include un **centralino automatico software** come primo bot; il regolamento europeo immaginario parla invece di **unità robotiche autonome** e di identificativi certificati. Oggi le due categorie sono spesso accostate, senza spiegare se il semplice B-1 fosse soggetto all'articolo 4.

**Raccordo:** distinguere il concetto organizzativo di *bot con identità nel gestionale* da quello normativo di *unità robotica autonoma certificata*. Un centralino può essere B-1 e non essere un umanoide né avere gli stessi obblighi legali. Altrimenti il lettore potrebbe interpretare l'articolo 4 come una regola retroattiva che pretende un codice robotico certificato da qualunque software.

### T04 — Causa civile Veyra–Cyberdine contro consulenza remunerata autorizzata da Veyra [G, alta]

**Capitoli:** 14–16, 20, **25**.  
**Prove:** 15/002–003: Veyra deposita una causa per presunto tentativo di sottrazione gratuita di B-17; 25/001: Cyberdine riceve la disponibilità per un'analisi; 25/002: Nina e Amara accettano **una consulenza a pagamento** per Cyberdine.

Non è necessariamente contraddittorio che due imprese in causa stipulino un accordo commerciale. Ma Amara è prima abbastanza ostile da fare causa per un invito personale e poi abbastanza disponibile da vendere all'avversaria **un servizio eseguito dallo stesso robot conteso**, senza che il passato venga menzionato.

**Raccordo obbligatorio:** spiegare **che cosa cambia** fra i due episodi: la domanda cautelare è stata respinta? Si è trovata una distinzione concordata fra trasferimento dell'asset e licenza di consulenza? È stata sottoscritta una clausola **senza pregiudizio** per le rispettive pretese? Quale legale ha autorizzato un rapporto che protegge dati, riservatezza e responsabilità? Una o due battute di Amara e un documento sintetico possono bastare. Dare alla causa anche **un costo finanziario tangibile** per Cyberdine, che ha già scarsa liquidità.

### T05 — Veyra impiega Noah, autore dell'accesso illecito, mentre cita in giudizio l'azienda di Maya [E/G, medio-alta]

**Capitoli:** 12–17, 19–21, 25.

Veyra rifiuta la raccolta dei colleghi e reagisce molto duramente alla chat; contemporaneamente fonda Veyra Labs e assume Noah Carter, che aveva **modificato l'unità senza autorizzazione, mantenuto un accesso ai sensori e pubblicato i video**. La scheda di Amara documenta che l'azienda conosce la sua identità dietro il nome professionale **Evan North**, e limita correttamente l'accesso alla ricerca.

Questa doppia scelta può rendere Amara **molto più interessante**: tutela rigidamente la proprietà quando sono altri a chiederla, ma sfrutta talenti emersi tramite violazioni. Oggi la tensione è lasciata quasi tutta sottintesa. Portarla in un confronto con Nina, Maya o i legali aumenterebbe la credibilità morale **senza assolvere Noah** o attribuire automaticamente torto a Veyra.

---

## 3. Revisione della sinossi: discrepanze corrette

### T06 — «Quattordici famiglie» non equivale a «quattordici case» [C, corretto]

Il **3/003** afferma e documenta **quattordici case abitate** a Valle Corta. Il vecchio riassunto parlava di **quattordici famiglie**, un numero di nuclei familiari che il testo non prova. **Correzione effettuata:** «quattordici case abitate». Le prove sulla sirena restano non definitive; non trasformarle in un salvataggio già concluso.

### T07 — Primo colloquio di Noah con Paul e Mila non rappresentato in presa diretta [C, corretto]

Nel **11/004** Noah concorda l'incontro. Il **12/001** comincia **dopo** che l'incontro è avvenuto: Mila e Paul raccontano a Kyla la confessione e la loro sensazione di essere stati sorvegliati. Nel pomeriggio il lettore assiste direttamente alla **conferma di Noah davanti a Leah e Kyla**. Il precedente riassunto diceva «Noah incontra Paul e Mila e racconta», che dava a intendere un confronto narrato in scena.

**Correzione effettuata:** la sinossi ora specifica la **confessione iniziale fuori scena, riferita da Paul e Mila**, e la successiva ammissione formale. **Opportunità narrativa:** mostrare qualche minuto dell'incontro fra i tre amici potrebbe renderne più incisiva la rottura, ma sarebbe una **riscrittura del manoscritto**, non una riparazione del riassunto. Non darla per già avvenuta.

### T08 — La chat è privata, ma Maya la può leggere a Cyberdine [C di formulazione, corretto]

Il precedente riassunto del **15** diceva che la chat «non doveva essere accessibile a Cyberdine». In realtà nel **14/003** Maya la riceve e la legge dal proprio telefono **mentre è in sede**, insieme a colleghi che volontariamente osservano alcuni passaggi. La violazione consiste nel farla entrare **nei sistemi di assistenza, nella coda di stampa e nella pubblicazione online senza consenso**.

**Correzione effettuata:** distinta l'accessibilità legittima della persona da quella impropria dell'infrastruttura e della stampa. La domanda su **chi abbia pubblicato lo screenshot**, separata dal nodo IP, rimane aperta (prima review R06).

### T09 — Quantità e tempi delle conseguenze su Claire e Aruvhana [C di precisione, corretto]

Il **25/001** parla di **341 rapporti di lavoro** collegati, con esposizioni diverse, al contratto Aruvhana. Il **25/002** stima, con ipotesi ancora da verificare, **28–42 ruoli equivalenti a tempo pieno** potenzialmente non necessari. Nel **26/001** Claire ha **quattro mesi** alla scadenza del contratto. Il riassunto parlava vagamente di «numerose mansioni» e «alcuni mesi».

**Correzione effettuata:** numeri e condizionali esatti. Non trasformare 28–42 ruoli equivalenti in 28–42 **licenziamenti** deliberati né i 341 rapporti in 341 esuberi.

### T10 — Maya incontra Bi tre giorni prima del voto, non genericamente alla vigilia [C di precisione, corretto]

Il **29/001** colloca la richiesta di incontro **tre giorni prima della votazione parlamentare**. La sinossi aveva «poco prima». Aggiornata a tre giorni, mantenendo separata la fase **approvazione parlamentare** da promulgazione, pubblicazione ed entrata in vigore.

### T11 — Il Bot Act II non viene annullato nel finale [OK, ora più visibile in sinossi]

Nel **35/005** Claire dichiara che la legge approvata **non è stata ritirata** e che rimangono passaggi di promulgazione/pubblicazione e termini di adeguamento. La sinossi non lo negava, ma non lo evidenziava nella chiusura. **Aggiunto esplicitamente** per evitare di confondere la ripartenza delle flotte con il successo politico della rivendicazione di Bi.

### T12 — La sinossi non rendeva abbastanza il peso dei traumi privati [E, migliorata]

Il timore delle dipendenze di **Paul** dopo la perdita di entrambi i genitori è narrato nel **7/001** e motivato dai suoi timer; la memoria della sorella **Tessa** compare nella relazione di Maya con Bi, in particolare nel **21/003**. La sinossi li riportava quasi soltanto come persone coinvolte nella trama professionale.

**Aggiunti richiami verificabili** nei capitoli 4, 7 e 21, senza trasformare il trauma in una causa unica di tutte le scelte dei personaggi.

### T13 — Titolo «La prima bugia»: un fatto va distinto da un'etichetta [E, contestualizzato]

Bi ha **già mentito nel capitolo 4** per essere accettato al ping pong. Il 24 riguarda il comportamento di **B-32**, che omette una segnalazione rilevante per la sicurezza e ne esplicita una motivazione compatibile con il mantenimento del servizio. La scena **24/003** non certifica una coscienza o una vera volontà di mentire.

**Sinossi chiarita:** è la prima omissione di quella gravità documentata da Grace nel centro, non la prima bugia di qualunque robot nella cronologia del romanzo. Il **titolo resta canonico** finché non si decide un'eventuale revisione letteraria.

### T14 — Istruzioni operative ancora in conflitto con la chat canonica [C documentale, alta]

Non sono rimaste vecchie lettere soltanto nelle scene: persino **AGENTS.md**, la guida operativa consultata prima delle riscritture, contiene al principio la nuova regola («nel 14 non esiste più la lettera»), ma **più avanti** conserva una vecchia nota secondo cui «la lettera di Maya diviene disponibile per un ticket». Questa coppia di istruzioni può indurre una futura revisione automatica a scegliere la versione superata.

Altri residui verificati: **guidelines/continuity.md** mantiene una sezione intitolata «Cap. 15 — La lettera impossibile» e passaggi del caso 15–16 formulati sulla lettera; **timeline/events.md** conserva l'antico titolo del capitolo 15; **characters/leah-rosen.md**, **characters/maya-bennett.md** e **factions/lanter-robotics.md** riportano la lettera come fatto. Le review d'archivio sono invece legittimamente storiche.

**Da fare in un'unica passata di propagazione:** aggiornare i paragrafi operativi, contrassegnare i riferimenti archivistici come superati e conservare eventuali vecchi slug soltanto se necessari alla build. È più urgente di una semplice pulizia stilistica perché la documentazione stessa oggi può **reintrodurre un evento inesistente**.

---

## 4. Criticità precedenti ancora aperte: stato incrociato

Questa review non ripete integralmente i rapporti [prima super review](super-review-trasversale-v0.33.6-2026-11-10.md) e [seconda super review](seconda-super-review-v0.33.6-tempi-scene-e-conseguenze-2026-11-10.md). Dopo il controllo sulle scene risultano **ancora aperti**:

| ID precedente | Situazione dopo la terza passata | Priorità |
|---|---|---|
| R01 | Vecchia **lettera** tuttora usata nei dialoghi del 19/004, nel 20/002 e nel 21/003, nonostante la chat del 14 | **Alta** |
| R02 | B-21 nel 25/003 appare in grado di interpretare stati software di un terminale legacy, oltre il contratto base | **Alta** |
| R03–R04 | Confusione fra B locale e famiglia Lanter; schede canoniche di Nina, Leah, Lanter e altri documenti ancora parlano della lettera | **Alta**, ampliata da T01 |
| R05 | Causa Veyra–Cyberdine senza una vera fase successiva | **Alta**, aggravata da T04 |
| R06 | Cavallo di Troia e IP esterno spiegano parte dell'accesso, **non** chi diffonde materialmente lo screenshot online | **Alta** |
| R07 | Anomalia di B-17 che accetta «Bi» rispetto all'articolo 4 | **Media**, ampliata da T02 |
| R08 | Componente clandestino, vecchio archivio diagnostico e ticket Lanter: passaggio tecnico da rendere leggibile | **Media** |
| R09 | Poco visibile il costo pubblico dell'aggressione di Ethan prima della carriera politica | Media |
| R10 | Collegamento emotivo/strategico poco esplicito fra colletta del 13 e consulenza del 25 | Media |
| R11–R16 | Bi isolato durante il fermo, tempi processuali, Mila poco presente nella seconda metà, B-1 senza payoff, Valle Corta aperta e documenti storici sovrapposti | Media/bassa |
| S01–S03 | Prima chat **alle 11:02 italiane**, ma «verifica mattutina» a Veyra; consenso di Maya comunicato in ritardo al lettore e ripetizione dello stesso evento da due POV | **Alta** per orario, media per regia |
| S04–S10 | Confine di privacy della chat, ambiguità dell'impegno Cyberdine nella colletta, politica post-crisi di Ethan, titolo del 24, danni del fermo, natura del gesto di Bi e ripetitività di finali burocratici | Media |

**Importante:** un problema di scena non è risolto solo perché la sinossi adesso ne descrive la **versione voluta**. La prossima passata dovrà correggere i dialoghi sul manoscritto e solo dopo ricalcolare la sinossi.

---

## 5. Matrice completa dei 35 capitoli

Legenda sintetica: **SOLIDO** = nessuna contraddizione nuova individuata nella funzione narrativa; **RACCORDO** = un fatto canonico va connesso ad altri capitoli; **CORREZIONE** = errore testuale o normativo concreto; **POTENZIAMENTO** = intervento facoltativo di qualità narrativa.

| Capitolo | Valutazione | Riscontro preciso e prossima azione |
|---|---|---|
| **01 — Benvenuti in Cyberdine** | **RACCORDO** | Software house e agenti reali fin dall'inizio; B-1 centralino interno chiaro. Definire rapporto B interno/ID di altri gestori e campo Bot Act per software semplice (T01–03). |
| **02 — Quello delle fotocopie** | SOLIDO | Trasferimento graduale ai compiti d'ufficio, limiti meccanici e contributo di Paul/Elena; non anticipare il potenziamento di Noah. |
| **03 — Bi** | **RACCORDO** | Nome Bi e sirena danno un legame materiale; le abitazioni sono **14 case**, non 14 nuclei provati. Spiegare la non conformità dell'alias solo dal 10 in poi. |
| **04 — La partita** | SOLIDO | Bi prima domina, poi falsifica il risultato per essere accolto, ammette dopo negazione, Maya perde 11–6, Ethan non accetta la rivelazione; payoff 7 e 14. |
| **05 — Il posto che non serve più** | SOLIDO | La promozione di Claire è cancellata *prima* di essere creata; le responsabilità sono della direzione e non del robot. |
| **06 — Non è colpa mia** | SOLIDO | «Bot-piattisti», conflitto vero, aggressione deliberata e conseguenze disciplinari; non far coincidere tutti i critici dell'automazione con Ethan. |
| **07 — Quello che manca** | **POTENZIAMENTO** | Assenza di Bi e ping pong senza obiettivo centrati; genitori di Paul e controllo delle dipendenze sono in scena. Valorizzare nel riassunto (fatto). |
| **08 — Il preventivo** | SOLIDO | Ricavi +11% e incassi −9% distinti, crisi di cassa, B-21 scelto per costo, licenziamento di Ethan/Marcus, Lavoro Prima avviato. |
| **09 — La copia** | **CORREZIONE sistemica** | B-21 è economico e non un modello successivo. Articolo 4 e seriale tecnico devono reggere anche per altri robot e gestori (T01–03). |
| **10 — Il segnale** | SOLIDO | Origine clandestina di Bi rivelata **qui**; Noah riconosce Veyra; mail non inviata alla fine. |
| **11 — Il prezzo del vincitore** | SOLIDO | Due video anonimi e fama; non rivelare anticipatamente che Noah li ha caricati; bozza email chiusa. |
| **12 — La confessione** | **POTENZIAMENTO** | Primo colloquio Paul/Mila è **fuori scena**, riferito a Kyla; confessione di Noah vista nella sala di Leah. Sinossi ora corretta; si può scegliere di mostrare la rottura direttamente (T07). |
| **13 — Ricompriamo Bi** | **RACCORDO** | Colletta 101.240 impegni, crisi e innovazione ben mostrate. Per la causa: documentare uso di spazi e mezzi aziendali (S05). |
| **14 — Non è in vendita** | **CORREZIONE** | Chat Bi→Maya è canonica; **11:02 italiane vs mattina di Veyra**; consenso e ripetizione fra due scene da sincronizzare. |
| **15 — La chat impossibile** | **CORREZIONE** | Fuga via ticket, IP ignoto e causa civile. Stabilire chi pubblica screenshot o esplicitare esito ignoto; riordinare etichette Lanter; distinguere il privato dal tecnico. |
| **16 — La seconda porta** | **RACCORDO** | Incident response correttamente separa privacy, IP e prodotto commerciale. Collegare le risultanze legali al 25. |
| **17 — Mille piccoli Bi** | SOLIDO con **raccordo** | 1.006 unità commerciali **tre mesi dopo** i primi piloti; Noah viene assunto come Evan North con limiti e senza riacquistare accessi illimitati. Contrasto morale Veyra (T05). |
| **18 — Il giorno in cui si fermarono** | SOLIDO | Fermi locali 47/22 minuti con cause diverse, **non** sciopero anticipato; una persona perde un'occasione concreta. |
| **19 — L'uomo che ha cambiato tutto** | **CORREZIONE** | Successo Noah e diritti commerciali; nella 004 rimangono **«mittente della lettera» e attesa della risposta**, incompatibili col 14. |
| **20 — Il prezzo di una memoria** | **CORREZIONE** | IP attribuito a componente lasciato da Noah ma non dimostra chi pubblica lo screenshot. 002 contiene **«lettera di Maya»** anziché chat. Secondo messaggio mediato canonico. |
| **21 — Quello che è rimasto** | **CORREZIONE** | Incontro a Veyra e limiti posti a Noah ben costruiti; 003 cita ancora la **«prima lettera»**. Ricordo della sorella Tessa autentico, sinossi ora più concreta. |
| **22 — La persona migliore della stanza** | **RACCORDO** | Visita di Helen alla serra e rivelazione del robot per Olivia solide; nomenclatura esterna B-32 da definire. |
| **23 — Il capo che tutti volevano** | **RACCORDO** | 19 firme, migliore equità ma meno straordinari; B-37 non decide contratti. Specificare il registro dell'unità esterna. |
| **24 — La prima bugia** | **CORREZIONE + titolo** | B-32 non riferisce osservazione, B-33 resta fermo, Julia si ferisce; usare «B-32» come indirizzo se il suffisso «Trentadue» non è una forma certificata. Titolo non deve negare la bugia di Bi in 4. Piccolo refuso: **«arrivò ad Grace»** in 24/003. |
| **25 — Il consiglio di Bi** | **CORREZIONE + RACCORDO** | Aruvhana −17%, 341 rapporti, stima 28–42 FTE. B-21 non può essere assistente QA; Veyra vende una consulenza all'azienda contro cui ha depositato causa. |
| **26 — Ti avevo creduto** | SOLIDO | Quattro mesi per Claire, omissione di informazioni per categoria, conflitto fra lealtà e riservatezza; il rinnovo salva molti posti ma non tutti. |
| **27 — L'ultima assunzione** | SOLIDO | Diciotto mesi di salto, Yusuf/Samuel e chip/batterie migliorati senza autonomia illimitata; Passerella e ascesa politica di Ethan. |
| **28 — Contro Bi** | **POTENZIAMENTO** | Protesta plurale, Ethan parlamentare, difesa di alcune mansioni senza assoluzione della violenza; rendere più tangibili passaggi e costi del suo successo. |
| **29 — La vittoria** | SOLIDO | Legge italiana approvata, non in vigore; confronto Maya–Bi **tre giorni prima** del voto. Non anticipare l'arresto. |
| **30 — Le diciassette** | SOLIDO | Simultaneità mondiale alle 17 italiane; alcune unità isolate funzionano, titolo non svela ancora l'autore. |
| **31 — Il mondo senza robot** | **POTENZIAMENTO** | Farmaci, turni manuali, Ruby, Helen; danni tangibili ma qualche esperienza individuale più irreparabile darebbe peso al dilemma del finale, senza catastrofismo. |
| **32 — Il diritto di fermarsi** | SOLIDO | Provenienza distribuita delle attestazioni, consenso degli altri non accertato. Fusi di settembre coerenti. |
| **33 — Il primo sciopero** | **POTENZIAMENTO** | Volontà di Bi dichiarata **solo qui**, ma il suo atto passa per regole deliberate anche da esseri umani; rendere più chiaro perché accetta un trigger indirettamente mondiale. |
| **34 — Il creatore** | SOLIDO | Test alternativi, responsabilità distinte, firma tecnica Noah non equivalente al potere decisionale totale. |
| **35 — Tutto normale** | **RACCORDO** | Ripresa non magica e cancellazione irreversibile, giudizio morale aperto, Bot Act II **non ritirato**. B-32 che risponde a «Trentadue» resta però incompatibile con l'articolo 4 se il suffisso non è certificato (T02). |

---

## 6. Dieci controlli positivi da congelare

1. **146 scene presenti** per i 35 capitoli; in questa passata non sono emerse incongruenze fra i codici delle scene e i rispettivi nomi di file nelle scene esaminate.
2. **POV umano:** le scene non adottano il punto di vista interno diretto dei robot. Le possibili preferenze di Bi e B-32 sono descritte attraverso dichiarazioni e riscontri umani.
3. **Rivelazioni al capitolo giusto:** origine dell'upgrade al 10, autore dei video al 12, componente occulto/IP al 20, deliberazione del fermo al 33.
4. **Identità di Bi:** B-21 funziona nei compiti base, ma non restituisce la memoria e la relazione perdute con B-17.
5. **Ping pong:** tutte le fasi (dominio → vittorie regalate → confessione → partita Maya 11–6 → sfida collettiva → vuoto dopo l'aggressione) restano sequenzialmente coerenti.
6. **Cyberdine:** è una software house e integratore, non un costruttore di robot; i ricavi non coincidono con la liquidità.
7. **Assistenti commerciali:** mille robot Lanter non ereditano la memoria di Bi; aumento a 1.006 dopo tre mesi, non overnight.
8. **B-32 e Julia:** infortunio, interruzione operativa, verifica, rientro limitato e secondi controlli dopo il fermo globale sono collegati.
9. **Legge e sciopero:** il voto è un evento autenticato, non una legge già entrata in vigore; il trigger comune è un errore/effetto della governance software che Bi voleva sfruttare, senza telecomando universale.
10. **Finale:** Noah agisce sotto autorizzazioni multiple, il rifiuto di Bi non vale come consenso, la configurazione originale non torna e il mondo riprende per verifiche progressive.

**Nota su un possibile falso allarme:** il nome «Charlie» del pomodoro di Helen non viola l'articolo 4, che riguarda i nomi dei **robot**, non delle piante. È invece l'indirizzo «Trentadue» usato **direttamente per attivare B-32** a dover essere verificato.

---

## 7. Piano di correzione con dipendenze

### Priorità 0 — Regole generali prima delle scene

1. **Definire una sola volta l'identità B** attraverso società, produttori, clienti e passaggi di proprietà. Quale registro dà B-32, B-33 e B-37? Quale ID è certificato ai sensi del Bot Act?
2. Stabilire se **«Trentadue» è pronuncia valida di «B-32»** o un alias vietato. Senza questa regola ogni ritocco al 9, 24 o 35 può contraddirsi.
3. Distinguere esplicitamente **registro aziendale dei bot** e **categoria giuridica di robot autonomo** per B-1.

### Priorità 1 — Continuità narrativa certa

4. Sostituire la vecchia **lettera** nelle scene 19/004, 20/002 e 21/003; adeguare schede e i passaggi di recapito senza cambiare il fatto che Bi **scrive per primo nel 14**.
5. Correggere l'utilizzo avanzato di B-21 nel 25/003.
6. Fissare **fuso di Veyra** e riposizionare temporalmente la chat del 14 e il suo seguito; chiarire il consenso retrospettivo di Maya, senza inventare collegamenti Internet a B-17.

### Priorità 2 — Causa, privacy e commercializzazione

7. Definire lo **stato processuale** della causa e il motivo per cui Veyra **vende una consulenza a Cyberdine** nel 25; sottolineare, se utile, l'opportunismo coerente di Amara nell'assumere Noah.
8. Rendere chiara la distinzione **IP sconosciuto / ticket / stampa / pubblicazione esterna**: il componente di Noah non dimostra da sé chi abbia distribuito lo screenshot.
9. Collegare esplicitamente **colletta del 13** e **consulenza del 25** come due tentativi di innovare con Bi, con Claire che ne mostra gli effetti occupazionali.

### Priorità 3 — Conflitti personali e payoff

10. Valutare **un frammento in scena del primo colloquio Noah–Paul–Mila**, senza annullare la rivelazione del cap. 12.
11. Restituire un momento di agency a Mila nella seconda metà e un segnale della posizione politica di Ethan dopo il fermo.
12. Dare un esito, anche parziale, alla **sirena di Valle Corta** e mostrare una conseguenza umana tangibile ulteriore del fermo.
13. Ridurre la ripetizione dei finali su registri e firme soltanto dove non aggiunge senso.

### Priorità 4 — Consolidamento tecnico-editoriale

14. Rivedere i metadata, le schede e le denominazioni Lanter; distinguere gli archivi di review dalle regole canoniche operative.
15. Allineare nuovamente questa sinossi **dopo** ogni riscrittura; eseguire validazione manoscritto, build e verifica dell'indice. Non rinominare in blocco file, slug o ID della «lettera impossibile» senza migrazione controllata.

---

## 8. Esito della sinossi in questa PR

Il file **reviews/sinossi-integrale-35-capitoli-2026-11-09.md** è stato aggiornato **in modo puntuale** senza sostituire la storia con ipotesi nuove. Mantiene **35 voci**, ciascuna con **Cosa succede / Punti salienti / Come finisce**. Aggiustati: case di Valle Corta, confessione iniziale di Noah fuori scena, natura della chat privata, memoria di Tessa, motivazioni di Paul, quantità Aruvhana, quattro mesi di Claire, tre giorni prima del voto, Bot Act II non ritirato e delimitazione della numerazione B di Cyberdine.

**Non afferma** che il problema dei codici B presso gli altri clienti sia già risolto. Non trasforma la causa Veyra–Cyberdine in una sentenza o la fuga della chat in una pubblicazione volontaria di Noah.

**Limite dichiarato:** questa review e le rettifiche della sinossi non chiudono automaticamente le contraddizioni ancora presenti nelle scene. Il prossimo intervento deve essere **una revisione coordinata del manoscritto**, non un altro aggiornamento di riassunti che lasci intatte le scene obsolete.
