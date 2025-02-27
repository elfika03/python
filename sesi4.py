# Deklarasi fungsi salam_olahraga
def salam_olahraga():
    # Mencetak ouput pada fungsi salam_olahraga
    print ("JANGAN LUPA OLAHRAGA HARI INI!")

# Memanggil fungsi salam_olahraga
salam_olahraga()  # memanggil fungsi salam_olahraga
salam_olahraga()  # fungsi salam_olahraga dipanggil lagi

# Program Fungsi dengan parameter 
# Fungsi untuk menyapa seseorang sesuai nama yang dimasukkan sebagai parameter 
def kenalan(nama): 
     print("Salam, " + nama + ". Apa kabar?") 

# pemanggilan fungsi 
kenalan('Hamzah') 

# Menghitung dan menampilkan nilai median dari inputan tiga angka
# Program ini dibuat dengan kata kunci def untuk membuat fungsi
# menghitung nilai median dari 3 nilai yang diinput

def median(a, b, c):
# Proses perhitungan median cara pertama dengan perbandingan
# Menggunakan kata kunci retun untuk mengembalikan nilai
# untuk masing-masing nilai, yaitu a, b dan c
  if a < b and b < c or a> b and b > c:
    return b
  if b < a and a < c or b > a and a > c:
    return a
  if c < a and b < c or c > a and b > c:
    return c

# Proses perhitungan median cara kedua
def median2(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)

# Menampilkan nilai inputan 3 angka
def utama():
  x = float(input("Masukkan nilai pertama:"))
  y = float(input("Masukkan nilai kedua:"))
  z = float(input("Masukkan nilai ketiga:"))

  print("Nilai median dengan cara pertama:", median(x, y, z))
  print("Nilai median dengan cara kedua:", median2(x, y, z))

  # Memanggil fungsi utama()
utama()
     