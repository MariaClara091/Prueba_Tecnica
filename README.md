# Caso 1 – Análisis de la Copa Mundial Femenina FIFA (1991–2023)

## Descripción

Este proyecto desarrolla un análisis histórico de la Copa Mundial Femenina de la FIFA utilizando información de todas las ediciones disputadas entre 1991 y 2023.

El objetivo es identificar patrones de rendimiento, evolución de la competitividad, tendencias de anotación y desempeño de las selecciones participantes a lo largo de la historia del torneo.

## Objetivos

*  1. Análisis donde identifique las variables del conjunto de datos mostrando los valores nulos, duplicados y el tipo de variable.
*  2. Validación cruzada entre las tablas, identifique los campos que relacionan las tablas y si existen datos faltantes en dichos campos.
*  3. Elabore la tabla de posiciones del mundial realizado en 1991. Tenga en cuenta que cada partido ganado da 3 puntos, cada partido empatado da 1 punto. Así mismo, las tarjetas amarillas suman -1 punto para juego limpio y las tarjetas rojas – 2 puntos a juego limpio. La tabla debe tener la siguiente estructura:
Equipo | Partidos Jugados (PJ) | Partidos Ganados (PG) | Partidos Empatados (PE) | Partidos Perdidos (PP)| Goles a Favor (GF) | Goles en Contra (GC) | Diferencia de Goles (GF – GC) | Juego Limpio (JL) | Puntos
*  4. Generar la tabla de goleadoras del Mundial 2023.
*  5. Construya una rutina cuya salida sea UNA ÚNICA TABLA que muestre:
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

```
```

