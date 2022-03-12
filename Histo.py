import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.792]
plt.plot(year, pop)
plt.show()

"""grafik dengan titik"""
plt.scatter(year, pop)
plt.show()

values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.5, 3.9, 4.2, 6]
plt.hist(values, bins = 3)
plt.show()
