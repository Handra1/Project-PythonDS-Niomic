import glob
import pandas as pd
pattern = '*.csv'
csv_files = glob.glob(pattern)
print(csv_files)
"""menapilkan semua data berjenis file csv"""

csv2 = pd.read_csv(csv_files[13])
print(csv2.head())

list_data = []
for filename in csv_files:
    data = pd.read_csv(filename)
    list_data.append(data)
print(pd.concat(list_data))
