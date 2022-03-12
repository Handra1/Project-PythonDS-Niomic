import pandas as pd
weather_p1 = pd.read_csv('C:/Users/Handra/Documents/Data Science/concat1.csv')
weather_p2 = pd.read_csv('C:/Users/Handra/Documents/Data Science/concat2.csv')
concatenated = pd.concat([weather_p1, weather_p2])
print(concatenated)

concatenated = concatenated.loc[0,:]
print(concatenated)
"""maka hasil yang didapatkan adalah multiple index. maka:"""

concatenated = pd.concat([weather_p1, weather_p2], ignore_index=True)
print(concatenated)
