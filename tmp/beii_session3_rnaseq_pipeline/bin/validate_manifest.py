#!/usr/bin/env python3
"""Validate a RNA-seq sample manifest TSV.

Required columns:
- sample_id
- condition
- reads_1
- reads_2

Rules:
- sample_id unique
- at least 2 conditions
- each condition has >= 2 samples (for didactic purposes)
- paths exist

Usage:
  python bin/validate_manifest.py --manifest data/manifest.tsv
"""
from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED = ["sample_id", "condition", "reads_1", "reads_2"]

def main() -> int:
    p = argparse.ArgumentParser(description="Validate manifest.tsv")
    p.add_argument("--manifest", required=True)
    args = p.parse_args()

    mpath = Path(args.manifest)
    if not mpath.exists():
        raise SystemExit(f"ERROR: manifest not found: {mpath}")

    lines = [ln.rstrip("\n") for ln in mpath.read_text(encoding="utf-8").splitlines() if ln.strip()]
    header = lines[0].split("\t")
    missing = [c for c in REQUIRED if c not in header]
    if missing:
        raise SystemExit(f"ERROR: missing columns: {missing}")

    idx = {c: header.index(c) for c in REQUIRED}
    rows = [ln.split("\t") for ln in lines[1:]]
    if not rows:
        raise SystemExit("ERROR: manifest has no samples")

    sample_ids = [r[idx["sample_id"]] for r in rows]
    if len(sample_ids) != len(set(sample_ids)):
        raise SystemExit("ERROR: duplicate sample_id found")

    conditions = [r[idx["condition"]] for r in rows]
    uniq_cond = sorted(set(conditions))
    if len(uniq_cond) < 2:
        raise SystemExit("ERROR: need at least 2 conditions for comparison")

    # Didactic rule: >=2 samples per condition
    for c in uniq_cond:
        n = sum(1 for cc in conditions if cc == c)
        if n < 2:
            raise SystemExit(f"ERROR: condition '{c}' has only {n} sample(s); need >=2")

    # Paths exist
    for r in rows:
        for col in ["reads_1", "reads_2"]:
            fp = Path(r[idx[col]])
            if not fp.exists():
                raise SystemExit(f"ERROR: file not found for {r[idx['sample_id']]}: {fp}")

    print(f"OK\tmanifest={mpath}\tsamples={len(rows)}\tconditions={','.join(uniq_cond)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
