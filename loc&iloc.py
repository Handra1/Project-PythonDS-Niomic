import pandas as pd

dict = {"Country": ["Brazil", "Russia", "India", "China", "South Africa"],
"Capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
"Area": [8.516, 17.100, 3.286, 16.223, 5.345], "Population":[12.555, 25.678, 29.678, 32.567, 10.234]}
brics = pd.DataFrame(dict)
brics.index = ["BR","RU","IN","CH","SA"]
print(brics.loc[["RU"]])
print(brics.loc[["RU", "CH", "SA"]])
print(brics.loc[["RU", "CH", "SA"], ["Country", "Capital"]])

print(brics.iloc[[1,2,3]])
print(brics.iloc[[1,2,3], [0,1]])
