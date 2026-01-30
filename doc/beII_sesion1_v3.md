# 🧠 BEII — Sesión 1

https://chatgpt.com/g/g-695c8a32e1188191849612ffeef32851-cientia


**Licenciatura en Ciencias Genómicas (LCG)**  
**Duración del curso:** 8–12 horas totales  
**Sesión 1:** Fundamentos epistemológicos del uso de IA en Bioinformática y Genética


## 1. Propósito de la sesión

Introducir a las y los estudiantes al uso **crítico, responsable y científicamente fundamentado** de modelos de IA generativa (LLMs) en bioinformática y genética, con énfasis en:

- calidad epistemológica,
- delimitación de inferencias,
- y verificación de resultados.

La sesión establece el **marco conceptual y metodológico** que se usará a lo largo del curso.



## 2. Objetivos de aprendizaje (medibles)

Al finalizar la sesión, el estudiante será capaz de:

1. **Distinguir** entre prompting creativo y prompting científico, identificando el tipo de conocimiento que produce cada uno.
2. **Formular un prompt científico** que incluya explícitamente:
   - rol,
   - contexto,
   - tarea,
   - restricciones,
   - criterios de verificabilidad.
3. **Identificar supuestos implícitos** y límites de inferencia en respuestas generadas por IA.
4. **Evaluar críticamente** un prompt deficiente y mejorarlo usando patrones avanzados.


## 3. Agenda sugerida (Sesión 1 – 3 horas)

| Tiempo | Actividad |
|------|----------|
| 0:00–0:15 | Presentación del curso y encuadre BEII |
| 0:15–0:45 | IA generativa: qué es y qué no es (en ciencia) |
| 0:45–1:15 | Prompting creativo vs científico (discusión guiada) |
| 1:15–1:30 | Pausa |
| 1:30–2:15 | Patrones epistemológicos de prompting científico |
| 2:15–2:50 | Ejercicio A/B/C (análisis crítico de prompts) |
| 2:50–3:00 | Cierre y takeaways |



## 4. IA generativa en BEII: marco epistemológico

### Contexto del módulo dentro del curso BEII

Este módulo se inserta en **Bioinformática y Estadística II (BEII)** como una **introducción metodológica** al uso responsable de herramientas de **inteligencia artificial generativa**, con un enfoque explícito en **formulación de problemas científicos**, **análisis crítico** y **reproducibilidad**.

BEII es un curso centrado en algoritmos, modelos y análisis de datos biológicos. En ese contexto, la IA generativa **no se introduce como una tecnología de moda**, ni como un sustituto del razonamiento estadístico o bioinformático, sino como:

- una **herramienta de apoyo cognitivo**,
- un medio para **estructurar preguntas científicas**,
- y un espacio para discutir **límites epistemológicos** (hasta dónde puede llegar el conocimiento de algo y qué cosas no puede conocer o justificar por sí mismo)  entre datos, modelos y conclusiones.


### ¿Por qué este módulo es necesario en BEII?

Este módulo responde a tres necesidades reales en la formación de científicas y científicos computacionales:

1. **Uso creciente de IA en investigación bioinformática**  
   Hoy en día, herramientas basadas en IA se usan para programar, documentar, explorar datos y diseñar análisis. Ignorar su existencia no evita su uso; **enseñar a usarlas críticamente sí reduce errores**.

2. **Riesgo de confundir respuestas plausibles con resultados científicos**  
   Los modelos generativos producen texto convincente, lo que puede inducir a aceptar conclusiones no verificadas. Este módulo entrena al estudiante para **distinguir entre texto bien escrito y conocimiento científico válido**.

3. **Preparación conceptual para el curso de Aprendizaje Supervisado**  
   Antes de entrenar modelos, es fundamental aprender a:
   - formular correctamente los problemas,
   - distinguir predicción de causalidad,
   - y reconocer los límites de los modelos.


### Relación con otros módulos del curso

Este módulo se conecta directamente con contenidos previos y posteriores de BEII:

- 🔙 **Algoritmos y análisis bioinformático**  
  Refuerza la idea de que ningún algoritmo sustituye la correcta formulación del problema.

- 🔜 **Aprendizaje supervisado**  
  Introduce de manera conceptual la diferencia entre:
  - *predecir patrones* (machine learning)
  - *explicar mecanismos* (biología experimental)

- 🔄 **Reproducibilidad y buenas prácticas**  
  El diseño de prompts se presenta como una extensión natural del diseño de protocolos y pipelines reproducibles.



###  Mensaje central del módulo

> *La inteligencia artificial no reemplaza al científico: amplifica tanto sus aciertos como sus errores.*

Por ello, este módulo no enseña a “usar IA”, sino a **pensar científicamente en un entorno donde la IA ya existe**.


- La IA **no es una fuente de verdad**, sino un **asistente cognitivo**.
- Produce texto plausible, no conocimiento validado.
- Toda salida debe clasificarse como:
  - observación,
  - inferencia,
  - o especulación.

#### Qué cuenta como evidencia en bioinformática

- Bases curadas (NCBI, RegulonDB, UniProt curated)
- Evidencia experimental > predicción in silico
- Reproducibilidad y criterios estadísticos explícitos



## 5. Prompting creativo vs Prompting científico

Una clasificación de prompts:   

- **Prompting creativo**: abierto y ambiguo.  
- **Prompting científico**: contextualizado, acotado y verificable.


### 🧠 PROMPTING CREATIVO
> Abierto, ambiguo, exploratorio

Es bueno aplicarlo cuando:

