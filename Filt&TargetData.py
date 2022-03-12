from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, Column, String, select
engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)
stmt = select([census])
stmt = stmt.where(census.columns.state == 'california')
results = connection.execute(stmt).fetchall()
for result in results:
    print(result.state, result.age)

stmt = select([census])
stmt = stmt.where(census.columns.state.startswith('New'))
for result in connection.execute(stmt):
    print(result.state, result.pop2008)

from sqlalchemy import or_
stmt = select([census])
stmt = stmt.where(
        or_(census.columns.state == 'california',
            census.columns.state == 'New York'
            )
)
for result in connection.execute(stmt):
    print(result.state, result.age)
