from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Northwind_small.sqlite')
with engine.connect() as con :
    rs = con.execute("SELECT * FROM Customer")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
print(df)

"""cara lebih ringkas"""
df2 = pd.read_sql_query("SELECT * FROM Customer", engine)
print(df2)
