import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Monitoramento Legislativo", layout="wide")

@st.cache_data
def carregar_dados():
    return pd.read_csv("data_fake.csv")

df = carregar_dados()
df["data_apresentacao"] = pd.to_datetime(df["data_apresentacao"])

st.title("Monitoramento Legislativo – Proteção de Crianças na Internet")

st.sidebar.header("Filtros")

categorias = st.sidebar.multiselect(
    "Categoria",
    options=sorted(df["categoria"].unique()),
    default=sorted(df["categoria"].unique())
)

partidos = st.sidebar.multiselect(
    "Partido",
    options=sorted(df["partido"].unique()),
    default=sorted(df["partido"].unique())
)

casas = st.sidebar.multiselect(
    "Casa legislativa",
    options=sorted(df["casa"].unique()),
    default=sorted(df["casa"].unique())
)

df_filtrado = df[
    (df["categoria"].isin(categorias)) &
    (df["partido"].isin(partidos)) &
    (df["casa"].isin(casas))
]

col1, col2, col3 = st.columns(3)
col1.metric("Total de proposições", len(df_filtrado))
col2.metric("Total de categorias", df_filtrado["categoria"].nunique())
col3.metric("Parlamentares únicos", df_filtrado["autor"].nunique())

st.subheader("Proposições por categoria")
por_categoria = df_filtrado["categoria"].value_counts().reset_index()
por_categoria.columns = ["categoria", "total"]
fig_bar = px.bar(por_categoria, x="categoria", y="total")
st.plotly_chart(fig_bar, use_container_width=True)

st.subheader("Evolução ao longo do tempo")
por_mes = (
    df_filtrado
    .groupby(df_filtrado["data_apresentacao"].dt.to_period("M"))
    .size()
    .reset_index(name="total")
)
por_mes["data_apresentacao"] = por_mes["data_apresentacao"].astype(str)
fig_line = px.line(por_mes, x="data_apresentacao", y="total", markers=True)
st.plotly_chart(fig_line, use_container_width=True)

st.subheader("Parlamentares mais ativos")
por_autor = df_filtrado["autor"].value_counts().reset_index()
por_autor.columns = ["autor", "proposicoes"]
st.dataframe(por_autor, use_container_width=True)

st.subheader("Distribuição por partido")
por_partido = df_filtrado["partido"].value_counts().reset_index()
por_partido.columns = ["partido", "total"]
fig_pie = px.pie(por_partido, names="partido", values="total")
st.plotly_chart(fig_pie, use_container_width=True)

st.subheader("Tabela de proposições")
st.dataframe(df_filtrado, use_container_width=True)