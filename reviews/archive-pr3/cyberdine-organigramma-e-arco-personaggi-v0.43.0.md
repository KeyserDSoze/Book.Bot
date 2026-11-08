---
type: guideline
id: guideline:cyberdine-organigramma-e-arco-personaggi
canon: canon
---

# Cyberdine e personaggi — prima passata di verosimiglianza

## Cos'è Cyberdine

Cyberdine è una software house B2B italiana: vende integrazione, manutenzione applicativa, licenze di piattaforma e continuità di sistemi che i grandi clienti non possono sostituire in blocco. **Non produce robot.** I robot Lanter sono stati comprati per manutenzione fisica del campus, movimentazioni e prove su dispositivi reali. Gli agenti software lavoravano già nei repository prima che B-17 arrivasse.

Sono necessarie almeno quattro distinzioni che non dipendono dall'opinione dei personaggi: codice proposto da un agente **non è** codice pubblicato; test che passano **non significa** test end-to-end; firma di un responsabile **non significa** conoscenza integrale del sistema; taglio di trentuno equivalenti a tempo pieno **non significa** trentuno licenziamenti.

## Proprietà delle decisioni

| Responsabilità | Chi opera | Chi non può sostituirlo |
| --- | --- | --- |
| Prezzo, condizioni e rinnovo cliente | Commerciale/account manager insieme a Cole | Taylor non negozia il prezzo di Aruvhana |
| Pianificazione, SLA, dipendenze e incidenti di una commessa | Delivery manager e responsabile di servizio | Un agente non risponde al cliente o modifica unilateralmente lo SLA |
| Requisiti e criteri di accettazione | Product owner/analista funzionale, con il cliente | «Il prompt era chiaro» non sostituisce un caso di prova |
| Architettura, sorgenti e code review | Tech lead, ingegneri e responsabili delle librerie (fra cui Gavin per Core Platform) | Un test verde non sostituisce leggere una regressione |
| QA, regressioni e prove su terminale | Claire e colleghi qualità; Olivia coordina la qualità del servizio nel suo insieme | La suite generata non descrive tutti i modi in cui il dispositivo fallisce |
| Rilascio, rollback, reperibilità | Responsabile release/operations, nel perimetro concordato | Chi risponde al telefono di notte può non essere chi è autorizzato a rilasciare |
| Dispositivi, reti e laboratorio IT/OT | Paul e colleghi | Il tecnico hardware non è automaticamente autore dell'architettura software |
| Sicurezza, accessi, dati personali | Sarah e team security | L'indagine non si fa continuando a usare la backdoor |
| Persone, formazione e comunicazioni | Taylor per People & Communications; responsabile HR per i rapporti individuali | La buona comunicazione non dà titolo ad approvare una patch o promettere un posto |
| Governance e scelte d'impresa | Victor Cole e, per la propria area, la direzione che include Olivia come socia di minoranza dal capitolo 8 | Né Bi né il software possono firmare decisioni economiche al posto degli umani |

Non inventare titoli per tutte le comparse. È più credibile lasciare taluni responsabili senza nome, ma mostrarne il lavoro: un ticket preso in carico, un rilascio fermato, una telefonata al cliente, una rotazione di reperibilità, una firma che costa una serata.

## Gli attriti di reparto

**Sviluppo e delivery.** Chi programma vuole una specifica stabile e tempo di verifica; chi risponde al cliente ha una data, un prezzo e una penale. Nessuno dei due è stupido. La frizione esplode quando un test automatico passa ma il terminale reale restituisce una seconda conferma.

**Gavin Shaw e Olivia Hayes.** Gavin dirige tredici persone in Core Platform, sa programmare e difendere il proprio gruppo; chiude il 96% dei ticket ma esclude troppo presto il supporto e QA dalla definizione del problema. Olivia, nel capitolo 8, entra nel capitale con una quota di minoranza e responsabilità trasversale sulla delivery. Il risentimento di Gavin non è solo gelosia: teme di dover rispondere di errori su cui non ha potere. Il difetto è il disprezzo con cui tratta il lavoro altrui, non la volontà di proteggere gli sviluppatori. **Non guarirlo in una scena.** Nei capitoli successivi deve partecipare a una revisione con assistenza e sicurezza, accettare almeno un rilascio rinviato, poi tornare a difendersi quando il contratto Aruvhana si stringe.

**Claire e Margaret.** Margaret conosce le ragioni delle eccezioni, guida la qualità trasversale ed è vicina alla pensione. Claire sa scrivere il test che l'agente non ha generato; spera di crescere in una responsabilità senior, invece l'azienda sopprime quella posizione. La sua qualifica non è «impiegata generica» e il mancato rinnovo non significa che il suo lavoro sia stato fatto male.

**Ethan e Marcus.** Ethan perde la centralità del coding; Marcus perde turni e attività materiali. Sono malcontenti differenti, non due programmatori espulsi dalla stessa mansione. Il danneggiamento volontario di B-17 è un crimine/illecito da accertare e una scelta loro: la frustrazione non assolve.

**Noah e Sarah.** Noah ha capacità vere nel prototipo software, ma abusa degli accessi; Sarah protegge evidenze e riservatezza, non si limita a ostacolare l'innovazione. Nessuno può usare la confessione di Noah per fingere che non servano prove.

