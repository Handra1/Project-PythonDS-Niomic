import numpy as np

step = 50;
dice = np.random.randint(1,7)
if dice <= 2:
    step = step - 1
elif dice <= 5:
    step = step + 1
else:
    step = step + np.random.randint(1,7)
print(dice)
print(step)
