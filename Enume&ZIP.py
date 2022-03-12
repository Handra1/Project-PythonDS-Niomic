avengers = ["Hawkeye", "Ironman", "Thor", "QuickSilver"]
e = enumerate(avengers)
print(type(e))

e_list = list(e)
print(e_list)

for index, v in enumerate(avengers):
    print(index, v)

for index, v in enumerate(avengers, start = 10):
    print(index, v)

names = ["Barton", "Stark", "Odinson", "Maximoff"]
for z1, z2 in zip(avengers, names):
    print(z1,z2)

z = zip(avengers, names)
print(*z)
