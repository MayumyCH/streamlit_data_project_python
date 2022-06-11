# Importar librerías
import numpy as np
import streamlit as st
import pickle
import pandas as pd
import altair as alt
from PIL import Image
import plotly_express as px

from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor

# MÉTRICAS MODELOS
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn import metrics

# Extraer los archivos pickle - Modelos
with open('model_lr.pkl', 'rb') as li: # Modo Lectura
    lin_reg = pickle.load(li)

with open('model_knn.pkl', 'rb') as kn:
    knn_reg = pickle.load(kn)

with open('model_svm.pkl', 'rb') as sv:
    svc_m = pickle.load(sv)

with open('model_rf.pkl', 'rb') as rf:
    rfr_m = pickle.load(rf)


def main():

    #  -------------------------------
    #  	            TITULO
    #  -------------------------------

    html_temp = """
      <div>
      <h1 style="color:#181082;text-align:center;">PREDICCIÓN DE VENTAS DE VIDEOJUEGOS 📈 </h1>
      </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True) # Permite agregar HTML
    # st.title('Predicción de ventas de videojuegos')

    image = Image.open('resources/videogames_banner.jpg')
    st.image(image)

    st.write("""
     _Este proyecto se propone el análisis de la [data](https://www.kaggle.com/saurabhshahane/wild-blueberry-yield-prediction/version/1) proporcionada por Kaggle el cual corresponde a videojuegos se tiene las ventas y
     los scores obtenidos (Vgchartz y Metacritic).
     Se busca Predecir la ventas de videojuegos para el género de Acción_
    """)


    #  -------------------------------
    #  	            DATOS
    #  -------------------------------
    df = pd.read_csv("data/data_videojuego.csv", sep=",", encoding="latin1")
    df = df.drop(columns=["Unnamed: 0"])

    print(df.select_dtypes(['object']).columns)

    try:
        numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
        non_numeric_columns = list(df.select_dtypes(['object']).columns)
        non_numeric_columns.append(None)
        #st.write(non_numeric_columns)
        #print(non_numeric_columns)
    except Exception as e:
        st.write("Error!! No se cargo la data.")


    #  -------------------------------
    #  	            SIDEBAR
    #  -------------------------------
    st.sidebar.title("Settings")

    nroRegistros = st.sidebar.number_input('Seleccionar el nro de datos:', min_value=3, max_value=10, step=1)
    #nroRegistros = st.sidebar.slider('Slope', min_value=3, max_value=10, step=1)

    #  ---------------------------------------------- | GRÁFICOS
    st.sidebar.header("Gráfico")
    chart_select = st.sidebar.selectbox(
    label="Seleccione el tipo de gráfico",
    options=['Scatterplots', 'Histogram', 'Boxplot'])

    if chart_select == 'Scatterplots':
        st.sidebar.subheader("Scatterplots Settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            #color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
            plot = px.scatter(data_frame=df, x=x_values, y=y_values)
            #plot = px.scatter(data_frame=df, x=x_values, y=y_values, color=color_value)
        except Exception as e:
            print(e)

    if chart_select == 'Boxplot':
        st.sidebar.subheader("Boxplot Settings")
        try:
            y_values = st.sidebar.selectbox("Y axis", options=numeric_columns)
            x_values = st.sidebar.selectbox("X axis", options=non_numeric_columns)
            #color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
            plot = px.box(data_frame=df, y=y_values, x=x_values)
            #plot = px.box(data_frame=df, y=y, x=x, color=color_value)
        except Exception as e:
            print(e)

    if chart_select == 'Histogram':
        st.sidebar.subheader("Histogram Settings")
        try:
            x_values= st.sidebar.selectbox('Feature', options=numeric_columns)
            bin_size = st.sidebar.slider("Number of Bins", min_value=10,
                                        max_value=100, value=40)
            color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
            plot = px.histogram(x=x_values, data_frame=df, color=color_value, nbins=bin_size)
        except Exception as e:
            print(e)

    # ---------------------------------------------- | MODELOS
    st.sidebar.subheader("Modelo ML")
    optModel = ['Linear Regression', 'KNN', 'SVM', 'RandomForest Regressor']
    model = st.sidebar.selectbox('Que modelo vas a usar?', optModel)


    st.sidebar.markdown("<br><br>",unsafe_allow_html=True)
    st.sidebar.write("⌨️ con ❤️ por MayumyCH ☠️")

    html_red = """
      <a href="https://www.linkedin.com/in/heydy-mayumy-carrasco-huaccha" target="_blank"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" height="30" width="114"></a>
      | <a href="https://twitter.com/MayumyCH" target="_blank"><img src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" height="30" width="114"></a>
    """
    st.sidebar.markdown(html_red,unsafe_allow_html=True)

    #  -------------------------------
    #  	            BODY
    #  -------------------------------

    st.header("1.- 🔎 Comprensión del Negocio")
    st.write("""
     **Ventas de videojuegos de Vgchartz y calificaciones correspondientes de Metacritic**

    Motivado por el web scraping de [Gregory Smith](https://www.kaggle.com/gregorut/datasets) de VGChartz [Video Games Sales](https://www.kaggle.com/gregorut/videogamesales).
    Este conjunto de datos simplemente amplía el número de variables con otro web scraping de [Metacritic](https://www.metacritic.com/browse/games/release-date/available).

    Desafortunadamente, faltan observaciones, ya que Metacritic solo cubre un subconjunto de las plataformas. Además, un juego puede no tener todas las observaciones de las variables adicionales que se analizan a continuación.
    Los casos completos son ~ 6,900
    """)


    # ----------------------------------- BODY
    st.header("2.- 📁 Comprensión de los datos")
    st.dataframe(df.head(nroRegistros))


    st.header("3.- 📊 Análisis exploratorios (EDA)")

    if chart_select == 'Histogram':
        st.subheader(chart_select + " : " + x_values)
    else:
        st.subheader(chart_select + " : " + x_values + " VS " + y_values)

    # GRÁFICA SELECCIONADA
    st.plotly_chart(plot)

    # st.subheader("Porcentaje de Incidencias por empresa")

    st.header("4.- 📈 Modelado")
    st.write("Ingresar el valor de los parámetros:")

    NA_Sales = st.number_input("NA_Sales:")
    Critic_Score = st.number_input("Critic_Score:")
    Critic_Count = st.number_input("Critic_Count:")
    User_Score = st.number_input("User_Score:")
    User_Count = st.number_input("User_Count:")
    GPlatforms_PC =  st.number_input("GPlatforms_PC:")
    GPlatforms_Playstation =  st.number_input("GPlatforms_Playstation:")
    GPlatforms_Portable =  st.number_input("GPlatforms_Portable:")
    GPlatforms_Xbox = st.number_input("GPlatforms_Xbox:")
    Rating_E =  st.number_input("Rating_E:")
    Rating_E10 =  st.number_input("Rating_E10:")
    Rating_M = st.number_input("Rating_M:")
    Rating_T = st.number_input("Rating_T:")

    # Botón para ejecutar el modelo
    if st.button('RUN'):
        data = {
                'NA_Sales': NA_Sales,
                'Critic_Score': Critic_Score,
                'Critic_Count':Critic_Count,
                'User_Score': User_Score,
                'User_Count': User_Count,
                'GPlatforms_PC': GPlatforms_PC,
                'GPlatforms_Playstation': GPlatforms_Playstation,
                'GPlatforms_Portable': GPlatforms_Portable,
                'GPlatforms_Xbox': GPlatforms_Xbox,
                'Rating_E10+': Rating_E10,
                'Rating_E': Rating_E,
                'Rating_M': Rating_M,
                'Rating_T': Rating_T,
                }
        dfPrueba = pd.DataFrame(data, index=[0])

        # Segundo encabezado
        st.subheader('Modelo: ')
        st.subheader(model)
        #st.write(df)

        if model == 'Linear Regression':
            st.success(lin_reg.predict(dfPrueba))
        elif model == 'RandomForest Regressor':
            st.success(rfr_m.predict(dfPrueba))
        elif model == 'KNN':
            st.success(knn_reg.predict(dfPrueba))
        else:
            st.success(svc_m.predict(dfPrueba))

if __name__ == '__main__':
    main()
