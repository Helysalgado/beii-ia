#!/usr/bin/env python3
"""Alignment stub: generates a placeholder 'BAM' text file per sample.

Usage:
  python bin/step_align_stub.py --sample S1 --out results/align/S1.bam.txt
"""
from __future__ import annotations

import argparse
from pathlib import Path

def main() -> int:
    p = argparse.ArgumentParser(description="Alignment stub")
    p.add_argument("--sample", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        f"BAM_STUB\t{args.sample}\nSTATUS\tOK\nNOTE\tThis is not a real BAM file.\n",
        encoding="utf-8",
    )
    print(f"OK\talign\t{args.sample}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
