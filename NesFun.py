"""ini tanpa menggunakan fungsi nested sehingga tidak efisien"""
def mod2plus5 (x1,x2,x3):
    new_x1 = x1 % 2 + 5
    new_x2 = x2 % 2 + 5
    new_x3 = x3 % 2 + 5
    return(new_x1, new_x2, new_x3)

print(mod2plus5(1,2,3))

"""ini menggunakan fungsi nested"""
def mod2plus5(x1,x2,x3):
    def inner(x):
        return x % 2 + 5
    return(inner(x1), inner(x2), inner(x3))

print(mod2plus5(1,2,3))
