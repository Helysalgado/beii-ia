#!/usr/bin/env python3
"""Agent-like orchestrator for a mini RNA-seq pipeline (stubs).

This agent is an ORCHESTRATOR, not an autonomous scientist.
It executes a human-designed plan:
- validate manifest
- QC per sample (stub)
- align per sample (stub)
- count matrix (stub)
- differential expression (stub)

Usage:
  python bin/agent_run_rnaseq.py --config config/config.yaml
  python bin/agent_run_rnaseq.py --config config/config.yaml --dry-run
"""
from __future__ import annotations

import argparse
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

@dataclass
class Config:
    manifest: Path
    results_dir: Path
    log_file: Path
    threads: int
    steps: dict

def read_simple_yaml(path: Path) -> dict:
    """Minimal YAML reader for key: value pairs and a single-level 'steps:' block."""
    data = {}
    steps = {}
    in_steps = False
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.strip() == "steps:":
            in_steps = True
            continue
        if in_steps and line.startswith("  "):
            k, v = line.strip().split(":", 1)
            steps[k.strip()] = v.strip().lower() == "true"
        else:
            in_steps = False
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip().strip('"').strip("'")
    if steps:
        data["steps"] = steps
    return data

def log(msg: str, log_path: Path) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(f"[{ts}] {msg}\n")

def run(cmd: list[str], log_path: Path, dry_run: bool) -> None:
    log(f"CMD: {' '.join(cmd)}", log_path)
    if dry_run:
        return
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.stdout:
        log(f"STDOUT: {p.stdout.strip()}", log_path)
    if p.stderr:
        log(f"STDERR: {p.stderr.strip()}", log_path)
    if p.returncode != 0:
        raise SystemExit(f"Command failed ({p.returncode}): {' '.join(cmd)}")

def parse_manifest(manifest: Path):
    lines = [ln.rstrip("\n") for ln in manifest.read_text(encoding="utf-8").splitlines() if ln.strip()]
    header = lines[0].split("\t")
    idx = {c: header.index(c) for c in header}
    for ln in lines[1:]:
        r = ln.split("\t")
        yield {
            "sample_id": r[idx["sample_id"]],
            "condition": r[idx["condition"]],
            "reads_1": r[idx["reads_1"]],
            "reads_2": r[idx["reads_2"]],
        }

def main() -> int:
    p = argparse.ArgumentParser(description="Run mini RNA-seq pipeline (stubs)")
    p.add_argument("--config", required=True)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    cfg_raw = read_simple_yaml(Path(args.config))
    cfg = Config(
        manifest=Path(cfg_raw["manifest"]),
        results_dir=Path(cfg_raw["results_dir"]),
        log_file=Path(cfg_raw["log_file"]),
        threads=int(cfg_raw.get("threads", "1")),
        steps=cfg_raw.get("steps", {"qc": True, "align": True, "count": True, "diffexpr": True}),
    )

    cfg.results_dir.mkdir(parents=True, exist_ok=True)
    log("Agent started", cfg.log_file)

    # 0) validate manifest
    run(["python", "bin/validate_manifest.py", "--manifest", str(cfg.manifest)], cfg.log_file, args.dry_run)

    samples = list(parse_manifest(cfg.manifest))

    # 1) QC
    if cfg.steps.get("qc", True):
        for s in samples:
            out = cfg.results_dir / "qc" / f"{s['sample_id']}.qc.txt"
            run(["python", "bin/step_fastqc_stub.py",
                 "--sample", s["sample_id"], "--r1", s["reads_1"], "--r2", s["reads_2"],
                 "--out", str(out)], cfg.log_file, args.dry_run)

    # 2) Align
    if cfg.steps.get("align", True):
        for s in samples:
            out = cfg.results_dir / "align" / f"{s['sample_id']}.bam.txt"
            run(["python", "bin/step_align_stub.py",
                 "--sample", s["sample_id"], "--out", str(out)], cfg.log_file, args.dry_run)

    # 3) Count
    counts = cfg.results_dir / "counts" / "counts.tsv"
    if cfg.steps.get("count", True):
        run(["python", "bin/step_count_stub.py", "--manifest", str(cfg.manifest), "--out", str(counts)],
            cfg.log_file, args.dry_run)

    # 4) Diffexpr
    if cfg.steps.get("diffexpr", True):
        out = cfg.results_dir / "diffexpr" / "deseq2_like_results.tsv"
        run(["python", "bin/step_diffexpr_stub.py", "--manifest", str(cfg.manifest),
             "--counts", str(counts), "--out", str(out)], cfg.log_file, args.dry_run)

    log("Agent finished successfully", cfg.log_file)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
