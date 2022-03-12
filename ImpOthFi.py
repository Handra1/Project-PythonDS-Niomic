import pickle

with open('contoh.pickle', 'rb') as file:
    data = pickle.load(file)
print(data)

import pandas as pd
file = 'contoh.xlsx'
data = pd.ExcelFile(file)
print(data.sheet_names)
