from sqlalchemy import create_engine

engine = create_engine('sqlite:///Northwind_small.sqlite')
table_names = engine.table_names()
print(table_names)
