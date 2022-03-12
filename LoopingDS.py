world = {"Afganistan": 30.55,"Albania":2.77,"Algeria":39.21}
for k, v in world.items():
    print(k +" " +"=="+" " + str(v))
"""key dan value disingkat jadi k dan v"""

import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight/np_height ** 2
for val in bmi:
    print(val)

meas = np.array([np_height, np_weight])
for v in meas:
    print(v)

for v in np.nditer(meas):
    print(v)
