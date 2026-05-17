import streamlit as st

app_mode = st.sidebar.selectbox('Secciones',['Home','Ejercicio 1','Ejercicio 2','Ejercicio 3','Ejercicio 4'])

if app_mode == 'Home':
  st.title ('Proyecto N°1 de la Especialización de Python')
  st.image('Python_logo.png')
  st.image('DMC.png')
  st.write('Miguel Angel Limaquispe Huaman')
  
