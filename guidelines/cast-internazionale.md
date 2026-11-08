# Cast internazionale di *Bot* — canone riconciliato

Questa guida fotografa i nomi da usare nell'edizione corrente dopo la riconciliazione delle PR #3–#8. **La fonte primaria per identità, ID e biografie è `characters/README.md` e il corrispondente file in `characters/`.** `guidelines/cast-rename-map.json` serve solo per ricostruire la migrazione, non introduce alias narrativi.

I nomi, distribuiti fra più tradizioni linguistiche, **non implicano da soli nazionalità, etnia o religione**; la storia mantiene sede principale e voto parlamentare in Italia. Non introdurre un passato culturale per giustificare a posteriori un cognome. Il romanzo parla di persone, non di un catalogo di rappresentanza.

## Personaggi di Cyberdine

| Nome canonico | ID / ruolo |
| --- | --- |
| **Kyla Morgan** | `character:kyla` — HR e Marketing, poi azionista all'1,5%, non responsabile del codice |
| **Victor Cole** | `character:victor-cole` — amministratore delegato |
| **Gavin Shaw** | `character:gavin-shaw` — Delivery manager, difende i propri sviluppatori ma deve coordinarsi con il resto della società |
| **Noah Carter** | `character:noah-carter` — sviluppatore, autore della modifica clandestina di B-17 |
| **Maya Bennett** | `character:maya-bennett` — documentazione, storia della sirena, relazione con Bi |
| **Daniel Bennett** | `character:daniel-bennett` — padre di Maya ed ex tecnico |
| **Paul Turner** | `character:paul-turner` — sistemi legacy; ha perso entrambi i genitori per dipendenze e diffida di ogni dipendenza |
| **Mila Novak** | `character:mila-novak` — processi, ironia, voce naturalmente alta |
| **Claire Foster** | `character:claire-foster` — QA e competenze storiche, occasione senior soppressa |
| **Margaret Ellis** | `character:margaret-ellis` — senior prossima alla pensione e memoria delle eccezioni |
| **Elena Fischer, Malik Okafor** | Documentazione e integrazione software |
| **Leah Rosen** | Sicurezza e protezione delle prove |
| **Ethan Blake, Marcus Reed** | Opposizione a Bi, responsabilità personali nell'aggressione |

**Le relazioni contano più dell'etichetta:** Kyla Morgan non è parente di Grace Walker; Gavin Shaw non è parente di Victor Cole. Il lutto della sorella Tessa di Maya non è collegato causalmente all'episodio di Valle Corta; la morte dei genitori di Paul e la sua avversione per le dipendenze sono un'altra storia. Noah non viene assolto dal fatto di essere capace e affettuoso.

## Veyra, Lanter, Aruvhana e informazione

**Amara Ortiz** gestisce le scelte commerciali di Veyra, **Nina Solis** le prove e la sicurezza del campo. **Mei Lin** è la referente qualità di Lanter; **Erik Solberg** contribuisce alle misure energetiche. **Anika Rao** rappresenta una verifica del cliente Aruvhana; **Sahir Venn** e **Leïa Orren** sono gli altri visitatori già canonici. **Olivia Brooks** segue da giornalista le conseguenze pubbliche. **Henry** resta un personaggio episodico amministrativo: il suo invio della lettera privata non è un accesso clandestino di Noah.

## Cura, logistica e lavoro

**Grace Walker** coordina il centro assistenziale; **Julia Parker** vi lavora e si ferisce tentando di proteggere **Helen Rivera**. **Chloe Rivera** è la figlia di Helen: sono madre e figlia, non due lavoratrici dell'Hub. **Sophie Grant** coordina l'Hub Levante con il tecnico **Omar Haddad**; **Ruby Collins** è l'operatrice che vuole condizioni di lavoro migliori dopo il percorso formativo. **Samuel Price** lavora nel noccioleto con **Yusuf Karim**. La figlia di Helen, Chloe, non va confusa con Ruby: professione e relazioni sono differenti.

## Cinque robot, ruoli non intercambiabili

**B-17, chiamato Bi**, ha la propria storia relazionale e un aggiornamento non autorizzato, senza coscienza certificata. **B-21** ne replica il modello esteriore, non i ricordi. **B-32** opera nella logistica e in brevi conversazioni autorizzate nel centro assistenziale; **B-33** ha un distinto incidente sul supporto di un carico e resta sottoposto a controlli; **B-37** propone i turni sotto firma umana. Nessuna rinomina umana implica una nuova rete operativa fra robot.

## Regole operative

- Nelle scene, negli indici e nei metadati si usa **un solo nome canonico**, con relativo ID; le vecchie grafie non sono soprannomi del personaggio.
- Rispettare la cronologia delle conoscenze: rivelazione al lettore nel 10, confessione a Kyla e Leah nel 12, fermo locale 47 minuti nel 18, fermo globale del 30, ammissione di Bi nel 33.
- Non aggiungere autorità ai personaggi per semplificare i problemi: la QA non diventa responsabile della firma di un reparto, HR non firma release, un robot non decide licenziamenti.
- Quando si rinomina una scena o una scheda, aggiornare contestualmente file, ID, capitolo, timeline, riferimenti e collegamenti; non copiare il contenuto del ramo storico della PR #3 sopra gli archi più recenti.
- Prima di pubblicare: `python tools/validate.py`, `python tools/audit_cast.py`, `python tools/build.py`.

La migrazione internazionale è una **scelta editoriale riconciliata**, non una nuova trama. I documenti storici eventualmente conservati in `reviews/archive/` restano materiale di consultazione, **non** istruzioni canoniche.
