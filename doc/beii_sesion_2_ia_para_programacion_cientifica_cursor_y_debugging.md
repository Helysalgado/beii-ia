# 🧠 BEII — Sesión 2
## IA para programación científica: Cursor, debugging y refactorización

> **Rol del profesor:** Experto en bioinformática, programación científica y buenas prácticas de software
>
> **Relación con Sesión 1:** Esta sesión parte del principio establecido previamente: *la IA asiste, no sustituye*. Aquí se aplica ese principio al **desarrollo de código bioinformático**.

---

## 📍 Contexto de la sesión dentro de BEII

### 🧩 Ecosistema de asistentes BEII (visión general)

En BEII, el uso de IA **no se basa en una sola herramienta**, sino en un **ecosistema de asistentes con roles bien delimitados**, alineados con el ciclo real de desarrollo científico-computacional.

Este ecosistema está compuesto por:

- **BEII Software Coach** → *pensamiento científico y diseño conceptual*  
  Ayuda a formular preguntas científicas, identificar supuestos, diseñar estrategias de análisis y definir criterios de validación **antes de escribir código**.

- **PyLIA-BEII** → *implementación técnica reproducible (CLI)*  
  Asiste en la escritura de software científico en Python, con foco en modularidad, pruebas, documentación y reproducibilidad.

- **Cursor** → *debugging y refactorización asistida*  
  Facilita la comprensión de código existente, detección de errores lógicos y refactorizaciones mínimas y justificadas.

> **Regla del curso:** ningún proyecto BEII debe empezar escribiendo código.  
> Primero se razona (Software Coach), luego se implementa (PyLIA), y finalmente se depura (Cursor).

---

## 🧩 ¿Qué es buen software científico?


### 🧩 ¿Qué es buen software científico?

En bioinformática, **buen software** no se define solo por que "corra", sino por que:

- produce **resultados correctos y verificables**,
- implementa correctamente un **algoritmo o razonamiento biológico**,
- es **reproducible** (mismos datos → mismos resultados),
- es **legible y mantenible** por otras personas (y por ti en el futuro),
- y puede **validarse** mediante pruebas y controles.

Un script que corre pero produce resultados incorrectos es **científicamente peligroso**.

---

### ⚠️ Uso de IA al programar: riesgos reales

La IA generativa puede acelerar el desarrollo, pero también puede:

- introducir **errores lógicos sutiles**,
- producir código plausible pero incorrecto,
- ocultar errores bajo explicaciones convincentes,
- llevar a aceptar soluciones sin entender el algoritmo.

Por ello, en BEII la IA se usa **como apoyo técnico**, no como autor del código.

---

### 🔄 Fases del desarrollo cubiertas en esta sesión

Esta sesión aborda explícitamente el uso de IA en las siguientes fases del desarrollo de software científico:

- **Comprensión del código** (explicación línea por línea)
- **Debugging** (detección de errores lógicos y de supuestos)
- **Refactorización mínima** (mejorar sin cambiar el comportamiento)
- **Documentación** (explicar qué hace y qué no hace el código)

### ❗ Fases que siguen siendo responsabilidad humana

Incluso usando IA, el científico debe encargarse de:

- definir correctamente el **problema biológico**,
- elegir el **algoritmo adecuado**,
- diseñar **controles y pruebas**,
- validar resultados con datos reales,
- interpretar los resultados biológicamente.

---

### 🧪 ¿Cómo asegurarnos de que el código es correcto?

Buenas prácticas mínimas que **no pueden delegarse** a la IA:

- ejecutar el código con **casos simples conocidos** (sanity checks),
- probar **casos límite**,
- comparar contra **resultados esperados** o calculables a mano,
- documentar supuestos y limitaciones,
- revisar cambios línea por línea.

> *La IA puede ayudarte a escribir código más rápido.  
> Verificar que sea correcto sigue siendo tu responsabilidad.*

---

## 🎯 Objetivos de aprendizaje

Al finalizar la sesión, el estudiante será capaz de:

- Usar IA para **entender, depurar y refactorizar código**, no solo para generarlo.
- Identificar **errores comunes inducidos por IA** en programación científica.
- Aplicar buenas prácticas de **debugging reproducible**.
- Mantener **autoría intelectual** sobre su código.

