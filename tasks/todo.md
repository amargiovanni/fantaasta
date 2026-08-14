# Aggiornamento ricerca pre-asta — 14/08/2026 ✅

- [x] Ricerca parallela (7 agenti): porte, mercato caldo, rigoristi/piazzati,
      infortunati/squalificati, probabili formazioni, cartellini/fairplay, sleepers
- [x] Sintesi in `research.json` (124 alert, 74 sleeper, 160 wishlist_ops, fairplay
      integrato: 9 alert dedicati + note nei giocatori)
- [x] `python3 build.py` senza righe `!!` (201 KB, 497 giocatori)
- [x] Wishlist aggiornata baked in `asta.xlsx` (verificata: estrazione == merge);
      `wishlist_ops` svuotate per le correzioni future
- [ ] Smoke test `test.html` nel browser (Chrome non raggiungeva localhost dalla
      sessione: da fare a mano — `python3 -m http.server 8642` → 26 PASS attesi)
- [ ] Il giorno dell'asta: rilanciare punto 7 di UPDATE.md (probabili vere del 19-21/8)
      e i dossier: Vicario-Juve, Leao, Pinamonti/Bowie, Badiashile, Lucumì,
      rigori Cagliari (Kevin Carlos vs Maldini), attacco Lazio a 3
