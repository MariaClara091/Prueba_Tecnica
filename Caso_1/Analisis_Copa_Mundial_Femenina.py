#!/usr/bin/env python
# coding: utf-8

# # Caso 1 – Análisis Histórico de la Copa Mundial Femenina FIFA (1991–2023)
# 
# ## Objetivo
# 
# Analizar el rendimiento histórico de las selecciones participantes en la Copa Mundial Femenina FIFA utilizando técnicas de manipulación, transformación y análisis de datos en Python.
# 
# ## Datasets utilizados
# 
# * world_cup_women.csv
# * matches_1991_2023.csv
# 
# ## Objetivos específicos
# 
# 1. Análisis donde identifique las variables del conjunto de datos mostrando los valores nulos, duplicados y el tipo de variable.
# 2. Validación cruzada entre las tablas, identifique los campos que relacionan las tablas y si existen datos faltantes en dichos campos.
# 3. Elabore la tabla de posiciones del mundial realizado en 1991. Tenga en cuenta que cada partido ganado da 3 puntos, cada partido 
# empatado da 1 punto. Así mismo, las tarjetas amarillas suman -1 punto para juego limpio y las tarjetas rojas – 2 puntos a juego 
# limpio.
# La tabla debe tener la siguiente estructura:
# Equipo | Partidos Jugados (PJ) | Partidos Ganados (PG) | Partidos Empatados (PE) | Partidos Perdidos (PP)| Goles a Favor (GF) | 
# Goles en Contra (GC) | Diferencia de Goles (GF – GC) | Juego Limpio (JL) | Puntos
# 4. Generar la tabla de goleadoras del Mundial 2023.
# 5. Construya una rutina cuya salida sea UNA ÚNICA TABLA que muestre:
# 
# Año| Host | Equipo | Partidos Jugados | Goles Totales marcados | Promedio de Goles marcados | Goles Totales recibidos | promedio 
# de goles recibidos | partidos totales ganados | partidos totales perdidos | partidos totales empatados | promedio de asistencia por 
# equipo. 
# 
# 

# ### Carga de librerias necesarias, lectura y tamaño de datasets

# In[ ]:


import pandas as pd
import re
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ── Carga de datos ──────────────────────────────────────────────────────────
URL_COPAS      = "https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/world_cup_women.csv"
URL_PARTIDOS = "https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/matches_1991_2023.csv"

copa_fem      = pd.read_csv(URL_COPAS)
partidos = pd.read_csv(URL_PARTIDOS)

print(f"  Tamaño de Copa Mundial Femenina : {copa_fem.shape[0]} filas × {copa_fem.shape[1]} columnas")
print(f"  matches         : {partidos.shape[0]} filas × {partidos.shape[1]} columnas")


# ## 1. Análisis de calidad de las variables

# In[140]:


copa_fem.head()


# In[141]:


partidos.head()


# ### Función de Naturaleza de variables y Nulos 

# In[142]:


def data_quality(df):

    return pd.DataFrame({
        "Variable": df.columns,
        "Tipo": df.dtypes.values,
        "Nulos": df.isnull().sum().values,
        "% Nulos": np.round(
            df.isnull().mean().values * 100,
            2
        )
    })


# In[143]:


data_quality(copa_fem)


# In[144]:


data_quality(partidos)


# ### Conteo de duplicados

# In[145]:


print(
    "Duplicados World Cup:",
    copa_fem.duplicated().sum()
)


# In[146]:


print(
    "Duplicados Matches:",
    partidos.duplicated().sum()
)


# ### Conclusión de Punto 1

# Las variables más importantes para analizar en este caso serían: 
# - home_team
# - away_team
# - home_score
# - away_score
# - Attendance
# - Venue
# - Round
# - Date
# - Host
# - Year

