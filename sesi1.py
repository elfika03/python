##
# Menampilkan alamat lengkap seseorang 
#
print("Elfika Citrifolia")
print("Department of Information Technology")
print("UIN Ar-Raniry")
print("Jalan Lingkar kampus UIN Ar-Raniry Banda Aceh, Tanjung Selamat, Darussalam ")
print("Banda Aceh")
print("Indonesia")

##
# Menghitung luas kamar
#

# Membaca angka yang dimasukkan oleh user
panjang = float(input("Masukkan ukuran panjang dalam satuan meter "))
lebar = float(input("Masukkan ukuran lebar dalam satuan meter "))

# Proses perhitungan luas
luas = panjang * lebar

# Tampilkan hasil
print("Luas dari kamar ini adalah", luas, "meter kuadrat")

##
# Menghitung jumlah dari bilangan positif pertama
#

# Membaca angka yang dimasukkan oleh user
n = int(input("Masukkan bilangan bulat positif:"))

# Proses Menghitung jumlah
sm = n * (n+1) / 2

# Tampilkan hasil
print("Jumlah pertama dari ", n, "bilangan positif adalah", sm)

## 
# Pengenalan operator matematika pada Python dan modul math
#

from math import log10

# Membaca input dari user
x = int (input("Masukkan bilangan dari x:"))
y = int (input("Masukkan bilangan dari y:"))

# Menghitung dan menampilkan operator matematika
print(x, "+", y, "adalah", x + y)
print(x, "-", y, "adalah", x - y)
print(x, "*", y, "adalah", x * y)
print(x, "/", y, "adalah", x / y)
print(x, "%", y, "adalah", x % y)

# Menghitung logaritma dan pangkat
print("Logaritma basis 10 dari", x, "adalah", log10(x))
print(x, "^", y, "adalah", x**y)

     