1. No sabes aún qué estás buscando  
   - Fase de ideas, lluvia de ideas, generación de hipótesis o metáforas.  
   - Ejemplo: “Explora posibles analogías entre regulación genética y lenguajes simbólicos”.

2. Quieres ampliar el espacio de posibilidades  
   - Diseño conceptual, narrativas, enfoques alternativos.  
   - Útil para romper marcos rígidos o sesgos previos.

3. El valor está en la originalidad, no en la verificabilidad inmediata  
   - Ensayos teóricos, pensamiento especulativo, divulgación, docencia creativa.

4. Trabajas con sistemas complejos mal definidos  
   - Sistemas biológicos, sociales o simbólicos aún no formalizados.

Riesgos si se usa mal:   

- Genera respuestas plausibles pero no falsables.
- Favorece la sobreinterpretación y analogías engañosas.
- No es adecuado para decisiones técnicas o conclusiones formales.




### 🔬 PROMPTING CIENTÍFICO
> Contextualizado, acotado, verificable


Es bueno aplicarlo cuando:

1. La pregunta está bien definida  
   - Variables claras, dominio específico, objetivo explícito.  
   - Ejemplo: “Resume los mecanismos de regulación transcripcional del operón lac en E. coli según RegulonDB”.

2. Necesitas precisión, trazabilidad y control de supuestos  
   - Revisión de literatura, análisis de datos, validación de hipótesis.

3. El resultado debe ser evaluable por criterios externos  
   - Reproducibilidad, referencias, consistencia lógica, datos observables.

4. Estás en fase de convergencia  
   - Refinar, comparar, decidir, escribir resultados, diseñar experimentos.

Riesgos si se usa mal:

- Cierra prematuramente el espacio de exploración.
- Reproduce sesgos del marco inicial si este es incorrecto.
- Limita la emergencia de ideas nuevas.



#### 🔁 REGLA CLAVE: FASE DEL PROCESO COGNITIVO


|    Fase del trabajo    |   → Tipo de prompting |
|------------------------|-------------------|
|Exploración                 |  → Creativo |
|Generación de hipótesis     |  → Creativo → Científico |
|Formalización               |  → Científico |
|Análisis / validación       |  → Científico |
|Síntesis conceptual         |  → Mixto. |
|Comunicación (según audiencia) |→ Creativo o Mixto. |


#### 🧩 USO AVANZADO: COMBINACIÓN ESTRATÉGICA

En proyectos complejos, la secuencia óptima suele ser:

1. Prompt creativo  
   → Abre el espacio conceptual

2. Prompt científico  
   → Selecciona, filtra y valida

3. Prompt creativo acotado  
   → Integra, sintetiza y comunica


#### 🧭 CRITERIO PRÁCTICO RÁPIDO

Antes de escribir un prompt, pregúntate:

“¿Busco sorprenderme o comprobar algo?”

- Sorprenderme → Prompting creativo
- Comprobar, justificar, medir → Prompting científico


#### Ejemplos

##### REGULACIÓN GENÉTICA (conceptual)

🧠 Prompt creativo:

```txt
“Imagina la regulación genética como un sistema de toma de decisiones.
¿Qué metáforas o estructuras abstractas ayudan a entender cómo una célula
elige entre múltiples programas de expresión?”
```

🔬 Prompt científico:

```txt
“Describe los mecanismos de regulación transcripcional dependientes de
factores sigma en E. coli, indicando condiciones de activación y genes regulados,
según la evidencia experimental reportada.”
```


#####  EXPRESIÓN DIFERENCIAL (RNA-seq)

🧠 Prompt creativo:

```txt
“Si la expresión diferencial fuera un ‘lenguaje de estados celulares’,
¿qué tipos de ‘frases’ o ‘gramáticas’ podrían emerger al comparar tejidos sanos
y cancerosos?”
```

🔬 Prompt científico:

```txt
“Realiza un análisis de expresión diferencial entre muestras de leucemia
y controles usando DESeq2. Reporta genes con FDR < 0.05 y |log2FC| > 1,
indicando el tamaño del efecto y la dirección del cambio.”
```


#####  INTERPRETACIÓN DE RESULTADOS ÓMICOS

🧠 Prompt creativo:

```txt
“Explora posibles narrativas funcionales que conecten los genes
sobreexpresados en este conjunto de datos con procesos adaptativos
del sistema celular.”
```

🔬 Prompt científico:

```txt
“Realiza un análisis de enriquecimiento funcional (GO Biological Process)
para los genes sobreexpresados. Reporta términos significativos con
ajuste por múltiples pruebas.”
```



#####  COMPARACIÓN ENTRE CONDICIONES

🧠 Prompt creativo:

```txt
“¿Qué historias biológicas podrían explicar que dos condiciones
muestren perfiles de expresión tan distintos pese a compartir
la mayoría de los genes?”
```

🔬 Prompt científico:

```txt
“Compara los perfiles de expresión entre condición A y B mediante
PCA y clustering jerárquico. Reporta la varianza explicada y la
estabilidad de los clusters.”
```



#####  CONSTRUCCIÓN DE HIPÓTESIS

🧠 Prompt creativo:

```txt
“¿Qué hipótesis no obvias podrían formularse a partir de este patrón
de coexpresión que no encajan con los reguladores conocidos?”
```

🔬 Prompt científico:

```txt
“Evalúa si los genes coexpresados comparten reguladores comunes
según RegulonDB. Aplica una prueba de enriquecimiento estadístico.”
```


