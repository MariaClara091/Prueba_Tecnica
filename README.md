# Caso 1 – Análisis de la Copa Mundial Femenina FIFA (1991–2023)

## Descripción

Este proyecto desarrolla un análisis histórico de la Copa Mundial Femenina de la FIFA utilizando información de todas las ediciones disputadas entre 1991 y 2023.

El objetivo es identificar patrones de rendimiento, evolución de la competitividad, tendencias de anotación y desempeño de las selecciones participantes a lo largo de la historia del torneo.

## Objetivos

* Análisis donde identifique las variables del conjunto de datos mostrando los valores nulos, duplicados y el tipo de variable.
* Validación cruzada entre las tablas, identifique los campos que relacionan las tablas y si existen datos faltantes en dichos campos.
* Elaborar la tabla de posiciones del mundial realizado en 1991. Tenga en cuenta que cada partido ganado da 3 puntos, cada partido empatado da 1 punto. Así mismo, las tarjetas amarillas suman -1 punto para juego limpio y las tarjetas rojas – 2 puntos a juego limpio. La tabla debe tener la siguiente estructura:
Equipo | Partidos Jugados (PJ) | Partidos Ganados (PG) | Partidos Empatados (PE) | Partidos Perdidos (PP)| Goles a Favor (GF) | Goles en Contra (GC) | Diferencia de Goles (GF – GC) | Juego Limpio (JL) | Puntos
* Generar la tabla de goleadoras del Mundial 2023.
* Construya una rutina cuya salida sea UNA ÚNICA TABLA que muestre:
Año| Host | Equipo | Partidos Jugados | Goles Totales marcados | Promedio de Goles marcados | Goles Totales recibidos | promedio de goles recibidos | partidos totales ganados | partidos totales perdidos | partidos totales empatados | promedio de asistencia por equipo. 

## Datasets utilizados

### world_cup_women.csv

Contiene información general de cada edición del torneo:

* Año
* País anfitrión
* Número de selecciones participantes
* Campeón
* Subcampeón
* Máxima goleadora
* Asistencia total
* Promedio de asistencia
* Número de partidos

### matches_1991_2023.csv

Contiene información detallada de los 348 partidos disputados entre 1991 y 2023:

* Equipos participantes
* Marcadores
* Asistencia
* Sede
* Árbitros
* Goles
* Tarjetas
* Sustituciones

## Actividades desarrolladas

### 1. Calidad de datos

* Identificación de tipos de variables.
* Detección de valores nulos.
* Identificación de registros duplicados.

### 2. Validación cruzada entre tablas

* Identificación de campos comunes.
* Verificación de integridad de los campos de relación.
* Validación de datos faltantes.

### 3. Tabla de posiciones – Mundial 1991

Construcción de la clasificación utilizando:

* Victoria = 3 puntos
* Empate = 1 punto
* Derrota = 0 puntos
* Juego limpio:

  * Tarjeta amarilla = -1 punto
  * Tarjeta roja = -2 puntos

### 4. Tabla de goleadoras – Mundial 2023

Extracción y consolidación de las anotaciones registradas durante la competición.

### 5. Resumen histórico por selección

Generación de una tabla única con:

* Año
* País anfitrión
* Equipo
* Partidos jugados
* Goles marcados
* Promedio de goles marcados
* Goles recibidos
* Promedio de goles recibidos
* Victorias
* Derrotas
* Empates
* Promedio de asistencia

## Estructura del proyecto

```text
Caso_1_Copa_Mundial_Femenina/
│
├── Analisis_Copa_Mundial_Femenina_EJ.ipynb
├── Analisis_Copa_Mundial_Femenina.py
├── README.md
└── resultados/
```

## Tecnologías utilizadas

* Python
* Pandas
* NumPy
* Jupyter Notebook

## Ejecución

```bash
pip install pandas numpy 
python Copa_Femenina.py
```

o mediante Jupyter Notebook:

```bash
jupyter notebook Analisis_Copa_Mundial_Femenina_EJ.ipynb
```

## Resultados

Los resultados generados incluyen:

* Análisis de calidad de datos.
* Validación cruzada entre tablas.
* Tabla de posiciones del Mundial Femenino 1991.
* Tabla de goleadoras del Mundial Femenino 2023.
* Tabla histórica consolidada de rendimiento por selección.

## Link de visualizaciones

```bash
https://pruebatecnicacaso1.streamlit.app/
```

# Caso 2: Factores que Impactan el Desempeño en Matemáticas

Análisis completo de datos estudiantiles universitarios para identificar los factores que influyen en el rendimiento académico, incluyendo modelos de Machine Learning y una API REST para detección temprana de estudiantes en riesgo.

---

## Estructura del Repositorio

