from sqlalchemy import create_engine
engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()
stmt = 'SELECT * FROM census'
result_proxy = connection.execute(stmt)
results = result_proxy.fetchall()
print(results)
first_row = results[0]
print(first_row)
print(first_row.keys())
print(first_row.state)

from sqlalchemy import Table, MetaData, Column, String, select
metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)
stmt = select([census])
results = connection.execute(stmt).fetchall()
print(results)
print(stmt)
