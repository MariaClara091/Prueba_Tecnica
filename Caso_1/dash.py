from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Copa Mundial Femenina FIFA",
    layout="wide"
)

# CARGA DE DATOS
BASE_DIR = Path(__file__).resolve().parent
RESULTADOS = BASE_DIR / "resultados"

tabla_1991 = pd.read_csv(
    RESULTADOS / "tabla_posiciones_1991.csv"
)

goleadoras = pd.read_csv(
    RESULTADOS / "tabla_goleadoras.csv"
)

resumen = pd.read_csv(
    RESULTADOS / "resumen_historico.csv"
)

# ==================================================
# ENCABEZADO
# ==================================================

st.title("Copa Mundial Femenina FIFA (1991–2023)")

st.markdown("""
### Caso 1 – Análisis de Datos

Este dashboard presenta los resultados obtenidos para el análisis histórico
de la Copa Mundial Femenina FIFA utilizando Python y Pandas.

**Objetivos del análisis**
- Evaluar el desempeño histórico de las selecciones.
- Analizar tendencias de goles a través de los torneos.
- Identificar equipos dominantes.
- Construir tablas de posiciones y goleadoras.
""")

# KPIs
c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Mundiales",
    resumen["Año"].nunique()
)

c2.metric(
    "Selecciones",
    resumen["Equipo"].nunique()
)

c3.metric(
    "Registros",
    len(resumen)
)

c4.metric(
    "Hosts",
    resumen["Host"].nunique()
)

st.subheader("Evolución del Promedio de Goles por Mundial")

goles_torneo = (
    resumen
    .groupby("Año")["Promedio Goles Marcados"]
    .mean()
    .reset_index()
)

fig = px.line(
    goles_torneo,
    x="Año",
    y="Promedio Goles Marcados",
    markers=True,
    title="Promedio de goles por partido en cada edición"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Selecciones con Más Victorias Históricas")

victorias = (
    resumen
    .groupby("Equipo")["Partidos Totales Ganados"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig2 = px.bar(
    victorias,
    x="Equipo",
    y="Partidos Totales Ganados",
    title="Top 10 selecciones con más victorias"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Tabla de Posiciones - Mundial 1991")
    st.dataframe(
        tabla_1991,
        use_container_width=True,
        hide_index=True
    )

with col2:
    st.subheader("Tabla de Goleadoras - Mundial 2023")
    st.dataframe(
        goleadoras,
        use_container_width=True,
        hide_index=True
    )

st.subheader("Explorador por Selección")

equipo = st.selectbox(
    "Seleccione una selección",
    sorted(resumen["Equipo"].unique())
)

datos_equipo = resumen[
    resumen["Equipo"] == equipo
]

st.dataframe(
    datos_equipo,
    use_container_width=True,
    hide_index=True
)


st.subheader("Principales Hallazgos")

st.info("""
• Estados Unidos es la selección con mejor rendimiento histórico a lo largo de los torneos.

• El número de goles por torneo muestra una tendencia creciente en las
ediciones más actuales.

• Las selecciones europeas han incrementado significativamente su competitividad a lo largo del tiempo.

• La asistencia promedio ha aumentado desde 1991, reflejando el crecimiento del fútbol femenino a nivel mundial.
""")

with st.sidebar:
    st.title("Caso 1")

    st.markdown("""

    Autor:
    María Clara Ávila Chinchia
    """)
