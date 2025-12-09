import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

st.title ("Manipulation de données et création de graphiques")

mes_datasets = {"flights": "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/flights.csv"}

dataset = st.selectbox("Quel dataset veux-tu utiliser", options = mes_datasets.keys())

url = mes_datasets[dataset]

df = pd.read_csv(url)

st.write(df)

colonnes_flights = df.columns.tolist()

colonne_X = st.selectbox("Choississez la colonne X", options = colonnes_flights)

options_y = [col for col in colonnes_flights if col != colonne_X]

colonne_y = st.selectbox("Choississez la colonne Y", options = options_y)

graphiques = st.selectbox("Quel graphique veux-tu utiliser ?", ['scatter_chart', 'line_chart', 'bar_chart'])

if graphiques == 'scatter_chart':
    st.scatter_chart(df, x = colonne_X, y = colonne_y)
if graphiques == 'line_chart':
    st.line_chart(df, x = colonne_X, y = colonne_y)
if graphiques == 'bar_chart':
    st.bar_chart(df, x = colonne_X, y = colonne_y)
    
if st.checkbox("Afficher la matrice de corrélation"):
    st.subheader("Ma matrice de corrélation")
    correlation_matrix = df.corr(numeric_only = True)
    
    fig = plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt='.2f')
    st.pyplot(fig)