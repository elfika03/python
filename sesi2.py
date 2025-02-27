##
# Program untuk menentukan apakah sebuah bilangan yang diinput ganjil atau genap
#

# Membaca bilangan yang dimasukkan user
bil = int(input("Masukkan sebuah bilangan:"))

# Proses untuk menentukan bilangan tersebut ganjil atau genap
# Menggunakan operator modulus
if bil % 2 == 1:
  print(bil, "adalah bilangan ganjil")
else:
  print(bil, "adalah bilangan genap")

##
# Program untuk menentukan apakah huruf tersebut vokal atau konsonan
# Dalam Ejaan Bahasa Inggris

# Membaca huruf yang dimasukkan user
hur= input("Masukkan sebuah huruf dari kumpulan abjad:")

#Proses menentukan huruf dan menampilkan hasilnya
if hur =="a" or hur == "e" or \
   hur =="i" or hur == "o" or \
   hur =="u":
  print("Ini adalah vokal.")
elif hur =="y":
  print("Kadang vokal...kadang konsonan")
else:
  print("Ini adalah konsonan.")
     
 ##
# Menampilkan nama ukuran geometri berdasarkan jumlah sisi yang diinput
#

# Membaca jumlah sisi yang diinput oleh user
sisi = int(input("Masukkan jumlah sisinya:"))

# Menampilkan nama ukuran geometri tersebut
nama = ""
if sisi == 3:
  nama = "triangle"
elif sisi == 4:
  nama = "quadrilateral"
elif sisi == 5:
  nama = "pentagon"
elif sisi == 6:
  nama = "hexagon"
elif sisi == 7:
  nama = "heptagon"
elif sisi == 8:
  nama = "ocatagon"
elif sisi == 9:
  nama = "nonagon"
elif sisi == 10:
  nama = "decagon"

# Menampilkan pesan kesalahan atau nama dari ruang geometri
if nama == "":
  print("Jumlah sisi yang diinput tidak ada dalam database")
else:
  print("Ini adalah", nama)

##
# Menentukan dan menampilkan nama musim berdasarkan tanggal
#

# Membaca tanggal yang diinput oleh user
bulan = input("masukkan nama bulan:")
tgl = int(input("masukkan tanggal dibulan tersebut:"))

# Proses menentukan nama musim
if bulan == "Januari" or bulan =="Februari":
  musim = "Winter"
elif bulan == "Maret":
  if tgl < 20:
    musim = "Winter"
  else:
    musim = "Spring"
elif bulan =="April" or bulan == "Mei":
  musim = "Spring"
elif bulan == "Juni":
  if tgl < 21:
    musim = "Spring"
  else:
    musim = "Summer"
elif bulan =="Juli" or bulan == "Agustus":
  musim = "Summer"
elif bulan == "September":
   if tgl < 22:
     musim = "Summer"
   else:
     musim = "Fall"
elif bulan =="Oktober" or bulan == "November":
  musim = "Fall"
elif bulan == "Desember":
    if tgl < 21:
      musim = "Fall"
    else:
      musim = "Winter"

# Tampilkan hasil
print(tgl, bulan, "adalah dalam musim", musim)

