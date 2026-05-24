import streamlit as st
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as lfp

app_mode = st.sidebar.selectbox('Secciones',['Home','Ejercicio 1','Ejercicio 2','Ejercicio 3','Ejercicio 4'])

if app_mode == 'Home':
  st.title ('Proyecto N°1 de la Especialización de Python')
  st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
 
  st.image('Python_logo.png')
  st.image('DMC.png')
  st.markdown(
    '''
    Estudiante: Miguel Angel Limaquispe Huaman
    
    Modulo 1: Pyhton Fundamentals
    
    Información General: Ingeniero de Sistemas con experiencia en Bussines Intelligence en Sectores de Banca, Telecomunicaciones, Consumo Masivo y Farmaceútico.
    
    Año: 34 años
    
    Descripción: Proyecto enfocado en el desarrollo de una Aplicación con Streamlit
    '''
    )
elif app_mode == 'Ejercicio 1':
    
  # --- Configuración de la página ---
  st.set_page_config(page_title="Ejercicio 1 - Flujo de Caja", page_icon="💰")
  
  # --- Descripción del ejercicio ---
  st.markdown("""
  ## Ejercicio 1 – Flujo de caja con listas
  Este módulo permite registrar movimientos financieros. 
  Puedes ingresar el **concepto**, el **tipo** (Ingreso/Gasto) y el **valor**. 
  Al finalizar, verás el historial, los totales y el estado actual de tu flujo.
  """)
  
  st.divider()
  
  # --- Inicialización del estado (Session State) ---
  if "historial" not in st.session_state:
      st.session_state.historial = []
  
  # --- Interfaz de entrada de datos ---
  col1, col2, col3 = st.columns([2, 1, 1])
  
  with col1:
      concepto = st.text_input("Concepto", placeholder="Ej: Pago de luz")
  
  with col2:
      tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
  
  with col3:
      valor = st.number_input("Valor", min_value=0.0, step=1.0)
  
  # Botón para agregar
  if st.button("Agregar movimiento"):
      if concepto.strip() == "":
          st.error("Por favor, ingresa un concepto.")
      elif valor <= 0:
          st.error("El valor debe ser mayor a 0.")
      else:
          # Guardar en la lista
          registro = {
              "Concepto": concepto,
              "Tipo": tipo,
              "Valor": valor
          }
          st.session_state.historial.append(registro)
          st.success(f"Registrado: {concepto}")
  
  st.divider()
  
  # --- Cálculos y Resultados ---
  if st.session_state.historial:
      # Convertir a DataFrame para facilitar cálculos
      df = pd.DataFrame(st.session_state.historial)
      
      # Calcular totales
      total_ingresos = df[df["Tipo"] == "Ingreso"]["Valor"].sum()
      total_gastos = df[df["Tipo"] == "Gasto"]["Valor"].sum()
      saldo_final = total_ingresos - total_gastos
  
      # Mostrar Tabla
      st.subheader("Lista de movimientos registrados")
      st.dataframe(df, use_container_width=True, hide_index=True)
  
      # Mostrar Métricas
      c1, c2, c3 = st.columns(3)
      c1.metric("Total Ingresos", f"S/{total_ingresos:,.2f}")
      c2.metric("Total Gastos", f"S/{total_gastos:,.2f}")
      c3.metric("Saldo Final", f"S/{saldo_final:,.2f}")
  
      # Mostrar Estado del flujo
      if saldo_final >= 0:
          st.success(f"### El flujo de caja está **A FAVOR** 📈")
      else:
          st.error(f"### El flujo de caja está **EN CONTRA** 📉")
      
      # Botón para reiniciar
      if st.button("Limpiar todo"):
          st.session_state.historial = []
          st.rerun()
  else:
      st.info("Aún no hay movimientos registrados.")

elif app_mode == 'Ejercicio 2':
    if "registros" not in st.session_state:
        st.session_state.registros = []
    producto =  st.text_input('Producto', placeholder="Ej: Ingrese producto")
    categoria = st.selectbox('Categoría',['Computadoras','Entrada','Salida','Almacenamiento'])
    precio_unitario = st.number_input('Precio Unitario', min_value=0.0, step=1.0)
    cantidad = st.number_input("Cantidad", min_value=0, step=1)
    total = cantidad*precio_unitario
    # Botón para agregar
    if st.button('agregar registro'):
        if producto.strip()=="":
          st.error('ingresar un producto')
        elif precio_unitario <0:
          st.error ('el precio debe ser mayor a cero')
        elif cantidad <0:
          st.error ('la cantidad debe ser mayor a cero')
        else: 
          registro = {
          'producto': producto,
          'categoria' : categoria,
          'precio unitario' : precio_unitario,
          'cantidad' : cantidad,
          'total': total
        }
        st.session_state.registros.append(registro)
        st.success("Agregado")
      
    if st.session_state.registros:
       df = pd.DataFrame(st.session_state.registros)
       st.dataframe(df,use_container_width=True, hide_index=True)
       
       # Botón para reiniciar
       if st.button("Limpiar todo"):
           st.session_state.registros = []
           st.rerun()
    else:
        st.info("Aún no hay registros.")
elif app_mode == 'Ejercicio 3':
  st.markdown("""
  ## la funcion a usar es calcular_disponibilidad_sistema
  contempla el ingreso de dos parámetros
  """)
  if 'registros' not in st.session_state:
    st.session_state.registros = []
  parametro_1 = st.selectbox('tiempototal',[1,2,3,4])
  parametro_2 = st.number_input('tiempocaida',min_value=0.0,step=1.0)
  dispo = lfp.calcular_disponibilidad_sistema(parametro_1,parametro_2)
  st.metric("Disponibilidad calculada", f"{dispo:.2f}")
  # Botón para agregar
  if st.button('Agregar Registro'):
    
    """
    if parametro_1<0:
      st.error('valor negativo, ingresar mayor a cero')
    elif parametro_2<0:
      st.error('valor negativo, ingresar mayor a cero')
    else:
    """
    tablero = {
        'tiempo1' : parametro_1,
        'tiempo2' : parametro_2,
        'dispo' : dispo
      }
      st.session_state.registros.append(tablero)
      st.success('Agregado')
  if st.session_state.registros:
    df= pd.DataFrame(st.session_state.registros)
    st.dataframe(df,use_container_width=True,hide_index=True)
  else:
    st.info('Aún no hay registros')

 
  
