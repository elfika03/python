# Deklarasi variabel contoh dan 10 itu sebagai tanda 10 kali perulangan
contoh = 10

# Variabel i berfungsi untuk menampung indeks, 
# dan fungsi range() berfungsi untuk membuat list dari 0-10.
for i in range(contoh):
    print ("Perulangan ke-" +str(i))
     

# Menampilkan range dari kumpulan deret tertentu
# range(5,10) akan membuat deret angka mulai dari 5, 6, 7, 8, dan 9.

for i in range(5,10):
  print(i)

# Deklarasi variabel contoh2 dengan tipe list
contoh2 = ['saya','suka','minum','kopi', 'gayo']

for isi in contoh2:
    print (isi)
     
# Deklarasi variabel hit
hit = 0
# Membuat kondisi
while (hit < 5):
    print(hit, "kurang dari 5")
    hit = hit + 1
else:
# Menampilkan output salam jika kondisi sudah terpenuhi
    print("Salammmm")
    
##
# Program menghitung Faktor Persekutuan Terbesa
#

# Membaca dua bilangan positif dari user
n = int(input("Masukkan bilangan positif:"))
m = int(input("Masukkan bilangan positif:"))

# Inisialisasi variabel untuk nilai terkecil dari n dan m
d = min(n, m)

# Gunakan loop while untuk mencari FPT
while n % d != 0 or m % d != 0:
  d = d - 1

# Menampilkan hasil
print("Faktor persekutuan terbesar dari", n, "dan", m, " adalah", d)

##
# Menentukan nilai maksimum 100 bilangan bulat, menghitung berapa kali 
# perulangan

from random import randrange

BIL_ITEMS = 100

# Generate the first number and menampilkan nya
maks_nilai = randrange(1, BIL_ITEMS + 1)
print(maks_nilai)

# Menghitung berapa kali perubahan
bil_update = 0

# Untuk setiap bilangan 
for i in range(1, BIL_ITEMS):
  # Generate bilangan acak
  current = randrange(1, BIL_ITEMS + 1)

  # Kondisi jika ditemukan bilangan terbesar
  if current > maks_nilai:
    # Update nilai maksimum dan hitung perubahan
    maks_nilai = current
    bil_update = bil_update + 1
    # Tampilkan bilangan jika masih ada proses update
    print(current, "<== Update")
  else:
    #Tampilkan bilangan
    print(current)
# Tampilkan Hasil Terakhir
print(" Nilai maksimum yang ditemukan adalah", maks_nilai)
print("Nilai maksimum yang di-update", bil_update, "kali")