# Al analizar el conjunto de datos `copa_fem`, observamos está compuesto por 9 registros y 9 variables. No se encontraron registros duplicados. Y se identificaron valores nulos en las variables `Champion` y `Runner-Up`, correspondientes a la edición 2023.
# 
# El conjunto de datos `partidos` contiene información detallada de 348 encuentros disputados entre 1991 y 2023, distribuidos en 44 variables, al igual que no se encontraron registros duplicados.
# 
# Las variables fundamentales para el análisis deportivo, como equipos participantes, goles anotados, año, sede, ronda y asistencia, presentan una completitud del 100%. Algunas variables relacionadas con eventos poco frecuentes del juego, como penales, goles en propia puerta y tarjetas rojas, presentan altos porcentajes de valores nulos. Lo podemos confirmar con su porcentaje:
# 
# | Variable      | % Nulos |
# | ------------- | ------- |
# | home_penalty  | 96.84%  |
# | away_penalty  | 96.84%  |
# | home_red_card | 97.70%  |
# | away_red_card | 96.84%  |
# | home_own_goal | 94.83%  |
# | away_own_goal | 96.26%  |
# | home_goal             | 27.59%  |
# | away_goal             | 42.53%  |
# | home_yellow_card_long | 38.79%  |
# | away_yellow_card_long | 33.91%  |
# 
# Este comportamiento puede atribuirse por la naturaleza de dichas variables, ya que estos eventos no ocurren en la mayoría de los partidos porque, por ejemplo, un penal solo existe cuando ocurre un penal o una tarjeta roja solo existe cuando ocurre una expulsión. Por ello, los nulos tienen significado deportivo.

# ## 2. Validación cruzada

# In[147]:


campos_comunes = list(
    set(copa_fem.columns)
    .intersection(partidos.columns)
)

campos_comunes


# In[148]:


for col in campos_comunes:

    print("\n", col)

    print(
        "World Cup:",
        copa_fem[col].isnull().sum()
    )

    print(
        "Matches:",
        partidos[col].isnull().sum()
    )


# ### Conclusiones de Punto 2

# Se realizó una validación cruzada para identificar los campos comunes entre los conjuntos de datos `copa_fem` y `partidos`.
# 
# Los campos compartidos encontrados fueron:
# 
# * Year
# * Host
# * Attendance
# 
# Se verificó de nuevo la presencia de valores nulos en dichos campos, mostraron que ninguno de los campos comunes presenta valores faltantes. Esto indica que existe consistencia en las variables utilizadas para relacionar ambas tablas, permitiendo realizar análisis y cruces de información sin necesidad de acciones adicionales de imputación o depuración de estas variables clave.
# 

# ## 3. Construir la tabla de posiciones del Mundial 1991

# Explicación de componentes y operaciones ejercidad en la tabla: 
# 
# | Campo  | Significado        |
# | ------ | ------------------ |
# | PJ     | Partidos jugados   |
# | PG     | Partidos ganados   |
# | PE     | Partidos empatados |
# | PP     | Partidos perdidos  |
# | GF     | Goles a favor      |
# | GC     | Goles en contra    |
# | DG     | GF - GC            |
# | JL     | Juego limpio       |
# | Puntos | 3 PG + 1 PE        |

# Filtro de partidos del año 1991:

# In[149]:


mundial_1991 = partidos[
    partidos["Year"] == 1991
].copy()

print(mundial_1991.shape)


# Búsquedas de equipos participantes:

# In[150]:


equipos = sorted(
    set(mundial_1991["home_team"])
    .union(
        set(mundial_1991["away_team"])
    )
)

print(equipos)
print("Total equipos:", len(equipos))


# In[151]:


# Almacenamiento de los componentes para la tabla final
tabla = []

# Análisis por equipo
for equipo in equipos:

    local = mundial_1991[
        mundial_1991["home_team"] == equipo
    ]

    visitante = mundial_1991[
        mundial_1991["away_team"] == equipo
    ]

    pj = len(local) + len(visitante)

    pg = (
        (local["home_score"] > local["away_score"]).sum()
        +
        (visitante["away_score"] > visitante["home_score"]).sum()
    )

    pe = (
        (local["home_score"] == local["away_score"]).sum()
        +
        (visitante["away_score"] == visitante["home_score"]).sum()
    )

    pp = pj - pg - pe

    gf = (
        local["home_score"].sum()
        +
        visitante["away_score"].sum()
    )

    gc = (
        local["away_score"].sum()
        +
        visitante["home_score"].sum()
    )

    dg = gf - gc

    amarillas = (
        local["home_yellow_card_long"].notna().sum()
        +
        visitante["away_yellow_card_long"].notna().sum()
    )

    rojas = (
        local["home_red_card"].notna().sum()
        +
        visitante["away_red_card"].notna().sum()
    )

    jl = -(amarillas + (2 * rojas))

    puntos = (pg * 3) + pe

    tabla.append({
        "Equipo": equipo,
        "PJ": pj,
        "PG": pg,
        "PE": pe,
        "PP": pp,
        "GF": gf,
        "GC": gc,
        "DG": dg,
        "JL": jl,
        "Puntos": puntos
    })


# La FIFA normalmente ordena por:
# 
# - Puntos
# - Diferencia de gol
# - Goles a favor