Mensaje clave:
> **La IA puede escribir código por ti, pero solo tú puedes garantizar que sea correcto.**

---

## 1️⃣ Marco conceptual: IA y programación científica

### ✔ Qué sí puede hacer la IA

- Explicar código línea por línea
- Detectar errores sintácticos
- Sugerir refactorizaciones
- Proponer estructuras de scripts

### ❌ Qué no puede hacer de forma confiable

- Garantizar corrección biológica
- Asegurar validez estadística
- Reemplazar pruebas y validación

Frase para clase:
> *Código que corre no es lo mismo que código correcto.*

---

## 2️⃣ Herramienta central: Cursor

**Cursor** es un IDE con integración profunda de modelos de lenguaje para:

- autocompletar código,
- explicar fragmentos,
- sugerir correcciones,
- mantener contexto del proyecto.

En BEII, Cursor se usa como:
- asistente de debugging,
- copiloto de refactorización,
- apoyo para documentación.

---

## 3️⃣ Anti-ejemplo — Uso incorrecto de IA para programar ❌

### Ejemplo peligroso A — Script completo generado por IA

**Situación:**

> *"Pídele a la IA que te escriba el script completo y entrégalo"*

**Por qué es peligroso:**

- El estudiante **no entiende el algoritmo** implementado.
- No puede explicar decisiones de diseño.
- No detecta errores lógicos o biológicos.
- El código puede fallar silenciosamente.

**Consecuencia científica:**

> *Aceptar resultados sin entender el método equivale a copiar resultados sin verificar.*

---

### Ejemplo peligroso B — Refactorización no solicitada

**Situación:**

> *Aceptar una refactorización extensa sugerida por IA sin entenderla.*

**Por qué es peligroso:**

- Cambia comportamiento del código sin notarlo.
- Introduce nuevas dependencias.
- Dificulta reproducibilidad.

**Mensaje clave:**

> *Una refactorización solo es buena si entiendes exactamente qué cambia y por qué.*

---

## 4️⃣ Ejemplo guiado — IA como apoyo al debugging

### Código con error

```python
# extract_gc.py
from Bio import SeqIO

for record in SeqIO.parse('genome.fasta', 'fasta'):
    gc = (record.seq.count('G') + record.seq.count('C')) / len(record)
    print(record.id, gc)
```

**Problema:** el GC reportado es incorrecto para algunas secuencias.

### Prompt correcto en Cursor

```text
Explícame este código línea por línea y detecta posibles errores lógicos.
No modifiques el código todavía.
```

### Discusión

- ¿Qué hace cada línea?
- ¿Qué supuestos hace el script?
- ¿Qué pasa con secuencias en minúsculas?

---

## 5️⃣ Refactorización asistida (bien hecha) ✅

### Prompt adecuado

```text
Propón una refactorización mínima para corregir el cálculo de GC.
Explica cada cambio y por qué es necesario.
No agregues funcionalidades nuevas.
```

### Resultado esperado (ejemplo)

```python
seq = record.seq.upper()
gc = (seq.count('G') + seq.count('C')) / len(seq)
```

Mensaje clave:
> *La IA sugiere; el humano decide.*

---

## 6️⃣ Errores comunes al usar IA para programar

- Confiar en código solo porque "se ve bien"
- No ejecutar pruebas después de cambios sugeridos por IA
- Aceptar refactorizaciones grandes sin entenderlas
- No distinguir errores sintácticos de errores lógicos
- Asumir corrección biológica a partir de corrección técnica

---

## 7️⃣ Empezar un proyecto desde cero con apoyo de IA (hacerlo bien desde el inicio)

Esta sección aborda una situación común en BEII: **no existe código previo**, pero se desea iniciar un proyecto bioinformático **de manera correcta, reproducible y entendible**, usando IA como apoyo.

---

### 🧠 Principio rector

> *Antes de escribir código, hay que diseñar el problema.*

La IA **no debe** usarse para “generar el proyecto completo”, sino para **guiar cada fase** del diseño y desarrollo.

---

## 🔄 Fases recomendadas de un proyecto científico-computacional

Las siguientes fases describen **cómo deben interactuar los asistentes BEII** durante el desarrollo de un proyecto desde cero:

