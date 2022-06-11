

# Creando una aplicación de ciencia de datos 📈 con Streamlit 🐍 🔥

![banner](https://raw.githubusercontent.com/MayumyCH/streamlit_data_project_python/main/resources/banner.png)

_Este Proyecto tiene como objetivo crear una aplicación de ciencia de datos donde podamos mostrar todos nuestros resultados (Gráficos, modelos, etc) y que estos sean visualizados de forma efectiva 🌟._


## 🔎 PASOS:

### 1-  💡  Crear un Environments Python

- Con gitbash:

    ```
    python3 -m venv envStreamlit
    python --version
    source envStreamlit/Scripts/activate

    deactivate
    ```
- Otros modos: [link](https://gist.github.com/MayumyCH/8641ce303572488239692db3a07f2334)

### 2- ⏳ Instalar las librerías necesarias a utilizar:

```
pip install -r requirement.txt
```

### 3- ⚙ Cargar los datos / Entrenar modelo / Jalar los pkl
En este paso es donde tenemos que tener nuestro proyecto de ciencia de datos, aquí se busca exportar los modelos a formato KML. Para que estos sean consumidos por la web que se creara


### 4- 🗒 Crear un archivo ``web.py``
Aquí es donde estará todo el código para crear la aplicación de ciencia de datos

### 5- 🚀 Desplegar la aplicación

- Forma LOCAL
    ```
    streamlit run web.py
    ```
- Forma REMOTO

  Usaremos [Streamlit.io ⚡](https://share.streamlit.io/) para publicar nuestra app !
  
  <br>

  **📌 NOTA: Hay que tener nuestro proyecto en un repositorio de Github**

  <br>

  Luego ejecutar los siguientes pasos:

  <br>


  ![Streamlit.io](https://raw.githubusercontent.com/MayumyCH/streamlit_data_project_python/main/resources/img/Streamlit_1.png)
  .

  ![Streamlit.io](https://raw.githubusercontent.com/MayumyCH/streamlit_data_project_python/main/resources/img/Streamlit_2.png)

  <br>

  Y listo ya tenemos nuestra app publicada  🔥🌟!!

## 🔗 Link importantes 
1. [Link de la data del proyecto](https://raw.githubusercontent.com/MayumyCH/streamlit_data_project_python/main/data/data_videojuego.csv)
2. [Notebook del proyecto](https://github.com/MayumyCH/streamlit_data_project_python/blob/main/data_science_project_python.ipynb)
3. [PDF presentación del proyecto](https://github.com/MayumyCH/streamlit_data_project_python/blob/main/resources/WiDS_2022_MAYUMY_CARRASCO.pdf)
3. [Link de la aplicación web del proyecto](https://share.streamlit.io/mayumych/streamlit_data_project_python/main/web.py)

---
⌨️ con ❤️ por  [Mayumy CH ☠️](https://github.com/MayumyCH)  
