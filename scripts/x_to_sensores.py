"""
  Dado un X, este script pasa los datos de X a un dataframe donde:
    - Columnas: Sensores
    - Filas: Valores de la serie temporal
"""

dataframe_sensores = pd.DataFrame()
num_sensores = int(len(X_train[0,:])/375)
columns = []
for i in range(1,num_sensores+1):
    nameSensor = 'sensor%s' % i 
    columns.append(nameSensor)
    dataframe_sensores[nameSensor] = pd.Series(X_train[0,(i-1)*375:i*375])
print(dataframe_sensores)