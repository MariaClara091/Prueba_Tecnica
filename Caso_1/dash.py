from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Copa Mundial Femenina FIFA",
    page_icon="⚽",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent

st.title("🔍 Diagnóstico de archivos")

st.write("Ruta actual:")
st.code(str(BASE_DIR))

st.write("Contenido encontrado:")

try:
    archivos = [x.name for x in BASE_DIR.iterdir()]
    st.write(archivos)
except Exception as e:
    st.error(e)

RESULTADOS = BASE_DIR / "resultados"

st.write("Carpeta resultados:")
st.code(str(RESULTADOS))

st.write("¿Existe?")
st.write(RESULTADOS.exists())

if RESULTADOS.exists():
    st.write("Archivos dentro de resultados:")
    st.write([x.name for x in RESULTADOS.iterdir()])

try:
    tabla_1991 = pd.read_csv(
        RESULTADOS / "tabla_posiciones_1991.csv"
    )

    goleadoras = pd.read_csv(
        RESULTADOS / "tabla_goleadoras.csv"
    )

    resumen = pd.read_csv(
        RESULTADOS / "resumen_historico.csv"
    )

    st.success("Archivos cargados correctamente")

    st.dataframe(tabla_1991.head())

except Exception as e:
    st.error(f"Error cargando archivos: {e}")
st.title("Copa Mundial Femenina FIFA (1991-2023)")

st.markdown("""
Dashboard desarrollado para el Caso 1 de análisis de datos.

Incluye:
- Tabla de posiciones 1991
- Goleadoras 2023
- Desempeño histórico de selecciones
- Evolución de goles por torneo
""")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Mundiales Analizados",
    resumen["Año"].nunique()
)

c2.metric(
    "Selecciones Analizadas",
    resumen["Equipo"].nunique()
)

c3.metric(
    "Registros Históricos",
    len(resumen)
)


st.header("Evolución de goles por Mundial")

goles_torneo = (
    resumen
    .groupby("Año")
    ["Promedio Goles Marcados"]
    .mean()
    .reset_index()
)

fig = px.line(
    goles_torneo,
    x="Año",
    y="Promedio Goles Marcados",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.header("Equipos con más victorias históricas")

victorias = (
    resumen
    .groupby("Equipo")
    ["Partidos Totales Ganados"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig2 = px.bar(
    victorias,
    x="Equipo",
    y="Partidos Totales Ganados"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)


st.header("Tabla de Posiciones - Mundial 1991")

st.dataframe(
    tabla_1991,
    use_container_width=True
)


st.header("Goleadoras Mundial 2023")

st.dataframe(
    goleadoras,
    use_container_width=True
)

st.header("Explorador por Selección")

equipo = st.selectbox(
    "Seleccione un equipo",
    sorted(resumen["Equipo"].unique())
)

datos_equipo = resumen[
    resumen["Equipo"] == equipo
]

st.dataframe(
    datos_equipo,
    use_container_width=True
)