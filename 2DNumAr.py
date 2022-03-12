import numpy as np

np_tinggi = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_lebar = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
print(np_tinggi)
print(np_lebar)

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],[65.4, 59.2, 63.6, 88.4, 68.7]])
print(np.shape(np_2d))
print(np_2d[1])

print(np_2d[0] [2])
"""atau"""
print(np_2d[0,2])

print(np_2d[:, 1:3])
print(np_2d[0, :])