# In[152]:


tabla = pd.DataFrame(tabla)

tabla = tabla.sort_values(
    ["Puntos", "DG", "GF"],
    ascending=False
).reset_index(drop=True)

tabla


# ### Conclusiones de Punto 3

# La tabla de posiciones muestra un claro dominio de Estados Unidos durante la primera edición de la Copa Mundial Femenina.
# 
# - Estados Unidos finalizó en la primera posición con 18 puntos, producto de seis victorias en seis partidos. Y registró la mejor diferencia de gol de 20 en todo el torneo, anotando 25 goles y recibiendo únicamente 5.
# - Suecia, Noruega y Alemania compartieron 12 puntos, aunque Suecia obtuvo una mejor posición gracias a una mayor diferencia de gol de 11.
# - China PR destacó como una de las selecciones más eficientes del torneo, logrando una diferencia de gol de 6 en solo cuatro partidos.
# - Y en la parte baja de la clasificación se ubicaron Japón, Nueva Zelanda y Nigeria, selecciones que no lograron sumar puntos durante el campeonato.
# 
# En términos generales, los resultados muestran una marcada superioridad de las selecciones europeas y de Estados Unidos durante los primeros años del fútbol femenino internacional.

# ## 4. Generar la tabla de goleadoras del Mundial 2023

# Para identificar en qué formato están registrados:

# In[153]:


partidos_2023 = partidos[
    partidos["Year"] == 2023
]

partidos_2023[
    ["home_goal_long", "away_goal_long"]
].sample(5)


# In[154]:


partidos_2023 = partidos[
    partidos["Year"] == 2023
].copy()


# In[155]:


import ast
from collections import Counter

def extraer_goleadoras(celda):

    if pd.isna(celda):
        return []

    try:

        eventos = ast.literal_eval(celda)

        nombres = []

        for evento in eventos:

            partes = evento.split("|")

            if len(partes) >= 3:

                nombres.append(
                    partes[2].strip()
                )

        return nombres

    except:

        return []


# In[ ]:


# Lista de Jugadoras y sus goles
goleadoras = []

for _, fila in partidos_2023.iterrows():

    goleadoras.extend(
        extraer_goleadoras(
            fila["home_goal_long"]
        )
    )

    goleadoras.extend(
        extraer_goleadoras(
            fila["away_goal_long"]
        )
    )


# In[157]:


contador = Counter(goleadoras)

tabla_goleadoras = pd.DataFrame(
    contador.items(),
    columns=[
        "Jugadora",
        "Goles"
    ]
)


# In[158]:


tabla_goleadoras = tabla_goleadoras.sort_values(
    by="Goles",
    ascending=False
)

tabla_goleadoras = tabla_goleadoras.reset_index(
    drop=True
)


# In[159]:


tabla_goleadoras.head(20)


# ### Conclusiones de punto 4

# Se construyó la tabla de goleadoras utilizando los registros de anotaciones de cada partido del Mundial Femenino 2023 con respecto a las jugadoras.
# 
# Los resultados muestran que:
# 
# - Hinata Miyazawa de Japón fue la máxima goleadora del torneo con 5 anotaciones.
# - Amanda Ilestedt de Suecia y Jill Roord de Países Bajos ocuparon las siguientes posiciones con 4 goles cada una.
# - Varias jugadoras finalizaron con 3 anotaciones, mostrando una distribución equilibrada de los goles entre las diferentes selecciones.
# - Y España, campeona del torneo, contó con varias jugadoras entre las más anotadoras, destacándose Aitana Bonmatí, Jennifer Hermoso y Alba Redondo.
# 
# Los resultados sugieren una mayor competitividad ofensiva entre las selecciones participantes en comparación con las primeras ediciones del campeonato, como el mayor entrenamiento que obtuvieron las jugadoras europeas con respecto a las jugadoras asiáticas o americanas, quienes destacaron en 1991.

# ## 5. ÚNICA TABLA consolidada de desempeño histórico por selección.

# In[169]:


# Lista donde almacenaremos el resumen final
resumen = []