```
caso-desempeno-matematicas/
├── notebook/
│   └── student_performance.ipynb     ← Análisis completo (con las fases 1, 2 y 3)
├── api/
│   ├── main.py                        ← Rutas FastAPI
│   ├── schemas.py                     ← Modelos Pydantic (entrada/salida)
│   ├── service.py                     ← Lógica de predicción ML
│   ├── crud.py                        ← CRUD simulado en memoria
│   ├── requirements.txt               ← Dependencias de la API
│   └── test_requests.http             ← Casos de prueba (REST Client / Postman)
├── models/
│   ├── best_model.pkl                 ← Gradient Boosting (mejor clasificador)
│   ├── best_regressor.pkl             ← Mejor modelo de regresión
│   └── scaler.pkl                     ← StandardScaler para preprocesamiento
├── data/
│   ├── student_performance_clean.csv  ← Dataset transformado
│   ├── data_dictionary.xlsx           ← Diccionario de datos
│   └── *.png                          ← Visualizaciones generadas
├── Dockerfile
└── README.md
```

---

## Dataset

**Fuente:** [Student Performance CSV](https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/Student_Performance.csv)  
**Registros:** 10,000 estudiantes universitarios  
**Variables:** 6 (5 features + 1 target)

| Variable | Tipo | Descripción |
|---|---|---|
| Hours Studied | Numérica discreta | Horas de estudio por semana |
| Previous Scores | Numérica continua | Puntaje en evaluaciones anteriores (0–100) |
| Extracurricular Activities | Categórica nominal | Asistencia a actividades extracurriculares (Yes/No) |
| Sleep Hours | Numérica discreta | Horas de sueño promedio por noche |
| Sample Question Papers Practiced | Numérica discreta | Ejercicios prácticos resueltos |
| **Performance Index** | Numérica continua | **Variable objetivo — índice de rendimiento (0–100)** |

---

## Metodología

### Fase 1 — Estructuras de Datos
- Carga directa del dataset desde URL
- Construcción del diccionario de datos con tipos estadísticos
- Visualizaciones: histogramas, heatmap de correlaciones, boxplots, scatter plots
- Transformaciones: codificación binaria de `Extracurricular Activities`, creación de variable `rendimiento_bajo` (umbral = Q1), renombrado a snake_case

### Fase 2 — Análisis Exploratorio
- Estadística descriptiva con coeficiente de variación por variable
- **Test estadístico:** Shapiro-Wilk (normalidad) → Mann-Whitney U + Cohen's d para comparar rendimiento entre grupos extracurriculares
- **Clustering K-Means (k=3):** método del codo + Silhouette score para identificar grupos de estudiantes (bajo, medio y alto rendimiento)

### Fase 3 — Modelos de Machine Learning

#### Regresión — predecir `indice_rendimiento`
| Modelo | R² | RMSE |
|---|---|---|
| Regresión Lineal | — | — |
| Random Forest Regressor | — | — |
| XGBoost Regressor | — | — |

#### Clasificación — predecir `rendimiento_bajo` (0/1)
| Modelo | F1-score | AUC-ROC |
|---|---|---|
| Regresión Logística | — | — |
| Árbol de Decisión | — | — |
| Random Forest | — | — |
| Gradient Boosting | **0.9424** | **0.997** |
| XGBoost | — | — |

**Modelo seleccionado: Gradient Boosting**

**Métrica principal: F1-score**, porque:
1. El dataset está desbalanceado (aprox. 25% bajo rendimiento) — accuracy sola es engañosa
2. El costo de un falso negativo (no detectar a un estudiante en riesgo) es mayor que el de un falso positivo
3. F1-score equilibra Precision y Recall como media armónica
4. AUC-ROC = 0.997 confirma excelente capacidad discriminativa

---

## API FastAPI

### Correr localmente (entorno virtual en revisión)

```bash
# 1. Activar entorno virtual
# Windows:
venv\Scripts\activate

# 2. Instalar dependencias
pip install fastapi "uvicorn[standard]" scikit-learn xgboost joblib numpy pydantic

# 3. Correr desde la raíz del proyecto
uvicorn api.main:app --reload --port 8000
```

Swagger UI disponible en: **http://localhost:8000/docs**

### Correr con Docker (por revisar)

```bash
docker build -t student-api .
docker run -p 8000:8000 student-api
```
## Instalación completa

```bash
# Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# Instalar dependencias del notebook
pip install pandas numpy matplotlib seaborn scipy scikit-learn xgboost joblib jupyter ipykernel openpyxl

# Instalar dependencias de la API
pip install fastapi "uvicorn[standard]"
```

---

## Pruebas de la API

Los casos de prueba están en `api/test_requests.http`. Se pueden ejecutar con:
- **VS Code REST Client** (extensión): abrir el archivo y hacer clic en "Send Request"
- **Swagger UI**: http://localhost:8000/docs
- **Postman**: importar las requests manualmente

---

## Hallazgos

- **`resultados_anteriores`** y **`horas_de_estudio`** son los factores más determinantes del rendimiento
- Las actividades extracurriculares **no presentan diferencia estadísticamente significativa** en el rendimiento (Mann-Whitney U, tamaño del efecto pequeño)
- El clustering identificó **3 perfiles claros** de estudiantes con características diferenciadas
- El modelo de Gradient Boosting alcanza **F1=0.9424 y AUC-ROC=0.997**, siendo altamente confiable para detección temprana

---

## Stack tecnológico

`Python 3.9` · `pandas` · `numpy` · `matplotlib` · `seaborn` · `scikit-learn` · `xgboost` · `scipy` · `FastAPI` · `uvicorn` · `joblib` · `Docker`




