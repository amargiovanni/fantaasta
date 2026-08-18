# Evoluzione post-asta (18/08) — mercato di riparazione + formazione settimanale

Contesto: asta conclusa il 17/8 (rosa completa 25/25, residuo 203). Il tool passa
dalla "sala d'asta" alla gestione stagione. Stato invariato: un solo localStorage
(`fantaasta_2627_v1`); le nuove feature sono azioni/campi aggiuntivi dello stesso
stato, così undo/export/import/mirror continuano a funzionare.

## Design (bounded, approccio scelto)

- **Svincolo (`cut`)**: nuova azione `{t:'cut', pid, name, role, team, slot, refund, ts}`.
  `derive()` processa le azioni in sequenza: un `cut` toglie il giocatore dalla rosa,
  libera lo slot e restituisce `refund` crediti (regola configurabile in ⚙:
  `recoupPct`, default 100% del prezzo pagato). Riacquisto possibile (flusso d'asta
  invariato: la ricerca in alto resta il modo per comprare, anche in riparazione).
- **Tab Mercato**: crediti disponibili, riepilogo svincoli, tabella rosa con bottone
  "Svincola" (conferma + anteprima rimborso), import rosa da CSV (formati:
  `slot;ruolo;nome;squadra;prezzo` o `ruolo;nome;squadra;prezzo`; assegna slot
  wishlist libero, altrimenti primo libero del ruolo; report nomi non trovati).
- **Tab Formazione**: `state.lineups[giornata] = {module, xi:{P,D,C,A}, bench:{P,D,C,A}}`
  + `state.curGiornata`. Moduli classic: 3-4-3, 3-5-2, 4-3-3, 4-4-2, 4-5-1, 5-3-2,
  5-4-1. Chips cliccabili per titolari (vincolo conteggi modulo), panchina ordinabile
  ↑↓ per ruolo, pallino alert dalla ricerca, bottone ✨auto (miglior FantaScore),
  giornata nuova pre-compilata dall'ultima salvata, testo formazione copiabile
  (textarea + clipboard best-effort). Autosave a ogni modifica.
- **Mirror**: `?view=mercato` e `?view=formazione` ammessi.
- **Log**: righe `cut` renderizzate (♻ + rimborso).

## Task

- [x] `derive()` sequenziale con `cut` (spent netto, spentRole netto, slot liberati)
- [x] `doCut` + settings `recoupPct` (⚙) + default state (`recoupPct`, `lineups`, `curGiornata`)
- [x] Tab Mercato (svincoli + import CSV `importRosterCsv`)
- [x] Tab Formazione (moduli, XI, panchina, auto, copia testo `buildLineupText`)
- [x] Log: rendering azioni `cut`
- [x] Mirror whitelist + footer invariati
- [x] test.html: nuovi assert (cut/refund/riacquisto/recoupPct 50, import CSV, lineup+testo)
- [x] `python3 update.py` (build, zero `!!`) + smoke test in Chrome **headless**
      (MAI il browser di default: azzererebbe la rosa reale)
