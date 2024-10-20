import music
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px

m = music.get_music()

latitude = []
longitude = []

for i in m:
    la = i['artist']['latitude']
    lo = i['artist']['longitude']

    if la == 0 or lo == 0:
        continue
    else:
        latitude.append(float(la))
        longitude.append(float(lo))

data = list(zip(latitude, longitude))
df = pd.DataFrame(data, columns = ['Latitude', 'Longitude'])

plt = px.scatter_geo(df, lat = 'Latitude', lon = 'Longitude')
plt.show()
