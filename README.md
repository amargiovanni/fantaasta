# FantaAsta 2026-27 — sala d'asta

App single-file (`index.html`) per condurre l'asta del fantacalcio (Classic, budget
1000, rosa 3P+8D+8C+6A, lega da 10). Nata per sostituire `asta.xlsx`, oggi è una sala
d'asta completa: ricerca istantanea sul listone, acquisto a due Invii, **tracking di
budget e rose degli avversari**, prezzo di **walk-away** calcolato live, **FantaScore**
di sintesi su ogni giocatore, **simulatore** per la prova generale, **report** finale e
vista **secondo schermo**. I consigli (alert, rigoristi, sleeper) vengono dalla ricerca
web multi-agente, rilanciabile con un comando (`/aggiorna-ricerca`).

## Avvio

Doppio click su `index.html` (o `python3 -m http.server` nella cartella e apri
`http://localhost:8000`). Tutto è embedded: funziona anche offline (i font Google sono
opzionali). Lo stato vive nel browser — **localStorage + cookie di backup** — quindi:
stesso browser e stesso profilo per tutta l'asta, export ⬇ a fine serata.

## Flusso durante l'asta

1. Digita 2+ lettere: la tendina mostra ruolo, squadra, Qt.A, FVM e FantaScore; se il
   giocatore è nella tua lista, anche **slot, priorità e prezzo max** (badge ★). Le
   occasioni dal web hanno il badge ◆; il pallino giallo è un alert
   (infortunio/mercato/ballottaggio/fairplay: passaci sopra col mouse).
2. **Invio** = l'ho comprato → scheda con consigli, rigoristi, alert, tetti di spesa e
   walk-away, col campo crediti già a fuoco. Prezzo, **Invio**: registrato nello slot
   giusto, budget aggiornato, focus di nuovo sulla ricerca.
3. **Shift+Invio** = l'ha preso un altro → mini-scheda: prezzo, **Invio**, poi un tasto
   **1-9** per dire chi (**0** o Invio = non so; **Esc** = registra e basta). È quello
   che alimenta il tracking degli avversari: ~2 secondi ben spesi.
4. `↑↓` scorri · `Esc` pulisci/annulla · `Ctrl/Cmd+Z` undo.

Il cap assoluto impedisce offerte che non ti lascerebbero 1 credito per ogni slot vuoto.

## Aiuti alla decisione

**Sul tavolo**
- **Strip avversari** sotto la testata — per ognuna delle 9 rivali (nomi in ⚙): crediti
  residui, slot mancanti per ruolo, max offerta teorica. La più ricca è evidenziata,
  chi ha finito si spegne.
- **Vs piano** in testata: quanto sei sopra/sotto il pianificato (residuo reale −
  budget degli slot vuoti). Verde se avanti, arancio se indietro.

**Nella scheda d'acquisto**
- **"Molla a" (walk-away)** — il prezzo oltre cui conviene lasciare: parte dal max del
  piano e lo corregge con le alternative ancora libere (FantaScore ≥75% del target),
  il tetto slot riproporzionato e la pressione reale del tavolo — se nessuno può
  superarti oltre X, non pagare più di X+1. Sotto, "possono superarti: …" coi nomi.
- **Tetto slot aggiustato**: il budget pianificato dello slot riproporzionato sui
  crediti reali (`≤35 → 42`). I prezzi max dei singoli restano quelli del piano.
- **"Se lo perdi"**: le prime 3 alternative libere della lista per lo slot; avviso se
  stai giocando l'ultimo nome.

**Sui giocatori**
- **FantaScore 0-99**, calcolato dal build: percentile FVM nel ruolo + titolarità +
  rigori/piazzati − infortuni − cartellini (fairplay) − rischio mercato. Colonna
  ordinabile nel Listone, badge `S` in ricerca e scheda; è anche l'ingrediente del
  walk-away.
- **Scarsità**: chip e slot arancio con 2 nomi rimasti in lista, rossi con 1
  ("ultimo!"). A reparto completo la ricerca smette di suggerire quel ruolo.

## Pannelli

