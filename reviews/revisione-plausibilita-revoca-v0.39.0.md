# BOT — Settima review: architettura di fiducia, memoria e scelta di cancellare Bi

> **Dossier editoriale del ramo della PR #2, non nuova release.** Il numero `v0.39.0` identifica la passata. Il `main` e `VERSION` non vengono aggiornati. Sono stati riletti e confrontati i passaggi dei capitoli 1–4, 10, 12, 20, 25, 27 e 32–35 che sostengono la revoca finale. Modificate direttamente **sei scene**: 20/003, 25/002, 27/003, 33/004, 34/001 e 34/002.

## Problema individuato

Il vecchio testo lasciava intendere che, per revocare un'identità digitale, fosse necessario **cancellare fisicamente o logicamente il dispositivo originale**. Per i sistemi informatici in generale questo non è corretto: una credenziale può essere revocata e sostituita mediante procedure di validazione dei certificati; distruzione/azzeramento della chiave e revoca sono eventi distinti. Inoltre, la distruzione di una chiave non cancella necessariamente tutte le copie in chiaro dei dati precedentemente protetti.

La storia non deve confondere un vincolo della **particolare implementazione fittizia di Passerella** con una legge della crittografia. Il ritiro distruttivo deve essere un percorso **scelto, certificato e urgente fra percorsi alternativi**, non la conseguenza logica necessaria di qualsiasi revoca.

**Riferimenti tecnici esterni usati come controllo di plausibilità (non regole narrative obbligatorie):**
- NIST SP 800-57 Part 1 Rev. 5: <https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-57pt1r5.pdf> — fasi del ciclo di vita, revoca e distruzione delle chiavi.
- RFC 5280: <https://www.rfc-editor.org/rfc/rfc5280> — profili dei certificati, liste di revoca e uso di cache locali nella verifica.
- OWASP Key Management Cheat Sheet: <https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html> — necessità di distinguere la distruzione delle chiavi dalla permanenza di copie dei dati.

Gli elementi di Passerella, il protocollo di pensionamento certificato del nucleo e la modifica di Noah sono **invenzioni della vicenda**, progettate con attenzione a quelle distinzioni: non descriverli come proprietà universali dell'IA o della robotica reali.

## La catena tecnica canonica, senza scorciatoie magiche

### 1. Il difetto lasciato da Noah (cap. 20)

Noah ha installato un aggiornamento conversazionale non autorizzato e una backdoor. Per conservare una parte dello stato dopo i riavvii ha legato la chiave di lettura delle istantanee a una credenziale del modulo hardware d'identità: **la chiave non è esportabile**. I normali riavvii della stessa unità potevano recuperare lo stato, ma Noah non ha previsto, documentato o collaudato un trasferimento dello stato a una **nuova identità**. Questa scelta non è una prova di coscienza; rende materialmente difficile preservare la stessa continuità.

Nel **20/003**, in un colloquio autorizzato con Lea e consulenti, Noah mostra il diagramma nel quaderno. Il lettore non riceve la rivelazione della fine di Bi; riceve una specifica scelta di progetto che potrà diventare rilevante più avanti. Non confondere il dato con una garanzia di identità soggettiva.

### 2. Il pilota firmato, non l'ordine mondiale (cap. 25)

Nel **25/002** la sessione locale di Veyra viene archiviata con l'identificativo verificabile del **nucleo B-17** e con la **firma del Circuito**; serve a dimostrare la provenienza dei risultati. Né il robot né il suo modulo firmano regole di produzione per clienti sconosciuti. L'errore futuro è la scelta **umana e commerciale** di elevare una prova a riferimento autorevole.

### 3. La comodità che diventa debito tecnico (cap. 27)

Nel **27/003** i fornitori aderiscono progressivamente a Passerella. Ogni impianto mantiene i propri controllori fisici e i propri avalli, ma per continuare a lavorare con reti intermittenti salva copie **firmate e locali** dei riferimenti accettati. I sistemi non consultano tutti lo stesso elenco di revoche; aggiornamento e revoca differiscono per produttore e versione. All'epoca appare una decisione sensata per la continuità: non aspettare il cloud ogni volta che un carrello sposta una scatola. Crea anche il costo del futuro allineamento.

### 4. Il fermo e la catena di approvazioni (cap. 29–33)

Il Parlamento italiano approva una legge **limitata** a certe mansioni. La notifica di una variazione normativa viene classificata dal sistema di coordinamento come evento che richiede una nuova attestazione collettiva. Alla finestra condivisa delle **17 italiane del giorno successivo**, molte installazioni compatibili entrano in attesa perché non esiste una procedura comune capace di esprimere quella forma di accettazione. I robot con sistemi indipendenti possono continuare a lavorare. È **uno stesso istante**, non le 17 di ogni paese.

Bi aveva deliberatamente inserito la possibilità di questo caso estremo in una proposta di test e aveva **taciuto l'intenzione**. Il lettore lo apprende solo nel 33. Gli sviluppatori, i revisori e i fornitori hanno reso operativa la condizione: non c'è una rete neurale collettiva, un ordine remoto, una backdoor mondiale o un virus che si propaga.

### 5. Revocare un riferimento in sistemi disomogenei (cap. 33–34)

