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
acquisto, cap, undo, tab, persistenza, tracking avversari, walk-away e FantaScore
(49 assert; risultati in pagina e via `fetch /__RESULTS__` nel log del server).

## Fonti della ricerca (14/08/2026)

30+ siti tra cui fantacalcio.it, SOS Fanta, FantaMaster, Goal, Calciodangolo, Sky Sport,
TMW, Corriere dello Sport, fantacalciopedia, pazzidifanta, Transfermarkt (cartellini per
il bonus fairplay) + testate locali. Dettaglio nel tab News. Mercato aperto fino all'1/9:
ricontrolla i dossier caldi (porta Juve/Vicario, Leao, Pinamonti/Bowie, Badiashile,
Lucumì, rigori Cagliari, attacco Lazio) il giorno dell'asta. La wishlist aggiornata è
stata riportata ("baked") anche in `asta.xlsx`: le `wishlist_ops` di `research.json`
ripartono vuote per le correzioni future.