1. **Clarificación científica (BEII Software Coach)**  
   - Reformular la idea en una pregunta científica evaluable.
   - Identificar qué partes son computables y cuáles no.
   - Declarar supuestos y riesgos de inferencia.

2. **Diseño conceptual del análisis (BEII Software Coach)**  
   - Definir el tipo de análisis requerido.
   - Diseñar el pipeline lógico sin código.
   - Proponer criterios de validación.

3. **Diseño del software (transición Coach → PyLIA)**  
   - Traducir el diseño conceptual en una estructura de proyecto.
   - Decidir modularización y responsabilidades.

4. **Implementación incremental (PyLIA-BEII)**  
   - Implementar funciones pequeñas y verificables.
   - Documentar decisiones.

5. **Debugging y refactorización (Cursor)**  
   - Detectar errores lógicos.
   - Mejorar legibilidad sin cambiar comportamiento.

6. **Validación final (humano + PyLIA)**  
   - Ejecutar pruebas.
   - Realizar sanity checks científicos.

> *La IA acompaña cada fase, pero la responsabilidad científica siempre es humana.*


### 1️⃣ Definición del problema (fase no delegable)

**Responsabilidad humana:** definir claramente la pregunta biológica.

**Prompt recomendado:**
```text
Ayúdame a reformular esta idea en una pregunta científica clara y evaluable.
No propongas soluciones todavía.
Pregunta:
[describe aquí tu idea inicial]
```

**Resultado esperado:**
- pregunta clara
- alcance definido
- variables implícitas identificadas

---

### 2️⃣ Diseño conceptual del análisis

**Objetivo:** decidir *qué tipo de análisis* se necesita, no cómo implementarlo aún.

**Prompt recomendado:**
```text
Dada esta pregunta científica:
[pega la pregunta]

Propón un esquema conceptual del análisis necesario.
Indica entradas, salidas y supuestos.
No escribas código.
```

---

### 3️⃣ Diseño del algoritmo o pipeline

**Objetivo:** definir los pasos lógicos del análisis.

**Prompt recomendado:**
```text
Diseña un algoritmo paso a paso para este análisis.
Usa pseudocódigo o lista numerada.
Indica qué se puede verificar en cada paso.
```

---

### 4️⃣ Diseño de estructura del proyecto

**Objetivo:** organizar el proyecto antes de escribir scripts.

**Prompt recomendado:**
```text
Propón una estructura de carpetas para un proyecto reproducible
(bin/, data/, results/, docs/, src/).
Explica el propósito de cada carpeta.
```

---

### 5️⃣ Escritura incremental de código (controlada)

**Regla:** escribir **una funcionalidad a la vez**.

**Prompt recomendado:**
```text
Escribe solo una función que haga:
[describe una tarea específica]

No escribas el script completo.
Explica el código línea por línea.
```

---

### 6️⃣ Validación y pruebas

**Objetivo:** asegurar corrección antes de continuar.

**Prompt recomendado:**
```text
Propón pruebas simples y casos límite para verificar
que esta función se comporta correctamente.
No asumas datos reales.
```

---

### 7️⃣ Documentación desde el inicio

**Objetivo:** que el proyecto sea entendible por otros (y por ti).

**Prompt recomendado:**
```text
Escribe un README breve que describa:
- objetivo del proyecto
- supuestos
- entradas y salidas
- limitaciones
```

---

### 📌 Mensajes clave para el estudiante

- *La IA acelera, pero no decide el diseño.*
- *Un proyecto bien diseñado evita bugs futuros.*
- *El mejor código es el que puedes explicar y validar.*

---

## 🧪 Ejercicio práctico (Sesión 2)

**Actividad:**

1. Elige un problema bioinformático sencillo.
2. Sigue las fases 1 a 4 **sin escribir código**.
3. Entrega:
   - pregunta científica reformulada
   - diseño conceptual
   - pseudocódigo
   - estructura del proyecto

**Opcional:** avanzar a código solo después de retroalimentación.

---

## 📌 Cierre pedagógico

> *Usar IA para programar sin entender es más peligroso que no usar IA.*

---

## 🔗 Conexión con la siguiente sesión

La próxima sesión abordará:
- agentes,
- automatización de pipelines,
- y límites del uso de IA en flujos complejos.

> *Primero entiende el código. Luego automatiza.*

