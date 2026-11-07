# BOT — Nona review: cast internazionale e arco della perdita di Bi

> **Stato:** nuovo ciclo editoriale post-merge. La PR #2 è già stata unita a `main` (`142818dbb57a800430dd261a511b511eaecf65da`); la PR #3 rimane in bozza e `VERSION` rimane **0.33.0**. La sigla `v0.41.0` designa questo dossier di revisione, **non** una release.

## Obiettivi raggiunti

1. Migrazione dei nomi di **tutto il cast umano conosciuto**, non soltanto dei protagonisti, verso nomi globalmente leggibili e distribuiti fra più tradizioni linguistiche. Il dettaglio biunivoco vecchio/nuovo è in `guidelines/cast-rename-map.json`; la guida pubblica al nuovo cast è `guidelines/cast-internazionale.md`.
2. Sostituzione **nei 35 capitoli e nelle 142 scene**, nei rispettivi metadati YAML di POV, cast e luoghi, nelle schede e nei dossier editoriali. Sono stati rinominati 26 file biografici individuali e tre file di luoghi nominativi, conservando i robot e i loro identificativi.
3. Seconda lettura completa delle **20 scene dei capitoli 5–9**: esame delle pressioni economiche, dell'aggressione, del lavoro senza Bi e dell'arrivo di B-21. Cinque scene hanno ricevuto modifiche narrative mirate.
4. Correzione del titolo visibile del capitolo 24 da *La prima bugia* a **Il dato taciuto**, per non negare la menzogna già rivelata nel capitolo 4; i suoi codici stabili rimangono invariati. Il file e l'ID della scena del pomodoro **Charlie** sono ora coerenti.

## Principi del cast nuovo

I nomi devono poter essere letti da un pubblico internazionale senza far apparire tutti i personaggi nati nello stesso paese anglofono. La presenza di nomi come **Maya Bennett**, **Noah Carter**, **Claire Foster**, **Mei Chen**, **Sarah Chen**, **Amara Ortiz**, **Omar Haddad** e **Yusuf Karim** riflette una distribuzione di tradizioni culturali, non un'affermazione a posteriori sulla cittadinanza, la religione o l'etnia dei personaggi. L'azione principale resta in una **software house italiana**, e i riferimenti a voto, fuso italiano, Montecitorio e diritto del lavoro narrato **non** sono stati spostati nel Regno Unito o negli Stati Uniti.

Le famiglie conservano i cognomi condivisi: **Maya e Daniel Bennett** (figlia e padre; sirena di Valle Corta) e **Helen e Chloe Rivera** (madre e figlia; centro assistenziale). La responsabile del centro è **Grace Morgan**, l'operatrice è **Julia Parker**; non sono parenti dei Bennett o dei Rivera.

Anche le comparse realmente nominate sono state convertite: **Henry** (amministrativo di Veyra che allega per errore la lettera privata), **signora Harper** (residente della valle) e **Charlie** (pomodoro piccolo di Helen). La delegazione Aruvhana presenta **Elias Hart** e **Leah Stone**. I robot restano **B-17/Bi, B-21, B-32, B-33 e B-37**. Le parole Cyberdine, Aruvhana, Veyra e Passerella non sono nomi personali da anglicizzare.

**Importante per il lettore:** il file `cast-rename-map.json` è un registro editoriale per la migrazione, non un personaggio con un alias. Nel testo un personaggio ha un solo nome attuale.

## Review narrativa delle 20 scene dei capitoli 5–9

