import streamlit as st

app_mode = st.sidebar.selectbox('Secciones',['Home','Ejercicio 1','Ejercicio 2','Ejercicio 3','Ejercicio 4'])

if app_mode == 'Home':
  st.title ('Proyecto N°1 de la Especialización de Python')
  st.image('Python_logo.png')
  st.image('DMC.png')
  st.write('Estudiante: Miguel Angel Limaquispe Huaman')
  st.write('Modulo 1: Pyhton Fundamentals')
  st.write('Información General: Ingeneriero de Sistemas con experiencia en Bussines Inteligencia en Sectores de Banca, Telecomunicaciones, Consumo Masivo y Farmaceútico')
  
