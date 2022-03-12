import numpy as np

print(np.random.rand ())
"""akan terus berubah nilainya"""
print(np.random.seed(123))
print(np.random.rand())
"""tidak berubah nilainya karena ada seed"""
print(np.random.rand())
"""tidak berubah"""
print(np.random.seed(123))
print(np.random.rand())
"""hasil sama karena sudah disetting menggunakan seed"""

print(np.random.randint(0,5))
print(np.random.randint(0,5))
"""dikarenakan random angka 1 - 4"""
