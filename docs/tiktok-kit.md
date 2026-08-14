# TikTok kit — "L'asta non è fortuna" (45s)

Tutto il girato dell'app è **auto-recitato**: apri l'URL, premi REC, la scena si
esegue da sola con tempi umani. Prima di registrare:

```bash
cd ~/dev/fantaasta && python3 -m http.server 8000
```

Poi apri gli URL qui sotto in Chrome a **finestra massimizzata, zoom 100%**,
registra lo schermo a 60fps (QuickTime/OBS). Ogni scena parte ~1s dopo il
caricamento: avvia REC, ricarica la pagina (⌘R), lascia correre.

## Cosa registrare (7 clip, ~15 min di lavoro)

| # | Clip | Come | Durata REC |
|---|------|------|-----------|
| 1 | **Selfie hook** — faccia seria, poi mezzo sorriso | telefono, verticale, luce frontale | 2 riprese da 5s |
| 2 | Hero + ricerca | `http://localhost:8000/docs/shots/_driver.html?s=rec-main` | 8s |
| 3 | Acquisto completo (cerca→scheda→95→comprato) | `…?s=rec-buy` | 13s |
| 4 | Shift+Invio: Leao va ad AC Picchia per 98 | `…?s=rec-gone` | 11s |
| 5 | Scheda Colombo ferma (walk-away) | `…?s=rec-walk` | 8s |
| 6 | Simulatore: 3 chiamate bot + una tua | `…?s=rec-sim` | 13s |
| 7 | Report con scroll lento | `…?s=rec-report` | 12s |
| 8 | **Selfie CTA** — sorriso da chi ha già vinto | telefono, verticale | 2 riprese da 6s |

Registra 2-3 secondi extra prima/dopo ogni clip: servono ai tagli.

## Voice-over (leggilo a ritmo alto, ~140 parole/min)

1. *(hook, in camera)* «Tuo cugino arriva all'asta con un Excel. Tu quest'anno
   arrivi con QUESTO.»
2. *(su clip 2)* «Il problema dell'asta non è chi comprare. È che a metà serata
   NESSUNO sa più chi ha quanti crediti. Nessuno… tranne te.»
3. *(su clip 4)* «Uno compra un giocatore? Due tasti: prezzo, e chi l'ha preso.
   L'app si segna tutto: budget, slot, quanto possono ancora rilanciare.»
4. *(su clip 5)* «E quando parte l'asta su un nome grosso, lei ti dice il numero
   più importante della tua vita: fin dove spingerti… e QUANDO mollare. Perché sa
   quante alternative ti restano e chi può ancora superarti.»
5. *(su clip 6)* «Ansia da prestazione? C'è il simulatore: i bot rilanciano, tu
   ti alleni. Prova l'asta PRIMA dell'asta.»
6. *(su clip 7 + flash di clip 3)* «Dentro c'è pure la ricerca fatta dall'AI su
   trenta siti: infortuni, rigoristi, perfino chi prende troppi cartellini. E a
   fine serata, il report: chi hai pagato bene e chi hai strapagato.»
7. *(CTA, in camera)* «Gratis, open source, UN file: lo scarichi e lo apri nel
   browser. Niente account, i dati restano tuoi. Link in bio — e all'asta, zero
   pietà.»

## Montaggio (CapCut)

Timeline 45s, formato 9:16 — le clip schermo sono orizzontali: **zoom & pan**
sulle zone indicate, mai lasciarle intere.

| Tempo | Clip | Zoom su | Overlay (testo grande, 2 righe max) |
|---|---|---|---|
| 0:00–0:03 | 1 | — | **il fantacalcio non perdona** |
| 0:03–0:10 | 2 | strip avversari in alto | **sai i crediti di TUTTI. in tempo reale.** |
| 0:10–0:18 | 4 | mini-scheda → strip che si aggiorna | **2 tasti. 2 secondi.** |
| 0:18–0:28 | 5 | riquadro "MOLLA A 35" → riga "possono superarti" | **il prezzo di walk-away. calcolato. non a sentimento.** |
| 0:28–0:35 | 6 | riga «🤖 I bot arrivano a…» | **allenati contro i bot 🤖** |
| 0:35–0:41 | 7 (+1s di clip 3) | colonna "Esito" (▼ verdi / ▲ arancio) | **124 alert · rigoristi · fairplay** |
| 0:41–0:45 | 8 | — | **GitHub → fantaasta ⭐ · gratis** |

- Taglio ogni ≤2,5s; sound design: un "click/pop" sui due tasti della clip 4.
- Musica: qualcosa di teso/epico dal Commercial Music Library di TikTok, drop
  sul passaggio a 0:18 (walk-away).
- Sottotitoli automatici attivi (molti guardano senza audio).

## Pubblicazione

**Caption:** L'Excel di tuo cugino non è pronto a tutto questo 💀 Un file, zero
account, open source. Link in bio prima che lo trovi il resto della tua lega.
#fantacalcio

**Hashtag:** #fantacalcio #astafantacalcio #seriea #fanta #calcio
#consiglifantacalcio #opensource

**Link in bio:** https://github.com/amargiovanni/fantaasta/releases/latest
(un tap → scarichi `index.html` → funziona).

**Orario:** 12:30–14:00 o 21:00–23:00, i giorni pre-asta (18–24 agosto = picco
stagionale della lega media).

**Hook alternativi** (stesso corpo, testali come video separati a 24h di
distanza): 1) «Ho fatto un'app per DISTRUGGERE la mia lega al fantacalcio. E
l'ho messa gratis su internet.» · 2) «POV: sei l'unico all'asta che sa quanti
crediti hanno gli altri.» · 3) «Se all'asta paghi un giocatore "a sensazione",
questo video ti fa risparmiare 100 crediti.»
