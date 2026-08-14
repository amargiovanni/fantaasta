# Sala d'asta intelligente — 14/08/2026 ✅ (49/49 test PASS)

- [x] FantaScore 0-99 in build.py (percentile FVM + titolarità + rigori/piazzati −
      infortuni − cartellini − mercato) — top: Orsolini 91, Da Cunha/Malen 89;
      flop coerenti: Neres 24, David 25, Ratkov 27
- [x] Setup avversari in ⚙ (textarea, default Squadra 2…10)
- [x] Shift+Invio → prezzo → tasto 1-9/0 per il compratore (Esc = registra e basta)
- [x] Strip avversari sotto la testata (crediti, slot per ruolo, max offerta)
- [x] Walk-away "Molla a" nella scheda + riga "possono superarti"
- [x] FantaScore in Listone (colonna+sort), ricerca (S xx) e scheda
- [x] test.html: 49 assert, tutti PASS (via /__RESULTS__ nel log del server)
- [x] README e UPDATE.md aggiornati

## Prossimi (in ordine, ognuno col suo mini-design)
- [x] Simulatore d'asta ✅ (modalità 🤖: stato separato, chiamate con bot a
      FVM×scala±25%, ×10 auto, reset; 57/57 test PASS; fix harness: il test ora
      pulisce anche il cookie di backup)
- [x] Pipeline ricerca a un click ✅ (`/aggiorna-ricerca` + `update.py`:
      snapshot/diff novità/build gate su `!!`/smoke test integrato — collaudati
      diff simulato e --test 57/57)
- [x] UX contorno ✅ (tab Report: acquisti vs piano, occasioni sfumate, tavolo;
      bottone ⧉ / ?view=liste: specchio sola-lettura per il secondo schermo con
      sync via storage event + poll; 64/64 test PASS)
- [ ] Il giorno dell'asta: rilanciare ricerca (probabili vere 19-21/8) — dossier:
      Vicario-Juve, Leao, Pinamonti/Bowie, Badiashile, Lucumì, rigori Cagliari,
      attacco Lazio a 3
