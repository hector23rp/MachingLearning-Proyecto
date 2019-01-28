# MachingLearning-Proyecto
Proyecto de Maching Learning de Decodificación Cerebral

## Instalación del entorno

	1. Arrancamos la línea de comandos de Anaconda Prompt

    2. Vamos a la carpeta donde se encuentre el repositorio

	3. Creamos el entorno virtual de tensorflow y lo activamos:

    ```sh
    conda create -n tensorflow_env tensorflow   // Creacion del entorno virtual
    
    conda activate tensorflow_env               // Activacion del entorno virtual
    ```
	 
    4. Instalamos jupyter-notebook y dependencias

    ```sh
    pip install jupyter-notebook pandas keras seaborn sklearn scipy
    ```

    5. Iniciamos jupyter

    ```sh
    jupyter noteook
    ```


### Dataset 

El dataset se encuentra en la carpeta de Drive. Estos archivos se deben descargar y poner en la carpeta data/data

### Estructura de carpetas

```sh
+--- data/
| +--- data/                  // Ficheros del dataset. Ficheros .mat
| +--- additional_files/      // Fichero que contiene las coordenadas de los sensores. Se utilizó para crear la imagen de los sensores
+--- examples/                // Scripts del repositorio oficial de la competición 
| +--- benchmark_pooling.py   // Script que lee todos los ficheros .mat, realiza un preprocesado y clasifica con LogicRegression
| +--- createCsv.py            // Script que permite pasar los ficheros .mat a formato csv
| +--- neuromag_vectorview_3d_layout.py  // Script que pinta los sensores en un dibujo.
+--- Presentacion1/           // Documentos y ficheros de la primera presentación
+--- .gitignore               // Git ignore
+---  DecMeg.ipynb            // Notebook que coge los datos de los ficheros .mat, realiza preprocesamiento de ventana de 500ms y devuelve X_train y y_train
+--- script_nocsv.py          // Script de pruebas sin coger ficheros csv. Sólo trabaando con ficheros .mat
+--- script.py                // Script de pruebas
+--- snapshot.png             // Imagen de los sensores
```