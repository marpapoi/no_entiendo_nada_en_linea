import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("YARDAS_PASOS_DATOS_TICS.xlsx")
st.title('Este es un analisis estadistico de la base de datos')
st.header('Base de datos de Yardas vs. Pases')  
st.dataframe(df.head())

# Esta es la estadistica descriptiva
st.header('Estadistica descriptiva')
st.dataframe(df.describe())

#Esto esta estandarizando las columnas
df.columns = [c.lower().replace(' ','_') for c in df.columns]

#Este es el diagrama de caja y bigote de las yardas
fig, ax = plt.subplots()
ax.boxplot(df['yardas_totales'])
st.header('Diagrama de caja y bigote\nde Yardas totales')
st.pyplot(fig)

#Este es el diagrama de caja y bigote de los pases completos
fig, ax = plt.subplots()
ax.boxplot(df['pases_completos'])
st.header('Diagrama de caja y bigote\nde Pases completos    ')
st.pyplot(fig)