#####  SÍNTESIS (HÍBRIDO)

🧠→🔬 Prompt creativo acotado:

```txt
“Propón interpretaciones funcionales para los resultados de expresión
diferencial, pero limita las conclusiones a aquellas compatibles con
la evidencia experimental disponible.”
```



## 6. Anatomía de un buen prompt (científico)


### Ejemplos 

### Analizar FastA

#### Prompt mal hecho ❌

```text
Analiza este FASTA y dime si está bien.
```

#### Problemas detectables (discusión en clase)

- ¿Qué FASTA?
- ¿Qué significa “bien”?
- ¿Qué criterios de calidad?
- ¿Cómo se verifica la respuesta?

Conclusión guiada:
> *Este prompt no es científico: es vago e irreproducible.*



### Analiza calidad de secuencias

#### Prompt aceptable ⚠️

```text
Tengo un archivo FASTA con secuencias de DNA.
Analiza su calidad y dime si sirve para análisis posteriores.
```

#### Aspectos positivos
- Hay contexto.
- Hay intención analítica.

#### Deficiencias
- No define criterios de calidad.
- No limita invención de resultados.
- No pide verificación.




Analicemos **cómo se construye un prompt científico correcto**.

Un **buen prompt** funciona como un **protocolo experimental escrito**: deja explícito *qué se quiere*, *bajo qué supuestos* y *cómo se evaluará la respuesta*.

A continuación se describen sus componentes. En cada uno se incluyen **ejemplos de frases** para que el estudiante analice **qué aportan y por qué son importantes**.


### 🧩 ROLE — Rol de la IA

**¿Qué es?**  
Define desde qué nivel de experiencia o perspectiva debe responder la IA.

**¿Por qué es importante?**  
- Evita respuestas genéricas.
- Ajusta profundidad y lenguaje.
- Simula el tipo de interlocutor académico esperado.

**Ejemplos de frases:**
- “Eres un asistente experto en bioinformática.”
- “Responde como bioinformático senior enfocado en reproducibilidad.”
- “Actúa como asesor técnico, no como divulgador.”

👉 **Discusión:** ¿qué cambiaría en la respuesta si no se especifica el rol?



### 🧩 CONTEXTO — Datos y objetivo biológico

**¿Qué es?**  
Describe los datos disponibles y el objetivo del análisis.

**¿Por qué es importante?**  
- Evita que la IA asuma información inexistente.
- Enmarca la respuesta en un problema biológico real.

**Ejemplos de frases:**
- “Archivo FASTA con secuencias de DNA bacteriano.”
- “No se cuenta con información de calidad PHRED.”
- “El objetivo es análisis de motivos regulatorios.”

👉 **Discusión:** ¿qué suposiciones incorrectas podría hacer la IA si falta contexto?



### 🧩 TAREA — Qué se quiere que haga la IA

**¿Qué es?**  
La instrucción central del prompt.

**¿Por qué es importante?**  
- Permite evaluar si la respuesta cumple o no.
- Reduce ambigüedad.

**Ejemplos de frases:**
- “Describe qué métricas de calidad evaluarías.”
- “Enumera posibles problemas que afectarían el análisis.”
- “Propón un checklist previo al análisis.”

👉 **Discusión:** ¿en qué se diferencia “describe” de “analiza” o “decide”?



### 🧩 RESTRICCIONES — Límites explícitos

**¿Qué es?**  
Reglas claras sobre lo que la IA no debe hacer.

**¿Por qué es importante?**  
- Reduce alucinaciones.
- Refuerza control humano.

**Ejemplos de frases:**
- “No ejecutes código.”
- “No inventes resultados ni cifras.”
- “Declara explícitamente cualquier supuesto.”

👉 **Discusión:** ¿qué tipo de errores evita cada restricción?



### 🧩 SALIDA ESPERADA — Formato del resultado

**¿Qué es?**  
Define cómo debe presentarse la respuesta.

**¿Por qué es importante?**  
- Facilita lectura y evaluación.
- Permite comparar respuestas.

**Ejemplos de frases:**
- “Devuelve una lista con viñetas.”
- “Usa una tabla con tres columnas.”
- “Incluye secciones claramente tituladas.”

👉 **Discusión:** ¿por qué el formato también es parte del método científico?



### 🧩 VERIFICACIÓN — Cómo validar la respuesta

**¿Qué es?**  
Indica cómo un humano puede comprobar la respuesta.

**¿Por qué es importante?**  
- Convierte texto en conocimiento científico.
- Garantiza reproducibilidad.

**Ejemplos de frases:**
- “Indica cómo verificar cada punto con herramientas estándar.”
- “Sugiere sanity checks.”
- “Describe cómo un humano confirmaría estas afirmaciones.”

👉 **Discusión:** ¿qué diferencia hay entre una respuesta convincente y una verificable?



### 📌 Mensaje clave

> *Un buen prompt no es para que la IA responda, sino para que tú puedas **evaluar, verificar y reproducir** la respuesta.*

> *El prompt es tu hipótesis escrita. La respuesta no es tuya hasta que la validas.*


> *Un buen prompt no es para que la IA responda, sino para que tú puedas **evaluar y verificar** la respuesta.*


### Errores frecuentes en genética al usar IA

- Homología ≠ función
- Coexpresión ≠ regulación directa
- Motivo encontrado ≠ regulador real
- Significativo estadístico ≠ biológicamente relevante

Estos errores se amplifican con prompts mal formulados.