- **Rosa** — i 25 slot; per i vuoti, il miglior nome ancora disponibile e il tetto.
- **Liste** — la wishlist per slot (priorità, prezzi max, note), depennamento live.
- **Listone** — tutti i giocatori quotati, filtri per ruolo/squadra, ordinamento per
  FVM / Score / Qt.A; click per aprire l'acquisto.
- **Log** — cronologia completa: prezzi modificabili, compratori correggibili.
- **Report** — come sta andando (e com'è andata): speso per reparto vs budget, ogni
  acquisto vs il max del piano (affare/strapagato), occasioni sfumate (top-3 di lista
  andati ad altri, con chi e a quanto), tabella del tavolo con la spesa di tutti.
- **News & Rigoristi** — gli alert pre-asta, rigoristi/piazzati delle 20 squadre,
  sleeper dal web, fonti della ricerca.
- Testata: **⚙** budget, reparti e nomi avversari · **⧉** secondo schermo · **🤖**
  simulatore · **⬇/⬆** export/import JSON · **CSV** rosa per Excel (`;`, slot vuoti
  inclusi) · **✕** reset (doppia conferma).

## Simulatore (prova generale)

**🤖** in testata: modalità SIMULAZIONE con stato separato (localStorage dedicato, il
cookie di backup resta dell'asta vera), banner arancione; si esce ritrovando l'asta
reale intatta. **Prossima chiamata ▶** mette sul banco un giocatore tra i migliori
rimasti: i bot (le tue 9 avversarie) arrivano a un prezzo ~FVM riscalato sui 10.000
crediti del tavolo ±25%; compri col flusso vero o **Esc** e se lo porta via il bot —
registrato con prezzo e compratore, così alleni anche la strip avversari. **×10 auto**
fa scorrere dieci chiamate senza di te; **reset sim** azzera solo la prova.

## Secondo schermo

**⧉** in testata (o `index.html?view=liste`): apre le Liste in una finestra separata in
**sola lettura** — colonna di ricerca e azioni nascoste, badge "specchio" — che si
aggiorna da sola a ogni acquisto o depennamento nella finestra principale (storage
event; polling di riserva per il file aperto in doppio click). Funziona con qualunque
tab: `?view=report` per proiettare il report, `?view=rosa` per la rosa.

## Architettura e rigenerazione

| File | Ruolo |
|---|---|
| `listone.xlsx` | Quotazioni ufficiali (foglio `Tutti`) — si scarica da fantacalcio.it |
| `asta.xlsx` | La wishlist per slot (fogli Portieri/Difensori/…) e il piano budget |
| `research.json` | La ricerca web: alert, rigoristi, sleeper, correzioni wishlist (`wishlist_ops`), fonti |
| `app_template.html` | Il codice dell'app (CSS+JS), con segnaposto per i dati |
| `build.py` | `listone + asta + research → index.html`; calcola anche il FantaScore |
| `update.py` | Pipeline: `snapshot` / build+**diff novità**+gate su `!!` / `--test` |
| `index.html` | L'app finita, autosufficiente |
| `test.html` | Smoke test (64 assert) — risultati in pagina e via `fetch /__RESULTS__` |

```bash
python3 build.py          # build "nudo"
python3 update.py         # build + diff delle novità vs snapshot (fallisce se op '!!')
python3 update.py --test  # come sopra + smoke test nel browser (attende i 64 PASS)
```

Per aggiornare i consigli si modifica `research.json` e si rilancia il build: lo stato
dell'asta nel browser **non viene toccato**. Le correzioni alla wishlist si scrivono
come `wishlist_ops` (`update`/`add`/`remove` per slot); una volta consolidate si
possono "bakare" in `asta.xlsx` (procedura già rodata: le op del 13-14/8 sono lì).
Lo stato dell'asta vive solo nel browser (localStorage + cookie); la simulazione in un
localStorage separato (`…_sim`): il rebuild non tocca né l'uno né l'altra.

## La mattina dell'asta (runbook, 20-30 min)

Ordine: prima i dati (1-3), poi build e verifica (4-5), poi il browser (6).

### 1 · Listone aggiornato (5 min)

- Scarica le **Quotazioni Fantacalcio** 2026-27 aggiornate da fantacalcio.it (Excel).
- Sostituisci `listone.xlsx` (tieni una copia: `cp listone.xlsx listone.old.xlsx`).
- Controllo rapido: foglio `Tutti`, intestazioni alla riga 2, dati dalla riga 3
  (`Id, R, RM, Nome, Squadra, Qt.A, …, FVM`). Formato cambiato? Dillo a Claude che
  adatta `build.py`.
- Un giocatore di wishlist sparito dal listone (ceduto all'estero) viene segnalato dal
  build: toglilo da `asta.xlsx`/`research.json` o ignoralo.

### 2 · Ricerca fresca (15-20 min, la fa Claude)

Apri Claude Code nella cartella e digita **`/aggiorna-ricerca`**: snapshot, 7 agenti di
ricerca paralleli, sintesi in `research.json`, build con diff delle novità e smoke
test. Argomenti opzionali per restringere: `/aggiorna-ricerca solo infortuni e porte`.
Alla fine rileggi gli alert nuovi nel tab **News & Rigoristi** e verifica che i dossier
aperti abbiano una risposta (non "invariato" per pigrizia dell'agente).

### 3 · Ritocchi manuali (5 min, opzionale)

Nomi che vuoi assolutamente, prezzi max da alzare/abbassare: `wishlist_ops` in
`research.json` — `{"op":"update","role":"A","slot":"A3","name":"Simeone","maxprice":70}`
(op: `update` / `add` / `remove`) — oppure chiedi a Claude in italiano.

### 4 · Build + diff (1 min)

`python3 update.py` → `index.html written: …` + sezione `=== NOVITÀ ===`. Esce con
errore se ci sono righe `!!` (nome di una op che non matcha il listone: correggi e
rilancia).

### 5 · Smoke test (1 min)

`python3 update.py --test` → **64 PASS e nessun FAIL** nel browser.
⚠ Il test azzera lo stato salvato nel browser in cui gira: usa una finestra in
incognito, oppure fallo PRIMA del punto 6.

### 6 · Browser dell'asta (5 min)

- Apri `index.html` **nel browser e profilo che userai la sera**: niente incognito,
  niente "l'apro sull'altro PC".
- Roba di prova dentro? **✕ Reset**. Poi **⚙**: budget, reparti e **nomi dei 9
  avversari** (servono per il tracking a tasti 1-9).
- Giro di prova: cerca → Invio → prezzo → Invio, poi Ctrl+Z; una chiamata del
  simulatore 🤖; un **⬇ export** (è il tuo salvagente).
- Pagina nei preferiti / tab pinnato; **⧉** sul secondo schermo se ce l'hai.

### 7 · Ultimi 10 minuti (la sera)

- Occhiata a SOS Fanta / FantaMaster per l'ultima ora: le novità le appunti nel campo
  note del Log — niente rebuild a quel punto.
- Laptop in carica. Durante l'asta registra ogni giocatore battuto (tuo =
  Invio+prezzo, altrui = Shift+Invio+prezzo+chi): è ciò che tiene affidabili
  "Prossimi obiettivi", strip avversari, walk-away e report. A fine asta: **⬇ export**.

## Fonti della ricerca (14/08/2026)

30+ siti tra cui fantacalcio.it, SOS Fanta, FantaMaster, Goal, Calciodangolo, Sky
Sport, TMW, Corriere dello Sport, fantacalciopedia, pazzidifanta, Transfermarkt
(cartellini per il bonus fairplay) + testate locali; dettaglio nel tab News. Mercato
aperto fino all'1/9: il giorno dell'asta rilancia `/aggiorna-ricerca` per chiudere i
dossier caldi (porta Juve/Vicario, Leao, Pinamonti/Bowie, Badiashile, Lucumì, rigori
Cagliari, attacco Lazio).

## Licenza e contributi

Rilasciato sotto licenza [MIT](LICENSE). Contributi benvenuti: leggi
[CONTRIBUTING.md](CONTRIBUTING.md); per le vulnerabilità di sicurezza
[SECURITY.md](SECURITY.md) (segnalazione privata, niente issue pubbliche).
