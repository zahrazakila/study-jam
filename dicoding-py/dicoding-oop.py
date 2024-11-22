# class object atribut
class Mobil:
    # Atribut
    warna = "Merah"


mobil_1 = Mobil()  # object
print(mobil_1.warna)

# merubah atribut


class Mobil:
    # Atribut
    warna = 'Merah'


mobil_1 = Mobil()
mobil_1.warna = "Biru"
print(mobil_1.warna)

# atribut kelas


class Mobil:
    # Atribut kelas
    warna = "Merah"


mobil1 = Mobil()
print(mobil1.warna)

mobil2 = Mobil()
print(mobil2.warna)

# Mengubah atribut kelas
Mobil.warna = "Hitam"

print(mobil1.warna)
print(mobil2.warna)

# atribut instance/objek
# membutuhkan class constructor


class Mobil:
    # Atribut Instance
    def __init__(self):
        self.warna = 'Merah'  # constructor


mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)

# Mengubah atribut instance
mobil_1.warna = "Hitam"

# Menampilkan kembali atribut warna
print(mobil_1.warna)
print(mobil_2.warna)


# class constructor
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan


mobil_1 = Mobil('Merah', 'DicodingCar', 160)  # memerlukan argumen

print(mobil_1.warna)
print(mobil_1.merek)
print(mobil_1.kecepatan)

# method


def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper

# Dekorasi fungsi dengan decorator


@my_decorator
def say_hello():
    print("Hello, world!")


# Memanggil fungsi yang sudah didekorasi
say_hello()


# object method
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10


mobil_1 = Mobil("Merah", "DicodingCar", 160)
print("Sebelum ditambahkan: ")
print(mobil_1.kecepatan)

mobil_1.tambah_kecepatan()        # Memanggil metode tambah_kecepatan.

print("Setelah ditambahkan: ")
print(mobil_1.kecepatan)

# static method


class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")


Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()

# class method


class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(cls):
        print("Ini adalah metode dari kelas Mobil")


Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()


class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(cls):
        print("Ini adalah metode dari kelas Mobil")


Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()

# inheritance/pewarisan


class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50


# Kelas Mobil Dasar
mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)

# override


class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 20


# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)
# Kelas Mobil Dasar
mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)
mobil_1.tambah_kecepatan()
print(mobil_1.kecepatan)

# super


class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("Kecepatan Anda meningkat! Hati-Hati!")


# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)


# """
# TODO:
# 1. Buatlah class bernama Animal dengan ketentuan:
#     - Memiliki properti:
#       - name: string
#       - age: int
#       - species: string
#     - Memiliki constructor untuk menginisialisasi properti:
#       - name
#       - age
#       - species
# 2. Buatlah class bernama Cat dengan ketentuan:
#     - Merupakan turunan dari class Animal
#     - Memiliki method:
#       - bernama "deskripsi" yang mengembalikan nilai string berikut ini.
#         "{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
#       - bernama "suara" yang akan mengembalikan nilai string "meow!"
#  3. Buatlah instance dari kelas Cat bernama "myCat" dengan ketentuan:
#     - Atribut name bernilai: "Neko"
#     - Atribut age bernilai: 3
#     - Atribut species bernilai: "Persian".
# """
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species


class Cat(Animal):
    #   def deskripsi(self):
    #   	return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
    def suara(self):
        return "meow!"


myCat = Cat("Neko", 3, "Persian")
print(myCat.deskripsi())
print(myCat.suara())
