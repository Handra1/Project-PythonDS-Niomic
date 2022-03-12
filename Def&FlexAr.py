"""hanya bisa 2 argumen"""
def power(nomor, pow=1):
    nilai_baru = nomor ** pow
    return nilai_baru

print(power(9,2))
print(power(9))

"""bisa dari 1 maupun lebih banyak argumen"""
def add_all(*args):
    sum_all = 0
    for num in args:
        sum_all += num
    return sum_all

print(add_all(1))
print(add_all(3,3))

"""jika ingin mengubah simbol perhitungan matematikanya maka (hanya bisa perkalian)"""
def add_all(*args):
    sum_all = 1
    for num in args:
        sum_all *= num
    return sum_all

print(add_all(2,50))
