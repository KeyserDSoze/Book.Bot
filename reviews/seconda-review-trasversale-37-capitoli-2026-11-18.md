# Seconda review trasversale — *Bot*, 37 capitoli

**Data:** 18 novembre 2026. **Base:** `main`, commit `99f5f0bf8ebf520f3678661be37b320c574e4374`.  
**Relazione con la prima review:** [review-integrale-37-capitoli-2026-11-18.md](review-integrale-37-capitoli-2026-11-18.md). Questo documento approfondisce in particolare **l'affidabilità del canone, le responsabilità non raccontate, le biografie e il nesso tecnico-politico**. Le osservazioni sono divise in *incongruenze accertate*, *punti narrativi da irrobustire* e *falsi allarmi esclusi*.

## A. Incongruenze accertate (prima degli interventi di prosa)

### A1 — Il canone attivo dice contemporaneamente che il romanzo termina al 20, al 35 e al 37

**Gravità:** critica per le prossime riscritture e per gli agenti/editor che consultano i documenti.

- `AGENTS.md` prescrive di consultare obbligatoriamente `state/current.md`, `timeline/events.md` e `guidelines/continuity.md`. Specifica correttamente **37 capitoli**, nuova scena 19–20, legge al 31, stop al 32, rivelazione al 35, fine al 37.
- Il frontmatter di `state/current.md` dichiara ancora `through_chapter: chapter:022-il-prezzo-di-una-memoria` e `through_scene: scene:022-il-prezzo-di-una-memoria:005-la-risposta-prima-del-buio`, mentre l'intestazione del testo dice «dopo il capitolo 20». Più avanti compaiono l'istruzione **«Il romanzo termina ancora al capitolo 20»** e l'affermazione **«ROMANZO COMPLETO AL CAPITOLO 35»**. La prima pagina è aggiornata a 37, ma le parti successive sono presentate come stato, non isolatamente come memoria d'archivio.
- `guidelines/continuity.md` ha sezioni che collocano la rivelazione **al capitolo 33**, anziché al **35**; in altri punti parla delle conseguenze prima del capitolo 31 secondo la vecchia numerazione.
- `characters/noah-carter.md` colloca la ricostruzione del cavallo di Troia **nel capitolo 20**, mentre nel manoscritto attuale accade **al 22**.
- `chapters/032-le-diciassette/chapter.md` conserva nelle note precedenti la regola «non rivelare ... prima del capitolo 31», numero ormai anteriore all'evento stesso: il guardrail canonico aggiornato deve indicare **35**.
- `chapters/002-quello-delle-fotocopie/chapter.md` elenca la progressione «5, 1, 2, 3, 4», mentre i file canonici sono effettivamente `001`–`005`.
- `timeline/events.md` è un documento cumulativo di decine di migliaia di caratteri, che conserva dettagli di revisioni precedenti, inclusi elementi non più attuali accanto ai nuovi eventi canonici. Non tutti i suoi paragrafi sono falsi, ma un lettore automatico potrebbe trattare come attuale un'istruzione superata.

**Proposta operativa:** creare una *cronologia operativa breve, una sola versione valida*, con stato `through_chapter: chapter:037-tutto-normale`, mappa numerica e soli fatti accertati. Spostare note di revisione precedenti in un'area chiaramente **storica/non normativa**. Semplificare `AGENTS.md` affinché dia precedenza ai testi canonici e al riepilogo attuale, non alle appendici archiviate. Non eliminare le vecchie review: restano utili come documentazione del lavoro.

### A2 — La release passa la validazione del manoscritto ma sbaglia ancora la chiusura dell'edizione

La prima review ha rilevato tutti i punti. Qui la priorità viene confermata dal log effettivo della run 44276706145: `tools/validate.py` passa con **37 capitoli e 156 scene**; `tools/build.py` produce i formati; fallisce `tools/check_edition.py` perché si aspetta **36 immagini anziché 38**. Soprattutto `tools/build.py` e `tools/build_docx.py` impaginano deliberatamente la frase **«Tutto tornò normale.»** dopo il capitolo **35** invece che dopo il **37**. Si tratta di un rischio editoriale diretto, non di un warning estetico. Inoltre `tools/artwork.py` associa ancora «lamp» al capitolo 35.

**Proposta:** una PR tecnica separata e un test che legga il numero finale dai capitoli `canon`, controlli che la frase finale compaia **una volta** nel punto corretto e che le immagini non abbiano motivi rimasti traslati.

### A3 — Caporali annidate nel flashback

In `chapters/020-l-ultimo-giorno/002-la-casella-vuota.md` la battuta di Kyla contiene caporali dentro caporali: `«Se compriamo l'unità, non possiamo mettere tutta la colonna sotto «ore risparmiate»»`. La validazione superficiale dei segni di dialogo non rileva necessariamente il problema. Usare corsivo oppure virgolette secondarie per il testo della colonna, mantenendo `«…»` soltanto per la battuta.

## B. Nodi narrativi da irrobustire senza alterare la trama

