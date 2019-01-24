# MachingLearning-Proyecto
Proyecto de Maching Learning de Decodificación Cerebral

### Dataset 

El dataset se encuentra en la carpeta de Drive. Estos archivos se deben descargar y poner en la carpeta data/data

### Estructura de carpetas

```sh
+--- data/
| +--- data/                  // Ficheros del dataset. Ficheros .mat
| +--- additional_files/      // Fichero que contiene las coordenadas de los sensores. Se utilizó para crear la imagen de los sensores
+--- examples/                // Scripts del repositorio oficial de la competición 
| +--- benchmark_pooling.py   // Script que lee todos los ficheros .mat, realiza un preprocesado y clasifica con LogicRegression
| +--- createCsvpy            // Script que permite pasar los ficheros .mat a formato csv
| +--- neuromag_vectorview_3d_layout.py  // Script que pinta los sensores en un dibujo.
+--- Presentacion1/           // Documentos y ficheros de la primera presentación
+--- .gitignore               // Git ignore
+---  DecMeg.ipynb            // Notebook que coge los datos de los ficheros .mat, realiza preprocesamiento de ventana de 500ms y devuelve X_train y y_train
+--- script_nocsv.py          // Script de pruebas sin coger ficheros csv. Sólo trabaando con ficheros .mat
+--- script.py                // Script de pruebas
+--- snapshot.png             // Imagen de los sensores
| | |-- ConceptController.js // Logística de la api con el documento Concept
| | |-- ProjectController.js // Logística de la api con el documento Project
| | |-- ProviderController.js // Logística de la api con el documento Provider
| | |-- UserController.js    // Logística de autenticación (Registrar usuario y loggearse) y con el documento User
| | └── ReservationController.js
```