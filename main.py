import streamlit as st
import pandas as pd
import os
import plotly.express as px

# ===================== CONFIGURACIÓN =====================
st.set_page_config(page_title="Desigualdad Post-Pandemia", layout="wide", page_icon="📊")

st.title("📊 Análisis de Desigualdad y Recuperación Post-Pandemia")
st.subheader("Bogotá D.C. • Meta (Villavicencio) • Cundinamarca | 2019 - 2024")
st.markdown("---")

# ===================== CARGA DE DATOS =====================
PROJECT_PATH = pd.read_excel('base_pobreza.xlsx')
ruta_excel = os.path.join(PROJECT_PATH, "base_pobreza.xlsx")

if not os.path.exists(ruta_excel):
    st.error("❌ No se encontró el archivo base_pobreza.xlsx en la carpeta del proyecto.")
    st.stop()

@st.cache_data
def load_data():
    df = pd.read_excel(ruta_excel, sheet_name="Pobreza_Bogota_Villavicencio")
    df_hoja1 = pd.read_excel(ruta_excel, sheet_name="Hoja1")
    return df, df_hoja1

df, df_hoja1 = load_data()



# ===================== GRÁFICOS Y ANÁLISIS =====================

# 1. Pobreza Monetaria
st.subheader("1. Evolución de la Pobreza Monetaria")
fig1 = px.line(df, x="Año", y="Pobreza monetaria (%)", color="Región",
               markers=True, line_shape="linear",
               color_discrete_map={"Bogotá D.C.": "#003087", "Meta": "#00a3e0", "Cundinamarca": "#8cc63f"},
               title="Pobreza Monetaria (%)")
fig1.update_layout(template="plotly_white", height=520, hovermode="x unified")
st.plotly_chart(fig1, use_container_width=True)

st.markdown("""
**Análisis económico:**  
La pandemia generó un fuerte aumento de la pobreza monetaria en 2020 en las tres regiones. Bogotá mostró la recuperación más rápida y profunda, reduciendo la pobreza de 40.1% en 2020 a 19.6% en 2024. Meta (Villavicencio) presentó una recuperación más lenta, manteniéndose en niveles superiores al 27% en 2024. Esto refleja una mayor vulnerabilidad estructural en ciudades intermedias no capitales.
""")

# 2. Pobreza Extrema
st.subheader("2. Evolución de la Pobreza Extrema")
fig2 = px.line(df, x="Año", y="Pobreza extrema (%)", color="Región",
               markers=True, color_discrete_map={"Bogotá D.C.": "#003087", "Meta": "#00a3e0", "Cundinamarca": "#8cc63f"})
fig2.update_layout(template="plotly_white", height=520)
st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
**Análisis económico:**  
La pobreza extrema se triplicó en Bogotá durante 2020, pero logró reducirse por debajo de los niveles pre-pandemia en 2024. En Meta la reducción ha sido más modesta, lo que evidencia dificultades persistentes en la generación de ingresos laborales de calidad en los Llanos Orientales.
""")

# 3. Coeficiente de Gini
st.subheader("3. Evolución del Coeficiente de Gini (Desigualdad)")
fig3 = px.line(df, x="Año", y="Gini", color="Región",
               markers=True, color_discrete_map={"Bogotá D.C.": "#003087", "Meta": "#00a3e0", "Cundinamarca": "#8cc63f"})
fig3.update_layout(template="plotly_white", height=520)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
**Análisis económico:**  
Bogotá presenta consistentemente mayor desigualdad (Gini más alto), pero mostró una mejora sostenida después de 2020. Meta y Cundinamarca mantienen niveles más estables pero altos, lo que sugiere una distribución del ingreso menos concentrada pero con menor dinamismo económico.
""")

# 4. Tasa de Ocupación
st.subheader("4. Tasa de Ocupación (TO)")
fig4 = px.line(df, x="Año", y="Tasa de Ocupación (TO)", color="Región",
               markers=True, color_discrete_map={"Bogotá D.C.": "#003087", "Meta": "#00a3e0", "Cundinamarca": "#8cc63f"})
fig4.update_layout(template="plotly_white", height=520)
st.plotly_chart(fig4, use_container_width=True)

st.markdown("""
**Análisis económico:**  
La recuperación del empleo fue más fuerte en Bogotá, alcanzando niveles superiores a los pre-pandemia. Villavicencio (Meta) muestra una recuperación importante pero aún incompleta, reflejando la dependencia de sectores más vulnerables como agricultura y servicios.
""")

# 5. Tasa de Desocupación
st.subheader("5. Tasa de Desocupación (TD)")
fig5 = px.line(df, x="Año", y="Tasa de Desocupación (TD)", color="Región",
               markers=True, color_discrete_map={"Bogotá D.C.": "#003087", "Meta": "#00a3e0", "Cundinamarca": "#8cc63f"})
fig5.update_layout(template="plotly_white", height=520)
st.plotly_chart(fig5, use_container_width=True)

st.markdown("""
**Análisis económico:**  
Todas las regiones experimentaron un pico de desempleo en 2020. Bogotá logró la reducción más significativa. La menor tasa de desocupación en Meta en los últimos años puede estar relacionada con mayor informalidad laboral.
""")

# Pie de página
st.markdown("---")
st.caption("Fuente: DANE (GEIH y Pobreza Monetaria) | Elaborado por: Facultad de Economía - Universidad Santo Tomás")
