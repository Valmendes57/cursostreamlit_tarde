import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("Dashboard de Vendas:shopping_trolley:")

url = "https://labdados.com/produtos"
response = requests.get(url)
df = pd.DataFrame.from_dict(response.json())
# baloes
st.balloons()
# Valor total
st.metric('Receita',df['Preço'].sum())
# a quantidade de vendas
st.metric('Qtde Vendas',df.shape[0]) # linhas
# a quantidade de variáveis
st.metric('Qtde de variaveis',df.shape[1]) # colunas
st.dataframe(df)
st.snow() #fim do projeto


