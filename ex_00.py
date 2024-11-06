# Escolha qualquer dataset no Kaggle

# Faça você mesmo! Faça como eu fiz
import streamlit as st
import requests
import pandas as pd
import plotly.express as px



st.title("Segmentação de clientes no ecommerce:")

url = "https://raw.githubusercontent.com/Valmendes57/dataset/refs/heads/main/vendas-por-fatura.csv"

df = pd.read_csv(url)
st.dataframe(df)