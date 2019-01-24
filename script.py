#%% 
import pandas as pd
import scipy.io
from matplotlib import pyplot

#%%

dataframe = pd.read_csv('./csv/train_subject13.csv', header=0)

#%%
dataframe.plot()
pyplot.show()

#%%
# Informacion de columnas
print(dataframe.info())

# Columnas 
print(dataframe.columns)

# Informacion estadistica
print(dataframe.describe())



