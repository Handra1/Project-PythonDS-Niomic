import pandas as pd

state_population = pd.read_csv('merging1.csv')
state_code = pd.read_csv('merging2.csv')
print(pd.merge(left=state_population, right=state_code, on=None, left_on='state', right_on='name'))
