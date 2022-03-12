nilai = lambda x, y : x ** y
print(nilai(2,3))
print(nilai(20,15))

nomor = [48, 6, 9, 21, 1]
kotak = (lambda nom : nom ** 2, nomor)
"""lambda sampai 2 adalah function sementara, nomor adalah secquence"""
print(kotak)
print(list(kotak))
