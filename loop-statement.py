# Menggunakan range()
for i in range(1,6):
    print(i)

y = 1
while y <= 5:
    print(y)
    y += 1

name = ["alice", "bob","fred"]

for names in name:
    print(name)

numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        print(num, "adalah angka genap")
    else:
        print(num, "adalah angka ganjil")

# Menggunakan List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Menggunakan String
message = "Hello"
for char in message:
    print(char)

# perulangan sederhana
count = 0
while count < 5:
    print(count)
    count += 1

# penggunaan break and continue
for i in range(10):
    if i == 5:
        break
    print(i)
# Penjelasan: Loop ini akan berhenti ketika i bernilai 5, jadi hanya mencetak angka 0 hingga 4.

# Digunakan untuk melewati iterasi saat ini dan melanjutkan ke iterasi berikutnya.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Loop Bersarang
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
# Loop luar akan berjalan 3 kali, dan untuk setiap iterasi loop luar, loop dalam akan berjalan 2 kali.

# menggunakan else dengan loop 
for i in range(5):
    print(i)
else:
    print("Loop selesai")

# menggunakan while dengan loop 
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop selesai")


#  Menghitung Jumlah Elemen dalam List
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print("Total:", total)

# Mencari Angka Prima
for num in range(2, 20):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "adalah angka prima")
# Loop ini mengecek setiap angka dari 2 hingga 19 dan mencetak angka-angka yang merupakan angka prima.