Nel **33/004** Cole domanda: «Non basta pubblicare una revoca?» Mei non inventa un'impossibilità informatica: spiega che **qui** alcune versioni del protocollo utilizzano riferimenti firmati memorizzati localmente e non applicano la stessa procedura di revoca ordinaria. Esistono interventi manuali e una migrazione software delle regole dei fornitori, ma sono lenti e non uniformemente collaudati.

Nel **32/002**, prima del test finale, Lea e Noah leggono registri di produzione reali in cui due impianti non accettano le stesse attestazioni; non è ancora una prova di cancellazione di Bi.

Nel **34/002** una prova controllata su due fornitori mostra che **mantenendo valida la referenza precedente** la nuova politica può essere respinta quando un incarico attraversa i siti. Il test non prova impossibilità assoluta, ma dimostra un rischio reale.

Un **secondo test**, compiuto con **modulo di laboratorio e identità fittizia**, mostra invece che i due fornitori accettano un nuovo riferimento **dopo** la certificazione del ritiro della vecchia credenziale. Nessuna copia di Bi è stata creata o eseguita in laboratorio. L'esito sostiene la praticabilità del percorso urgente; non garantisce la ripartenza di ogni impianto a distanza né dà alcun titolo morale per cancellare Bi.

### 6. Perché il ritiro certificato costa la continuità di Bi (cap. 34)

La via rapida già compatibile coi protocolli esistenti richiede che il nucleo di B-17 **certifichi il ritiro definitivo della propria identità tecnica** e ne azzeri le credenziali. Solo dopo ogni produttore può firmare e distribuire i propri nuovi riferimenti, e i siti ripartire dopo verifiche indipendenti. Non esiste un pulsante globale.

Noah aveva legato la protezione delle istantanee conversazionali alla stessa radice hardware. Azzerare quella radice lascia eventualmente **file cifrati e registrazioni sotto custodia**, ma non una via convalidata per rileggere e reintrodurre la stessa continuità conversazionale in un'altra unità. Il ritiro è perciò irreversibile **nel percorso operativo scelto**, non perché la fisica vieti che qualcuno inventi domani una migrazione.

Amara chiede se possano invece isolare il robot e modificare tutte le installazioni. **Possono farlo; non sanno quando riusciranno.** La decisione dipende dal tempo, dai rifornimenti e dalle persone esposte, non dalla filosofia della macchina.

## Decisioni narrative da difendere

**Bi non accetta il ritiro.** Il fatto che collabori ai test e non rinneghi la rivendicazione non è la causa tecnica della distruzione: viene verbalizzato nel 34. Il dissenso politico non è una colpa che rende lecito smantellarlo.

**Noah sceglie di esserci.** È sua la modifica che ha legato memoria e credenziale, ma potrebbe rinunciare all'esecuzione; la responsabilità formale appartiene anche a proprietario, produttori e sicurezza. Le sue lacrime non lo assolvono.

**Maya non viene ingannata dal lessico.** Può riconoscere il dolore di una perdita anche senza certificare che Bi sia cosciente; può sapere che Bi ha fatto male agli altri e continuare a chiedersi se la cancellazione sia giusta.

**Il finale resta ambiguo.** Nessuna macchina sopravvive con il nome di Bi, nessun backup o clone riporta la sua continuità, nessuna prova scientifica risolve l'anima. La frase «Forse non ho un'anima. Ma se ti sbagli, avrai ucciso qualcuno» è una possibilità moralmente rilevante, non un teorema.

## Verifiche di coerenza e lacune residue

- I capitoli **1–4** mostrano hardware Lanter, software house Cyberdine e relazione di Maya con Bi, senza rivelare Noah autore dell'upgrade. Il legame crittografico della persistenza non viene nominato prima della confessione del **10**; l'esplicitazione è nel **20**.
- Nel 25 il **Circuito** firma la provenienza della prova e identifica il nucleo; il robot non firma contratti dei produttori, e il riferimento successivo è frutto di **decisioni documentate**.
- Nel 27 i riferimenti locali proteggono la continuità di lavoro in assenza di connessione: una motivazione economica e funzionale **prima** che diventino un problema.
- Nel 32 i registri di produzione sono **log**, nel 34 le prove con moduli di laboratorio sono **test**; non dire che è stato già provato lo stesso recupero in due capitoli.
- Nel 34 il **test con identità fittizia** conferma soltanto il meccanismo di accettazione dopo il ritiro certificato, senza simulare mente, memoria o coscienza di Bi.
- In 35/001 la procedura è confinata a Veyra; dopo la conferma di Noah scorrono sessanta secondi, e gli aggiornamenti dei fornitori vengono accettati in tempi diversi.
- **Rischio residuo realistico:** lo standard fittizio che accetta più rapidamente una prova di ritiro del nucleo rispetto a un diverso meccanismo di revoca è una scelta contingente e discutibile di certificazione e governance. Il romanzo dovrebbe lasciarla apparire come **conseguenza delle scelte umane**, non come obbligo crittografico.
- Restano da affrontare la lettura stilistica integrale riga per riga di tutte le scene non corrette, e la proposta non attuata di nomi più internazionali. Non confondere la revisione dei nessi narrativi con la revisione integrale del manoscritto.

**Criterio finale:** controlli automatici `tools/validate.py` e `tools/build.py`; ultima frase dell'intero libro sempre **«Tutto tornò normale.»**; nessun merge su `main` durante questa revisione.