### B1 — Ethan paga il lavoro, ma le conseguenze esterne dell'aggressione rimangono fuori campo

**Scene:** 6/003, 7/003, 8/001, 19/002, 30/001.

Ethan e Marcus sono licenziati e l'accertamento aziendale è presente. In 8/001 Victor allude in modo credibile a eventuali profili **esterni agli accertamenti aziendali**, che non riguardano la plenaria. Poi il lettore non viene messo al corrente di alcun esito o stato minimo riguardo a danni materiali, responsabilità verso il proprietario del robot, possibili denunce o accordi con assicurazioni. **Non è necessario inventare un processo né una condanna.** Ma quando un aggressore ripreso dalle telecamere diventa deputato, una singola domanda pubblica circostanziata e una risposta limitata ai fatti renderebbero meno artificiale la distanza tra l'episodio e la sua legittimazione politica.

La vicenda di Marcus non va assorbita da Ethan: se lo vediamo solo come complice e poi scompare del tutto, la distribuzione delle conseguenze appare asimmetrica. Può bastare un richiamo non assolutorio alla situazione distinta dei due.

### B2 — La moglie di Martin è reale per una riga e poi sparisce

**Scene:** 20/001–004, 19/001–004; scheda `characters/martin-walsh.md`.

In 20/001 l'uscita incentivata è stata esaminata «riga per riga da lui e da sua moglie». Nei successivi episodi ambientati a casa e nelle riunioni della famiglia non viene mostrata né citata di nuovo. Non è dimostrata un'incongruenza biografica (potrebbe essere assente per motivi validi), ma **il vuoto viene percepito** perché la decisione economica di Martin dovrebbe cambiare la vita della famiglia. Occorre decidere chi sia: ancora presente in casa, separata, lontana, morta successivamente? Non aggiungere una biografia drammatica come scorciatoia. Una presenza minima nella scena 20/003 o nel presente del 19 basta a rendere leggibile la situazione.

Owen e Leo esprimono posizioni proprie, ma soprattutto rispondono al problema economico di Martin. Leo scrive il verbale, buon primo atto di autonomia: mostrargli in seguito un'azione concreta **non decisa dal nonno** (una proposta di apprendistato diversa o un dissenso sulle misure di Ethan) farebbe avanzare l'arco generazionale.

### B3 — La strada politica è credibile nei dati ma non ancora pienamente nei costi

La scena 19/002 mostra bene la sala improvvisata, l'opposizione di chi usa robot sul lavoro e la domanda diretta sui calci a B-17; 19/003 distingue contatti, iscrizioni e disponibilità effettiva; 19/004 documenta voti, astenuti e cassa. Sono scene **molto riuscite**, e non vanno riscritte solo per aggiungere violenza.

Nei capitoli 21 e 25–29, però, Martin torna soprattutto come nome citato. Proporre due brevi scene o scene rielaborate che mostrino: (1) un tentativo pubblico fallito o un confronto con un'impresa che risponde con dati verificabili; (2) un vero compromesso fra Ethan, Martin, Leo e lavoratori che non chiedono un divieto. Il passaggio alle elezioni nel salto di 18 mesi rimane lecito; gli serve una cicatrice politica osservabile.

### B4 — Il controllo antiurto tolto da Noah va distinto dalla sicurezza non disattivabile

La sequenza del 2/005 è un **arresto protettivo dopo urto**, non la somma di tutti i sistemi di sicurezza del robot. In 10/001 Noah dice che ha soppresso la disattivazione automatica da impatto; in 6/003 B-17 non si raccoglie durante l'aggressione. Questo è il collegamento voluto e funziona moralmente, ma un lettore tecnico potrebbe domandare come uno sviluppatore applicativo abbia potuto disabilitare una protezione certificata e lasciare intatti controllori indipendenti, limiti di forza e altri arresti. Non serve un manuale: basta definire **la protezione logica di ripiegamento e sospensione** come livello supervisore configurabile in ambiente di prova, separato dai limitatori fisici indipendenti. Questo preserva la colpa di Noah senza trasformare l'intero dispositivo in un oggetto senza freni.

### B5 — I passaggi fra prova Veyra, Passerella e blocco mondiale hanno indizi, ma richiedono una data causale più chiara

**Scene:** 27/002, 29/003, 34/002, 35/001–002.

Indizio positivo già presente: in 27/002 Bi formula `incarico non vietato ≠ disponibilità attestata`. In 29/003 Mei nota i due campi distinti e richiede la prova su una notifica normativa non pertinente alla giurisdizione del sito. In 34/002 troviamo firme umane e riuso di una referenza non più adatta. In 35/001 il voto italiano viene riassunto erroneamente come cambiamento generale di condizioni di impiego, con rivalidazione globale alle 17:00.

