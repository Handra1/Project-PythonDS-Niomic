import pandas as pd
df = pd.read_csv('C:/Users/Handra/Documents/Data Science/pivot_data.csv')
weather_tidy = df.pivot(index='date', columns='element',values='value')
print(weather_tidy)

df = pd.read_csv('C:/Users/Handra/Documents/Data Science/pivot_data2.csv')
"""jika menggunakan cara pertama maka akan error karena ada duplikat entries di data tersebut. maka:"""

import numpy as np
weather_tidy2 = df.pivot_table(values='value', index='date',columns='element',aggfunc=np.mean)
print(weather_tidy2)
