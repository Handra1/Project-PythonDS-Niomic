print(2<3)
print("Alan"<"Alin")

import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight/np_height ** 2
print(bmi)
print(bmi[bmi>23])

print(np.logical_and(bmi>21, bmi<22))
print(bmi[np.logical_and(bmi>21, bmi<22)])

x = 12
print(x>5 and x<15)
print(not True)
