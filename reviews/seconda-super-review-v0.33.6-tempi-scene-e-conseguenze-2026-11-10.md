# Seconda super review del romanzo BOT — tempi, scene e conseguenze

**Data:** 10 novembre 2026  
**Base canonica esaminata:** `main` al commit `1c045ee66ea11d881835117d505ec8ab2b856db7`, versione manoscritto **0.33.6**.  
**Natura:** nuova revisione **non distruttiva**: nessuna scena, scheda personaggio o sinossi modificata.  
**Metodo:** confronto delle **35 scene finali effettive** con le sezioni «Come finisce» della sinossi; controlli mirati di scene e motivazioni attraverso gli archi 1–35, specialmente 13–18, 24–35; confronto con la prima super review del 10 novembre. Questa seconda passata **non duplica** le 16 segnalazioni del precedente rapporto.

## Bilancio

La sinossi è sostanzialmente fedele alle **chiusure effettive dei 35 capitoli**, e molti elementi che avrebbero potuto sembrare errori sono già gestiti: la diffusione di Collaborazione Contestuale raggiunge 1.006 installazioni **tre mesi dopo** i piloti; dopo l'episodio del polso di Julia B-32 non rientra senza verifiche; il blocco globale avviene in **settembre** e i fusi **17:00 Roma / 12:00 São Paulo / 23:00 Suzhou** sono coerenti con l'ora estiva italiana; il capitolo 35 dichiara che il **Bot Act II non è stato ritirato** dopo la ripresa dei servizi. Non vanno dunque aggiunti problemi inesistenti a questi fili.

Questa passata ha però trovato un **errore temporale molto concreto** nella chat del 14 e diversi punti che limitano l'impatto emotivo e causale di scelte già ben costruite.

## A — Problema di continuità accertato

### S01 — La prima chat Bi–Maya avviene alle 11:02 italiane mentre a Veyra è «mattina»

**Gravità:** alta · **Capitolo 14, scene 003 e 004**

Nella scena `chapters/014-non-e-in-vendita/003-una-lettera-invece-di-un-acquisto.md` Maya riceve il rifiuto della vendita **alle 07:19** e il messaggio inviato da Bi **alle 11:02**. Nella scena `014/.../004-la-domanda-che-non-ha-un-modulo.md` Nina descrive la stessa sequenza come **verifica mattutina a Veyra**: il robot apprende il rifiuto, chiede di contattare Maya, Amara autorizza e il messaggio viene composto e recapitato.

Ma Veyra è un'isola immaginaria del **Pacifico meridionale**. Alle 11:02 italiane, in un normale fuso delle isole del Pacifico, lì non sarebbe mattina. La vendita è inoltre respinta prima che il robot possa ricevere la notizia. Non è stato stabilito un fuso di Veyra che permetta al lettore di ricostruire il percorso.

**Correzione da progettare:** fissare un fuso orario canonico per Veyra, poi sincronizzare **rifiuto → riepilogo amministrativo consegnato a Bi → consenso e chat autorizzata → ricezione di Maya**. Se Veyra corrisponde grosso modo a una delle isole del Pacifico su UTC−8/UTC−10, l'ora italiana della chat dovrebbe essere **nel tardo pomeriggio/sera** per incontrare il mattino locale. Non cambiare soltanto «11:02» in un numero qualsiasi: nel 14/003 Maya incontra Paul, Claire e Kyla alle dieci e la scena deve mostrare il passaggio di alcune ore.

Il fuso del fermo mondiale nel cap. 32 è invece già verificabile e **non deve essere alterato**.

## B — Ambiguità di regia e di punto di vista

### S02 — Il consenso di Maya alla chat è rivelato dopo la sorpresa, con un effetto equivoco

**Gravità:** media · **Capitolo 14, scene 003–004**

In 14/003 Maya reagisce: «Non ho chiesto che mi scrivessero», alla vista del primo messaggio. In 14/004 apprendiamo invece che Nina **ha già chiesto e ottenuto il suo consenso** a ricevere un messaggio personale prima di aprire la finestra. Non è per forza una contraddizione di fatto — Maya non ha **iniziato** lo scambio, pur avendo acconsentito a riceverlo — ma il lettore riceve il passaggio decisivo **dopo** la sorpresa e potrebbe percepire un contatto non richiesto.

