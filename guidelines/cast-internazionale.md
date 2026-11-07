# Cast internazionale di *Bot*

Questa guida è la fonte editoriale per **nomi pubblici e relazioni** dopo la migrazione globale documentata da `guidelines/cast-rename-map.json`. Non assegna alle persone nazionalità, origini etniche o biografie che la prosa non racconti: i nomi scelti devono essere riconoscibili, pronunciabili e distribuiti fra tradizioni linguistiche diverse. Il contesto principale resta una software house italiana con clienti e colleghi internazionali.

## Cyberdine e vita del campus

| Personaggio | Ruolo narrativo |
| --- | --- |
| **Maya Bennett** | Documentazione e rapporto personale con Bi; la sirena di Valle Corta |
| **Noah Carter** | Programmatore dell'upgrade clandestino di B-17 |
| **Claire Foster** | Ingegnera delle eccezioni; desiderava il ruolo senior |
| **Margaret Ellis** | Mentore senior in uscita verso la pensione |
| **Ethan Blake** | Sviluppatore frustrato dall'automazione del coding |
| **Marcus Reed** | Addetto alla movimentazione; partecipa all'aggressione |
| **Taylor** | HR e Marketing, media gli effetti dell'automazione |
| **Victor Cole** | Amministratore delegato di Cyberdine |
| **Olivia Hayes** | Qualità documentale e autorizzazioni |
| **Emma Walsh** | Processi e Spazio Comune |
| **Paul Turner** | Sistemi legacy, stampanti e banco prove |
| **Sarah Chen** | Sicurezza informatica e analisi forense |
| **Hannah Brooks** | Giornalista indipendente su lavoro e robotica |

## Veyra e Lanter

| Personaggio | Ruolo narrativo |
| --- | --- |
| **Amara Ortiz** | Comproprietaria e direttrice del Circuito Veyra |
| **Nina Solis** | Coordinatrice delle prove di Veyra |
| **Mei Chen** | Responsabile qualità Lanter a Suzhou |
| **Henry** | Impiegato amministrativo coinvolto nella lettera privata |

## Lavoro, assistenza e famiglia

| Personaggio | Ruolo narrativo |
| --- | --- |
| **Grace Morgan** | Responsabile del centro di assistenza |
| **Julia Parker** | Operatrice che si infortuna e continua ad assistere gli ospiti |
| **Helen Rivera** | Ospite del centro e interlocutrice di B-32 |
| **Chloe Rivera** | Figlia di Helen |
| **Sophie Grant** | Responsabile dell'Hub Levante |
| **Omar Haddad** | Tecnico dell'Hub |
| **Ruby Collins** | Lavoratrice dell'Hub e madre |
| **Samuel Price** | Agricoltore del noccioleto |
| **Yusuf Karim** | Stagionale esperto dell'azienda agricola |
| **Daniel Bennett** | Padre di Maya, ex tecnico della sirena |

## Visitatori, nomi minori e macchine

**Elias Hart** e **Leah Stone** sono i due interlocutori della delegazione Aruvhana. **Signora Harper** è una residente di Valle Corta; **Charlie** è il pomodoro piccolo a cui Helen dà un nome.

Il nome **Bi** resta il soprannome scelto da Maya per **B-17**. Restano invariati i codici **B-17, B-21, B-32, B-33, B-37**, e i nomi di aziende, luoghi, protocolli e impianti. B-21 non condivide la storia personale di Bi; cambiare i nomi umani non cambia conoscenze, motivazioni o permessi.

## Regole di applicazione

- Nomi nuovi in **tutte** le scene, schede, cronologia, luoghi con denominazione personale, fascicoli editoriali e riferimenti YAML; gli identificativi `character:` dei personaggi umani seguono il nuovo nome.
- Le relazioni familiari restano coerenti: Maya/Daniel **Bennett** e Helen/Chloe **Rivera**.
- Non attribuire retroattivamente nazionalità a un personaggio soltanto per giustificare il suo nome: bastano un'impresa e relazioni internazionali già presenti nella trama.
- Conservarne una corrispondenza reversibile in `cast-rename-map.json` per le modifiche editoriali; i vecchi nomi **non** sono alias diegetici. Un personaggio non viene presentato con due identità.
- Controllare a ogni revisione `python tools/audit_cast.py`, `python tools/validate.py` e `python tools/build.py`.
