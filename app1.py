from pandas.io.formats.format import CategoricalFormatter
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Holax")
st.markdown("### Bienvenido")
df = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/TotalesPorRegion.csv")
col1,col2=st.columns(2)
with col1:
     region = st.radio("Region", df.Region.unique())
     st.markdown("Su seleccion es"+region)
with col2:
     categorica = st.radio("Categoria", df.Categoria.unique())
     st.markdown("Su seleccion es"+categorica)
filtro=df[(df.Region==region)&(df.Categoria==categorica)]
fig,ax=plt.subplots()
to_plot=filtro.iloc[:,2:-1] 
ax.plot(to_plot.T)
ax.set_title(region)
ax.set_ylabel(categorica)
ax.set_xlabel("Fechas")




