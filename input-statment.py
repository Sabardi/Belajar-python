

name = input("Enter your name: ")
print("Hello, " + name + "!")



# 1. Input Bilangan Bulat
age = int(input("Enter your age: "))
print("You are " ,age,  " years old.")
# Karena input() selalu mengembalikan string, jika Anda ingin mengambil input angka, Anda harus mengonversinya ke tipe data yang sesuai, seperti int atau float.

# 2. Mengambil Input Bilangan Pecahan
height = float(input("Enter your height in meters: "))
print("Your height is " , height , " meters.")

# 3. Mengambil Beberapa Input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Your full name is " + first_name + " " + last_name + ".")

# Menggunakan split() untuk Mengambil Beberapa Input Sekaligus
data = input("Enter your age and height separated by a space: ")
age, height = data.split()
age = int(age)
height = float(height)
print("You are " + str(age) + " years old and " + str(height) + " meters tall.")

# Input dengan Validasi

while True:
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        break
    else:
        print("Invalid input. Please enter a number.")

print("You are " + str(age) + " years old.")
