print(float(2))
print(float("2.3"))


def kotak(x):
    return x ** (0.5)

print(kotak(4))

def kotak(x):
    try:
        return x ** 0.5
    except :
        print("X harus INTERGER atau FLOAT")

print(kotak(4))
print(kotak(10.0))
print(kotak("Hai"))
"""ada banyak jenis error yang ada yang telah didokumentasikan di https://docs.python.org/3/tutorial/errors.html"""
