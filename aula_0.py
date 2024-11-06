import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("Dashboard de Vendas:shopping_trolley:")
# Configurar o layout da página
st.set_page_config(layout="wide")

# Carregar os dados do arquivo "vendas.csv" (certifique-se de que o arquivo está no mesmo diretório)
df = pd.read_csv("vendas.csv", sep=";", decimal=",")

# Exibir o DataFrame
st.write(df)