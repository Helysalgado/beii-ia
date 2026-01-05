# 🤖 BEII — Sesión 3
## Agentes, automatización y pipelines científicos

> **Rol del profesor:** Experto en bioinformática, software científico y reproducibilidad  
> **Relación con sesiones previas:**
> - Sesión 1: Prompting científico y pensamiento crítico
> - Sesión 2: IA para desarrollo de software reproducible
>
> **Sesión 3:** Uso responsable de **agentes y automatización** para escalar análisis bioinformáticos sin perder control científico.

---

## 📍 Contexto de la sesión dentro de BEII

Hasta ahora, el estudiante ha aprendido a:
- formular buenas preguntas científicas (Sesión 1),
- diseñar e implementar software reproducible con apoyo de IA (Sesión 2).

En esta sesión damos un paso más:

> **¿Cómo escalar análisis y flujos de trabajo sin delegar el razonamiento científico a la IA?**

Aquí introducimos el concepto de **agentes** y **automatización**, entendidos no como “IA que trabaja sola”, sino como **orquestadores de tareas bien definidas**.

---

## 🎯 Objetivos de aprendizaje

Al finalizar la sesión, el estudiante será capaz de:

- Explicar qué es un **agente** en el contexto de IA y software.
- Distinguir entre automatización segura y delegación acrítica.
- Diseñar pipelines bioinformáticos **modulares y auditables**.
- Usar agentes para tareas repetitivas **sin perder control científico**.
- Identificar riesgos de usar agentes en análisis científicos.

---

## 🧠 Conceptos clave de la sesión

### 🤖 ¿Qué es un agente?

Un **agente** es un sistema que:
- recibe un objetivo,
- ejecuta una secuencia de tareas,
- puede usar herramientas (scripts, archivos, APIs),
- y toma decisiones **dentro de límites definidos**.

> En BEII, un agente **no decide ciencia**: ejecuta tareas técnicas.

---

### 🔄 Automatización vs razonamiento

- **Automatización**: ejecutar pasos repetitivos y bien definidos.
- **Razonamiento científico**: formular hipótesis, interpretar resultados, decidir validez.

⚠️ Error común:
> “El agente ya hizo el análisis.”

Corrección:
> “El agente ejecutó el pipeline que yo diseñé.”

---

### 🧪 Pipeline científico

Un **pipeline** es una secuencia reproducible de pasos computacionales:

```
entrada → validación → procesamiento → análisis → salida → validación
```

Características deseables:
- modular,
- reproducible,
- auditable,
- versionado.

---

## 🚨 Principios BEII para uso de agentes

1. El humano diseña el pipeline.
2. El agente **no formula preguntas científicas**.
3. Cada paso debe poder ejecutarse manualmente.
4. Todo resultado debe ser verificable sin el agente.
5. El agente **no interpreta resultados**.

---

## 1️⃣ Ejemplo introductorio — Automatización bien usada

### Ejemplo 1 — Cálculo masivo de GC content (automatización segura)

**Escenario científico**  
Se desea comparar el contenido GC promedio entre genomas bacterianos de distintos grupos taxonómicos.

**Pregunta científica (humana)**  
¿Existen diferencias globales en el GC content entre estos grupos bacterianos?

**Tarea computacional**  
Calcular el GC content de cada genoma completo y generar una tabla resumen.

**Diseño humano (antes del agente)**
- Script validado para calcular GC content.
- Lista de archivos FASTA.
- Definición clara de salida (tabla TSV).
- Sanity checks: secuencias vacías, caracteres inválidos.

**Rol del agente**
- Iterar sobre múltiples FASTA.
- Ejecutar el script validado.
- Guardar salidas con nombres consistentes.

**Qué NO hace el agente**
- No interpreta diferencias.
- No decide relevancia biológica.

📌 *El agente escala el cómputo, no el razonamiento.*

---



## 2️⃣ Ejemplo peligroso — Delegación acrítica ❌

### Ejemplo 2 — “Que el agente analice y concluya” (mala práctica)

**Solicitud al agente**
> “Analiza estos datos de RNA-seq y dime qué genes regulan la condición.”

**Problemas científicos**
- Confunde asociación con causalidad.
- No define qué significa “regular”.
- No especifica evidencia aceptable.

**Problemas computacionales**
- No hay pipeline explícito.
- No hay criterios de validación.
- No es reproducible.

