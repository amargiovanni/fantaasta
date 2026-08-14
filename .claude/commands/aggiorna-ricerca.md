---
description: Rilancia la ricerca pre-asta multi-agente, aggiorna research.json, build + diff novità + smoke test
argument-hint: "[note extra, es. 'solo infortuni e porte']"
---

Esegui la pipeline di aggiornamento pre-asta di FantaAsta. Argomenti extra dell'utente (se presenti, restringono o estendono i filoni): $ARGUMENTS

## 1. Snapshot

Esegui `python3 update.py snapshot` (salva lo stato attuale per il diff finale).

## 2. Ricerca parallela (7 subagent)

Leggi `research.json` per conoscere lo stato attuale (data, dossier aperti, gerarchie).
Poi lancia **in un unico messaggio** 7 agenti `general-purpose` paralleli, uno per filone.
Ogni prompt DEVE essere autosufficiente (l'agente non vede questa conversazione):
data di OGGI, elenco delle 20 squadre di Serie A se serve, lo stato attuale dei dossier
pertinenti copiato da research.json, e queste regole fisse:

- usa WebSearch/WebFetch in modo estensivo (10+ ricerche in italiano), notizie degli ultimi 1-2 giorni;
- per ogni claim: fonte + data; verdetto CONFERMATO / CAMBIATO / APERTO / NON VERIFICABILE;
- MAI inventare: se non trovi notizie fresche su un punto, scrivilo;
- il messaggio finale è un report strutturato per squadra/dossier, non una sintesi vaga.

I 7 filoni (adatta i dossier aperti a quelli correnti in research.json):

1. **Porte** — gerarchie portieri delle 20 squadre, titolare atteso alla prossima giornata, ballottaggi con %.
2. **Mercato** — dossier aperti da research.json (sezione sources/alerts di tipo mercato) + operazioni ufficializzate negli ultimi 2 giorni.
3. **Rigoristi e piazzati** — verifica delle 20 gerarchie, in particolare quelle marcate APERTO/CONTESO.
4. **Infortunati e squalificati** — lista completa per la prossima giornata + infortuni nuovi delle ultime 48h.
5. **Probabili formazioni** — XI e ballottaggi per squadra; segnala dove gli aggregatori sono in ritardo sulla cronaca.
6. **Cartellini / fairplay** — solo se sono passati 15+ giorni dall'ultima verifica o su richiesta: aggiornare la mappa rischio cartellini (Transfermarkt/BeSoccer). Altrimenti saltalo.
7. **Sleeper / consigli d'asta** — verdetto sui nostri sleeper (CONFERMATO / BRUCIATO / BOCCIATO / nessuna notizia) + nomi nuovi con quotazione e fonte.

Se un agente va in idle senza consegnare, sollecitalo via SendMessage chiedendo il report finale.

## 3. Sintesi in research.json

Aggiorna `research.json` integrando i report: `date`, `rigoristi`, `alerts` (aggiorna gli
esistenti, aggiungi i nuovi, rimuovi gli obsoleti; tipi validi: infortunio, mercato,
ballottaggio, squalifica, ok, fairplay), `sleepers`, `sources` (con date).
Le correzioni alla wishlist vanno in `wishlist_ops` (`update`/`add`/`remove` per slot —
la lista riparte vuota perché le op precedenti sono già state applicate in `asta.xlsx`).
Se un giocatore nuovo va aggiunto, prendi Qt.A e FVM dal listone via
`python3 -c "import build; ..."`. Non inventare mai quotazioni.

## 4. Build, diff e test

- `python3 update.py` — build + verifica (zero righe `!!`, altrimenti correggi i nomi e
  rilancia) + **diff delle novità** rispetto allo snapshot: mostralo all'utente com'è.
- `python3 update.py --test` — apre lo smoke test nel browser e attende i PASS
  (64 assert; se l'utente non può aprire il browser, salta e dillo).

## 5. Chiusura

- Se le `wishlist_ops` accumulate sono tante e verificate, proponi (senza farlo da solo)
  di "bakarle" in `asta.xlsx` come da procedura in `tasks/lessons.md`/README.
- Commit: `feat|chore(research): ...` con il sommario delle novità. Push solo se il
  workflow del repo lo prevede già.
- Ricorda all'utente i dossier rimasti aperti (verdetti APERTO/NON VERIFICABILE).
