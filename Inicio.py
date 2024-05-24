import streamlit as st
import PIL
import os 

# Configuración del sidebar
st.set_page_config(page_title='Balanza de Pagos',page_icon='⚖️')
st.sidebar.header('Análisis Balanza de Pagos'+'⚖️')
st.sidebar.image('logo banrep.png')
st.sidebar.page_link('pages/Inicio2.py',label='🔗¿Qué es la balanza de pagos?')


year = st.sidebar.selectbox('Seleccione el año que desee consultar:', list(range(2013, 2024)))

# Ejecutar el contenido del año seleccionado
if os.path.exists(f"pages/{year}.py"):
    with open(f"pages/{year}.py", "r", encoding="utf-8") as f:
        exec(f.read())
else:
    st.error(f"Página para el año {year} no encontrada")



