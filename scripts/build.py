#!/usr/bin/env python3
"""Build a curated M3U using only entries in IPTV-org's public Worldwide M3U.

No streams are hosted or proxied. Missing channels are reported, not fabricated.
"""
import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))


def fetch_playlist(url):
    req = urllib.request.Request(url, headers={"User-Agent": "MyPersonalIPTVPlaylist/1.0"})
    with urllib.request.urlopen(req, timeout=75) as response:
        content = response.read().decode("utf-8-sig", errors="replace")
    if not content.startswith("#EXTM3U"):
        raise ValueError("La fuente no es una playlist M3U válida")
    return content


def parse_playlist(content):
    entries, meta, extras = [], None, []
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("#EXTINF:"):
            meta, extras = line, []
        elif meta is not None and line.startswith("#"):
            extras.append(line)
        elif meta is not None and line and not line.startswith("#"):
            name = meta.rsplit(",", 1)[-1].strip()
            tvg = re.search(r'tvg-id="([^"]*)"', meta)
            entries.append({"name": name, "tvg_id": tvg.group(1) if tvg else "", "meta": meta, "extras": extras, "url": line})
            meta, extras = None, []
    return entries


def matches(entry, rule):
    if not any(re.search(p, entry["name"], re.IGNORECASE) for p in rule["patterns"]):
        return False
    countries = rule.get("countries")
    if countries:
        # IPTV-org tvg-id convention: Channel.pe or Channel.pe@HD.
        # If id does not exist, avoid attributing country without evidence.
        id_country = re.search(r"\.([a-z]{2})(?:@|$)", entry["tvg_id"], re.I)
        if not id_country or id_country.group(1).lower() not in countries:
            return False
    # Remove countries explicitly excluded by the playlist owner.
    # IPTV-org generally identifies channels as Name.br or Name.nl in tvg-id.
    excluded_countries = set(rule.get("exclude_countries", []))
    id_country = re.search(r"\\.([a-z]{2})(?:@|$)", entry["tvg_id"], re.I)
    if id_country and id_country.group(1).lower() in excluded_countries:
        return False
    # Also catch regional labels such as ESPN Brasil or ESPN NL.
    if any(re.search(p, entry["name"], re.IGNORECASE)
           for p in rule.get("exclude_patterns", [])):
        return False
    return True


def build(content):
    entries = parse_playlist(content)
    result, seen, counts = ["#EXTM3U"], set(), {}
    for rule in CONFIG["favorites"]:
        count = 0
        for entry in entries:
            if not matches(entry, rule):
                continue
            count += 1
            identity = (entry["name"].casefold(), entry["url"])
            if identity in seen:
                continue
            seen.add(identity)
            group = rule["group"].replace('"', "").replace("\n", " ")
            meta = re.sub(r'\s+group-title="[^"]*"', "", entry["meta"])
            meta = meta.replace(",", f' group-title="{group}",', 1)
            result.extend([meta, *entry["extras"], entry["url"]])
        counts[rule["label"]] = count
    return "\n".join(result) + "\n", counts


def main():
    playlist, counts = build(fetch_playlist(CONFIG["source_url"]))
    public = ROOT / "public"
    public.mkdir(exist_ok=True)
    (public / "playlist.m3u").write_text(playlist, encoding="utf-8")
    (public / "status.json").write_text(json.dumps({"matches": counts, "total": len(parse_playlist(playlist))}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Canales seleccionados:", counts)
    if not any(counts.values()):
        print("AVISO: no se encontraron coincidencias; se publica una playlist vacía (sin enlaces inventados).")


if __name__ == "__main__":
    main()
