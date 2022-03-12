import pandas as pd

brics = pd.read_csv("C:/Users/Handra/Documents/Data Science/brics.csv", index_col = 0)
print(brics[["Area"]])

print(brics[["Area"]] > 8)
is_huge = brics[["Area"]] > 8
print(is_huge)

import numpy as np

print(brics[np.logical_and(brics["Area"]>8, brics["Area"]<10)])
