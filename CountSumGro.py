"""Sum"""
from sqlalchemy import create_engine
engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

from sqlalchemy import MetaData, Table, select
metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

from sqlalchemy import func
stmt = select([func.sum(census.columns.pop2008)])
results = connection.execute(stmt).scalar()
print(results)

"""Group By"""
stmt = select([census.columns.sex, func.sum(census.columns.pop2008)])
stmt = stmt.group_by(census.columns.sex)
results = connection.execute(stmt).fetchall()
print(results)

"""Group by multiple"""
stmt = select([census.columns.sex, census.columns.age, func.sum(census.columns.pop2008)])
stmt = stmt.group_by(census.columns.sex, census.columns.age)
results = connection.execute(stmt).fetchall()
print(results)
