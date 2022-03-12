import pandas as pd
df = pd.read_csv('duplicate_data.csv')
print(df)

df = df.drop_duplicates()
print(df)

df = pd.read_csv('missing_data.csv')
print(df)
print(df.info())

df = df.dropna()
print(df)

"""akan kehilangan 40% data jika menggunakan metode tersebut"""

df = pd.read_csv('missing_data.csv')
print(df['sex'])

df['sex'] = df['sex'].fillna('missing')
print(df['sex'])

print(df[['total_bill','size']])
df[['total_bill','size']] = df[['total_bill','size']].fillna(0)
print(df[['total_bill','size']])

print(df['total_bill'].mean())
