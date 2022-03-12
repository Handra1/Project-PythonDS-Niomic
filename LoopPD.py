import pandas as pd

brics = pd.read_csv("C:/Users/Handra/Documents/Data Science/brics.csv", index_col = 0)
for val in brics:
    print(val)

for lab, row in brics.iterrows():
    print(lab)
    print(row)

for lab, row in brics.iterrows():
    print(lab + ":" + row ["Capital"])

for lab, row in brics.iterrows():
    brics.loc[lab, "panjang_karakter"] = len(row["Country"])
print(brics)
