from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert, select
engine = create_engine('sqlite:///demography.sqlite')
connection = engine.connect()
metadata = MetaData()
demography = Table('Demography', metadata,
        Column('kode BPS', Integer(), primary_key=True),
        Column('Nama', String(255), nullable=False),
        Column('Ibukota', String(255), nullable=False),
        Column('Populasi', String(255)),
        Column('Luas', String(255)),
        Column('Pulau', String(255), nullable=False))
metadata.create_all(engine)
demography = Table('Demography', metadata, autoload=True, autoload_with=engine)
print(engine.table_names())
import csv
values_list = []
with open('demography.csv') as data :
    next(data)
    reader = csv.reader(data)
    for row in reader:
        data = {'kode_BPS':row[0], 'Nama':row[1], 'Ibukota':row[2], 'Populasi':row[3], 'Luas':row[4], 'Pulau':row[5]}
        values_list.append(data)
print(values_list)

stmt = insert(demography)
results = connection.execute(stmt, values_list)
print(results.rowcount)
stmt = select([demography])
results = connection.execute(stmt).fetchall()
print(*results, sep='\n')

from sqlalchemy import func
stmt = select([demography.columns.Pulau, func.sum(func.replace(demography.columns.Populasi, '.','')).label('Populasi')])
stmt = stmt.group_by(demography.columns.Pulau)
stmt = stmt.order_by(demography.columns.Pulau)
results = connection.execute(stmt).fetchall()
print(*results, sep='\n')

import pandas as pd

df = pd.DataFrame(results)
df.columns = results[0].keys()
print(df)

import matplotlib.pyplot as plt

df.plot(kind='bar', x='Pulau', y='Populasi')
plt.xlabel('Pulau')
plt.ylabel('Populasi')
plt.title('Total Populasi di Indonesia')
plt.show()