**Riesgo real**
- Aceptar conclusiones falsas bien redactadas.

📌 *Un agente no formula hipótesis ni conclusiones científicas.*

---



## 3️⃣ Diseño correcto de un pipeline con agentes

### Ejemplo 3 — Pipeline automatizado de expresión diferencial (uso correcto)

**Escenario científico**  
Comparar expresión génica entre dos condiciones experimentales.

**Pregunta científica (humana)**  
¿Qué genes muestran cambios significativos de expresión entre condición A y B?

**Diseño conceptual humano**
1. Control de calidad de lecturas.
2. Mapeo contra genoma de referencia.
3. Conteo de lecturas por gen.
4. Análisis estadístico diferencial.
5. Validación y visualización.

**Qué se automatiza con agentes**
- Ejecución secuencial de herramientas.
- Manejo de múltiples muestras.
- Organización de resultados.

**Qué NO se automatiza**
- Elección de parámetros críticos.
- Interpretación de genes diferenciales.
- Decisiones biológicas.

📌 *El agente ejecuta el pipeline diseñado por el humano.*

---



## 4️⃣ Actividad guiada en clase (implementación completa)

A continuación se incluye una práctica **totalmente implementable** (con scripts y un “agente” sencillo) para que el estudiante vea cómo se automatiza un pipeline **sin delegar el razonamiento científico**.

> **Importante:** aquí llamamos “agente” a un **orquestador**: un programa que ejecuta pasos definidos por el humano, registra evidencias y falla de forma segura.

---

### 🧪 Práctica: Mini‑pipeline automatizado para GC content por lote

#### Objetivo didáctico
- Diseñar un pipeline modular.
- Automatizar ejecuciones repetitivas con un agente **auditable**.
- Practicar trazabilidad (logs) y validación mínima.

#### Entradas
- Carpeta con archivos `*.fasta` o `*.fa`.

#### Salidas
- `results/gc_summary.tsv`
- logs por ejecución en `logs/`

---

## 🗂️ Estructura del proyecto (reproducible)

```text
beii_session3_gc_pipeline/
├── bin/
│   ├── calculate_gc.py
│   ├── validate_fasta.py
│   └── agent_run_gc_batch.py
├── config/
│   └── config.yaml
├── data/
│   └── fasta/                 # colocar aquí *.fasta
├── results/
│   └── gc_summary.tsv         # se genera
├── logs/
│   └── agent.log              # se genera
├── docs/
│   ├── analysis.md            # pregunta, supuestos, validación
│   └── ai_usage.md            # transparencia de IA
└── README.md
```

---

## 4.1 — Paso A: Documento conceptual (humano, antes del código)

En `docs/analysis.md` el estudiante debe escribir:

- **Pregunta científica:** ¿Cómo varía el GC content entre los genomas de este conjunto?
- **Tarea computacional:** calcular GC por FASTA y resumir.
- **Supuestos:** archivos FASTA válidos, secuencias no vacías.
- **Validación:** sanity checks y casos límite.

> Esto puede apoyarse con **BEII Software Coach**, pero debe quedar escrito por el estudiante.

---

## 4.2 — Paso B: Script 1 — cálculo GC (módulo computacional)

`bin/calculate_gc.py`

