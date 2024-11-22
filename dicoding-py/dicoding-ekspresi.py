# ekspresi uner

# Ekspresi biner merupakan jenis yang memiliki dua operan. Operatornya meliputi penjumlahan (+), pengurangan (-), perkalian (*), pembagian (/), perpangkatan (**), lebih kecil dari (<), lebih kecil dari sama dengan (<=), lebih besar dari (>), lebih besar dari sama dengan (>=), modulus (%),sama dengan (==), dan tidak sama dengan (!=).Namun, ekspresi uner adalah jenis ekspresi yang memiliki bentuk dasar operasi dengan satu operan. Contohnya adalah increment (x+=1), decrement (x-=1),dan negasi (not x)


a = True
a = not a
print(a)

b = 6
b -= 1
print(b)

c = 6
c += 1
print(c)

d = 10
print(-d)

print(2+2)  # ekspresi aritmatika
print(3 < 10)  # ekspresi relasional
print(True or False)  # ekspresi logika

# operator aritmatika
x = 11
y = 5

print(x + y)  # penjumlahan
print(x - y)  # pengurangan
print(x * y)  # perkalian
print(x // y)  # pembagian bulat
print(x / y)  # pembagian rill
print(x % y)  # modulo(sisa hasil pembagian)
print(x ** y)  # pangkat

# operator relasional

x = 5
y = 10

print(x == y)  # sama dengan
print(x != y)  # tidak sama dengan
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# operator logika
print(True and False)
print(False or True)
print(not True)

# operator assignment

# += menyederhanakan operasi x= x+y
x = 11
x += 5
print(x)

# -=
x = 11
x -= 5
print(x)

# *=
x = 11
x *= 5
print(x)

# /=
x = 11
x /= 5
print(x)

# %=
x = 11
x %= 5
print(x)
