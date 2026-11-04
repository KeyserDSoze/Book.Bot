# Istruzioni editoriali per Bot

Questo repository è la **fonte canonica** del romanzo. Non scrivere un capitolo isolato ignorando la continuità.

## Ordine di consultazione

1. `book.md` per tema, punto di vista e livello di rivelazione.
2. `context.md` per limiti plausibili di LLM, robotica, poteri aziendali.
3. **OBBLIGATORIO:** `guidelines/innovazione-non-chiede-permesso.md`, testo guida integrale e non parafrasato. Poi `guidelines/style.md` e `guidelines/continuity.md`.
4. `state/current.md`, `timeline/`, schede di luoghi, persone e organizzazioni.
5. Il capitolo corrente e le scene già canoniche.

## Principio fondamentale e non negoziabile

**L'innovazione non chiede permesso.** La traccia completa dell'autore è conservata **verbatim** in `guidelines/innovazione-non-chiede-permesso.md`: è la linea guida primaria per tutti i capitoli futuri e non va riscritta, abbreviata o sostituita da un riassunto.

Applicazione narrativa obbligatoria:

- Mostrare la trasformazione attraverso decisioni locali plausibili e convenienti: una fotocopia, un turno, un acquisto, un incarico automatizzato; **nessuno intende cambiare il mondo**.
- Rendere credibili anche i vantaggi, senza stabilire a priori vincitori morali: maggiore produttività può convivere con effetti sociali, fiscali e distributivi diversi.
- Porre attenzione a chi possiede la tecnologia, chi dipende dal lavoro e come cambiano le relazioni tra persone e imprese, senza trasformare ipotesi sociali in destini inevitabili.
- Non attendere robot perfetti per mostrare impatti reali; un miglioramento piccolo, replicabile e vantaggioso può essere sufficiente.
- Seguire la progressione **curioso e goffo → utile → normale → conseguenze collettive visibili**, lasciando che il lettore inferisca la rivoluzione dai dettagli.
- Non mettere in bocca ai personaggi il manifesto dell'autore, non predicare, non annunciare continuamente la rivoluzione. Mostrare prima azioni e conseguenze, poi dissenso e interpretazioni diverse.

Ogni nuova scena deve poter rispondere alla domanda: **quale scelta ordinaria fa avanzare un cambiamento più grande delle intenzioni di chi l'ha compiuta?** Se non ne introduce una, deve almeno mostrarne una conseguenza sul lavoro, sulle abitudini o nelle relazioni.

## Procedura

- Definisci desiderio del POV, ostacolo, evento irreversibile, informazione mostrata/nascosta.
- Scrivi una scena che si possa leggere come romanzo, non un manifesto o una presentazione tecnica.
- Prima di canonizzare, controlla fatti, cronologia, ruoli, tono, conseguenze e regola delle rivelazioni.
- Ogni scena nuova ha metadati `type: scene`, `id`, `chapter`, `number`, `title`, `canon`, `pov`, `characters`, `locations`, `factions`; le referenze devono esistere.
- Conserva le descrizioni dei luoghi e la distinzione fra percezione del personaggio e verità del mondo.
- Aggiorna `state/current.md` e `timeline/` con i cambiamenti accertati.
- Non cambiare il senso di scene canoniche o di una release esistente senza registrare una nuova versione.
- Lancia `python tools/validate.py` e `python tools/build.py`.

## Narratore e dialoghi

Prosa in italiano, focalizzazione ravvicinata, tensione e azioni visibili; dialoghi tra «caporali». Nessuna imitazione letterale o riconoscibile di scrittori contemporanei.

## Regola speciale del capitolo 1

Kyla crede genuinamente nella missione di Cyberdine. L'automazione è raccontata dal suo sguardo con entusiasmo e orgoglio, non con lessico della coercizione. Non anticipare in modo esplicito il futuro conflitto sui diritti robotici. Il lettore deve poter condividere per intero la promessa positiva prima di riconsiderarla.