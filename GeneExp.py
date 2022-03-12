print([2 * num for num in range(10)])
print(2 * num for num in range(10))

result = (num for num in range(6))
for num in result:
    print(num)

print(list(result))
result = (num for num in range (6))
print(list(result))

result = (num for num in range (6))
print(next(result))

"""jika menggunakan list comprehensions yg bernilai ngka sampai besar seperti sampai 10jt maka bisa
mengakibatkan session dc karena output yg lama"""
"""cara yg efektif dengan generator expression"""
print(num for num in range(10**10000000))

even_nums = (num for num in range(10) if num % 2 == 0)
print(list(even_nums))

def num_sequence(n):
    """generate values from 0 to n."""
    i = 0
    while i < n:
        yield i
        i += 1

result = num_sequence(5)
print(type(result))
for item in result:
    print(result)