# Recorrer cada edición del Mundial
for anio in sorted(partidos["Year"].unique()):

    datos_anio = partidos[
        partidos["Year"] == anio
    ]

    host = datos_anio["Host"].iloc[0]

    equipos = sorted(
        set(datos_anio["home_team"])
        .union(set(datos_anio["away_team"]))
    )

    # Recorrer cada selección
    for equipo in equipos:

        local = datos_anio[
            datos_anio["home_team"] == equipo
        ]

        visitante = datos_anio[
            datos_anio["away_team"] == equipo
        ]

        # Partidos jugados
        pj = len(local) + len(visitante)

        # Goles a favor
        gf = (
            local["home_score"].sum()
            +
            visitante["away_score"].sum()
        )

        # Goles en contra
        gc = (
            local["away_score"].sum()
            +
            visitante["home_score"].sum()
        )

        # Victorias
        pg = (
            (local["home_score"] > local["away_score"]).sum()
            +
            (visitante["away_score"] > visitante["home_score"]).sum()
        )

        # Empates
        pe = (
            (local["home_score"] == local["away_score"]).sum()
            +
            (visitante["away_score"] == visitante["home_score"]).sum()
        )

        # Derrotas
        pp = pj - pg - pe

        # Promedios de goles
        prom_gf = round(gf / pj, 2)
        prom_gc = round(gc / pj, 2)

        # Asistencia promedio en los partidos disputados
        asistencia = pd.concat([
            local["Attendance"],
            visitante["Attendance"]
        ])

        prom_asistencia = round(
            asistencia.mean(),
            2
        )

        # Guardar resultados
        resumen.append({
            "Año": anio,
            "Host": host,
            "Equipo": equipo,
            "Partidos Jugados": pj,
            "Goles Totales Marcados": gf,
            "Promedio Goles Marcados": prom_gf,
            "Goles Totales Recibidos": gc,
            "Promedio Goles Recibidos": prom_gc,
            "Partidos Totales Ganados": pg,
            "Partidos Totales Perdidos": pp,
            "Partidos Totales Empatados": pe,
            "Promedio Asistencia por Equipo": prom_asistencia
        })


# In[163]:


tabla_resumen = pd.DataFrame(resumen)

tabla_resumen = tabla_resumen.sort_values(
    by=["Año", "Equipo"]
).reset_index(drop=True)

tabla_resumen.head()


# In[164]:


tabla_resumen.shape


# ### Conclusiones de Punto 5

# Se desarrolló la rutina que consolida la información histórica de todas las selecciones participantes entre las ediciones de 1991 y 2023.
# 
# La tabla generada contiene indicadores de desempeño ofensivo, defensivo y de resultados para cada equipo en cada edición del torneo.
# 
# Las métricas calculadas incluyen:
# 
# * Partidos jugados.
# * Goles totales marcados.
# * Promedio de goles marcados por partido.
# * Goles totales recibidos.
# * Promedio de goles recibidos por partido.
# * Partidos ganados.
# * Partidos perdidos.
# * Partidos empatados.
# * Promedio de asistencia en los encuentros disputados.
# 
# La tabla final contiene 168 registros correspondientes a la participación histórica de las selecciones en las nueve ediciones analizadas del Mundial Femenino de la FIFA.
# 

# ## Retroalimentación y Conclusión

# Algunas preguntas propuestas para este caso se pueden responder gracias a estas conclusiones de cada punt: 
# 
# - ¿Cómo ha cambiado el promedio de goles por partido a lo largo de los torneos?
# 
# En los primeros mundiales existían diferencias muy marcadas entre selecciones fuertes y débiles, produciendo goleadas frecuentes. Con el paso de los años el nivel competitivo aumentó, reduciendo las diferencias entre equipos y generando partidos más equilibrados.
# 
# Esto sugiere una evolución positiva del fútbol femenino a nivel internacional y una distribución más homogénea del talento entre las selecciones participantes.
# 
# - ¿Cuáles son las selecciones con mejor desempeño en términos de victorias?
# 
# La selección más dominante históricamente son los Estados Unidos porque, desde la edición de 1991, obtuvo el mejor rendimiento al ganar todos sus partidos, registrar la mayor cantidad de goles anotados y finalizar como campeón del torneo. Y otras selecciones que han mantenido resultados consistentes en estos mundiales han sido Alemania, Suecia y Noruega.
# 
# - ¿Existen tendencias en los equipos dominantes y con peor desempeño?
# 
# Sí, pues los resultados muestran que algunas selecciones han mantenido un alto nivel competitivo durante varias décadas, especialmente Estados Unidos, Alemania, Suecia y Noruega.
# 
# Por otro lado, varias selecciones que participaron en las primeras ediciones registraron pocas victorias y diferencias de gol negativas, evidenciando brechas competitivas. Pero en las ediciones más recientes estas diferencias tienden a reducirse debido al crecimiento global del fútbol femenino, mayores inversiones en formación deportiva y una expansión del número de selecciones participantes.