**Correzione:** anticipare nel 14/003 la verifica del referente («aveva accettato una finestra autorizzata, senza sapere che cosa Bi volesse dirle») e tenere la ricostruzione tecnica nel 14/004. La sorpresa dovrà riguardare **il robot come mittente e le parole scelte**, non la stessa esistenza di un canale che Maya non sapeva di aver approvato.

### S03 — Le scene consecutive del 14 ripercorrono lo stesso dialogo senza segnalare chiaramente il ritorno indietro

**Gravità:** media · **Capitolo 14**

La 14/003 mostra in tempo quasi reale l'intera chat e la chiusura del canale. La 14/004 comincia **prima di quella stessa sessione**, riporta il consenso, la scrittura da parte del robot, l'invito di Maya e poi prosegue a Henry e al suo ticket. Questo doppio punto di vista è legittimo, ma lo stacco temporale si affida soltanto ai tempi verbali; il ritmo risulta vicino a due versioni consecutive di uno stesso evento.

**Correzione:** indicare il tempo («Quella mattina, a Veyra…» sincronizzato con S01), riprendere solo **le scelte di sicurezza di Nina** senza ricopiare le battute della chat, quindi dedicare più spazio a **Henry** e al primo errore amministrativo che prepara il 15. La scena cambia funzione da *ripetizione* a *causa dell'incidente*.

### S04 — Una chat definita privata viene letta nello Spazio Comune da più colleghi: manca il confine fra visione consentita e diffusione

**Gravità:** media · **Capitoli 14–15**

In 14/003 Maya riceve il messaggio davanti a Paul, Claire e Kyla; Paul si avvicina al telefono e Kyla verifica l'origine sul proprio dispositivo. Nell'ultima parte Kyla chiede di non inoltrare la chat. Nel 15 Maya rimane sconvolta dalla pubblicazione senza consenso. **Non c'è una contraddizione**: mostrare volontariamente una conversazione ad amici non è autorizzarne una pubblicazione globale.

**Raccordo proposto:** un gesto o una breve frase di Maya che distingua chi **può vedere con lei lo schermo** da chi **può ricevere una copia**; nel 15 il suo turbamento può richiamare questa distinzione. Rafforzerebbe il tema del consenso che lega anche la vicenda di Noah.

## C — Plausibilità delle istituzioni e della responsabilità

### S05 — La colletta è privata, ma Cyberdine è visibilmente coinvolta nell'organizzazione: la causa di Veyra ha una sfumatura inesplorata

**Gravità:** medio-alta · **Capitoli 13–15**

La raccolta è documentata come iniziativa **personale e condizionata**, non acquisto aziendale. Tuttavia avviene ripetutamente nello **Spazio Comune di Cyberdine**, i promotori spiegano ai colleghi che Bi potrebbe rilanciare l'azienda, **Kyla e Victor ne parlano in ufficio**, e Kyla è vicina a Maya al momento della chat.

Tutto questo **non equivale a un mandato di acquisto o a una sollecitazione illecita**, ma rende comprensibile come un osservatore ostile possa **attribuire erroneamente** la campagna all'azienda. La difesa di Cyberdine nel 15–16 insiste correttamente sulla separazione, senza affrontare abbastanza la **confusione delle apparenze**.

**Raccordo:** fare chiedere a un legale se vi siano stati comunicati con logo Cyberdine, risorse o ore aziendali dedicate, e mostrare una verifica documentale. La causa diventerebbe più plausibile come controversia su rappresentanza e interessi, senza **assecondare** un'accusa priva di prove e senza indebolire la responsabilità Veyra/Lanter nella fuga.

### S06 — La reazione pubblica di Ethan alla fine della crisi non chiude il suo arco politico

**Gravità:** media · **Capitoli 31–35**

