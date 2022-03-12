from sqlalchemy import create_engine, MetaData
engine = create_engine('sqlite:///employees.sqlite')
connection = engine.connect()
metadata = MetaData()
from sqlalchemy import(Table, Column, String, Integer, Float, Boolean)
employees = Table('employees', metadata,
    Column('Id', Integer()),
    Column('Name', String(255), unique=True, nullable=False),
    Column('Salary', Float(), default=100.00),
    Column('Active', Boolean(), default=True))
print(employees.constraints)
metadata.create_all(engine)
print(engine.table_names())

from sqlalchemy import insert
employees = Table('employees', metadata, autoload=True, autoload_with=engine)
stmt = insert(employees).values(Id=1, Name='Regis', Salary=1.00, Active=True)
result = connection.execute(stmt)
print(result.rowcount)
stmt = insert(employees)
values_list = [
        {'Id': 2, 'Name': 'Halo', 'Salary': 2.00, 'Active': True},
        {'Id': 3, 'Name': 'Noct', 'Salary': 5.00, 'Active': True}
        ]
result = connection.execute(stmt, values_list)
print(result.rowcount)

from sqlalchemy import select
stmt = select([employees])
result = connection.execute(stmt).fetchall()
print(*result, sep='\n')

"""JIKA INGIN MENAMBAH DATA KE DALAM TABLE DATABASE MAKA HARUS MENGHAPUS DOKUMEN DATABASE SQLITENYA BERADA
SUPAYA TIDAK ERRROR"""
