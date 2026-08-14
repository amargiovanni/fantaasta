# Security policy

FantaAsta è un'app **single-file e locale**: `index.html` gira nel tuo browser, non ha
backend, non invia dati a nessun server e lo stato (acquisti, budget) vive solo in
localStorage/cookie del tuo browser. La superficie d'attacco è quindi piccola, ma non
nulla: il build (`build.py`/`update.py`) elabora file Excel e JSON, e l'HTML generato
rende contenuti provenienti dalla ricerca web (`research.json`).

## Segnalare una vulnerabilità

Usa la **segnalazione privata di GitHub**: tab *Security* del repository →
*Report a vulnerability*. Per favore **non aprire una issue pubblica** per problemi
di sicurezza.

Includi, per quanto puoi:

- versione/commit interessato;
- cosa può ottenere un attaccante e da dove parte (es. un `listone.xlsx` o un
  `research.json` malevolo, un backup JSON importato, XSS nell'HTML generato);
- passi per riprodurre o proof of concept.

## Cosa aspettarti

Progetto personale mantenuto nel tempo libero, quindi tempi onesti e non contrattuali:

| Fase | Obiettivo |
|---|---|
| Presa in carico | entro ~1 settimana |
| Valutazione e risposta | entro ~2 settimane |
| Fix per problemi confermati | appena ragionevolmente possibile; le segnalazioni con exploit noto hanno precedenza |

Disclosure coordinata: pubblica dopo il fix, con credito a chi ha segnalato (se
gradito).

## Fuori scope

- Vulnerabilità nei siti terzi consultati dalla ricerca (fantacalcio.it, ecc.);
- problemi che richiedono che l'attaccante abbia già accesso al tuo browser/profilo;
- l'uso dell'app per farsi battere all'asta dal cugino.
