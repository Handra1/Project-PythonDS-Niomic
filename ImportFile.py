namafile = "lorem-ipsum.txt"
file = open(namafile, mode='r')
teks = file.read()
file.close()
print(teks)

with open('lorem-ipsum.txt', 'r') as file:
    print(file.read())
