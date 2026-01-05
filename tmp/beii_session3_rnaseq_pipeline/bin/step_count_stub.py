#!/usr/bin/env python3
"""Counting stub: creates a toy count matrix.

Usage:
  python bin/step_count_stub.py --manifest data/manifest.tsv --out results/counts/counts.tsv
"""
from __future__ import annotations

import argparse
from pathlib import Path
import random

def read_manifest(path: Path):
    lines = [ln.rstrip("\n") for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]
    header = lines[0].split("\t")
    idx = {c: header.index(c) for c in header}
    for ln in lines[1:]:
        r = ln.split("\t")
        yield r[idx["sample_id"]], r[idx["condition"]]

def main() -> int:
    p = argparse.ArgumentParser(description="Counting stub")
    p.add_argument("--manifest", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()

    mpath = Path(args.manifest)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    samples = [sid for sid, _ in read_manifest(mpath)]
    genes = [f"gene_{i:03d}" for i in range(1, 21)]  # 20 toy genes

    rnd = random.Random(7)  # deterministic toy counts
    with out.open("w", encoding="utf-8") as w:
        w.write("gene_id\t" + "\t".join(samples) + "\n")
        for g in genes:
            counts = [str(rnd.randint(10, 500)) for _ in samples]
            w.write(g + "\t" + "\t".join(counts) + "\n")

    print(f"OK\tcounts\tgenes={len(genes)}\tsamples={len(samples)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