| Scena | Funzione narrativa e decisione di revisione |
| --- | --- |
| **5/001** | Margaret sta per andare in pensione e Claire ricostruisce un vecchio connettore; Bi aiuta con una prova senza assumere responsabilità di rilascio. **Protetta**: la vicinanza fra gratitudine e timore professionale è credibile |
| **5/002** | Olivia e Taylor valutano due piani organizzativi, entrambi razionali nel loro perimetro. La qualifica di Claire resta apprezzata, ma il ruolo non verrà riaperto. **Protetta**: la direzione non demonizzata |
| **5/003** | Ethan e Marcus distinguono perdita della capacità di scrivere codice personalmente da perdita di straordinari per trasporti fisici. **Modificata** la coda: anziché una formula generica sui test verdi, Ethan cerca nel sorgente una vecchia conversione delle date mentre arriva la richiesta urgente di firma |
| **5/004** | Claire perde l'opportunità e non il contratto; disegna un modo per insegnare a verificare il codice. **Corretto** un errore grammaticale nel dialogo Taylor/Claire. La libreria che vorrebbe comprare è un desiderio personale, non soltanto simbolico |
| **6/001** | Due manifesti opposti: «Chi perderà il prossimo posto?» e «Bi non decide chi assumere». Claire si rifiuta di farsi usare come slogan, senza invalidare il problema di Ethan e Marcus. **Protetta** |
| **6/002** | L'incontro HR mostra l'assenza di gradini futuri per imparare a dirigere; lo spostamento di una sedia per il robot diventa terreno di conflitto. **Protetta** |
| **6/003** | L'aggressione di Ethan e Marcus è una decisione volontaria: Marcus potrebbe andare a restituire un pacco, ma sceglie di restare. Bi chiede «Non fatemi del male». **Protetta senza giustificare o ripetere la violenza** |
| **6/004** | Maya riceve nello stesso momento un progresso verificabile per la sirena e la notizia del danno a Bi. Noah arriva ma non rivela le modifiche clandestine, né la sua backdoor. **Protetta** |
| **7/001** | Paul sbaglia il caffè perché B-17 non rifornisce più i bicchieri; l'ufficio ritrova compiti piccoli. **Protetta**: nessuna incompetenza caricaturale |
| **7/002** | Claire e Margaret devono trovare un registro cartaceo e risalire a una libreria che nessun riepilogo conosce interamente. **Protetta**: la prova human-in-the-loop dà un risultato |
| **7/003** | Ethan è a casa, con accessi sospesi e una chat che non lo assolve. Il rimpianto non giustifica i colpi. **Protetta** |
| **7/004** | Maya torna nella stanza della carta e sceglie di parlare al padre; offre a Claire la stessa domanda che Bi aveva fatto a lei. **Corretto** un ricordo di sedia trascinata che era stato eliminato nella review 3/003 |
| **8/001** | Victor comunica costi, responsabilità e non riparazione di B-17. La presentazione è precisa ma non può restituire la relazione. **Protetta** |
| **8/002** | Paul confronta riparazione e sostituzione: compatibile per la funzione non significa identico nei rapporti umani. **Protetta** |
| **8/003** | Maya rifiuta di far diventare la propria storia una giustificazione economica per il recupero di Bi. **Protetta** |
| **8/004** | **Riscritta la verifica tecnica**: non si ripete l'ennesimo caso di doppia conferma già descritto nel cap. 4 e 7. Il nuovo episodio è sul passaggio all'ora solare: due operazioni con orario locale **02:17**, identificate da un contatore che l'agente voleva rimuovere. Claire fa respingere la patch e mostra che il programmatore può ancora imparare a leggere il sorgente |
| **9/001** | B-21 arriva visivamente identico ma con un altro numero di serie, e dimostra buone capacità di lavoro. **Protetta**: il nuovo robot non è cattivo, stupido o una copia della memoria di Bi |
| **9/002** | Olivia registra un miglioramento delle attività e la necessità di verificare il codice precedente; non deve dire che B-21 è Bi. **Protetta** |
| **9/003** | Claire conserva il proprio talento ma non il posto senior che non è nato. Il lavoro utile non implica una promozione. **Protetta** |
| **9/004** | Maya pronuncia per errore il nome Bi davanti a B-21: la risposta corretta dimostra la differenza. **Corretto** un ricordo di gesti della prima sera incompatibile con la versione asciugata del cap. 3 |

## Il criterio morale che regge l'arco

L'azienda fa scelte economicamente razionali e talvolta insufficienti sul piano umano. **Victor Cole non picchia Bi** e non attribuisce a Bi lo status di persona per giustificare una spesa; **Ethan e Marcus non possono attribuire la loro violenza** alla razionalità dell'impresa. Claire non perde ogni opportunità o competenza perché è «sostituita da un robot»: è il ruolo di responsabilità a non essere istituito. Paul non diventa incapace di fare copie senza Bi; sta riconoscendo la rete di piccole abitudini che le macchine avevano preso in carico. B-21 ripristina un lavoro misurabile e non un rapporto storico.

In questo modo il primo atto costruisce il prezzo che il mondo pagherà per essersi progressivamente affidato a robot e software autonomi: gli esseri umani **non sono diventati stupidi**. Hanno smesso, in certi contesti, di tenere a portata di mano tutti i dettagli che permettevano di ricostruire un guasto con rapidità.

## Audit e guardrail

- La migrazione è stata applicata a tutte le schede `characters/`, alle scene e ai `chapter.md`; tre luoghi nominativi sono stati rinominati e i relativi metadati aggiornati.
- L'audit nuovo `tools/audit_cast.py` è eseguito nei workflow di validazione e release. Controlla i nomi legacy, la presenza delle nuove biografie, i metadati ID e i percorsi dei luoghi. Un falso positivo nelle prime versioni dell'espressione regolare Unicode è stato corretto prima di questa review.
- `tools/validate.py` continua a verificare l'esistenza e univocità di tutti gli ID (cast, POV, scene, luoghi).
- L'ultima frase resta **«Tutto tornò normale.»**. La rivelazione del potenziamento di Bi rimane al cap. 10; la confessione del piano mondiale al 33; la cancellazione è locale, irreversibile e contro il consenso di Bi.
- **Non unire la PR #3 a `main` senza una richiesta esplicita**. `VERSION` resta quello pubblicato, indipendentemente dai numeri dei dossier.

## Da controllare nelle revisioni successive

1. Rilettura stilistica completa di **10–14**: la fama del Circuito Veyra e le ragioni economiche del rifiuto di vendere Bi ai colleghi devono creare tensione senza ripetere gli stessi argomenti in quattro capitoli.
2. Controllo di **15–16** sulla distinzione tra privacy e provenienza, ora con Henry, Maya, Nina e Amara nominati in modo coerente.
3. Verifica a campione del nuovo cast sul manoscritto assemblato per i pronomi e le forme di cortesia: la sostituzione dei nomi non deve cambiare la voce dei personaggi.
