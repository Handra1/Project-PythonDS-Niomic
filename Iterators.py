employees = ["Elv", "Han", "Riel", "Me", "Saya"]
for employee in employees:
    print(employee)
for letter in "NIOMIC":
    print(letter)
"""N adalah iterasi 1, I adalah iterasi kedua dan seterusnya"""
for i in range(4):
    print(i)

"""harus bisa membedakan iterators dengan iterable, setelah metode iter diterapkan di iterable
maka berhasil dibuat. contoh iterable : lists, strings, dictionaries, file connection.
iterators adalah objek dengan metode next untuk menghasilkan nilai berturut-turut"""

word = "Da"
it = iter(word)
print(next(it))
print(next(it))

word = "Niomic"
it = iter(word)
print(*it)
"""tanda * adalah untuk menampilkan semuanya"""
print(*it)
"""tidak ada yg ditampilkan karena sudah habis"""

dict = {"Country": "Indonesia", "Capital": "Jakarta"}
for k, v in dict.items():
    print(k,v)

file = open("C:/Users/Handra/Documents/Data Science/file.txt")
it = iter(file)
print(next(it))
print(next(it))
