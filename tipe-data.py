# Tipe Data Dasar
# Integer (int)
x = 10
y = -5

# Float (float):
pi = 3.14
g = 9.81

# String (str):
greeting = "Hello"
language = 'Python'

print(x+y)

print("Tipe Data Koleksi")

# boolean
benar = True
salah = False

#list
daftar_nama_buah = ['apel', 'mangga', 'jeruk']
daftar_nama_buah[2] = 'bengkoang' #isi nya yg indek kedua yaitu jeruk akan di ganti menjadi bengkoang
print(daftar_nama_buah)

#tuple
daftar_nama_buah = ('apel', 'mangga', 'jeruk')
print(daftar_nama_buah)

#dictinorery
# dictinorery adalah tipe data yang digunakan untuk menyimpan nilai berdasarkan key dan value

benda = {"buah" :"apel", "sepatu":"adidas"}
benda["sepatu"] = "nike" # merubah nilai nya
print(benda)

# Set (set):
unique_numbers = {1, 2, 3, 4}
print(unique_numbers)

# Operasi Dasar pada set

# 1.  Menambahkan Elemen
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
# Output: {'apple', 'banana', 'cherry', 'orange'}

#  2. Menghapus Elemen
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)
# Output: {'apple', 'cherry'}

fruits.discard("cherry")
print(fruits)
# Output: {'apple'}
# Perbedaan antara remove() dan discard() adalah remove() akan menghasilkan error jika elemen yang akan dihapus tidak ada dalam set, sedangkan discard() tidak.

# 3. Menggabungkan set
# Anda bisa menggabungkan dua set menggunakan operasi union() atau operator |.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print('menggunakan union')
# Menggunakan union()
combined_set = set1.union(set2)
print(combined_set)
# Output: {1, 2, 3, 4, 5}

# Menggunakan operator |
combined_set = set1 | set2
print(combined_set)
# Output: {1, 2, 3, 4, 5}

#  4.Irisan set
print('4.Irisan set')
# Anda bisa menemukan irisan dari dua set (elemen yang ada di kedua set) menggunakan metode intersection() atau operator &.
set1 = {1, 4, 3}
set2 = {3, 4, 5,1}

# Menggunakan intersection()
common_elements = set1.intersection(set2)
print(common_elements)
# Output: {3}

# Menggunakan operator &
common_elements = set1 & set2
print(common_elements)
# Output: {3}

# 5. Selisih set
# Anda bisa menemukan selisih dari dua set (elemen yang ada di set pertama tetapi tidak di set kedua) menggunakan metode difference() atau operator -.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Menggunakan difference()
difference_set = set1.difference(set2)
print(difference_set)
# Output: {1, 2}

# Menggunakan operator -
difference_set = set1 - set2
print(difference_set)
# Output: {1, 2}

#  Symmetric Difference
# Anda bisa menemukan elemen yang ada di salah satu dari dua set, tetapi tidak di keduanya, menggunakan metode symmetric_difference() atau operator ^.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Menggunakan symmetric_difference()
sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)
# Output: {1, 2, 4, 5}

# Menggunakan operator ^
sym_diff_set = set1 ^ set2
print(sym_diff_set)
# Output: {1, 2, 4, 5}

# Penggunaan Lain dari set
print("Penggunaan Lain dari set")
# 1. Menghilangkan Duplikat dari List
print("1. Menghilangkan Duplikat dari List")
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)
# Output: {1, 2, 3, 4, 5}

print("2. Mengecek Keanggotaan")
# 2. Mengecek Keanggotaan
# Anda bisa mengecek apakah sebuah elemen ada dalam set menggunakan operator in.
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)  # Output: True
print("orange" in fruits)  # Output: False


print("3. Menemukan Elemen yang Unik di Dua List")
# 3. Menemukan Elemen yang Unik di Dua List
# Menggunakan operasi set, Anda bisa menemukan elemen yang hanya ada di salah satu dari dua list.
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

unique_in_list1 = set(list1) - set(list2)
unique_in_list2 = set(list2) - set(list1)
unique_elements = unique_in_list1 | unique_in_list2
print(unique_elements)
# Output: {1, 2, 5, 6}

print("")
print("")
print("")
print("")
print("")
print("")




# Ringkasan
# Integer (int): Kotak untuk menyimpan bilangan bulat.
# Float (float): Botol untuk menyimpan bilangan pecahan.
# String (str): Kotak surat untuk menyimpan teks.
# Boolean (bool): Saklar lampu untuk menyimpan nilai benar atau salah.
# List (list): Kotak besar untuk menyimpan beberapa item.
# Tuple (tuple): Kotak dengan sekat tetap untuk menyimpan beberapa item.
# Dictionary (dict): Kamus untuk menyimpan pasangan kunci-nilai.
# Set (set): Kotak untuk menyimpan item unik.