### ⚠️ Analizar el siguiente prompt 
> Ejemplo peligroso — Buen prompt, mala pregunta científica

```text
ROLE:
Eres un asistente experto en bioinformática.

CONTEXTO:
Tengo datos de expresión génica bajo dos condiciones.

TAREA:
Determina si el gen X regula al gen Y.
```


### 🗣️ Mini‑debate en clase — Correlación, causalidad y evidencia

**Objetivo didáctico:**  
Que el estudiante distinga explícitamente entre *lo que los datos permiten afirmar* y *lo que biológicamente se desea saber*.

#### Organización (10–15 minutos)

- Dividir al grupo en **dos equipos**:
  - **Equipo A**: “Con estos datos **sí** se puede afirmar que X regula a Y”.
  - **Equipo B**: “Con estos datos **no** se puede afirmar regulación”.

> ⚠️ Ambos equipos deben argumentar **solo con los datos descritos** (expresión génica).

#### Preguntas guía para el debate

- ¿Qué evidencia real aportan los datos de expresión?
- ¿Qué afirmaciones **no** se pueden sostener?
- ¿Qué experimentos o datos adicionales serían necesarios?
- ¿Qué riesgos hay al usar lenguaje causal sin evidencia?

> Puente explícito — Causalidad vs predicción en Aprendizaje Automático


#### Cierre del debate (mensaje del profesor)

> *Los datos responden solo a las preguntas que fueron diseñados para responder.*

**Discusión crítica:**

- **Confunde correlación con causalidad**  
  Los datos de expresión génica solo permiten observar **asociaciones estadísticas** entre genes. Aun si dos genes muestran patrones similares, eso **no implica** que uno regule directamente al otro. La regulación génica requiere evidencia adicional (por ejemplo, unión a DNA, mutantes, ensayos funcionales).

- **No define qué se entiende por “regular”**  
  El término *regular* es biológicamente ambiguo: puede referirse a regulación transcripcional directa, indirecta, post-transcripcional o incluso a efectos contextuales. Sin una definición clara, la pregunta no es evaluable.

- **No especifica el tipo de evidencia aceptable**  
  No se indica si la conclusión debe basarse en:
  - correlación de expresión
  - presencia de sitios de unión
  - datos experimentales previos
  - modelos estadísticos
  
  Sin criterios de evidencia, cualquier respuesta carece de validez científica.

- **No propone un método de análisis**  
  La pregunta no menciona ningún enfoque (clustering, regresión, análisis de redes, pruebas estadísticas), por lo que no existe un camino reproducible para llegar a una conclusión.

- **Induce a una respuesta categórica injustificada**  
  Pedir “determina si el gen X regula al gen Y” sugiere una respuesta binaria (sí/no), cuando en biología real la evidencia suele ser **probabilística y contextual**.

- **Riesgo pedagógico**  
  Un prompt así puede llevar al estudiante a aceptar una respuesta bien redactada como verdadera, reforzando una mala práctica científica: confiar en conclusiones no sustentadas.

> *Buena forma no garantiza buena ciencia.*

> Puente explícito — Causalidad vs predicción en Aprendizaje Automático**


En **Machine Learning**, especialmente en aprendizaje supervisado:

- Los modelos aprenden a **predecir** patrones
- **No aprenden causalidad biológica** por sí mismos

Un clasificador puede aprender que:

> “Cuando X está alto, Y suele estar alto”

Pero eso solo significa:

- buena capacidad predictiva
- **no** implica que X cause Y


En clases posteriores:

- Entrenarán modelos para **predecir clases o valores**
- Evaluarán desempeño con métricas (accuracy, error, etc.)
- **No demostrarán causalidad**, solo capacidad predictiva


### Mensaje clave para el estudiante

> *Un modelo puede predecir muy bien y aun así estar científicamente equivocado.*

### Advertencia formativa

Confundir predicción con causalidad puede llevar a:

- malas interpretaciones biológicas
- conclusiones exageradas
- errores en diseño experimental

### 📌 Cierre conceptual

> *La inteligencia artificial es excelente para encontrar patrones.  
> La biología experimental es necesaria para explicar causas.*



### ⚠️ Ejemplo 2 
> Ejemplo peligroso — Buen prompt, mala pregunta científica

```text
ROLE:
Eres un asistente experto en bioinformática.

CONTEXTO:
Tengo un conjunto de variantes genéticas (SNPs) asociadas a una enfermedad compleja
obtenidas de un estudio de asociación genómica (GWAS).

TAREA:
Determina cuáles de estas variantes causan la enfermedad.
```

**Discusión crítica:**

- **Confunde asociación estadística con causalidad biológica**  
  Los resultados de GWAS identifican variantes **asociadas** a una enfermedad, no variantes que necesariamente la causen. La asociación puede deberse a ligamiento, estructura poblacional u otros factores de confusión.

- **Ignora el contexto poligénico de la enfermedad**  
  Muchas enfermedades complejas no son causadas por una sola variante, sino por la interacción de múltiples loci y factores ambientales. La pregunta simplifica en exceso el fenómeno biológico.

- **No define qué significa “causar” una enfermedad**  
  La causalidad puede referirse a:
  - aumento de riesgo
  - efecto funcional directo
  - impacto regulatorio
  Sin esta definición, la pregunta es ambigua.

- **No especifica evidencia funcional o experimental**  
  Para inferir causalidad serían necesarios datos adicionales como:
  - estudios funcionales
  - análisis de eQTL
  - experimentos de edición génica

