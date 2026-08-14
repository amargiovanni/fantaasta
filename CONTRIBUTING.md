# Contribuire a FantaAsta

Grazie dell'interesse! Questo è un progetto personale nato per un'asta vera: PR e
issue sono benvenute, con qualche regola per tenere il tutto affidabile a ridosso
delle aste.

## Setup

```bash
git clone https://github.com/amargiovanni/fantaasta.git
cd fantaasta
python3 -m pip install openpyxl   # unica dipendenza (per leggere gli xlsx)
python3 build.py                  # genera index.html
```

L'architettura è descritta nel [README](README.md#architettura-e-rigenerazione).
La regola d'oro: **`index.html` è generato** — si modifica `app_template.html` (codice
dell'app), `build.py`/`update.py` (pipeline) o `research.json` (dati), mai l'output.

## Prima di aprire una PR

1. `python3 update.py --test` → **tutti gli assert PASS** nel browser (lo smoke test
   copre ricerca, acquisti, cap, tracking avversari, walk-away, simulatore, mirror).
   Una feature o un fix nuovo porta con sé almeno un assert nuovo in `test.html`.
2. `python3 update.py` senza righe `!!` se hai toccato wishlist o research.
3. Niente dipendenze nuove (né npm né pip) senza discuterne prima in una issue:
   l'app deve restare un singolo file che funziona offline.

## Convenzioni

- Commit: `type(scope): imperative subject` in inglese, ≤72 caratteri
  (`feat|fix|refactor|test|docs|chore`). Un commit = una modifica logica.
- Codice e identificatori in inglese; la documentazione utente è in italiano.
- PR: cosa cambia, perché, come testarla.

## Issue

Per i bug: passi per riprodurre, browser usato, e se possibile l'export JSON dello
stato (⬇) anonimizzato. Per le vulnerabilità di sicurezza **non aprire una issue**:
vedi [SECURITY.md](SECURITY.md).
