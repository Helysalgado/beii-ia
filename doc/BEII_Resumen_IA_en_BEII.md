# 🧠 Resumen general — Integración de IA en BEII

**Materia:** Bioinformática y Estadística II (BEII)  
**Licenciatura:** Ciencias Genómicas  

Este documento resume el diseño e implementación del **módulo de Inteligencia Artificial en BEII**, con el objetivo de permitir la **continuidad del trabajo en otros contextos o conversaciones** sin pérdida de información.

---

## 🎯 Objetivo global

Integrar IA de forma **crítica, ética y científicamente responsable** dentro de BEII, **sin sustituir** el razonamiento científico ni adelantar formalmente el curso de *Algoritmos de Aprendizaje Supervisado*, pero preparando conceptualmente al estudiante.

> **Principio rector:**  
> La IA es una herramienta de apoyo técnico; el criterio científico sigue siendo humano.

---

## 🧩 Arquitectura del módulo de IA en BEII

El módulo se organiza en **tres sesiones progresivas**, coherentes con los contenidos del curso.

---

## 🧠 Sesión 1 — IA generativa y prompting científico

### Objetivo
Desarrollar **criterio científico** para el uso de IA generativa.

### Contenidos
- Qué es y qué no es la IA generativa
- Tokens, prompts y alucinaciones
- Verificación y reproducibilidad
- El prompt como **protocolo científico escrito**

### Actividades clave
- Anti‑ejemplos de prompts mal definidos
- Anatomía de un buen prompt:
  - Rol
  - Contexto
  - Tarea
  - Restricciones
  - Salida esperada
  - Verificación
- Ejemplos: buen prompt / mala pregunta científica
  - Correlación vs causalidad
  - GWAS ≠ causalidad
- Mini‑debates en clase
- Puente conceptual hacia predicción vs causalidad (ML)

**Resultado:** el estudiante aprende a **validar, cuestionar y verificar** resultados generados por IA.

---

## 💻 Sesión 2 — IA para desarrollo de software científico

### Objetivo
Usar IA para **programar con buenas prácticas**, no para copiar código.

### Contenidos
- Qué define buen software científico
- Fases del desarrollo asistidas por IA
- Riesgos del uso acrítico de IA al programar

### Herramientas desarrolladas

#### 🤖 PyLIA‑BEII v5 (CLI)
Asistente para:
- análisis
- diseño
- implementación
- validación
- empaquetado

Incluye:
- flujo por fases
- confirmaciones
- pruebas unitarias
- diagramas
- artefactos por fase

#### 🧠 BEII Software Coach (no‑CLI)
Asistente **conceptual** para:
- diseño
- supuestos
- riesgos
- validación

No escribe código.

### Evaluación
- Rúbrica específica para uso de:
  - IA
  - Cursor
  - PyLIA / Software Coach
- Ejemplos de entregas bien y mal evaluadas

**Resultado:** formación en **ingeniería científica reproducible**.

---

## 🤖 Sesión 3 — Agentes, automatización y pipelines científicos

### Objetivo
Escalar análisis computacionales **sin delegar el razonamiento científico**.

### Principios BEII
- Automatizar ≠ pensar
- El agente **orquesta**, no interpreta
- Todo pipeline debe ser:
  - modular
  - auditable
  - reproducible

### Ejemplos
1. Automatización segura (GC content)
2. Ejemplo peligroso (delegación acrítica)
3. Pipeline correcto de expresión diferencial

---

## 🧬 Prácticas implementadas

### 1️⃣ Mini RNA‑seq pipeline — STUBS (didáctico)
- Corre en cualquier computadora
- Simula QC, alineamiento, conteo y diferencial
- Incluye agente/orquestador, logs y sanity checks

📦 **BEII_Sesion3_Mini_RNAseq_Pipeline_STUBS.zip**

---

### 2️⃣ Mini RNA‑seq pipeline — REAL HOOKS + fallback
- Mismo agente/orquestador
- Usa herramientas reales si están disponibles:
  - FastQC
  - STAR
  - featureCounts
  - DESeq2
- Fallback automático a stubs
- Preparado para HPC

📦 **BEII_Sesion3_RNAseq_Pipeline_REAL_HOOKS.zip**

---

## 📜 Política BEII de uso ético de IA

Documento formal que establece:
- usos permitidos y no permitidos
- obligación de documentar uso de IA
- validación humana obligatoria

📄 **BEII_Politica_Uso_Etico_IA.md**

---

## 🧠 Mensaje transversal del módulo

> La IA acelera, organiza y asiste.  
> El científico diseña, valida e interpreta.

---

## 🔜 Estado actual

El curso cuenta con:
- sesiones completas (1–3)
- materiales descargables
- prácticas funcionales
- asistentes propios
- rúbricas y política ética

Este documento sirve como **punto de reinicio** para continuar el desarrollo del módulo en otro momento o conversación.