- **Induce a conclusiones deterministas**  
  La pregunta sugiere una respuesta categórica (causa/no causa), cuando en genética humana la evidencia suele ser probabilística.

> *Una asociación estadística fuerte no implica causalidad biológica.*


### 🔗 Puente adicional hacia Aprendizaje Supervisado

En el curso de **aprendizaje supervisado**, modelos entrenados con datos de GWAS pueden:

- predecir riesgo genético
- priorizar variantes
- clasificar individuos

Pero:

- **no demuestran causalidad**
- requieren interpretación biológica cuidadosa

> *Predecir riesgo no es explicar el mecanismo.*




### Ejemplo 3
> correcto  ✅

```text
ROLE:
Eres un asistente experto en bioinformática y análisis de secuencias.

CONTEXTO:
Tengo un archivo FASTA con secuencias de DNA (longitud variable, sin calidad PHRED).
El objetivo es evaluar si los datos son adecuados para análisis posteriores
como descubrimiento de motivos o conteo de k-mers.

TAREA:
Describe qué métricas de calidad revisarías en este FASTA
y qué problemas potenciales podrían afectar el análisis.

RESTRICCIONES:
- No ejecutes código.
- No inventes resultados.
- Si falta información, indícalo explícitamente.
- Limítate a razonamiento conceptual.

SALIDA ESPERADA:
- Lista de métricas de calidad
- Posibles problemas asociados
- Recomendaciones generales

VERIFICACIÓN:
- Indica cómo un humano podría verificar cada métrica usando herramientas estándar.
```

#### Discusión guiada

- ¿Se puede verificar cada punto?
- ¿Evita alucinaciones?
- ¿Proporciona criterios claros?



### Ejemplo 4 
> Prompt con estructura científica ⭐⭐⭐

```text
ROLE:
Actúa como bioinformático senior enfocado en reproducibilidad.

CONTEXTO:
Archivo FASTA de DNA genómico (organismo bacteriano).
Planeo usarlo para análisis de motivos regulatorios.

TAREA:
Propón un checklist de control de calidad previo al análisis,
explicando por qué cada punto es relevante biológicamente.

RESTRICCIONES:
- No asumas datos que no se mencionan.
- No generes cifras.
- Declara supuestos explícitamente.

FORMATO DE SALIDA:
Tabla con columnas:
1) Métrica
2) Justificación biológica
3) Herramienta típica de verificación

VERIFICACIÓN:
Incluye una sección final titulada:
“Cómo validar que estas recomendaciones son correctas”.
```

Mensaje:
> *Esto es pensar como científico, no como usuario de IA.*




# 7. Prompting científico Avanzado


## Patrones avanzados de prompting científico

Este apéndice presenta **patrones avanzados de prompting científico** que ayudan a usar la IA como una herramienta que **fortalece** —y no sustituye— el razonamiento científico.


### A.1 Separar pregunta científica de tarea al asistente

**Idea clave:** en ciencia, primero se define *qué se quiere saber* y después *qué apoyo se solicita*.

**Bloque reutilizable:**

```text
PREGUNTA CIENTÍFICA:
(qué fenómeno biológico se desea entender)

TAREA AL ASISTENTE:
(qué tipo de apoyo se solicita: análisis conceptual, checklist, plan, etc.)
```

> *El prompt no es la pregunta científica; es la forma de pedir ayuda para pensarla.*



### A.2 Supuestos y riesgos de inferencia

**Idea clave:** toda inferencia depende de supuestos que deben hacerse explícitos.

**Bloque reutilizable:**

```text
SUPUESTOS:
Enumera los supuestos necesarios para que la respuesta sea válida.

RIESGOS DE INFERENCIA:
Lista al menos 3 formas en que esta inferencia podría fallar (confusores).
```

> *Una conclusión es tan fuerte como los supuestos que la sostienen.*



### A.3 Lenguaje calibrado y niveles de certeza

**Idea clave:** la ciencia rara vez permite afirmaciones categóricas.

**Instrucciones útiles:**

```text
Usa lenguaje calibrado ("sugiere", "es compatible con").
Evita afirmaciones categóricas si la evidencia es observacional.
```

> *El lenguaje científico refleja el nivel de evidencia disponible.*



### A.4 Trazabilidad: hecho vs inferencia vs hipótesis

**Idea clave:** no todo lo que se escribe tiene el mismo estatus epistemológico.

**Bloque reutilizable:**

```text
Etiqueta cada afirmación como:
- HECHO (derivado directamente de datos o fuentes)
- INFERENCIA (interpretación de los datos)
- HIPÓTESIS (posible explicación que requiere prueba)
```



### A.5 Contraejemplos y explicaciones alternativas

**Idea clave:** una hipótesis científica debe sobrevivir a explicaciones alternativas.

**Instrucciones útiles:**

```text
Propón al menos 2 explicaciones alternativas a la hipótesis principal.
Describe qué resultados esperaríamos si la hipótesis principal fuera falsa.
```


### A.6 Debugging del razonamiento

**Analogía:** así como se depura código, se deben depurar inferencias.

**Bloque reutilizable:**

```text
Revisa tu razonamiento buscando saltos lógicos.
Identifica supuestos no justificados.
Reescribe la conclusión con las mínimas afirmaciones soportadas por los datos.
```



### A.7 Delimitación explícita del universo de datos

**Idea clave:** sin delimitación, la IA tiende a generalizar incorrectamente.

Especificar cuando sea relevante:
- organismo y ensamblado
- tipo de experimento (RNA-seq, ChIP-seq, GWAS, etc.)
- nivel de resolución (gen, transcrito, variante)
- unidad de medida