```python
#!/usr/bin/env python3
"""Calculate GC content for sequences in a FASTA file.

Outputs a TSV with columns: file, record_id, length, gc_fraction

Usage:
  python bin/calculate_gc.py --fasta data/fasta/sample.fasta --out results/sample.gc.tsv
"""

from __future__ import annotations

import argparse
from pathlib import Path


def gc_fraction(seq: str) -> float:
    """Return GC fraction in [0,1] for a DNA sequence.

    Notes:
    - Converts to uppercase.
    - Ignores non-ACGT characters by raising a ValueError.
    """
    s = seq.strip().upper()
    if not s:
        raise ValueError("Empty sequence")
    allowed = set("ACGT")
    bad = set(s) - allowed
    if bad:
        raise ValueError(f"Invalid characters found: {sorted(bad)}")
    gc = s.count("G") + s.count("C")
    return gc / len(s)


def parse_fasta(path: Path):
    """Minimal FASTA parser yielding (record_id, sequence)."""
    record_id = None
    chunks = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("
")
            if not line:
                continue
            if line.startswith(">"):
                if record_id is not None:
                    yield record_id, "".join(chunks)
                record_id = line[1:].split()[0]
                chunks = []
            else:
                chunks.append(line.strip())
        if record_id is not None:
            yield record_id, "".join(chunks)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compute GC content for FASTA records")
    parser.add_argument("--fasta", required=True, help="Input FASTA file")
    parser.add_argument("--out", required=True, help="Output TSV file")
    args = parser.parse_args()

    fasta = Path(args.fasta)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    with out.open("w", encoding="utf-8") as w:
        w.write("file	record_id	length	gc_fraction
")
        for rid, seq in parse_fasta(fasta):
            frac = gc_fraction(seq)
            w.write(f"{fasta.name}	{rid}	{len(seq)}	{frac:.6f}
")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## 4.3 — Paso C: Script 2 — validación de FASTA (guardrail)

`bin/validate_fasta.py`

```python
#!/usr/bin/env python3
"""Validate FASTA files for basic scientific computing safety.

Checks:
- file exists and is readable
- at least one record
- sequences contain only A/C/G/T (case-insensitive)

Usage:
  python bin/validate_fasta.py --fasta data/fasta/sample.fasta
"""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_fasta(path: Path):
    record_id = None
    chunks = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("
")
            if not line:
                continue
            if line.startswith(">"):
                if record_id is not None:
                    yield record_id, "".join(chunks)
                record_id = line[1:].split()[0]
                chunks = []
            else:
                chunks.append(line.strip())
        if record_id is not None:
            yield record_id, "".join(chunks)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a FASTA file")
    parser.add_argument("--fasta", required=True)
    args = parser.parse_args()

    fasta = Path(args.fasta)
    if not fasta.exists():
        raise SystemExit(f"ERROR: file not found: {fasta}")

    allowed = set("ACGT")
    n_records = 0
    for rid, seq in parse_fasta(fasta):
        n_records += 1
        s = seq.strip().upper()
        if not s:
            raise SystemExit(f"ERROR: empty sequence in record {rid}")
        bad = set(s) - allowed
        if bad:
            raise SystemExit(f"ERROR: invalid characters in {rid}: {sorted(bad)}")

    if n_records == 0:
        raise SystemExit("ERROR: no FASTA records found")

    print(f"OK	{fasta.name}	records={n_records}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## 4.4 — Paso D: Configuración del lote

`config/config.yaml`

```yaml
input_dir: data/fasta
output_dir: results
log_file: logs/agent.log
pattern: "*.fasta"
```

---

## 4.5 — Paso E: El “agente” (orquestador auditable)

`bin/agent_run_gc_batch.py`

```python
#!/usr/bin/env python3
"""Agent-like orchestrator to run a validated GC pipeline over many FASTA files.

This is NOT an autonomous scientist.
It executes a human-designed plan:
- validate inputs
- run GC computation
- aggregate results
- log everything

Usage:
  python bin/agent_run_gc_batch.py --config config/config.yaml

Optional:
  --dry-run   : show planned commands without executing
"""

from __future__ import annotations

import argparse
import glob
import subprocess
from dataclasses import dataclass
from pathlib import Path
from datetime import datetime


@dataclass
class Config:
    input_dir: Path
    output_dir: Path
    log_file: Path
    pattern: str


def read_simple_yaml(path: Path) -> dict:
    """Minimal YAML reader for key: value pairs (no nesting)."""
    data = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def log(msg: str, log_path: Path) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(f"[{ts}] {msg}
")


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


def main() -> int:
    parser = argparse.ArgumentParser(description="Run GC pipeline over many FASTA files")
    parser.add_argument("--config", required=True, help="Path to config YAML")
    parser.add_argument("--dry-run", action="store_true", help="Do not execute, only log")
    args = parser.parse_args()

    cfg_raw = read_simple_yaml(Path(args.config))
    cfg = Config(
        input_dir=Path(cfg_raw["input_dir"]),
        output_dir=Path(cfg_raw["output_dir"]),
        log_file=Path(cfg_raw["log_file"]),
        pattern=cfg_raw.get("pattern", "*.fasta"),
    )

    cfg.output_dir.mkdir(parents=True, exist_ok=True)
    log("Agent started", cfg.log_file)

    fasta_files = sorted(glob.glob(str(cfg.input_dir / cfg.pattern)))
    if not fasta_files:
        raise SystemExit(f"No FASTA files found in {cfg.input_dir} with pattern {cfg.pattern}")

    per_file_outputs = []
    for fasta in fasta_files:
        fasta_path = Path(fasta)

        # 1) validate
        run(["python", "bin/validate_fasta.py", "--fasta", str(fasta_path)], cfg.log_file, args.dry_run)

        # 2) compute
        out_tsv = cfg.output_dir / f"{fasta_path.stem}.gc.tsv"
        run([
            "python", "bin/calculate_gc.py",
            "--fasta", str(fasta_path),
            "--out", str(out_tsv),
        ], cfg.log_file, args.dry_run)

        per_file_outputs.append(out_tsv)

    # 3) aggregate
    summary = cfg.output_dir / "gc_summary.tsv"
    log(f"Aggregating -> {summary}", cfg.log_file)
    if not args.dry_run:
        with summary.open("w", encoding="utf-8") as w:
            w.write("file	record_id	length	gc_fraction
")
            for tsv in per_file_outputs:
                lines = tsv.read_text(encoding="utf-8").splitlines()
                for line in lines[1:]:  # skip header
                    w.write(line + "
")

    log("Agent finished successfully", cfg.log_file)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## 4.6 — Ejecución (cómo correrlo)

1) Coloca FASTA en `data/fasta/`

2) Dry‑run (ver plan sin ejecutar):

```bash
python bin/agent_run_gc_batch.py --config config/config.yaml --dry-run
```

3) Ejecutar:

```bash
python bin/agent_run_gc_batch.py --config config/config.yaml
```

4) Revisa:
- `results/gc_summary.tsv`
- `logs/agent.log`

---

## 4.7 — Validación mínima (sanity checks)

El estudiante debe demostrar al menos:

- Caso simple: FASTA con una secuencia pequeña cuyo GC puede calcular a mano.
- Caso error: FASTA con carácter inválido → debe fallar con mensaje claro.

---

## 4.8 — Prompts sugeridos (alineados a BEII)

### Para BEII Software Coach (diseño)
```text
Tengo esta idea de análisis: [idea].
Ayúdame a convertirla en:
- pregunta científica evaluable
- tarea computacional
- supuestos
- criterios de validación
No escribas código.
```

### Para PyLIA-BEII (implementación incremental)
```text
Implementa solo la función gc_fraction(seq) con validación estricta.
Incluye docstring en inglés y casos límite.
No escribas el script completo.
```

### Para Cursor (debugging)
```text
Explica este script línea por línea y detecta posibles errores lógicos.
No lo modifiques todavía.
```

---

### ✅ Resultado esperado del ejercicio

Al final, el estudiante entrega:
- `docs/analysis.md`
- `docs/ai_usage.md`
- `bin/` con scripts (modulares)
- `results/gc_summary.tsv`
- `logs/agent.log`

> *Aquí el “agente” no hace ciencia: ejecuta un plan científico-computacional diseñado por el humano.*

---

## 🧪 Puente hacia proyectos finales

En proyectos largos:

- agentes pueden:
  - correr pipelines,
  - organizar resultados,
  - generar reportes técnicos.

- humanos deben:
  - validar,
  - interpretar,
  - decidir conclusiones.

---

## ⚠️ Anti-patrones comunes

- “Que el agente diseñe el análisis.”
- “Que el agente interprete los resultados.”
- “Confiar en resultados no auditables.”

---

## 📌 Mensajes clave de la sesión

- *Automatizar no es delegar pensamiento.*
- *Un pipeline bien diseñado es más importante que un agente sofisticado.*
- *La IA escala procesos, no criterio científico.*

---

## 🏁 Cierre

> **Los agentes son herramientas poderosas.
> Su valor depende de la calidad del diseño humano que los gobierna.**

---

# 🧬 Práctica alternativa (implementación completa)
## Mini-pipeline automatizado de RNA-seq (con stubs auditables)

Esta práctica simula un pipeline de RNA-seq **sin depender de herramientas externas** (FastQC, STAR, featureCounts, DESeq2), usando **stubs** (scripts que imitan entradas/salidas y validan el flujo). Es ideal para enseñar:

- orquestación modular,
- trazabilidad (logs),
- control de errores,
- y el principio BEII: *automatización ≠ interpretación científica*.

> **Importante:** el objetivo NO es hacer RNA-seq real en esta sesión, sino aprender a **diseñar y automatizar** un pipeline de forma **auditable**.

---

## 5.1 — Estructura del proyecto

```text
beii_session3_rnaseq_pipeline/
├── bin/
│   ├── validate_manifest.py
│   ├── step_fastqc_stub.py
│   ├── step_align_stub.py
│   ├── step_count_stub.py
│   ├── step_diffexpr_stub.py
│   └── agent_run_rnaseq.py
├── config/
│   └── config.yaml
├── data/
│   ├── reads/                 # FASTQ (reales o de juguete)
│   └── manifest.tsv           # lista de muestras
├── results/
│   ├── qc/
│   ├── align/
│   ├── counts/
│   └── diffexpr/
├── logs/
│   └── agent.log
├── docs/
│   ├── analysis.md
│   └── ai_usage.md
└── README.md
```

---

## 5.2 — Manifiesto de muestras (data/manifest.tsv)

Formato mínimo:

```text
sample_id	condition	reads_1	reads_2
S1	A	data/reads/S1_R1.fastq	data/reads/S1_R2.fastq
S2	A	data/reads/S2_R1.fastq	data/reads/S2_R2.fastq
S3	B	data/reads/S3_R1.fastq	data/reads/S3_R2.fastq
S4	B	data/reads/S4_R1.fastq	data/reads/S4_R2.fastq
```

**Nota:** En esta práctica los FASTQ pueden ser:
- reales,
- o de juguete (pocas líneas),
porque los stubs no ejecutan análisis real.

---

## 5.3 — Configuración (config/config.yaml)

```yaml
manifest: data/manifest.tsv
results_dir: results
log_file: logs/agent.log
threads: 4
steps:
  qc: true
  align: true
  count: true
  diffexpr: true
```

---

## 5.4 — Diseño humano (docs/analysis.md)

El estudiante debe escribir:
- **Pregunta científica:** p.ej. ¿Qué genes cambian su expresión entre A y B?
- **Tarea computacional:** pipeline QC → mapeo → conteo → diferencial.
- **Supuestos:** replicados, diseño experimental, control de batch (si aplica).
- **Validación:** checks de integridad y consistencia (no “verdad biológica”).

---

## 5.5 — Qué hace el agente (orquestador) y qué hacen los stubs

El pipeline se ejecuta en el orden:

1. Validar manifiesto
2. QC stub (genera reporte por muestra)
3. Align stub (genera BAM simulado por muestra)
4. Count stub (genera matriz de conteos)
5. Diffexpr stub (genera tabla de resultados)

**Qué hace el agente:**
- ejecuta pasos definidos,
- registra comandos y salidas,
- falla con errores explícitos.

**Qué NO hace el agente:**
- no decide parámetros biológicos,
- no interpreta genes diferenciales.

---

## 5.6 — Ejecución

Dry-run:

```bash
python bin/agent_run_rnaseq.py --config config/config.yaml --dry-run
```

Ejecución:

```bash
python bin/agent_run_rnaseq.py --config config/config.yaml
```

Revisar:
- `logs/agent.log`
- `results/` (carpetas por etapa)

---

## 5.7 — Validación mínima (sanity checks)

El estudiante debe demostrar al menos:

- El manifiesto tiene todas las columnas requeridas.
- Los paths existen (o en dry-run se detectan).
- El pipeline produce outputs con nombres consistentes.
- Si falta una muestra o condición, el pipeline falla con mensaje claro.

---

## 5.8 — Debate guiado (5–10 min)

Preguntas:
- ¿Qué partes del pipeline pueden automatizarse sin riesgo?
- ¿Qué partes NO deben automatizarse (diseño experimental, interpretación)?
- ¿Qué evidencia faltaría para afirmar causalidad?

---

## 5.9 — Prompts sugeridos (alineados a BEII)

### Software Coach (diseño y supuestos)
```text
Tengo este diseño experimental (A vs B) con RNA-seq.
Ayúdame a:
- explicitar supuestos
- riesgos de inferencia
- validaciones mínimas
No escribas código.
```

### PyLIA-BEII (módulos incrementales)
```text
Escribe un validador de manifest.tsv con columnas obligatorias.
Debe fallar con mensajes claros.
No escribas el pipeline completo.
```

### Cursor (auditoría)
```text
Revisa este orquestador y dime dónde puede fallar silenciosamente.
Propón refactorización mínima.
```

---

> *Este mini RNA-seq pipeline enseña orquestación, trazabilidad y control. La ciencia sigue siendo humana.*

