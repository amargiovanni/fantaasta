# FantaAsta 2026-27 — sala d'asta

App single-file (`index.html`) per condurre l'asta del fantacalcio (Classic, budget 1000,
rosa 3P+8D+8C+6A). Sostituisce `asta.xlsx`: stessa wishlist per slot, ma con ricerca
istantanea, flusso d'acquisto a due Invii e dati aggiornati dalla ricerca web del 14/08/2026.

## Avvio

Doppio click su `index.html` (o `python3 -m http.server` nella cartella e apri
`http://localhost:8000`). Tutto è embedded: funziona anche offline (i font Google sono
opzionali). Lo stato vive nel browser: **localStorage + cookie di backup** — usa sempre
lo stesso browser per tutta l'asta e fai un export a fine serata.

## Flusso durante l'asta

1. Digita 2+ lettere: la tendina mostra ruolo, squadra, Qt.A, FVM e — se il giocatore è
   nella tua lista — **slot, posizione di preferenza e prezzo max** (badge ★). Le
   occasioni scovate dalla ricerca web hanno il badge ◆; il pallino giallo segnala un
   alert (infortunio/mercato/ballottaggio: passaci sopra col mouse).
2. **Invio** = l'ho comprato → si apre la scheda con consigli, rigoristi della squadra,
   alert e i tre tetti di spesa (max consigliato, cap assoluto, residuo reparto), col
   campo crediti già a fuoco. Digiti il prezzo, **Invio** di nuovo: registrato nello
   slot giusto, budget aggiornato, focus di nuovo sulla ricerca.
3. **Shift+Invio** = l'ha preso un altro → si apre la mini-scheda: digiti il prezzo,
   **Invio**, poi un tasto **1-9** per dire chi l'ha comprato (**0** o Invio = non so;
   **Esc** = registra e basta, come una volta). Così l'app traccia budget e slot
   residui di ogni avversario.
4. `↑↓` scorri i risultati · `Esc` pulisci/annulla · `Ctrl/Cmd+Z` undo.

Il cap assoluto impedisce offerte che non ti lascerebbero 1 credito per ogni slot vuoto.

## Pannelli

- **Rosa** — i 25 slot; per gli slot vuoti mostra il miglior nome ancora disponibile.
- **Liste** — la wishlist completa per slot (priorità, prezzi max, note), con depennamento live.
- **Listone** — tutti i 499 giocatori, filtrabili; click per aprire l'acquisto.
- **Log** — cronologia: prezzi modificabili, per i giocatori "andati" puoi segnare chi li ha presi.
- **News & Rigoristi** — 70 alert pre-asta, rigoristi/piazzati delle 20 squadre, sleeper dal web, fonti.
- **⚙** budget totale e per reparto · **⬇/⬆** export/import JSON · **CSV** rosa per
  Excel (`;`, slot vuoti inclusi) · **✕** reset.

## Sala d'asta intelligente

- **Strip avversari** (sotto la testata) — per ognuna delle 9 squadre rivali (nomi in ⚙,
  uno per riga): crediti residui, slot mancanti per ruolo e max offerta teorica. La più
  ricca è evidenziata; a rosa completa si spegne.
- **"Molla a" (walk-away)** nella scheda d'acquisto — prezzo oltre cui conviene lasciare:
  parte dal max del piano e lo corregge con le alternative ancora libere in lista
  (FantaScore ≥75% del target), il tetto slot riproporzionato e la pressione reale degli
  avversari (se nessuno può superarti oltre X, non pagare più di X+1). Sotto, la riga
  "possono superarti: …" coi nomi.
- **FantaScore 0-99** — sintesi calcolata dal build: percentile FVM nel ruolo +
  titolarità + rigori/piazzati − infortuni − cartellini (fairplay) − rischio mercato.
  Colonna ordinabile nel Listone, badge `S` nella ricerca e nella scheda.

## Simulatore (prova generale)

