import pandas as pd
df = pd.read_csv('C:/Users/Handra/Documents/Data Science/data_mp.csv')
tb_melt = pd.melt(frame=df, id_vars=['country','year'])
print(tb_melt)

tb_melt['Sex'] = tb_melt.variable.str[0]
print(tb_melt)
