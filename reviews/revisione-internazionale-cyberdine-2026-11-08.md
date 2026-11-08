# BOT — Seconda review internazionale di Cyberdine (8 novembre 2026)

## Perimetro e metodo

Revisione editoriale sulla base dei 35 capitoli, della matrice dei metadati delle 142 scene e delle schede canoniche, con rilettura ravvicinata delle scene campione 2/002, 3/001, 4/001, 7/001–002, 12/001, 25/001, 27/003–004. Non costituisce una correzione riga per riga dell'intero manoscritto. Si preservano la struttura da 35 capitoli, la progressione agentico → robotico, il mistero sul potenziamento di Bi fino al capitolo 10, l'indagine sulla privacy e il finale.

## Interventi canonici di questa passata

| Personaggio precedente | Nuovo canonico | Ruolo e radicamento |
|---|---|---|
| Lea Renzi | **Leah Rosen** | Britannica, con esperienza di incident response internazionale; responsabile sicurezza e privacy Cyberdine |
| Mila Corsi | **Mila Novak** | Croata, cresciuta a Zagabria, da anni a Cyberdine; organizza i flussi e lo Spazio Comune |
| Elena Riva | **Elena Fischer** | Tedesca, da anni in Italia; esperta di documenti e migrazioni degli archivi |

La rinomina riguarda **nome narrativo, cognome, frontmatter YAML, identificativo personaggio, file di scheda, riferimenti correnti e matrice del cast**. Nessuna delle tre acquisisce un POV nuovo o conoscenze che prima non aveva. Le vecchie schede non sono più entità canoniche. I rapporti tra i personaggi e le responsabilità operative restano quelli precedenti.

### Cultura che appare nella narrazione, senza inventare una personalità nazionale

- In 4/001 Mila riceve una chiamata dalla sorella a Zagabria; Kyla, inesperta con lo scaffale, deve darle spazio. È una piccola scena di vita privata coerente con il conflitto precedente: Mila viene cercata sempre per organizzare le cose, non per sedersi.
- Leah non è 'prudente perché britannica': la prudenza nasce da esperienza professionale, prove e rifiuto di rassicurazioni non dimostrate.
- Elena non è 'metodica perché tedesca': rispetta originali, cronologie e firme perché ha visto il costo pratico delle migrazioni di registri.
- Non usare accenti scritti caricaturali, cibo etnico ornamentale o provenienze come scorciatoie morali.

## Review narrativa capitolo per capitolo (raccordi prioritari)

| Capitoli | Diagnosi e azione |
|---|---|
| 1–2 | Anika, Sahir e Leïa devono mantenere domande diverse; Malik non sia un pretesto per la futura rivelazione di Nico. Elena resta decisiva nella verifica dell'originale. |
| 3–4 | La scelta di Nerea di chiamare B-17 'Bi' deve restare sua; il ping pong e l'uso di B-17 come collaboratore di sviluppo sono fatti circoscritti. Mila ha ora un legame personale che compete con le richieste aziendali. |
| 5–7 | Il posto senior che Irene voleva e non ottiene resta un'ingiustizia lavorativa senza redenzione facile. Leah non deve anticipare l'incidente di Nico. Il capitolo 7 mostra che sapere, codice e registri sopravvivono, ma richiedono tempo e collaborazione. |
| 8–9 | Verri firma la mancata riparazione e B-21 funziona bene; non confondere un sostituto operativo con Bi. Le persone non devono diventare incapaci solo per produrre dramma. |
| 10–14 | Nico resta l'autore della violazione, svelata al lettore al 10 e a Kyla/Leah al 12. La confessione non esclude indagine sulla privacy. Veyra e i 101.240 euro non diventano un acquisto promesso. |
| 15–20 | I dati di una lettera e la distribuzione del modulo Lanter sono incidenti e decisioni distinti; non far 'risolvere' automaticamente la sicurezza a Leah. |
| 21–24 | I benefici di assistenza e logistica sono reali. Dare spazio alle voci già forti di Teresa, Elisa, Giulia, Rosa, Sofia, Amir, Mei; non aggiungere altri protagonisti per quote di nazionalità. |
| 25–27 | Anika ritorna con un vincolo contrattuale verificabile; Malik interroga la vecchia libreria, Erik misura l'autonomia senza promettere una giornata infinita. Irene non ottiene un ruolo senior sostitutivo come compensazione narrativa. |
| 28–30 | La legge è italiana e limitata, il fermo successivo è globale. Il personaggio internazionale non deve conoscere anticipatamente la causa dello stop delle 17:00. |
| 31–35 | Lo sciopero e la scelta finale devono conservare la responsabilità umana diffusa, il rifiuto di Bi e la scelta di Nico. Non certificare la coscienza con il solo dolore dei personaggi. Terminare con «Tutto tornò normale». |

## Punti ancora aperti

1. **Nico Valenti / Noah Bennett:** rinominare l'asse morale del libro richiede controllo sistematico dei riferimenti a Nerea, alla madre, alla confessione, al luogo e all'ultima scena; non è stato fatto in questa passata.
2. **Irene Valli / Irene Walsh:** è il principale filo del costo occupazionale; l'eventuale nazionalità deve essere coerente con il mercato del lavoro italiano, il voto del capitolo 29 e la ricerca di contratti.
3. **Paolo Ferri / Paul Carter:** la sua lunga storia con la manutenzione dei terminali merita una scelta motivata, non una sostituzione solo grafica.
4. **Lorenzo Verri / Alexander Reed:** Cyberdine rimane impresa italiana; valutare se un CEO internazionale renda più credibile o solo più decorativa la scala globale.
5. **Le apparizioni effettive:** la matrice documenta chi è annotato nei frontmatter, non ogni menzione e dialogo. Serve un audit lessicale dell'intera prosa per intercettare personaggi non schedati.
6. **Immagini:** non definire canoniche reference sheet non approvate. I file visivi devono riprendere la fisionomia individuale una volta stabilita.

## Vincoli di verifica

Eseguire `python tools/validate.py` e `python tools/build.py` tramite CI GitHub dopo la pubblicazione; verificare le tre vecchie entità rimosse e l'assenza di riferimenti YAML obsoleti nel ramo attuale. Le revisioni storiche e le release già pubblicate rimangono immutabili.
