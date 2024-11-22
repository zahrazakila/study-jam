
usia = "Perseus Evans"
print("Nama saya ", usia)

greeting = 'Hello World!'  # this is assignment
print(greeting)

addition = 2+2
result = addition - 1
print(result)

age = 17
salary = 5000000.0

print(type(age))
print(type(salary))

x = 6
print(type(x))

x = "6"
print(type(x))

x = 6.0
print(type(x))

x = 1+2j
print(type(x))

var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)

x = 'Dicoding'
print(x[0])

name = "Perseus Evans"  # formatted string
print(f"Hello, nama saya {name}")

name = "Perseus Evans"  # %-formatting
print("Nama saya %s" % (name))

name = "Perseus Evans"  # str.format()
print("Nama saya {}".format(name))


# data type

x = [1, 2.2, 'Dicoding']  # list
print(type(x))

x = [1, 2.2, 'Dicoding']  # list is muttable
x[0] = 'Indonesia'
print(x)

x = ["laptop", "monitor", "mouse", "mousepad",
     "keyboard", "webcam", "microphone"]  # indexing

print(x[0])
print(x[2])
print(x[-1])
print(x[-3])

x = ["laptop", "monitor", "mouse", "mousepad",
     "keyboard", "webcam", "microphone"]  # slicing

print(x[0:5:2])
print(x[1:])
print(x[:3])

x = (1, "Dicoding", 1+3j)  # tuple
print(type(x))

x = {1, 2, 7, 2, 3, 13, 3}  # set
print(x)

set1 = {1, 2, 3, 4, 5}  # set math operation
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)

x = {'name': 'Perseus Evans', 'age': 20, 'isMarried': False}  # dictionary
print(type(x))

x = {'name': 'Perseus Evans', 'age': 20, 'isMarried': False}
print(x['name'])

x = {'name': 'Perseus Evans', 'age': 20, 'isMarried': False}
x['Job'] = "Web Developer"
print(x)

x = {'name': 'Perseus Evans', 'age': 20, 'isMarried': False}
del x['isMarried']
print(x)

print(dict([[1, 2], [3, 4]]))  # list to dictionary

print(float(5))  # int to float

# Transformasi Angka, Karakter, dan String

kata = 'dicoding'
kata = kata.upper()
print(kata)

kata = 'DICODING'
kata = kata.lower()
print(kata)

print("Dicoding          ".rstrip())

print("           Dicoding".lstrip())

print("         Dicoding          ".strip())

kata = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code"))

print('Dicoding Indonesia'.startswith('Dicoding'))

print('Dicoding Indonesia'.endswith('Dicoding'))

print(' '.join(['Dicoding', 'Indonesia', '!']))

print('Dicoding Indonesia !'.split())

print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))  # newline

# mengganti elemen string

string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))

# pengecekan string

kata = 'DICODING'
print(kata.isupper())

kata = 'dicoding'
print(kata.islower())

kata = 'dicoding'
print(kata.isalpha())

kata = 'dicoding123'
print(kata.isalnum())  # alfanumerik, hanya angka, hanya huruf, atau keduanya

print('123'.isdecimal())

print('         '.isspace())

print('Dicoding Indonesia'.istitle())

teks = 'Code'
tambah_number = teks.zfill(7)
print(tambah_number)

print('Dicoding'.rjust(20))

print('Dicoding'.ljust(20))

print('Dicoding'.center(10, '-'))

print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu \t hari \\ Jum\'at yang lalu.")

print(r'Dicoding\tIndonesia')  # rawstring (akan dicetak sesuai teks string)

# operasi pada list, set, string

contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]

print(contoh_list)
print(len(contoh_list))  # menghitung panjang list

contoh_list = set([1, 3, 3, 5, 5, 5, 7, 7, 9])  # mengubah ke set

print(contoh_list)
print(len(contoh_list))

angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]  # min max suatu list
print(min(angka))
print(max(angka))

genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]  # menghitung jumlah objek
print(genap.count(6))

kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

data = ['shirt', 'white', 'L']  # memberikan nilai uintuk multiple variable
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)

kendaraan = ['motor', 'mobil', 'helikopter',
             'pesawat']  # mengurutkan angka atau huruf
kendaraan.sort()

print(kendaraan)

kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)

kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort(key=str.lower)

print(kendaraan)
