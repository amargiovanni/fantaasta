#!/usr/bin/env python3
"""Pipeline pre-asta: snapshot → (ricerca via /aggiorna-ricerca) → build+diff+test.

  python3 update.py snapshot   salva research.json in .research_prev.json (prima della ricerca)
  python3 update.py            build + verifica (zero '!!') + diff novità vs snapshot
  python3 update.py --test     come sopra, poi apre test.html nel browser e attende i 57 PASS
"""
import io
import json
import sys
import contextlib
import threading
import urllib.parse
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

HERE = Path(__file__).parent
PREV = HERE / ".research_prev.json"
CUR = HERE / "research.json"


def snapshot():
    PREV.write_text(CUR.read_text())
    print(f"snapshot: research.json → {PREV.name}")


def run_build():
    import build
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        build.main()
    text = out.getvalue()
    print(text, end="")
    bad = [l for l in text.splitlines() if l.strip().startswith("!!")]
    if bad:
        print(f"\nBUILD CON ERRORI: {len(bad)} op saltate — correggi research.json e rilancia.")
        sys.exit(1)


def akey(a):
    return (a.get("name", ""), a.get("team", ""))


def diff():
    if not PREV.exists():
        print("\n(nessuno snapshot precedente: lancia 'update.py snapshot' prima della ricerca "
              "per avere il diff delle novità)")
        return
    old = json.loads(PREV.read_text())
    new = json.loads(CUR.read_text())
    print(f"\n=== NOVITÀ: {old.get('date', '?')} → {new.get('date', '?')} ===")

    oa = {akey(a): a for a in old.get("alerts", [])}
    na = {akey(a): a for a in new.get("alerts", [])}
    added = [na[k] for k in na if k not in oa]
    removed = [oa[k] for k in oa if k not in na]
    changed = [na[k] for k in na if k in oa and (na[k]["text"] != oa[k]["text"] or na[k]["type"] != oa[k]["type"])]
    for label, items in (("ALERT NUOVI", added), ("ALERT CAMBIATI", changed), ("ALERT RIMOSSI", removed)):
        if items:
            print(f"\n-- {label} ({len(items)}) --")
            for a in items:
                print(f"  [{a.get('type', '?'):12}] {a['name']} ({a.get('team', '')}) — {a.get('text', '')[:110]}")

    orig, nrig = old.get("rigoristi", {}), new.get("rigoristi", {})
    rchanged = [t for t in nrig if json.dumps(nrig[t], sort_keys=True) != json.dumps(orig.get(t), sort_keys=True)]
    if rchanged:
        print(f"\n-- RIGORISTI CAMBIATI ({len(rchanged)}) --")
        for t in rchanged:
            print(f"  {t}: {nrig[t].get('rigori', '')[:110]}")

    for role in ("P", "D", "C", "A"):
        os_ = {s["name"] for s in old.get("sleepers", {}).get(role, [])}
        ns_ = {s["name"] for s in new.get("sleepers", {}).get(role, [])}
        if ns_ - os_ or os_ - ns_:
            plus = ", ".join(sorted(ns_ - os_)) or "—"
            minus = ", ".join(sorted(os_ - ns_)) or "—"
            print(f"\n-- SLEEPER {role}: nuovi: {plus} · usciti: {minus}")

    ops = new.get("wishlist_ops", [])
    if ops:
        print(f"\n-- WISHLIST_OPS da applicare: {len(ops)} (il build le applica; "
              f"valuta se 'bakarle' in asta.xlsx a fine giornata)")
    if not (added or removed or changed or rchanged):
        print("\nNessuna differenza sostanziale rispetto allo snapshot.")


def smoke_test():
    results = {}
    done = threading.Event()

    class H(SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_GET(self):
            if self.path.startswith("/__RESULTS__"):
                q = urllib.parse.unquote(self.path.split("?", 1)[1]) if "?" in self.path else ""
                results["list"] = q.split("|")
                self.send_response(204)
                self.end_headers()
                done.set()
            else:
                super().do_GET()

    srv = HTTPServer(("127.0.0.1", 8642), H)
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    print("\nApro test.html nel browser (attendo i risultati, max 60s)…")
    webbrowser.open("http://127.0.0.1:8642/test.html")
    if not done.wait(60):
        print("TIMEOUT: nessun risultato ricevuto dal browser.")
        srv.shutdown()
        sys.exit(1)
    srv.shutdown()
    res = results["list"]
    fails = [r for r in res if not r.startswith("PASS")]
    print(f"smoke test: {len(res)} assert, {len(fails)} non-PASS")
    for f in fails:
        print(" >>", f)
    if fails:
        sys.exit(1)


def main():
    if "snapshot" in sys.argv:
        snapshot()
        return
    run_build()
    diff()
    if "--test" in sys.argv:
        smoke_test()
    print("\nOK. Prossimi passi: rileggi il diff qui sopra, poi commit.")


if __name__ == "__main__":
    main()
