import numpy as np
import array

x = array.array("i", [1, 2, 3, 4, 5])
print(x)
print(type(x))

# mendeklarasikan array
var_list = [1, 2, 3]
for elemen in var_list:
    print(id(elemen))

# mendeklarasikan array dengan list

# mendefinisikan isi array
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr)

# mendefinisikan nilai default
var_arr = [0 for i in range(10)]
print(var_arr)

var_arr = [0 for i in range(10)]

for i in range(10):
    var_arr[i] = i

print(var_arr)

# mengakses elemen array
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr[0])

# pemrosesan sekuensial array
var_arr = [1, 2, 3, 4, 5]

for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i+1

    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None

    print(f"Current element: {current_element}, next elements: {next_element}")

# mencari nilai terbesar di array
var_arr = [1, 7, 2, 89, 3]
left_pointer = var_arr[0]

for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)

# N baris dan M Kolom (NxM).

matriks = [[0 for j in range(4)] for i in range(3)]

print(matriks)

# akses elemen matriks
var_mat = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]

print(var_mat[2][1])

# operasi pada matriks

# Membuat matriks 2x2
var_mat = [[5, 0],
           [1, -2]]
def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_mat)):
    for j in range(len(var_mat[0])):
        def_mat[i][j] = var_mat[i][j]*2

print(def_mat)


var_mat = np.array([[5, 0],
                    [1, -2]])

result = var_mat * 2

print(result)
