x = "Belajar"
y = "Python"
result = x > y
print(result)

for i in range(10):
    print(i)

# control flow

score = 100

if score == 100:
    print("Nilai Anda sempurna!")

nilai = 65

if nilai >= 80:
    print("Selamat! Anda mendapat nilai A")
    print("Pertahankan!")
elif nilai >= 70:
    print("Hore! Anda mendapat nilai B")
    print("Tingkatkan!")
elif nilai >= 60:
    print("Hmm.. Anda mendapat nilai C")
    print("Ayo semangat!")
else:
    print("Waduh, Anda mendapat nilai D")
    print("Yuk belajar lebih giat lagi!")

nilai = 81
perilaku = 'tidak baik'

if nilai >= 80 and perilaku == 'baik':
    print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
    print("Pertahankan!")
elif nilai >= 80 and perilaku != 'baik':
    print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
    print("Perbaiki lagi ya!")
else:
    print("Yuk belajar lebih giat lagi!")

# ternary operator
lulus = False
print("selamat") if lulus else print("perbaiki")

lulus = True
kelulusan = ("Perbaiki, Anda belum lulus.", "Selamat, Anda lulus!")[lulus]
print(kelulusan)

for i in range(1, 10, 2):  # start stop step
    print(i)

counter = 1
while counter <= 5:
    print(counter)
    counter += 1    # Increment harus ada dlm looping

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# kontrol perulangan

# break
for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1

for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))


# continue
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

# else setelah for
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")

# else setelah while
count = 0

while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")

n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")

# pass
x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")

# list comprehension

angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
    pangkat.append(n**2)
print(pangkat)

angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

# tugas
evenNumber = []
for i in range(0, 501, 2):
    evenNumber.append(i)
print(evenNumber)

# raise exception
var = -1
if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan")
else:
    for i in range(var):
        print(i+1)