### A.8 Salidas listas para auditoría

**Idea clave:** el conocimiento científico debe ser auditable.

**Formatos recomendados:**
- checklist
- tablas de decisiones
- listas de comandos
- criterios explícitos de aceptación / rechazo


### A.9 Validación independiente (triangulación)

**Idea clave:** una sola vía de validación rara vez es suficiente.

**Instrucción típica:**

```text
Propón al menos dos vías independientes para validar estas conclusiones.
```


### A.10 Prompt mínimo vs prompt de investigación

| Tipo | Uso principal | Características |
|------|--------------|-----------------|
| Prompt mínimo | Tareas operativas | Corto, directo, específico |
| Prompt de investigación | Análisis científico | Largo, con supuestos, riesgos y validación |




## Ejemplos completos de prompts científicos

A continuación se presentan **dos ejemplos completos** que **siguen explícitamente** los patrones recomendados en este apéndice. No son plantillas rígidas, sino **referencias de buena práctica**.


### 🧪 Ejemplo A — Análisis de calidad previo a RNA-seq (prompt de investigación)

```text
PREGUNTA CIENTÍFICA:
¿Los datos de RNA-seq disponibles son adecuados para un análisis confiable de expresión diferencial?

ROLE:
Eres un asistente experto en bioinformática con énfasis en análisis reproducible de RNA-seq.

CONTEXTO:
Se dispone de lecturas RNA-seq de un organismo bacteriano.
No se han evaluado métricas de calidad previamente.
El objetivo es realizar análisis de expresión diferencial entre dos condiciones.

TAREA AL ASISTENTE:
Propón un checklist de control de calidad previo al análisis.

SUPUESTOS:
- Las lecturas provienen del mismo protocolo experimental.
- No hay información previa de filtrado.

RIESGOS DE INFERENCIA:
- Sesgos por profundidad de secuenciación.
- Contaminación o lecturas de baja calidad.
- Diferencias técnicas entre condiciones.

RESTRICCIONES:
- No ejecutes código.
- No inventes valores numéricos.
- Limítate a razonamiento conceptual.

SALIDA ESPERADA:
Checklist estructurado con breve justificación por punto.

VERIFICACIÓN:
Indica cómo un humano puede verificar cada punto usando herramientas estándar
(FastQC, MultiQC, etc.).

VALIDACIÓN INDEPENDIENTE:
Propón al menos dos métricas o enfoques distintos para evaluar la calidad global.
```

**Por qué es un buen prompt científico:**

- Separa claramente pregunta y tarea.
- Explicita supuestos y riesgos.
- Produce una salida auditable.
- No induce conclusiones categóricas.



### 🧬 Ejemplo B — Priorización de variantes post-GWAS (prompt avanzado)

```text
PREGUNTA CIENTÍFICA:
¿Cómo priorizar variantes genéticas asociadas a una enfermedad compleja para estudios funcionales?

ROLE:
Actúa como bioinformático senior con experiencia en genética humana y GWAS.

CONTEXTO:
Se cuenta con un conjunto de SNPs asociados a una enfermedad compleja obtenidos de un GWAS.
No se dispone aún de evidencia funcional directa.

TAREA AL ASISTENTE:
Propón un marco de priorización de variantes basado en criterios biológicos y estadísticos.

SUPUESTOS:
- Las asociaciones provienen de un GWAS bien controlado.
- La enfermedad tiene un componente poligénico.

RIESGOS DE INFERENCIA:
- Confundir asociación con causalidad.
- Sobreinterpretar efectos individuales.
- Ignorar factores poblacionales.

RESTRICCIONES:
- No afirmes causalidad.
- Usa lenguaje calibrado.
- Declara explícitamente las limitaciones.

SALIDA ESPERADA:
Tabla con criterios de priorización y justificación.

VERIFICACIÓN:
Describe cómo cada criterio puede validarse con datos independientes
(eQTL, anotaciones regulatorias, estudios funcionales).

VALIDACIÓN INDEPENDIENTE:
Propón al menos dos tipos de datos adicionales que fortalecerían la priorización.
```

**Por qué es un buen prompt científico:**

- Evita determinismo genético.
- Diferencia claramente predicción y explicación.
- Promueve triangulación de evidencia.


### 📌 Mensaje final del apéndice

> *Un buen prompt científico no busca respuestas rápidas, sino **razonamiento defendible**.*




## 8. Ejercicio — Análisis crítico de prompts

**Objetivo:** mejorar la calidad epistemológica de un prompt.

**Instrucciones:**

1. Toma dos de los prompts descritos a continuación.
2. Incorpora **al menos dos** patrones avanzados de este apéndice.
3. Explica brevemente cómo esos patrones mejoran la calidad científica del prompt.

**Entregable sugerido:** `prompt_epistemology.md`



### 🔴 Prompt A 

```text
Eres un asistente experto en genética.

Tengo una secuencia de DNA bacteriano recién ensamblada.

Analiza la secuencia y dime qué genes contiene
y cuáles son sus funciones.

```


### 🟡 Prompt B 

```text
Eres un asistente experto en bioinformática.

Encontré un gen con alta similitud a otro gen conocido.

Describe qué función tiene este gen
y qué papel cumple en la célula.
```


### 🟢 Prompt C 

```text
Eres un asistente experto en bioinformática.

Tengo un archivo FASTA con secuencias de DNA bacteriano.

Describe qué aspectos de calidad revisarías antes de usar estos datos
para análisis de motivos regulatorios.
```


