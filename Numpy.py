tinggi = [1.73, 1.68, 1.71, 1.89, 1.79]
lebar = [65.4, 59.2, 63.6, 88.4, 68.7]

import numpy as np

np_tinggi = np.array(tinggi)
np_lebar = np.array(lebar)
print(np_tinggi)
print(np_lebar)
hasil = np_lebar/np_tinggi ** 2
print(hasil)
print(hasil[1])
print(hasil > 23)
print(hasil[hasil>23])

"""perbedaan python list dengan numpy array"""
python_list = [1,2,3]
numpy_array = np.array ([1,2,3])
print(python_list)
print(numpy_array)
print(python_list + python_list)
print(numpy_array + numpy_array)
