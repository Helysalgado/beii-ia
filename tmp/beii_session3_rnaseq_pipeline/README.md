# BEII Sesión 3 — Mini RNA-seq pipeline (stubs)

Este proyecto **simula** un pipeline de RNA-seq con stubs para enseñar:
- orquestación por etapas
- trazabilidad (logs)
- control de errores

## Ejecutar

Dry-run:
```bash
python bin/agent_run_rnaseq.py --config config/config.yaml --dry-run
```

Ejecución:
```bash
python bin/agent_run_rnaseq.py --config config/config.yaml
```

## Salidas
- results/qc/*.qc.txt
- results/align/*.bam.txt (simulado)
- results/counts/counts.tsv
- results/diffexpr/deseq2_like_results.tsv
- logs/agent.log

## Nota
Este pipeline no reemplaza herramientas reales; solo enseña automatización responsable.
