import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numerize.numerize import numerize

    
st.title("DASHBOARD DE VENDAS:shopping_trolley:")
url="https://labdados.com/produtos"
response=requests.get(url)
def formatar(valor,prefixo = '' ):
    for unidade in ['','mil','milhões']:
        if valor < 1000:
            return f'{prefixo} {valor:.2f} {unidade}'
        valor /= 1000
        if valor < 1000:
            return f'{prefixo} {valor:.2f} {unidade}'
        valor /= 1000
    return f'{prefixo} {valor:.2f} milhoes'
# O dataframe, só entende dicionário, nao em arquivo json
# precisamos fazer uma conversão de json para dicionário
df=pd.DataFrame.from_dict(response.json())

if st.button("todos"):
    receita_total = df["Preço"].sum()
    texto_formatado = formatar(receita_total)  # Passa o valor total para formatar
    st.metric("Receita", numerize(receita_total), texto_formatado)  # Usando numerize para exibir melhor
    st.metric("Quantidade de vendas (linhas)", df.shape[0])
    st.metric("Quantidade de variáveis (colunas)", df.shape[1])
else:
    st.write("clique no botao todos")

st.dataframe(df)