# UPDATE.md — la mattina dell'asta

Runbook per arrivare alla sera con dati freschi. Tempo totale stimato: **30-45 minuti**,
di cui la metà la fa Claude da solo. Ordine consigliato: prima i dati (1-3), poi il
build (4), poi la verifica (5-6).

---

## 1 · Listone aggiornato (5 min)

Le quotazioni ufficiali cambiano fino all'ultimo (nuovi acquisti, ceduti, cambi ruolo).

- [ ] Scarica le **Quotazioni Fantacalcio** aggiornate da fantacalcio.it
      (formato Excel, stagione 2026-27 — lo stesso file da cui viene `listone.xlsx`).
- [ ] Sostituisci `listone.xlsx` nella cartella (tieni una copia del vecchio:
      `cp listone.xlsx listone.old.xlsx`).
- [ ] Controllo rapido: il foglio si chiama ancora `Tutti`, intestazioni alla riga 2,
      dati dalla riga 3 (`Id, R, RM, Nome, Squadra, Qt.A, …, FVM`). Se il formato è
      cambiato, dillo a Claude che adatta `build.py`.

> Se un giocatore della wishlist è sparito dal listone (ceduto all'estero), il build
> lo segnala e in app comparirà senza scheda: va tolto da `research.json`/asta.xlsx
> o semplicemente ignorato.

## 2 · Ricerca fresca (15-20 min, la fa Claude)

Apri Claude Code nella cartella e incolla questo prompt:

> Rifai la ricerca pre-asta di UPDATE.md: lancia agenti paralleli su fantacalcio.it,
> SOS Fanta, FantaMaster, Goal, Calciodangolo, Sky e TMW con le notizie di OGGI e
> aggiorna `research.json` (alerts, rigoristi, sleepers, wishlist_ops), poi rilancia
> `python3 build.py` e i test. Verifica in particolare i dossier aperti:
> 1. **Porta Juventus** — Vicario è arrivato? Di Gregorio è partito? Chi gioca la 1ª?
> 2. **Rigorista Milan** — Nkunku / Ramos G. / Pulisic: gerarchia definita? Pulisic recuperato? Gimenez partito?
> 3. **Atalanta** — ballottaggio Scamacca/Krstovic dopo le ultime amichevoli.
> 4. **Uscite calde** — Lukaku (Fenerbahçe ufficiale?), Pinamonti, Pellegrino M., Suzuki, Solet, Dodò, David, Morata, Milinkovic-Savic V.: chi è ancora in Serie A?
> 5. **Porta Torino** (Perri ufficiale? Paleari dov'è?), **porta Parma** (Corvi/Daffara), **Lecce** (Geubbels vs Stulic), **rigori Napoli** (De Bruyne vs Hojlund), **rigori Cagliari**.
> 6. **Infortunati e squalificati per la 1ª giornata** — lista completa aggiornata (occhio a Malen, Pulisic, Beukema, Tavares N., Sulemana K.).
> 7. **Probabili formazioni della 1ª** appena pubblicate: ballottaggi nuovi rispetto al 12/8.

- [ ] Rileggi gli alert nuovi nel tab **News & Rigoristi** e verifica che i 7 punti
      abbiano una risposta (non "invariato" per pigrizia dell'agente).

## 3 · Ritocchi manuali alla lista (5 min, opzionale)

- [ ] Se nella settimana ti sei fatto idee tue (nomi che vuoi assolutamente, prezzi max
      da alzare/abbassare), aggiungile come `wishlist_ops` in `research.json` — formato:
      `{"op":"update","role":"A","slot":"A3","name":"Simeone","maxprice":70}`
      (op: `update` / `add` / `remove`). Oppure chiedi a Claude in italiano.

## 4 · Build (1 min)

```bash
cd ~/dev/fantaasta && python3 build.py
```

- [ ] Output atteso: `index.html written: … KB, ~500 players, N alerts, N sleepers`.
- [ ] **Zero righe `!!`** (op saltate / nomi non trovati). Se compaiono, il nome nella
      op non matcha il listone nuovo: correggilo e rilancia.

## 5 · Smoke test (3 min)

```bash
python3 -m http.server 8642
```

- [ ] Apri `http://localhost:8642/test.html`: in fondo alla pagina devono esserci
      **26 PASS e nessun FAIL** (⚠ il test azzera lo stato salvato nel browser in cui
      lo apri: usa una finestra in incognito, oppure fallo PRIMA del punto 6).
- [ ] Chiudi il server (Ctrl+C).

## 6 · Preparazione del browser dell'asta (5 min)

- [ ] Apri `index.html` (doppio click) **nel browser e nel profilo che userai la sera**
      — lo stato vive lì (localStorage): niente incognito, niente "l'apro sull'altro PC".
- [ ] Se c'è dentro roba di prova: **✕ Reset** (doppia conferma).
- [ ] **⚙**: budget totale e budget per reparto come li vuoi (default 1000 · P80 D130 C265 A525).
- [ ] Prova il giro completo una volta: cerca → Invio → prezzo → Invio, poi Ctrl+Z.
- [ ] Prova **⬇ export**: scarica il JSON e verifica che arrivi (è il tuo salvagente).
- [ ] Metti la pagina tra i preferiti / lasciala aperta in un tab pinnato.

## 7 · Ultimi 10 minuti prima dell'asta (la sera)

- [ ] Occhiata veloce a SOS Fanta / FantaMaster per news dell'ultima ora (una cessione
      alle 19 può cambiare un ballottaggio): eventuali novità le tieni a mente o le
      appunti nel campo note del Log — niente rebuild a quel punto.
- [ ] Laptop in carica, seconda finestra col tab **Liste** già aperto se hai due schermi.
- [ ] Durante l'asta: ogni giocatore battuto va registrato (tuo = Invio+prezzo, altrui =
      Shift+Invio) — è quello che tiene affidabili i "Prossimi obiettivi".
- [ ] A fine asta: **⬇ export** del JSON.

---

### Riferimenti rapidi

| Cosa | Dove |
|---|---|
| Consigli/alert/rigoristi | `research.json` → `build.py` → embedded in `index.html` |
| Wishlist di base (slot e priorità) | `asta.xlsx` (fogli Portieri/Difensori/…) |
| Stato dell'asta | Solo nel browser (localStorage `fantaasta_2627_v1` + cookie) — il rebuild NON lo tocca |
| Istruzioni complete | `README.md` |
