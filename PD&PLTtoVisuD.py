from sqlalchemy import create_engine, MetaData, Table, select
engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)
stmt = select([census.columns.sex, (census.columns.pop2008). label('sum_pop2008')])
print(stmt)
stmt = stmt.order_by(census.columns.sex)
results = connection.execute(stmt).fetchall()
print(results)

import pandas as pd
df = pd.DataFrame(results)
df.columns = results[0].keys()
print(df)

"""diubah ke dalam grafik"""
import matplotlib.pyplot as plt
df[10:20].plot.barh()
plt.show()
