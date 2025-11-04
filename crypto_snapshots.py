import os, requests, pandas as pd
from datetime import datetime, timezone
from pathlib import Path

URL = "https://cryptobubbles.net/backend/data/bubbles1000.usd.json"
OUT_DIR = r"G:\Coding\data_analysis_project\Undone\Live Encryto Dashboard\snapshot"
Path(OUT_DIR).mkdir(parents=True, exist_ok=True)

def fetch_json():
    r = requests.get(URL, timeout=30)
    r.raise_for_status()
    return r.json()

def to_rows(data) -> pd.DataFrame:
    """
    Accepts either:
      - dict: { "BTC": {...}, "ETH": {...}, ... }
      - list: [ {...}, {...}, ... ]
    Returns tidy rows: Symbol, PriceUSD, VolumeUSD, ChangePct, SnapshotUTC
    """
    ts = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    rows = []

    def extract_row(sym_hint, obj):
        # tolerate different field names
        sym = (sym_hint
               or obj.get("s") or obj.get("symbol") or obj.get("code")
               or obj.get("ticker") or obj.get("name"))
        price = obj.get("p") or obj.get("price") or obj.get("priceUSD") or obj.get("price_usd")
        vol   = obj.get("v") or obj.get("volume") or obj.get("VolumeUSD") or obj.get("volume_usd")
        chg   = obj.get("pc") or obj.get("change") or obj.get("change24h")

        # handle nested performance.day if present
        perf = obj.get("performance") or {}
        if chg is None:
            chg = perf.get("day")

        return {
            "Symbol": sym,
            "PriceUSD": price,
            "VolumeUSD": vol,
            "ChangePct": chg,
            "SnapshotUTC": ts
        }

    if isinstance(data, dict):
        for sym, obj in data.items():
            rows.append(extract_row(sym, obj))
    elif isinstance(data, list):
        for obj in data:
            rows.append(extract_row(None, obj))
    else:
        raise TypeError(f"Unexpected payload type: {type(data)}")

    df = pd.DataFrame(rows, columns=["Symbol","PriceUSD","VolumeUSD","ChangePct","SnapshotUTC"])
    # coerce numerics
    for c in ["PriceUSD","VolumeUSD","ChangePct"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df

def save_snapshot(df: pd.DataFrame):
    fname = f"snapshot_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(os.path.join(OUT_DIR, fname), index=False)

if __name__ == "__main__":
    data = fetch_json()
    df = to_rows(data)
    # Sanity check: should be ~1000 rows x 5 columns
    print("shape:", df.shape)           # e.g., (1000, 5)
    print(df.head().to_string())
    save_snapshot(df)
