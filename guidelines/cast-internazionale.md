---
type: guideline
id: guideline:cast-internazionale
canon: canon
---

# Cast internazionale — edizione consolidata

La fonte dei nomi canonici è `characters/README.md`; la trasformazione dalle bozze precedenti è registrata in `guidelines/cast-rename-map.json`. Questa guida integra la **PR #3** con tutte le successive passate dei capitoli 1–24. I vecchi nomi non sono pseudonimi nella finzione: i rapporti nei documenti di review storici testimoniano edizioni superate.

## Cyberdine: software, non una fabbrica di robot

| Nome attuale | Funzione / contraddizione |
| --- | --- |
| **Kyla Morgan** | HR/Marketing e socia all'1,5%; sa parlare alla squadra, a volte rinvia un confronto privato; sorella Hazel morta |
| **Victor Hale** | AD; decide su margini, clienti, ruoli e rischio economico |
| **Gavin Cole** | manager Delivery, difende il proprio team trascurando i costi di QA e supporto |
| **Maya Bennett** | documentazione, Valle Corta, fiducia difficile con Bi; sorella Tessa morta |
| **Noah Carter** | sviluppatore talentuoso, upgrade e backdoor non autorizzati a B-17 |
| **Claire Foster** | QA e legacy; seniority non riconosciuta, mancato rinnovo al 26 |
| **Margaret Ellis** | senior in pensionamento, conoscenze sui sistemi legacy |
| **Ethan Blake** | sviluppatore in crisi, lutto per Nora, responsabile volontario dell'aggressione |
| **Marcus Reed** | supporto materiale e aggressione a B-17, poi escluso dall'azienda |
| **Paul Turner** | terminali e infrastrutture, rifiuta le dipendenze per il lutto dei genitori |
| **Mila Novak** | processi; croata, parla molto forte anche quando è calma |
| **Elena Fischer** | qualità documentale; non è la giornalista Olivia Brooks |
| **Leah Rosen** | sicurezza e privacy, conserva prove senza riaprire la backdoor |
| **Malik Okafor** | prove tecniche e responsabilità sui rilasci |

Il nome **Kyla** resta perché già apprezzato e consolidato; non diventa Taylor. Gavin Cole, Mila Novak, Elena Fischer, Leah Rosen e Olivia Brooks restano quelli del canone più recente. Le coppie **Victor Hale/Gavin Cole** e **Grace Mercer/Kyla Morgan** evitano cognomi identici senza rapporti familiari. **Layla Stone** nella delegazione di Aruvhana resta distinta da **Leah Rosen**, addetta alla sicurezza.

## Altri luoghi

Aruvhana: **Elias Hart**, **Layla Stone**, **Anika Rao**. Veyra: **Amara Ortiz** (direttrice), **Nina Solis** (campo), **Henry** (amministrazione). Lanter: **Mei Chen** (qualità), con Erik Solberg su progetti energetici.

Centro assistenziale: **Grace Mercer**, **Julia Parker**, **Helen Rivera**, figlia **Chloe Rivera**, robot B-32 e B-33. Hub Levante: **Sophie Grant**, **Omar Haddad**, **Ruby Collins**, robot B-37. Agricoltura: **Samuel Price**, **Yusuf Karim**. **Lucy** e **Lauren** sono figure del centro, non la figlia di Helen.

**Nora Blake**, sorella di Ethan, è morta quattro anni prima della storia per incidente stradale; **Hazel Morgan**, sorella minore di Kyla, è morta cinque anni prima senza causa specificata. **Tessa Bennett**, sorella di Maya, è morta nove anni prima: non sono lo stesso lutto e nessuno di essi viene attribuito all'AI. Non inventare nazionalità o origini come giustificazione dei nomi.

Il soprannome **Bi**, dato a **B-17** da Maya, rimane intatto. B-21 non eredita la memoria di Bi; B-32, B-33 e B-37 sono macchine distinte. I luoghi italiani, l'isola fittizia di Veyra, le aziende, il testo della legge, i risultati numerici e l'ultima frase non cambiano con la rinomina.

## Verifiche editoriali

Per ogni nuova scena verificare il riferimento YAML e la scheda del personaggio, il luogo, la competenza professionale, chi conosce le informazioni e l'eventuale autorizzazione umana. Il controllo CI esegue `python tools/audit_cast.py`, `python tools/validate.py` e `python tools/build.py`.

I rapporti in `reviews/` precedenti all'integrazione sono **archivi storici**: possono parlare di Nerea, Nico, Irene o Taylor perché documentano lo stato del manoscritto al momento della review; non definiscono i nomi canonici di questa edizione.
