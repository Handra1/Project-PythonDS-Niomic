import numpy as np

np_kota = np.array([[1.67, 71.78], [1.37, 63.35],[1.6, 55.09],[2.04, 74.85],[2.01, 73.57]])
print(np_kota)
print(np.mean(np_kota [:,0]))
print(np.median(np_kota[:,0]))
print(np.std(np_kota[:,0]))
print(np.corrcoef(np_kota[:,0],np_kota[:,0]))