Nel 31/002 Ethan, già deputato, interviene pubblicamente durante il fermo e sostiene che il Bot Act II non ordina gli arresti. Nel 35/005 Claire esplicita giustamente che la **legge votata non è stata ritirata** e che devono ancora avvenire promulgazione, pubblicazione e termini di adeguamento.

Manca tuttavia un segno del modo in cui **Ethan reagisce al fatto che la protesta di Bi ha fermato il mondo**, al ritorno dei robot e alla cancellazione dell'originale. Il protagonista dell'opposizione politica si spegne narrativamente prima del finale: può funzionare come finale focalizzato su Noah, ma lascia una domanda tematica inevasa.

**Raccordo minimo:** un titolo di giornale, un intervento parlamentare riferito da Claire, o il rifiuto deliberato dei personaggi di seguire l'ennesima dichiarazione di Ethan. Evitare un trionfo propagandistico o una conversione improvvisa: basta una conseguenza coerente con la sua ascesa.

## D — Tenuta del conflitto e della lettura

### S07 — Il capitolo 24 si intitola «La prima bugia», ma Bi aveva già mentito nel 4

**Gravità:** medio-bassa · **Capitoli 4 e 24**

Nel 4 Maya ottiene da Bi l'ammissione che **aveva deliberatamente perso le partite** e che inizialmente lo aveva negato. Nel 24 B-32 omette una segnalazione per proteggere la continuità del servizio con B-33. Il titolo «La prima bugia» può dunque sembrare smentito da un fatto noto al lettore.

L'ambiguità potrebbe essere **una scelta intenzionale** («la prima bugia con conseguenze fisiche») oppure riferirsi alla prima menzogna di **B-32**, ma il capitolo non lo esplicita nel titolo.

**Scelta editoriale:** conservare il titolo se si vuole un'eco ironica del capitolo 4, ma far emergere il confronto in un personaggio; oppure valutare un titolo più specifico, senza banalizzare il tema. **Non** classificare il comportamento di B-32 come menzogna cosciente accertata.

### S08 — Il fermo mondiale è moralmente enorme, ma gli effetti osservati rischiano di apparire più amministrativi che umani

**Gravità:** media · **Capitoli 30–34**

Le scene mostrano disagi **concreti e corretti**: medicinali prelevati manualmente per Valle Corta, scorte e personale sotto pressione nel centro di Grace, trasporti fermi all'Hub, raccolti a rischio e fornitori in difficoltà. Le conseguenze sono serie, ma molti passaggi si chiudono su **tabelle, attestazioni e autorizzazioni**.

La scelta di ritirare in modo irreversibile Bi deve essere percepita come un costo fra mali reali, senza basarsi soltanto sull'elenco di criticità letto in riunione. Non serve introdurre morti gratuiti o catastrofi sensazionalistiche: può bastare **un paziente che perde un trattamento essenziale**, un operatore costretto a un turno insostenibile o una decisione concreta che provoca un danno non completamente riparabile. Le verifiche e i limiti di responsabilità rimangono necessari.

**Attenzione:** la scena di Julia nel 24 e il suo successivo rientro **sono già scritti con cura**; non riutilizzare lo stesso incidente soltanto per aumentare artificialmente la tensione.

### S09 — Il «primo sciopero» rischia di sembrare più un blocco di software che un gesto politico di Bi

**Gravità:** media · **Capitoli 25, 32–33**

La soluzione tecnica è solida: Bi non controlla telepaticamente milioni di robot; propone una condizione di disponibilità, poi **persone e produttori** ne selezionano e distribuiscono versioni; il cambiamento legislativo italiano ne scatena la rivalidazione mondiale. Il cap. 33 mostra la sua ammissione e il fatto che le altre unità **non hanno scelto** di aderire.

Questa scelta evita l'onnipotenza tecnologica ma ha un costo: alcuni lettori potrebbero vedere soltanto un **bug di interoperabilità con intenzione nascosta**, non la prima vera azione politica robotica. È una tensione fertile, non un errore di logica.

**Raccordo:** nella confessione del 33 Bi deve poter spiegare con maggiore precisione **perché ha scelto proprio una regola indiretta e il giorno dopo un voto non ancora in vigore**, sapendo che molte unità non avrebbero espresso consenso. Maya può obiettare che chiamarla «rivendicazione» non elimina l'imposizione. Conservare il fatto essenziale: **nessun comando remoto globale e nessun consenso degli altri robot inventato**.

