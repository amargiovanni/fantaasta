# Riconciliazione wishlist (16/08) — approvata in chat

Obiettivo: eliminare la deriva accumulata dagli update incrementali senza rifare
la lista. Meccanismo: `wishlist_ops` in research.json (il build le applica;
"bake" in asta.xlsx rimandato a fine giornata come da update.py) + edit diretto
delle sole 3 celle target stantie nel foglio "Asta".

- [x] Ops P: rimuovere Di Gregorio (P1), Suzuki (P2), Paleari (P3); Perin → prio 1
      in P3; Milinkovic-Savic max 5→2 e demote; nota Meret senza "Falcone in arrivo"
- [x] Ops D: unificare Kempf (max 2 declassato in D6/D7/D8), Tavares (max 3 ko
      ginocchio in D7/D8), Correia (max 2 in D7/D8), Mangas (max 10 in D7/D8),
      Bisseck (max 12 + nota campo in D4), Kristensen team→Atalanta, Celik nota
      "ballottaggio Kalulu" (D5/D7), Vojvoda tit (D6), Zortea max 6 (D6, trovato
      dalla verifica automatica)
- [x] Ops C: Frattesi via da C7 → add in C4 come Lazio; Samardzic max 28 in C3 e
      via da C7 (non più low cost); Pessina (operato) via da C7; Basic congelato
      anche in C8; Calò max 15 in C8; Perez K. max 4; Rabiot C2 allineato a C1
      (rientro tardivo, max 45)
- [x] Ops A: Nkunku (fuori rosa) via da A4; Pellegrino via da A3 → add in A6 come
      Fiorentina (vice Kean, max 5); Adams A. max 22 in A5; Tourè non più
      "rigorista" (A4/A6); Yeboah → prio 1 A6; Ghedjemis demote
- [x] asta.xlsx foglio "Asta": target P3 Paleari→Perin, C7 Berisha→Calò,
      A6 Ghedjemis→Yeboah (righe 19/34/41); i 4 grafici in "Grafici" verificati
      intatti dopo il round-trip openpyxl
- [x] `python3 update.py` — build verde, 39 ops applicate, zero "!!"
- [x] `python3 update.py --test` — smoke test: 66 assert, 0 non-PASS
- [x] Verifica post-ops: zero maxprice divergenti cross-slot; target slot ==
      prio 1 per tutti i 25 slot

Nota: le ops restano in research.json come previsto da update.py; il "bake" in
asta.xlsx è un passo separato da fare a fine giornata se si vuole azzerare la lista.
