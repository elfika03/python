# Deklarasi variabel stup1, stup2 dan stup3
stup1 = ('bahasa arab', 'bahasa aceh', 2019, 2020)
stup2 = (1, 2, 3, 4, 5, 6, 7, 8)
stup3 = "e", "f", "g", "h"

# Mengakses nilai pada variabel ketiga tupel diatas
print ("stup1[1]: ", stup1[1])
print ("stup2[1:5]: ", stup2[1:5])
     
# Deklarasi Variabel ach
ach = ("Mie Aceh", 10000, 3.5, True, 'AyamPramugari', 88j)

# Mengakses nilai tuple  
# Data pertama indeks 0
print("ach[0]:", ach[0])
# Data kedua indeks 1
print("ach[1]:", ach[1])
# Data ketiga indeks 2
print("ach[2]:", ach[2])
# Data antara indeks 2 dan 5
print("ach[2:5]:", ach[2:5])
# Data dari indeks satu sampai indeks 3
print("ach[:3]:", ach[:3])
# Data dari indeks 3 sampai dengan indeks seterusnya
print("ach[3:]:", ach[3:])
# Data keseluruhan
print("ach[:]:", ach[:])
     
# Contoh menambah variabel baru pada daftar tuple
stup1 = (10, 5.78)
stup2 = ('def', 'opq')

# Jika ditambah baris berikut:
# stup1[0] = 100;
# tidak bisa dilakukan pada tuple python

# Jadi, buatlah variabel tuple baru sebagai berikut
stup3 = stup1 + stup2
print (stup3)

del stup3 
print("setelah dihapus:")