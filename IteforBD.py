import pandas as pd

result = []
for chunk in pd.read_csv('C:/Users/Handra/Documents/Data Science/data.csv', chunksize=1000):
    result.append(sum(chunk['x']))
total = sum(result)
print(total)

total = 0
for chunk in pd.read_csv('C:/Users/Handra/Documents/Data Science/data.csv', chunksize=1000):
    total += sum(chunk['x'])
print(total)
