import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from tqdm import tqdm

# Abrindo Planilha do Excel
df = pd.read_excel(r'Dimensionamento PG v1.xlsx', sheet_name='LatLong')
df.index = np.arange(1, len(df)+1)

# Reescrevendo Lat e Long para inserir na Biblioteca
coordenadas = []
for i in range(len(df)):
    lat, long = df.iloc[i]
    coordenadas.append(str(lat) + ', ' + str(long))

# Extraindo Infos de cada Coordenada
geolocator = Nominatim(user_agent="yama")

loop = tqdm(total=len(coordenadas), position=0, leave=False)

address = []
for i in range(len(coordenadas)):
    location = geolocator.reverse(coordenadas[i])
    address.append(location.raw)
    loop.set_description("Loading...".format(i))
    loop.update(1)          
loop.close()

# Separando as Infos de cada Coordenada por Título
place_id = []
lat = []
long = []
name = []
road = []
city_district = []
village = []
municipality = []
state_district = []
state = []
region = []
country = []
country_code = []

for i in range(len(address)):
   for key, value in address[i].items():
      if key == 'place_id':
         place_id.append(value)
      elif key == 'lat':
         lat.append(value)
      elif key == 'lon':
         long.append(value)
      elif key == 'display_name':
         name.append(value)
      elif key == 'address':
         for KEY, VALUE in address[0]['address'].items():
            if KEY == 'road':
               road.append(VALUE)
            elif KEY == 'city_district':
               city_district.append(VALUE)
            elif KEY == 'village':
               village.append(VALUE)
            elif KEY == 'municipality':
               municipality.append(VALUE)
            elif KEY == 'state_district':
               state_district.append(VALUE)
            elif KEY == 'state':
               state.append(VALUE)
            elif KEY == 'region':
               region.append(VALUE)
            elif KEY == 'country':
               country.append(VALUE)
            elif KEY == 'country_code':
               country_code.append(VALUE)
   
# Adicionando na Dataframe
df['Place Id'] = place_id
df['Lat'] = lat
df['Long'] = long
df['Display Name'] = name
df['Road'] = road
df['City District'] = city_district
df['Village'] = village
df['Municipality'] = municipality
df['State District'] = state_district
df['State'] = state
df['Region'] = region
df['Country'] = country
df['Country Code'] = country_code

# Movendo Planilha Final
df.to_excel('Infos Coordenadas.xlsx')