**Taylor e la direzione.** Taylor coordina People & Communications, partecipa alle visite clienti, supporta le decisioni HR e la comunicazione interna; **non è** in contemporanea responsabile del codice, commerciale, capocommessa e direttrice di tutte le funzioni. Il responsabile HR consegna le comunicazioni individuali, i responsabili tecnici approvano le prove, la direzione decide l'organico. Taylor può essere capace di parlare davanti a duecento persone e incapace di richiamare la madre.

## Il lutto di Taylor

**Hazel, sorella minore di Taylor, è morta cinque anni prima della prima scena.** La causa del decesso non è ancora definita nel testo: non inventare una relazione causale con l'intelligenza artificiale o un incidente informatico, né una malattia diagnostica funzionale a spiegare il personaggio.

La madre trova vecchie fotografie e domanda se debba tenerle. Nel **capitolo 1/001** Taylor lascia in sospeso il messaggio, irritandosi per una domanda innocente e poi per la propria irritazione. È più abile a condurre clienti che a trovare un accordo con la madre. Nel **25/004** decide di andare a guardare le foto insieme a lei domenica. Non è una guarigione improvvisa: rimane una professionista che a volte rinvia una telefonata e pronuncia una frase di circostanza quando è troppo stanca per trovare quella giusta.

La perdita **non spiega** il suo interesse per Bi e non va usata come equivalenza tra cancellazione del robot e morte di una persona. Hazel non deve diventare un'icona angelica. Più avanti potrebbe emergere anche un ricordo irritante o buffo della sorella: qualcosa che impedisca al lutto di ridurla a simbolo.

## Beat di evoluzione delle figure principali

| Personaggio | Inizio | Frattura | Evoluzione che serve |
| --- | --- | --- | --- |
| Taylor | entusiasmo misurato per il tempo recuperato; amicizia e madre trascurate | soppressione del ruolo senior; scoperta della backdoor; tagli di Aruvhana | imparare a comunicare limiti e decisioni senza promettere ciò che non esiste; un gesto concreto fuori dal lavoro |
| Victor | razionalità su margini e SLA; seleziona numeri veri nel discorso | cattivi risultati di cassa, violenza, perdita di competenze, riduzione richiesta del 17% | firmare anche costi sociali, senza diventare «cattivo che odia i robot» |
| Olivia | qualità dei documenti e responsabilità delle consegne | quota di minoranza e responsabilità interfunzionale dal capitolo 8 | essere competente ma compromessa anche nelle scelte che penalizzano Claire |
| Gavin | protezione del proprio team Core Platform | Olivia socia, 42 ticket riaperti dall'assistenza, accusa dei suoi confini tossici | mettere il codice in un perimetro condiviso, senza fingere che la sua paura di perdere controllo sparisca |
| Claire | competenza di QA e aspirazione a succedere a Margaret | posizione senior non aperta; quattro mesi al mancato rinnovo | mantenere dignità tecnica, cercare lavoro e contestare come vengono distribuiti i benefici |
| Noah | prototipazione brillante e accesso clandestino | confessione e verifica della memoria | assumere responsabilità, senza essere riammesso automaticamente |
| Margaret | sa perché la procedura è stata scritta | azienda non ricrea la sua posizione | accompagnare Claire senza prometterle l'impiego e senza diventare consulente gratuita |
| Paul | i dispositivi reali non mentono come un dashboard | Bi perso e protocolli documentati male | costruire continuità senza possedere la soluzione di tutti i problemi |
| Maya | sirena, chiave e colpa privata | fiducia tradita da Noah e poi da Bi | chiedere conto delle scelte senza diventare un personaggio soltanto morale |
| Sarah | prova, autorizzazioni, privacy | incidenti distribuiti, decisione irrevocabile su B-17 | distinguere prova tecnica da scelta etica e non firmare ciò che non può verificare |

## Correzioni narrative già eseguite

- **1/001:** Taylor lavora in People & Communications mentre account e delivery possiedono prezzo e commessa; compaiono Hazel e il messaggio della madre.
- **1/002:** la proposta dell'agente viene respinta nel repository e passa per riproduzione QA su dispositivo e finestra di rilascio concordata.
- **5/002:** Margaret chiede chi gestisce incidenti fra squadre, chi parla al cliente e chi autorizza il rollback.
- **8/001 e 8/005:** nuovo arco Olivia–Gavin aggiunto nella bozza mentre avanzava la revisione; considerarlo canonico nella prossima lettura.
- **25/001, 25/004:** la riduzione del 17% viene valutata da commerciale, delivery, architetti, sicurezza e People; Taylor non è l'autrice unica del piano tecnico.
- **26/001:** Claire riceve un'informativa individuale sul non rinnovo prima della comunicazione aggregata, presenta comunque i test e fa registrare una verifica rimasta aperta. Il fatto che la procedura sia più corretta non la consola.

## Limiti e lavori successivi

Il contesto dell'azienda è stato rafforzato solo nelle scene indicate: **non dire che tutte le 35 sezioni siano state riscritte**. Priorità: mostrare una giornata di sviluppo con ticket e release (capitoli 2–5); far ricomparire Gavin in un riesame con supporto e sicurezza (9, 25 e 31–32); dare a Olivia conflitti veri dopo la quota azionaria; allineare i capitoli 8 e 26 ai nuovi ruoli; correggere outline, numero scene e metadati. Conservare lo stop locale del 18 distinto da quello mondiale del 30, la confessione di Bi solo al 33, la scelta irreversibile del 35 e l'ultima frase «Tutto tornò normale.»
