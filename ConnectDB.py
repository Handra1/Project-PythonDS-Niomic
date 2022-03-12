from sqlalchemy import create_engine

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()
print(engine.table_names())

from sqlalchemy import MetaData, Table
metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)
print(repr(census))
