def kotak(nilai):
    nilai_baru = nilai ** 2
    return nilai_baru
"""sebuah "local scope" yang hanay bisa diakses oleh kotak"""
print(kotak(4))

"""global scope, cth"""
nilai_baru = 10
def kotak(nilai):
    nilai_baru = nilai ** 2
    return nilai_baru

print(kotak(5))
"""dikarenakan yang diambil tetap dalam local scope"""
"""kecuali"""
nilai_baru = 10
def kotak(nilai):
    nilai_baru2 = nilai_baru ** 2
    return nilai_baru2

print(kotak(3))
"""dikarenakan global scope telah didefinisikan dalam sebuah local scope sehingga diambil valuenya"""
