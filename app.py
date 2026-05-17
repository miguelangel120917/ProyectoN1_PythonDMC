import streamlit as st

app_mode = st.sidebar.selectbox('Secciones',['Home','Ejercicio 1','Ejercicio 2','Ejercicio 3','Ejercicio 4'])

if app_mode == 'Home':
  st.title ('Proyecto N°1 de la Especialización de Python')
  st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
 
  st.image('Python_logo.png')
  st.image('DMC.png')
  st.write('Estudiante: Miguel Angel Limaquispe Huaman')
  st.write('Modulo 1: Pyhton Fundamentals')
  st.write('Información General: Ingeniero de Sistemas con experiencia en Bussines Intelligence en Sectores de Banca, Telecomunicaciones, Consumo Masivo y Farmaceútico.')
  st.write('Año: 34 años')
  st.write('Descripción: Proyecto enfocado en el desarrollo de una Aplicación con Streamlit')
  st.markdown(
    """
    Estudiante: Miguel Angel Limaquispe Huaman
    Modulo 1: Pyhton Fundamentals
    Información General: Ingeniero de Sistemas con experiencia en Bussines Intelligence en Sectores de Banca, Telecomunicaciones, Consumo Masivo y Farmaceútico.
    Año: 34 años
    Descripción: Proyecto enfocado en el desarrollo de una Aplicación con Streamlit
    """
    )
 
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
  
 
  