### 🟢 Prompt D 

```txt
Eres un asistente experto en genética comparativa.

Un conjunto de genes está conservado
entre varias especies bacterianas.

Describe qué implicaciones funcionales
tiene esta conservación.
```


### 🟢 Prompt E

```txt
Eres un asistente experto en bioinformática.

Realicé un análisis de enriquecimiento funcional
y obtuve varios términos significativos.

Describe qué significan estos resultados
y cómo interpretarlos biológicamente.

```


### 8.1 Criterios de evaluación (rúbrica breve)

| Criterio | Insuficiente | Adecuado | Excelente |
|--------|--------------|----------|-----------|
| Contexto | Ausente | Parcial | Claro y específico |
| Acotamiento | Vago | Moderado | Estricto |
| Verificabilidad | Nula | Implícita | Explícita |
| Supuestos | Ignorados | Parciales | Claramente declarados |
| Límites inferenciales | No considerados | Mencionados | Claramente delimitados |




# 🅐 Apéndice : Glosario de términos


> **Nota de alcance para el estudiante**  
> 
> En esta sesión aprenderás a **analizar y escribir prompts científicos**.  
> **No** se espera que domines IA generativa ni que produzcas prompts “perfectos”.  
> El objetivo es desarrollar **criterio científico y pensamiento crítico**.

Estos conceptos se utilizarán **a lo largo del curso**. No se busca dominarlos técnicamente, sino **entenderlos correctamente para usarlos con criterio científico**.


### 🤖 ¿Qué es la IA generativa?
Modelos computacionales capaces de **generar texto, código u otros contenidos** a partir de patrones estadísticos aprendidos en grandes volúmenes de datos.

- No razona como un humano
- No tiene un modelo interno del mundo
- No comprende biología
- Predice secuencias de texto plausibles


### 📘 ¿Qué es un LLM (Large Language Model)?

Un **LLM (Large Language Model)** es un modelo de inteligencia artificial entrenado con grandes volúmenes de texto para **aprender patrones del lenguaje** y **predecir la siguiente palabra (token)** en una secuencia.

**Características clave**

- Aprende a partir de datos textuales masivos.
- No “entiende” el contenido como un humano; **modela probabilidades**.
- Funciona a nivel de **tokens**, no de ideas o conceptos.
- Puede generar texto coherente, responder preguntas y explicar procedimientos.

**Qué puede hacer**

- Explicar conceptos técnicos.
- Sugerir estructuras de análisis o código.
- Resumir y reformular información.
- Asistir en tareas de documentación y aprendizaje.

**Qué NO puede hacer**  

- Generar conocimiento científico nuevo.
- Validar la veracidad de resultados experimentales.
- Entender causalidad biológica.
- Sustituir el criterio y la responsabilidad humana.


> Un LLM no conoce: **predice texto**.  
> El conocimiento científico sigue siendo responsabilidad del estudiante.


###  Modelos de Lenguaje Grande (LLM) más conocidos


| Familia / Nombre | Desarrollador | Tipo de modelo | Arquitectura base | Multimodal | Acceso | Uso típico |
|------------------|--------------|---------------|------------------|------------|--------|-----------|
| GPT | OpenAI | GPT-like | Transformer (decoder-only) | Sí | Propietario | Chatbots, código, análisis |
| Gemini | Google | Multimodal nativo | Transformer | Sí | Propietario | Asistentes integrados |
| Claude (Sonnet / Opus / Haiku) | Anthropic | GPT-like | Transformer (decoder-only) | Parcial | Propietario | Razonamiento, redacción |
| LLaMA | Meta | GPT-like | Transformer (decoder-only) | No | Abierto / semi-abierto | Investigación |
| Mistral | Mistral AI | GPT-like | Transformer (decoder-only) | No | Abierto | Modelos ligeros |
| Falcon | TII | GPT-like | Transformer (decoder-only) | No | Abierto | Investigación |
| BLOOM | BigScience | GPT-like | Transformer (decoder-only) | No | Abierto | Ciencia abierta |


**Cómo leer la columna “Tipo de modelo”**

- **GPT-like**  Modelos autoregresivos que predicen el siguiente token (la gran mayoría).
- **Multimodal nativo**  Diseñados desde el inicio para manejar texto, imágenes y otros datos.
- **Decoder-only Transformer**   Arquitectura dominante en LLM modernos.



### 🔢 ¿Qué es un token?

Unidad mínima de texto que procesa un modelo de lenguaje.

- Puede ser una palabra, parte de una palabra o un símbolo
- No representa una unidad semántica
- El costo y el límite de los modelos dependen del número de tokens


Saber cuántos tokens consume tu prompt te ayuda a **no exceder la ventana de contexto y reducir costos** cuando usas APIs.
Cada modelo tiene distintos límites de tokens por interacción.

**Importancia:** prompts claros y concisos reducen ambigüedad y errores.

Ver:

