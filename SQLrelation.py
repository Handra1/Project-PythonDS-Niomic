from sqlalchemy import create_engine, MetaData, Table, select, func, desc, case, cast
engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)
state_fact = Table('state_fact', metadata, autoload=True, autoload_with=engine)
stmt = select([census.columns.pop2008, state_fact.columns.abbreviation])
results = connection.execute(stmt).fetchall()
print(results)
print(*results, sep="\n")

from sqlalchemy import join
stmt = select([func.sum(census.columns.pop2008)])
stmt= stmt.select_from(census.join(state_fact, state_fact.columns.name == census.columns.state))
print(stmt)
stmt = stmt.where(state_fact.columns.circuit_court == '10')
results = connection.execute(stmt).scalar()
print(results)
