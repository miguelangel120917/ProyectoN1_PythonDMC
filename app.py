import streamlit as st

app_mode = st.sidebar.selectbox('Secciones',['Home','Ejercicio 1','Ejercicio 2','Ejercicio 3','Ejercicio 4'])

if app_mode == 'Home':
  st.title ('Proeycto N°1 de la Especializacipon de Python')
