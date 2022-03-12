"""Updating data in database"""
from sqlalchemy import create_engine, MetaData, Table, Column, func, select
engine = create_engine('sqlite:///employees.sqlite')
connection = engine.connect()
metadata = MetaData()
employees = Table('employees', metadata, autoload=True, autoload_with=engine)
stmt = select([employees])
results = connection.execute(stmt).fetchall()
print(*results, sep='\n')

from sqlalchemy import update
stmt = update(employees)
stmt = stmt.where(employees.columns.Id == 3)
stmt = stmt.values(Active = True)
print(stmt)
results = connection.execute(stmt)
print(results.rowcount)
stmt = update (employees)
stmt = stmt.where(employees.columns.Active==True)
stmt = stmt.values(Active=False, Salary = 0.00)
results = connection.execute(stmt)
print(results.rowcount)

from sqlalchemy import desc
new_salary = select([employees.columns.Salary])
new_salary = new_salary.order_by(desc(employees.columns.Salary))
new_salary = new_salary.limit(1)
print(new_salary)
stmt = update(employees)
stmt = stmt.values(Salary=new_salary)
results = connection.execute(stmt)
print(results.rowcount)
