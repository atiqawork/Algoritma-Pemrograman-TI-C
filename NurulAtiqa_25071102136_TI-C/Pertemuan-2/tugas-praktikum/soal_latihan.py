# 1. (Function dan Validasi Data) => rata_rata(nilai)
  # list berisi nilai mahasiswa, hitung rata-ratanya, jika list kosong print "Data Kosong"
  # kemudian panggil fungsi dengan list [80, 75, 90, 60, 85], tampilkan output
def rata_rata(nilai):
    if len(nilai) == 0:
        print("Data Kosong")
    return sum(nilai) / len(nilai)
    
data_nilai = [80, 75, 90, 60, 85]
hasil = rata_rata(data_nilai)
print("Rata rata nilai adalah: ", hasil)    

# 2. (Range dan Pola Bilangan) => bilangan_prima(n)
  # menggunakan range(), mengembalikan list bilangan prima dari 1 sampai n
  # kemudian panggil fungsi untuk n = 50, tampilkan output
def bilangan_prima(n):
    prima = []
    for bil in range(2, n + 1):
        is_prima = True
        for i in range(2, int(bil**0.5) + 1):
            if bil % i == 0:
                is_prima = False
                break
        if is_prima:
            prima.append(bil)
    return prima
n = 50
hasil_prima = bilangan_prima(n)
print("Bilangan prima dari 1 sampai ", n, "adalah ", hasil_prima)

# 3. (Rekursi - Penjumlahan Digit) => jumlah_digit(n)
  # menghitung jumlah seluruh digit dari sebuah bilangan menggunakan konsep rekursi
def jumlah_digit(n):
    if n == 0:
        return 0
    else:
        return n % 10 + jumlah_digit(n // 10)
n = 12345
hasil_hitung = jumlah_digit(n)
print("Jumlah digit dari ", n, "adalah ", hasil_hitung)

# 4. (Rekursi dan Deret) => pangkat_rekursif(a, b)
  # menghitung nilai a pangkat b, tidak boleh pakai operator pangkat (**), harus pake rekursi
def pangkat_rekursif(a, b):
    if b == 0:
        return 1
    else:
        return a * pangkat_rekursif(a, b-1)
a = 2
b = 5
hasil_pangkat = pangkat_rekursif(a, b)
print(a, " pangkat ", b, "adalah ", hasil_pangkat)

# 5. (Python Module dan ALgoritma)
  # menggunakan module math, buat fungsi jarak(x1, y1, x2, y2) untuk hitung jarak dua titik bidang kartesius
  # gunakan rumus jarak = sqrt((x2 - x1)^2 + (y2 - y1)^2)
import math
def jarak(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
x1, y1 = 1, 2
x2, y2 = 4, 6
hasil_jarak = jarak(x1, y1, x2, y2)
print("Jarak antara titik (", x1, y1,") dan titik (", x2, y2,") adalah ", hasil_jarak) 