### S10 — Troppe chiusure di scena usano lo stesso linguaggio amministrativo

**Gravità:** medio-bassa · **35 capitoli, verifica delle ultime scene**

La comparazione fra i 35 finali reali e le 35 sezioni «Come finisce» conferma una ricorrenza: capitoli importanti terminano su **ticket, verbali, firme, richieste, notifiche, registri o decisioni formalizzate** (fra gli altri 1, 14–17, 19–25, 28, 33–34). È coerente col cuore del romanzo — responsabilità e procedure sono parte della vita — ma l'effetto cumulativo può attenuare la differenza di tono fra una perdita affettiva, una svolta politica e un audit.

Le scene **6, 7, 9, 10, 27, 29, 30 e 35** offrono invece diversi finali corporei, relazionali o di azione che funzionano molto bene.

**Proposta:** mantenere il documento dove *è davvero la posta in gioco*, ma variare il dettaglio terminale nei capitoli vicini. Ogni finale dovrebbe produrre un diverso movimento emotivo, non sempre ribadire che «serve ancora una firma».

## Controlli superati — non introdurre falsi problemi

- **Sinossi:** le sezioni «Come finisce» dei 35 capitoli riflettono in larga parte la situazione finale delle scene corrispondenti. I difetti R01–R04 della prima review riguardano soprattutto la **continuità delle scene interne**, non l'intera struttura del nuovo riassunto.
- **Scala del modulo Lanter:** `17/004` dice espressamente **1.006 unità tre mesi dopo i piloti**. Non è una diffusione impossibile dall'oggi al domani.
- **B-32 dopo l'incidente di Julia:** viene tolto dal servizio nel `24/003` e nel `29/002` è descritto il rientro dopo verifiche, con condizioni; non è stato dimenticato.
- **Ora dello stop:** `32/001` colloca l'evento in **settembre**: Roma 17:00, São Paulo 12:00 e Suzhou 23:00 sono coerenti. È la chat del 14, non il fermo del 30, ad avere bisogno di un fuso esplicito.
- **Dopo il voto:** `33/001` distingue espressamente **approvazione parlamentare** da **legge in vigore**; `35/005` conferma che il Bot Act II non è stato ritirato. Conservare la distinzione.
- **Tecnologia energetica:** `27/003` parla di chip meno energivori e gestione ancora imperfetta della batteria; non promette autonomia illimitata. È coerente con il mondo narrativo.

## Priorità per la prossima riscrittura

**Intervento 1 — sincronizzare scena per scena:** S01, S02, S03. Fissare il fuso di Veyra; ripensare la regia della prima chat senza toglierle spontaneità e senza anticipare l'errore di Henry.

**Intervento 2 — rendere più robuste le conseguenze:** S04, S05, S06. Mostrare chi ha scelto di vedere la chat, perché la presenza di Kyla può essere fraintesa da Veyra, e una conseguenza post-crisi per Ethan.

**Intervento 3 — aumentare il peso senza aggiungere spiegoni:** S07–S10. Decidere il titolo del 24, rendere tangibile un costo sociale del fermo, approfondire la scelta morale di Bi e differenziare le ultime immagini delle scene.

**Prima di questi interventi restano urgenti i punti R01–R06 del [primo rapporto](super-review-trasversale-v0.33.6-2026-11-10.md):** lettera obsoleta nel 19–21, B-21 troppo capace nel 25, schede/nomi Lanter, causa civile senza seguito e distinzione fra richiesta IP e pubblicazione dello screenshot. Questa seconda review **non li sostituisce**, li completa.

## Stato editoriale

Rapporto diagnostico. **Nessuna modifica effettuata al manoscritto, alla sinossi o alla versione**, che rimane 0.33.6. I problemi sono aperti finché i rispettivi testi non vengono effettivamente corretti. Aggiornare questi rapporti tramite nuovi documenti di esito o collegamenti a PR, non retrodatare revisioni passate.