- [Token Calculator for LLMs](https://token-calculator.net/?utm_source=chatgpt.com)
- [OpenAI Tokenizer](https://platform.openai.com/tokenizer?utm_source=chatgpt.com)



### 📝 ¿Qué es un prompt?

Una **especificación escrita** que describe:
- el contexto
- la tarea
- las restricciones
- el formato esperado

En este curso, un prompt es equivalente a un **protocolo experimental**.


### 🚨 ¿Qué es una alucinación?

Respuesta generada por la IA que **suena correcta pero es falsa**, sin intención ni conciencia de error.

Ejemplos:
- referencias inexistentes
- datos inventados
- conclusiones no sustentadas

**Regla de BEII:** toda salida de IA debe poder **verificarse independientemente**.

### 🤖 ¿Qué es un chatbot?

Un **chatbot** es una aplicación de software diseñada para **interactuar con personas mediante lenguaje natural**, simulando una conversación humana.

Un chatbot moderno:
- Recibe texto (o voz) del usuario
- Lo procesa con un modelo de lenguaje
- Genera una respuesta en lenguaje natural

👉 El chatbot **no es el modelo**, es la **interfaz** que permite conversar con él.

### 🧪 Verificación y reproducibilidad
Principio central del curso:

> *Si no se puede verificar, no es conocimiento científico.*


### ✍️ ¿Qué es prompting?

**Prompting** es el proceso de **formular instrucciones, preguntas o contextos (prompts)** para guiar el comportamiento de un modelo de lenguaje (LLM) y obtener una respuesta útil, controlada y relevante.

En términos simples:
> Prompting es **decidir qué decirle a la IA y cómo decírselo** para que responda de forma adecuada.


**Prompting en contexto de IA**

Un prompt puede incluir:

- Contexto (qué problema se quiere resolver)
- Instrucciones claras (qué se espera de la respuesta)
- Restricciones (qué no debe hacer la IA)
- Formato deseado de salida
- Criterios de validación

El modelo **no entiende la intención**,  
solo responde a los **patrones explícitos** del prompt.

> Un buen prompt no hace inteligente a la IA;  
> **revela qué tan claro piensa quien lo escribe**.


##### Creación de prompts

- Consejos generales al diseñar prompts
	- https://www.promptingguide.ai/es/introduction/tips
	- https://www.promptingguide.ai/es/introduction/examples?utm_source=chatgpt.com
	- https://github.com/dair-ai/Prompt-Engineering-Guide?utm_source=chatgpt.com
	- https://www.amalytix.com/en/blog/free-prompt-engineering-guides/?utm_source=chatgpt.com
	
- Técnicas
	- Zero-shot
	- Few-shot
	- CoT
	- Auto-consistencia
	- Promt Chaining
	
# 📚 Apéndice B — Recursos recomendados para prompting científico y uso de IA en investigación

Este apéndice reúne **recursos externos curados** que los estudiantes pueden consultar para profundizar en:
- diseño de *prompts científicos*,
- uso responsable de modelos tipo GPT,
- y apoyo a análisis académicos y bioinformáticos.

No son obligatorios, pero están **alineados con el enfoque crítico y reproducible** del curso.



## B.1 Guías generales de Prompt Engineering

Estos recursos explican **cómo estructurar prompts efectivos**, con ejemplos y fundamentos conceptuales.

- **Prompt Engineering Guide — DAIR.AI**  
  Repositorio y guía ampliamente citada sobre técnicas de prompting, con ejemplos prácticos y taxonomías.  
  👉 https://github.com/dair-ai/Prompt-Engineering-Guide

- **Prompting Guide (promptingguide.ai)**  
  Guía interactiva con introducciones claras, ejemplos y patrones reutilizables.  
  👉 https://www.promptingguide.ai/

- **OpenAI — Prompt Engineering Guide**  
  Documentación oficial con recomendaciones para controlar salidas de modelos GPT.  
  👉 https://platform.openai.com/docs/guides/prompt-engineering

- MetaPrompting. Carolina Uribe
https://www.linkedin.com/pulse/meta-prompting-la-f%C3%B3rmula-para-crear-prompts-1010-con-uribe-velasco-qpbde/

## B.2 Recursos académicos y marcos conceptuales

Estos materiales discuten el prompting desde una **perspectiva académica y metodológica**.

- **The Prompt Canvas (arXiv)**  
  Marco estructurado para enseñar y analizar prompts de forma sistemática.  
  👉 https://arxiv.org/abs/2412.05127

- **A Systematic Survey of Prompt Engineering (arXiv)**  
  Revisión académica de técnicas, categorías y desafíos del prompting en LLMs.  
  👉 https://arxiv.org/abs/2406.06608



## B.3 Herramientas con IA para apoyo a investigación científica

Plataformas que permiten **aplicar prompts directamente** a literatura científica o flujos de análisis.

- **SciSpace**  
  Plataforma para interactuar con artículos científicos (PDFs), hacer preguntas y obtener resúmenes guiados por IA.  
  👉 https://typeset.io/

- **Research Rabbit**  
  Herramienta para exploración de literatura, redes de citación y descubrimiento de trabajos relacionados.  
  👉 https://www.researchrabbit.ai/



## B.4 Prompts y uso de IA en contextos académicos

Recursos con **ejemplos de prompts aplicados a investigación y docencia**.

- **Prompts para la academia — Lluís Codina**  
  Colección comentada de prompts útiles para investigación, revisión de literatura y escritura académica.  
  👉 https://www.lluiscodina.com/prompts-inteligencia-artificial-academia/

- **Manual de buenas prácticas en escritura de prompts (ResearchGate)**  
  Documento académico centrado en el uso responsable de prompts en educación superior.  
  👉 https://www.researchgate.net/publication/398211173



## B.5 Recomendaciones de uso para BEII

- Estos recursos deben usarse como **apoyo**, no como autoridad final.
- Cualquier resultado obtenido con IA debe:
  - poder verificarse,
  - contrastarse con datos o literatura,
  - y documentarse adecuadamente.

> *El objetivo no es usar más IA, sino usarla mejor.*

