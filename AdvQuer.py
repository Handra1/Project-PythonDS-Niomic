from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Northwind.db')
df = pd.read_sql_query('SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers on Orders.CustomerID = Customers.CustomerID', engine)
print(df.head())
