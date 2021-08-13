import random
import pandas as pd
import numpy as np

latitude = []
longitude = []

n = int(input("Número de Coordenadas: "))

for i in range(n):
   lat = random.uniform(-90, 90)
   long = random.uniform(-180, 180)

   latitude.append(lat)
   longitude.append(long)

data = {'Latitude': latitude, 'Longitude': longitude}

df = pd.DataFrame(data)
df.index = np.arange(1, len(df)+1)

df.to_excel('Planilhas/Coordenadas Geradas.xlsx')
print('DataFrame is written successfully to Excel File.')