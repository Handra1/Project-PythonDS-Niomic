print([num ** 2 for num in range(10) if num % 2 == 0])
print(5%2)
print(6%2)
print([num ** 2 if num % 2 == 0 else 0 for num in range(10)])

"""list comprehensions dictionaries"""
pos_neg = {num : -num for num in range(9)}
print(pos_neg)
print(type(pos_neg))
