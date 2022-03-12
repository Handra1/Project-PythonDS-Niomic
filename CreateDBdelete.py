"""removing data from datatbase"""
from sqlalchemy import create_engine, MetaData, Table, Column, func, select
engine = create_engine('sqlite:///employees.sqlite')
connection = engine.connect()
metadata = MetaData()
employees = Table('employees', metadata, autoload=True, autoload_with=engine)
stmt = select([employees])
results = connection.execute(stmt).fetchall()
print(*results, sep='\n')

from sqlalchemy import delete
stmt = delete(employees).where(employees.columns.Id==3)
results = connection.execute(stmt)
print(results.rowcount)
stmt = select([func.count(employees.columns.Id)])
print(connection.execute(stmt).scalar())

delete_stmt = delete(employees)
results = connection.execute(delete_stmt)
print(results.rowcount)
employees.drop(engine)
print(employees.exists(engine))
"""metadata.drop_all(engine)) digunakan untuk menghapus semua table dan print(engine.table_names())
untuk menapilkan apakah sudah dihapus atau belum"""
