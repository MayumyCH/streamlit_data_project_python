# Importar librerias
import streamlit as st
import pickle
import pandas as pd

# Extrar los archivos pickle
with open('knn_model.pkl', 'rb') as li: # Modo Lectura
    lin_reg = pickle.load(li)

with open('lr_model.pkl', 'rb') as lo:
    log_reg = pickle.load(lo)

with open('rf_model.pkl', 'rb') as sv:
    svc_m = pickle.load(sv)


def main():


    # TITULO
    st.title('Predicción de ventas de videojuegos')
    st.header("Introducción ")
    st.write("""
     proyecto se propone el análisis de la data proporcionada por Kaggle el cual corresponde a videojuegos se tiene las ventas y 
     los scores obtenidos (Vgchartz y Metacritic); se busca Predecir la ventas de videojuegos para el género de Acción. !! --!!
    """)

    # -- SIDEBAR
    st.sidebar.header('Ingresar Parametros')


    #escoger el modelo preferido
    option = ['Linear Regression', 'KNN', 'SVM']
    model = st.sidebar.selectbox('Que modelo vas a usar?', option)


    # Segundo encabezado
    st.subheader('Modelo: ')
    st.subheader(model)
    #st.write(df)


if __name__ == '__main__':
    main()
