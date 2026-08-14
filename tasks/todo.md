# FantaAsta 2026-27 — web app + ricerca profonda

- [x] Estrarre dati da asta.xlsx (slot, wishlist per reparto) e listone.xlsx (499 giocatori)
- [x] Ricerca profonda web (20+ siti, 6 agenti paralleli): gerarchie portieri, rigoristi 20 squadre, sleeper per reparto, neopromosse/provincia, infortuni/mercato agosto 2026
- [x] Aggiornare la wishlist con i risultati (55 correzioni: Hien/Buongiorno infortuni, Di Gregorio/Suzuki/Lukaku/Pinamonti/Pellegrino in uscita, Calò/Colombo/Ratkov promossi, +9 nomi nuovi)
- [x] Costruire index.html (single file, dati embedded, localStorage + cookie backup)
  - [x] Ricerca istantanea senza accenti → ruolo, squadra, Qt.A, FVM, badge wishlist (slot + priorità + prezzo max), badge occasioni, alert
  - [x] Invio = comprato → autofocus prezzo → Invio = registrato nello slot giusto
  - [x] Shift+Invio / bottone = preso da altri
  - [x] Dashboard budget: totale/speso/residuo, meter per reparto, media/slot, cap assoluto
  - [x] Rosa 25 slot con suggerimento per slot vuoto, Liste con depennamento, Listone filtrabile, Log modificabile, News & Rigoristi
  - [x] Undo (Ctrl+Z), modifica/rimozione acquisto, reset doppia conferma, export/import JSON, impostazioni budget
- [x] Verifica: 26/26 smoke test PASS in Chrome headless + screenshot ok

## Upgrade sala d'asta (13/08/2026) — design approvato in chat

- [x] `derive()`: fattore di ridistribuzione (residuo / somma budget slot vuoti), delta vs piano, tetto slot aggiustato
- [x] Indici: `slotById`, `wishBySlot`, helper `slotAvailable(slotId, d)` (wishlist ancora libera per slot)
- [x] Testata: indicatore "Vs piano" (+/− crediti rispetto al pianificato, verde/arancio)
- [x] Rosa: tetto aggiustato accanto al pianificato (`≤35 → 42`) + badge scarsità su slot vuoti
- [x] Suggerimenti: chip arancio a 2 nomi rimasti, rosso a 1 ("ultimo!")
- [x] Scheda acquisto: cap "Tetto slot" aggiustato + sezione "Se lo perdi" (3 alternative libere, avviso ultimo nome), reattiva al cambio slot
- [x] Export CSV rosa (`;`, BOM per Excel, slot vuoti inclusi) da bottone in testata
- [x] Test in test.html: factor/delta, slotAvailable, buildCsv, sezione alternative, tetto slot
- [x] `python3 build.py` + smoke test 35/35 PASS in Chrome headless
- [x] (dalla chat precedente) autocomplete: niente suggerimenti per reparti già completi