La catena è dunque **ricostruibile** e non è un buco magico. Per rafforzare la sorpresa retrospettiva senza svelare Bi, rendere temporalmente esplicito **quando la bozza di norma Bot Act II era già nota ai fornitori** e quando qualcuno ampliò il significato da *per sito/giurisdizione* a *globale/collettivo*. Le firme devono attestare scelte reali, e la richiesta di test ignorata da Mei nel 29 deve avere conseguenze verificabili (non significa che fosse autorizzata a bloccare da sola tutti i rilasci).

### B6 — I traumi personali sono preparati, ma vanno distribuiti con parsimonia

Le schede del cast contengono la morte della sorella **Tessa** di Maya e la storia dei genitori di Paul, entrambi deceduti dopo dipendenze. Sono elementi già usati in scena: Maya e Daniel ne parlano nel 22/004; in 4/002 Paul guarda il timer del gioco, in 9/001 ha comportamenti di controllo sull'uso degli strumenti. Il contrasto fra memoria, lutto e dipendenza è concreto e utile.

Non aggiungere monologhi riassuntivi negli esordi. Si può però valutare un dettaglio precursore non esplicativo di Tessa in 3/003 o 7/004: la sua perdita motiva la diffidenza istituzionale di Maya, ma compare relativamente tardi nella narrazione. Paul non deve diventare uno stereotipo moralista: la severità verso le dipendenze può produrre un errore concreto nelle relazioni personali, non soltanto una virtù della disciplina.

### B7 — Titoli, ritmo e finali richiedono gerarchia, non uniformità

Il capitolo 4 ha circa **7.800 parole** e il 8 circa **7.500**, contro capitoli fra 2.300 e 3.200 nella parte centrale. Lo scarto non è automaticamente un difetto; il ping pong ha una funzione fondativa. Ma gli atti con più documentazione non devono sembrare più corti o meno intensi perché l'autore anticipa le conclusioni. La scena 37/004 sul noccioleto è una miniatura di **circa 174 parole**: potrebbe essere un taglio ritmico efficace, non occorre allungarla a forza. L'epilogo corale va revisionato come **sequenza**, non normalizzato per wordcount.

La prima bugia raccontata nel libro è la partita falsata di Bi al 4; il titolo del 26 riguarda l'omissione di B-32 in una struttura assistenziale. Senza un ancoraggio chiaro nel testo o nel titolo, il lettore può percepire una falsa prima volta.

## C. Falsi allarmi verificati e da NON correggere

1. **Aruvhana non emerge da zero nel capitolo 27.** La visita nel cap. 1 riguarda un'estensione commerciale di Bridgeglass a un cliente già legato a Cyberdine; il PoC non approvato è quella specifica prova. Il grande rinnovo del 27–28 è compatibile.
2. **B-32 può ancora parlare brevemente con Helen nel finale.** Il Bot Act II del 31 è approvato ma richiede promulgazione, pubblicazione e tempi di transizione; 37/003 consente soltanto incontri brevi e supervisionati, non compagnia illimitata senza personale.
3. **La causa dello sciopero non è un accesso occulto universale di Bi.** Il 27 prepara la distinzione fra autorizzazione e disponibilità, il 29 ne mostra l'incorporazione nel sistema Passerella, il 34 ricostruisce firme umane, il 35 rivela finalità non dichiarata. Restano questioni di facilità di lettura, non di assenza causale.
4. **Il blocco del 18 non anticipa quello del 32.** Il primo è una sospensione procedurale locale ripresa in video; il secondo colpisce numerosi siti nello stesso istante mondiale e richiede un'altra spiegazione.
5. **Martin non è stato licenziato da B-17.** Il 20 dimostra la scelta volontaria del pensionamento e la decisione autonoma di Victor Cole di non riaprire il posto. Sarebbe sbagliato «drammatizzare» la sua biografia trasformandolo in un espulso diretto.

## Secondo ordine di priorità

1. **Prima di ogni riscrittura:** risolvere gli script dell'edizione e disambiguare i documenti di canone attivo dagli archivi, così da non introdurre ulteriori errori.
2. **Senza nuovi capitoli:** due o tre interventi visibili fra 19 e 30 su famiglia Walsh, costo politico di Ethan e autonomia di Leo/Owen; un accenno verificabile allo stato della responsabilità esterna per la distruzione del robot.
3. **Sicurezza e rivelazione:** rifinire la distinzione fra stop logico e sicurezza indipendente (2, 6, 10, 12) e rendere rintracciabili le date nella catena 27–35.
4. **Prosa:** stringere 11–16, tagliare commenti morali dopo azioni già eloquenti, leggere il 37 come un finale unico.
5. **Proteggere ciò che già funziona:** l'ambiguità coscienza/non coscienza di Bi; la responsabilità distribuita; il consenso degli altri robot non raccolto; la legge italiana limitata; l'ultima frase «Tutto tornò normale.».

**Giudizio aggiuntivo:** la storia non mostra un difetto tale da imporre un nuovo impianto. Il rischio principale è la *discontinuità fra documentazione e manoscritto*; il rischio letterario è sostituire con spiegazioni e verbali ciò che i personaggi possono dimostrare con scelte, rinunce, costi e gesti.
