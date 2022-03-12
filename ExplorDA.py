import pandas as pd

df = pd.read_csv('C:/Users/Handra/Documents/Data Science/data2.csv')
print(df.info())
print(df.Continent.value_counts(dropna=False))
print(df['Continent'].value_counts(dropna=False))
print(df.Country.value_counts(dropna=False).head())
print(df.fertility.value_counts(dropna=False).head())
print(df.population.value_counts(dropna=False).head())
print(df.describe())
