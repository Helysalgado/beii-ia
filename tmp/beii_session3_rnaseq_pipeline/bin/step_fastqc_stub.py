#!/usr/bin/env python3
"""FASTQC stub: generates a minimal QC report per sample.

This does NOT run FastQC. It creates an auditable placeholder output.

Usage:
  python bin/step_fastqc_stub.py --sample S1 --r1 data/reads/S1_R1.fastq --r2 data/reads/S1_R2.fastq --out results/qc/S1.qc.txt
"""
from __future__ import annotations

import argparse
from pathlib import Path

def count_reads(fastq: Path) -> int:
    lines = fastq.read_text(encoding="utf-8").splitlines()
    if len(lines) % 4 != 0:
        raise SystemExit(f"ERROR: FASTQ format issue (lines not multiple of 4): {fastq}")
    return len(lines) // 4

def main() -> int:
    p = argparse.ArgumentParser(description="FASTQC stub")
    p.add_argument("--sample", required=True)
    p.add_argument("--r1", required=True)
    p.add_argument("--r2", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()

    r1 = Path(args.r1); r2 = Path(args.r2); out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    n1 = count_reads(r1)
    n2 = count_reads(r2)
    if n1 != n2:
        raise SystemExit(f"ERROR: paired reads mismatch for {args.sample}: R1={n1} R2={n2}")

    # placeholder metrics
    out.write_text(
        f"SAMPLE\t{args.sample}\nREADS\t{n1}\nSTATUS\tPASS\nNOTE\tThis is a stub QC report\n",
        encoding="utf-8",
    )
    print(f"OK\tqc\t{args.sample}\treads={n1}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
