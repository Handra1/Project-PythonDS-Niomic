import pandas as pd

dict = {"Country": ["Brazil", "Russia", "India", "China", "South Africa"],
"Capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
"Area": [8.516, 17.100, 3.286, 16.223, 5.345], "Population":[12.555, 25.678, 29.678, 32.567, 10.234]}
brics = pd.DataFrame(dict)
print(brics)
brics.index = ["BR","RU","IN","CH","SA"]
print(brics)
print(brics[["Country"]])
print(brics[["Country", "Area", "Population"]])
"""jika ingin menampilkan baris"""
print(brics[1:4])

"""atau cara mudah"""
brics = pd.read_csv("C:/Users/Handra/Documents/Data Science/brics.csv")
print(brics)

brics = pd.read_csv("C:/Users/Handra/Documents/Data Science/brics.csv", index_col = 0)
print(brics)
