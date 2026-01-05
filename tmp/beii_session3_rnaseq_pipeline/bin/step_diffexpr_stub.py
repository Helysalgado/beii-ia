#!/usr/bin/env python3
"""Differential expression stub: generates a toy DE table.

This is NOT DESeq2. It creates an auditable placeholder output.

Usage:
  python bin/step_diffexpr_stub.py --manifest data/manifest.tsv --counts results/counts/counts.tsv --out results/diffexpr/deseq2_like_results.tsv
"""
from __future__ import annotations

import argparse
from pathlib import Path
import math
import random

def read_manifest(path: Path):
    lines = [ln.rstrip("\n") for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]
    header = lines[0].split("\t")
    idx = {c: header.index(c) for c in header}
    rows = []
    for ln in lines[1:]:
        r = ln.split("\t")
        rows.append((r[idx["sample_id"]], r[idx["condition"]]))
    return rows

def main() -> int:
    p = argparse.ArgumentParser(description="Diffexpr stub")
    p.add_argument("--manifest", required=True)
    p.add_argument("--counts", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()

    rows = read_manifest(Path(args.manifest))
    conditions = sorted(set(c for _, c in rows))
    if len(conditions) != 2:
        raise SystemExit("ERROR: this stub expects exactly 2 conditions")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    # toy DE results
    rnd = random.Random(11)
    with out.open("w", encoding="utf-8") as w:
        w.write("gene_id\tlog2FoldChange\tpvalue\tpadj\tnote\n")
        for i in range(1, 21):
            lfc = rnd.uniform(-3, 3)
            pval = max(1e-6, min(1.0, 10 ** (-abs(lfc))))
            padj = min(1.0, pval * 20)  # crude
            w.write(f"gene_{i:03d}\t{lfc:.3f}\t{pval:.6g}\t{padj:.6g}\tSTUB\n")

    print("OK\tdiffexpr\tstub_results=20_genes")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
