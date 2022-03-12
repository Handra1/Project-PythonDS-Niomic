from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Northwind_small.sqlite')
con = engine.connect()
rs = con.execute("SELECT * FROM Customer")
df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys()
con.close()
print(df)

"""konteks manager"""
with engine.connect() as con :
    rs = con.execute("SELECT CompanyName, phone FROM Customer")
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()
print(df)
