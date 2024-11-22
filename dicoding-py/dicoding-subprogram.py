# fungsi

# user defined functions
def mencari_luas_persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang


persegi_panjang_pertama = mencari_luas_persegi_panjang(5, 10)
print(persegi_panjang_pertama)

persegi_panjang_kedua = mencari_luas_persegi_panjang(4, 15)
print(persegi_panjang_kedua)

# fungsi terdiri dari header, body, dan return


def mencari_luas_persegi_panjang(panjang, lebar):  # header
    luas_persegi_panjang = panjang*lebar  # body
    return luas_persegi_panjang  # return


persegi_panjang_pertama = mencari_luas_persegi_panjang(5, 10)
print(persegi_panjang_pertama)


def mencari_luas_persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang


persegi_panjang_pertama = mencari_luas_persegi_panjang(
    lebar=10, panjang=5)  # keyword argument

print(persegi_panjang_pertama)

# parameter

# positional or keyword


def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan


print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))

# positional only


def penjumlahan(a, b, /):
    return a + b


print(penjumlahan(8, 50))

# keyword only


def greeting(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan


print(greeting(pesan="Selamat sore!", nama="Dicoding"))

# Var-Positional (Variadic Positional Parameter)


def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total


print(hitung_total(1, 2, 3))

# Var-Keyword (Variadic Keyword Parameter)


def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info


print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))

# fungsi anonim (lambda expression)


def mencari_luas_persegi_panjang(panjang, lebar): return panjang*lebar


print(mencari_luas_persegi_panjang(5, 10))

# variabel global dan lokal

# variabel global
a = 10


def add(b):
    result = a+b
    return result


bilanganPertama = add(20)
print(bilanganPertama)

# variabel lokal


def add(a, b):
    lokal_var = 5
    result = a+b-lokal_var
    return result


bilanganPertama = add(10, 20)
print(bilanganPertama)

# modul

# import hello (nama file)

# persegi_panjang_pertama = hello.mencari_luas_persegi_panjang(5,10)
# print(persegi_panjang_pertama)

# from hello import mencari_luas_persegi_panjang, nama

# persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
# print(persegi_panjang_pertama)

# print(nama)

# kuis
# Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
# - Menerima dua buah argumen berupa number, yaitu a dan b.
# - Mengembalikan nilai terkecil antara a atau b.
# - Bila nilai keduanya sama, kembalikan dengan nilai a.


def minimal(a, b):
    if a <= b:
        return a
    else:
        return b


print(minimal(4, 3))

# prosedur


def greeting(name):
    print("Halo " + name + ", Selamat Datang!")


greeting("Dicoding Indonesia")