Bottone **🤖** in testata: entra in modalità SIMULAZIONE — stato separato
(`localStorage` dedicato, il cookie di backup resta dell'asta vera), banner
arancione, si esce quando vuoi ritrovando l'asta reale intatta.
**Prossima chiamata ▶** mette sul banco un giocatore tra i migliori rimasti: i bot
(le tue 9 avversarie) arrivano a un prezzo ~FVM riscalato sui 10.000 crediti del
tavolo ±25%; compri col flusso vero (prezzo + Invio) o **Esc** e se lo porta via il
bot (registrato con prezzo e compratore: alleni anche la strip avversari).
**×10 auto** fa scorrere dieci chiamate senza di te; **reset sim** azzera solo la prova.

## Aiuti alla decisione (in asta)

- **Vs piano** in testata: quanto sei sopra/sotto il pianificato (residuo reale −
  budget degli slot vuoti). Verde se avanti, arancio se indietro.
- **Tetto slot aggiustato**: il budget pianificato di ogni slot vuoto viene
  riproporzionato sui crediti reali (`≤35 → 42` in Rosa e nella scheda d'acquisto).
  I prezzi max dei singoli giocatori restano quelli del piano.
- **"Se lo perdi"** nella scheda d'acquisto: le prime 3 alternative ancora libere
  della wishlist per lo slot selezionato; avviso se stai giocando l'ultimo nome.
- **Scarsità**: chip e slot diventano arancio con 2 nomi rimasti in lista, rossi
  con 1 ("ultimo!"). A reparto completo la ricerca smette di suggerire quel ruolo.

## Rigenerare `index.html`

```
python3 build.py
```

Estrae slot e wishlist da `asta.xlsx`, il listone da `listone.xlsx`, applica
`research.json` (alert, rigoristi, sleeper, correzioni wishlist) e inietta tutto in
`app_template.html`. Per aggiornare i consigli a ridosso dell'asta si modifica
`research.json` e si rilancia il build — i dati di stato nel browser non vengono toccati.

`test.html` è lo smoke test: servito via http accanto a `index.html`, esercita ricerca,
acquisto, cap, undo, tab, persistenza, tracking avversari, walk-away, FantaScore e
simulatore (57 assert; risultati in pagina e via `fetch /__RESULTS__` nel log del server).

## La mattina dell'asta (runbook, 20-30 min)

Ordine consigliato: prima i dati (1-3), poi build e verifica (4-5), poi il browser (6).

### 1 · Listone aggiornato (5 min)

Le quotazioni ufficiali cambiano fino all'ultimo (nuovi acquisti, ceduti, cambi ruolo).

- Scarica le **Quotazioni Fantacalcio** aggiornate da fantacalcio.it (Excel, stagione
  2026-27 — lo stesso file da cui viene `listone.xlsx`).
- Sostituisci `listone.xlsx` (tieni una copia: `cp listone.xlsx listone.old.xlsx`).
- Controllo rapido: foglio `Tutti`, intestazioni alla riga 2, dati dalla riga 3
  (`Id, R, RM, Nome, Squadra, Qt.A, …, FVM`). Se il formato è cambiato, dillo a
  Claude che adatta `build.py`.
- Se un giocatore della wishlist è sparito dal listone (ceduto all'estero), il build
  lo segnala: va tolto da `asta.xlsx`/`research.json` o semplicemente ignorato.

### 2 · Ricerca fresca (15-20 min, la fa Claude)

Apri Claude Code nella cartella e digita **`/aggiorna-ricerca`** — fa tutto da solo:
snapshot, 7 agenti di ricerca paralleli, sintesi in `research.json`, build con **diff
delle novità** e smoke test. Argomenti opzionali per restringere, es.
`/aggiorna-ricerca solo infortuni e porte`. Alla fine rileggi gli alert nuovi nel tab
**News & Rigoristi** e verifica che i dossier aperti abbiano una risposta (non
"invariato" per pigrizia dell'agente).

### 3 · Ritocchi manuali (5 min, opzionale)

Nomi che vuoi assolutamente, prezzi max da alzare/abbassare: aggiungili come
`wishlist_ops` in `research.json` — formato
`{"op":"update","role":"A","slot":"A3","name":"Simeone","maxprice":70}`
(op: `update` / `add` / `remove`) — oppure chiedi a Claude in italiano.

### 4 · Build + diff (1 min)

```bash
python3 update.py
```

Output atteso: `index.html written: …` + sezione `=== NOVITÀ ===` col diff rispetto
allo snapshot. Lo script **esce con errore se ci sono righe `!!`** (nome di una op che
non matcha il listone: correggilo e rilancia). `python3 update.py snapshot` salva lo
stato per il diff; `python3 build.py` resta il build "nudo".

### 5 · Smoke test (1 min)

```bash
python3 update.py --test
```

Apre `test.html` nel browser e attende i risultati: **57 PASS e nessun FAIL**.
⚠ Il test azzera lo stato salvato nel browser in cui gira: usa una finestra in
incognito, oppure fallo PRIMA del punto 6.

### 6 · Browser dell'asta (5 min)

- Apri `index.html` **nel browser e profilo che userai la sera** — lo stato vive lì
  (localStorage): niente incognito, niente "l'apro sull'altro PC".
- Roba di prova dentro? **✕ Reset** (doppia conferma). Poi **⚙**: budget, reparti e
  **nomi dei 9 avversari** (servono per il tracking a tasti 1-9).
- Prova il giro completo: cerca → Invio → prezzo → Invio, poi Ctrl+Z. Prova anche una
  chiamata del simulatore 🤖 e un **⬇ export** (è il tuo salvagente).
- Pagina nei preferiti / tab pinnato.

### 7 · Ultimi 10 minuti (la sera)

- Occhiata a SOS Fanta / FantaMaster per le news dell'ultima ora: eventuali novità le
  appunti nel campo note del Log — niente rebuild a quel punto.
- Laptop in carica; seconda finestra col tab **Liste** se hai due schermi.
- Durante l'asta registra ogni giocatore battuto (tuo = Invio+prezzo, altrui =
  Shift+Invio+prezzo+chi): è ciò che tiene affidabili "Prossimi obiettivi", strip
  avversari e walk-away. A fine asta: **⬇ export**.

### Riferimenti rapidi

| Cosa | Dove |
|---|---|
| Consigli/alert/rigoristi | `research.json` → `build.py` → embedded in `index.html` |
| Wishlist di base (slot e priorità) | `asta.xlsx` (fogli Portieri/Difensori/…) |
| Stato dell'asta | Solo nel browser (localStorage + cookie) — il rebuild NON lo tocca |
| Stato della simulazione | localStorage separato (`…_sim`) — reset sim non tocca l'asta |

## Fonti della ricerca (14/08/2026)

30+ siti tra cui fantacalcio.it, SOS Fanta, FantaMaster, Goal, Calciodangolo, Sky Sport,
TMW, Corriere dello Sport, fantacalciopedia, pazzidifanta, Transfermarkt (cartellini per
il bonus fairplay) + testate locali. Dettaglio nel tab News. Mercato aperto fino all'1/9:
ricontrolla i dossier caldi (porta Juve/Vicario, Leao, Pinamonti/Bowie, Badiashile,
Lucumì, rigori Cagliari, attacco Lazio) il giorno dell'asta. La wishlist aggiornata è
stata riportata ("baked") anche in `asta.xlsx`: le `wishlist_ops` di `research.json`
ripartono vuote per le correzioni future.
