#!/usr/bin/env python3
"""Build index.html: extract data from asta.xlsx + listone.xlsx, merge research.json,
inject everything into app_template.html as the DATA constant."""
import json
import re
import unicodedata
from pathlib import Path

import openpyxl

HERE = Path(__file__).parent


def norm(s):
    if not s:
        return ""
    s = unicodedata.normalize("NFD", str(s))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()


def extract_listone():
    wb = openpyxl.load_workbook(HERE / "listone.xlsx", data_only=True)
    players = []
    for r in wb["Tutti"].iter_rows(min_row=3, values_only=True):
        if r[3] is None:
            continue
        players.append({
            "id": r[0], "r": r[1], "rm": r[2], "name": r[3],
            "team": r[4], "qta": r[5], "fvm": r[11],
        })
    return players


def extract_asta():
    wb = openpyxl.load_workbook(HERE / "asta.xlsx", data_only=True)
    slots = []
    for row in wb["Asta"].iter_rows(min_row=17, max_row=41, values_only=True):
        if not row[0]:
            continue
        slots.append({
            "id": row[0], "role": row[1], "profile": row[2], "target": row[3],
            "team": row[4], "qta": row[5], "budget": row[6],
        })
    wishlist = {}
    sheet_role = {"Portieri": "P", "Difensori": "D", "Centrocampisti": "C", "Attaccanti": "A"}
    for sheet, role in sheet_role.items():
        ws = wb[sheet]
        groups = []
        cur = None
        for row in ws.iter_rows(values_only=True):
            a = row[0]
            if isinstance(a, str) and a.startswith("SLOT"):
                m = re.match(r"SLOT (\S+) — (.+?)\s+·\s+budget consigliato: (\d+)", a)
                cur = {
                    "slot": m.group(1) if m else a.split()[1],
                    "profile": m.group(2) if m else a,
                    "budget": int(m.group(3)) if m else None,
                    "players": [],
                }
                groups.append(cur)
            elif cur is not None and isinstance(a, (int, float)) and row[1]:
                cur["players"].append({
                    "prio": int(a), "name": row[1], "team": row[2], "qta": row[3],
                    "fvm": row[4], "tit": row[5], "rig": row[6], "bonus": row[7],
                    "maxprice": row[8], "note": row[9],
                })
        wishlist[role] = groups
    return slots, wishlist


def apply_ops(wishlist, ops):
    """ops: list of {op, role, slot, name, ...}. Supported ops:
    remove          — drop player `name` from slot list
    add             — append/insert player dict at `prio` (others reflow)
    update          — merge given fields into matching player
    """
    for o in ops:
        groups = wishlist.get(o["role"], [])
        grp = next((g for g in groups if g["slot"] == o["slot"]), None)
        if grp is None:
            print(f"  !! op skipped, slot not found: {o}")
            continue
        if o["op"] == "remove":
            before = len(grp["players"])
            grp["players"] = [p for p in grp["players"] if norm(p["name"]) != norm(o["name"])]
            if len(grp["players"]) == before:
                print(f"  !! remove: name not found: {o}")
        elif o["op"] == "update":
            hit = False
            for p in grp["players"]:
                if norm(p["name"]) == norm(o["name"]):
                    p.update({k: v for k, v in o.items() if k not in ("op", "role", "slot")})
                    hit = True
            if not hit:
                print(f"  !! update: name not found: {o}")
        elif o["op"] == "add":
            entry = {k: v for k, v in o.items() if k not in ("op", "role", "slot")}
            entry.setdefault("prio", len(grp["players"]) + 1)
            grp["players"].append(entry)
        # reflow priorities by 'prio' then original order
        grp["players"].sort(key=lambda p: p.get("prio", 99))
        for i, p in enumerate(grp["players"], 1):
            p["prio"] = i


def main():
    players = extract_listone()
    slots, wishlist = extract_asta()
    research = {}
    rpath = HERE / "research.json"
    if rpath.exists():
        research = json.loads(rpath.read_text())
        apply_ops(wishlist, research.get("wishlist_ops", []))

    data = {
        "season": "2026-27",
        "budget": 1000,
        "roleBudget": {"P": 80, "D": 130, "C": 265, "A": 525},
        "roleSlots": {"P": 3, "D": 8, "C": 8, "A": 6},
        "players": players,
        "slots": slots,
        "wishlist": wishlist,
        "rigoristi": research.get("rigoristi", {}),
        "alerts": research.get("alerts", []),
        "sleepers": research.get("sleepers", {}),
        "researchDate": research.get("date", ""),
        "sources": research.get("sources", []),
    }

    tpl = (HERE / "app_template.html").read_text()
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    html = tpl.replace("/*__DATA__*/null", payload)
    (HERE / "index.html").write_text(html)
    print(f"index.html written: {len(html)//1024} KB, {len(players)} players, "
          f"{len(data['alerts'])} alerts, {sum(len(v) for v in data['sleepers'].values()) if data['sleepers'] else 0} sleepers")


if __name__ == "__main__":
    main()
