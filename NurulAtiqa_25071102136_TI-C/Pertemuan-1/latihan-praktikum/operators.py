# python operators
print(7 + 7) # penjumlahan menggunkan operator +
print(7 - 7) # pengurangan menggunakan operator -
print(7 * 7) # perkalian menggunakan operator *
print(7 / 7) # pembagian menggunakan operator /

# arithmetic operators
a = 10
b = 5
print(a + b) # penjumlahan
print(a - b) # pengurangan  
print(a * b) # perkalian
print(a / b) # pembagian
print(a % b) # modulus (sisa bagi)  
print(a ** b) # eksponen (pangkat)
print(a // b) # floor division (pembulatan ke bawah)

# assignment operators
c = 7
print(c) # output: 7
c += 3 # c = c + 3
print(c) # output: 10
c -= 3 # c = c - 3
print(c) # output: 7 karena 10 - 3 = 7
c *= 2 # c = c * 2
print(c) # output: 14 karena 7 * 2 = 14
c /= 2 # c = c / 2  
print(c) # output: 7.0 karena 14 / 2 = 7.0

# comparison operators => operator perbandingan yang menghasilkan nilai boolean (True atau False)
x = 10
y = 5
print(x == y) # sama dengan, output: False
print(x != y) # tidak sama dengan, output: True

# logical operators => kombinasi beberapa kondisi yang menghasilkan nilai boolean (True atau False)
 # menggunakan and, ot, not
a = 5
b = 3
print(a > 2 and b < 4) # output: True (karena kedua kondisi benar)
print(a < 5 or b > 4) # output: False (karena kedua kondisi salah)
print(not(a > b)) # output: False (karena a > b adalah True, maka not True = False)

# identity operators => membandingkan apakah dua objek merujuk ke objek yang sama atau tidak
a = ["kaos kaki", "sepatu"]
b = ["kaos kaki", "sepatu"]
c = b
print(a is b) # output: False (karena a dan b adalah objek yang berbeda meskipun isinya sama)
print(b is c) # output: True (karena b dan c merujuk ke objek yang sama)
print(a is not c) # output: True (karena a dan c adalah objek yang berbeda)

# membership operators => mengecek apakah suatu nilai ada di dalam sebuah data/koleksi (seperti list, string, dll)
warna = ["merah", "biru", "hijau"]
print("merah" in warna) # output: True (karena "merah" ada di dalam list warna)
print("kuning" not in warna) # output: True (karena "kuning" tidak ada di dalam list warna)
print("jingga" in warna) # output: False (karena "jingga" tidak ada di dalam list warna)

# bitwise operators => operasi pada level bit (biner)
a = 5
b = 3
print(a & b) # AND bitwise, output: 1 (0101 & 0011 = 0001 => cuma ada 1 yang sama-sama 1)
print(a | b) # OR bitwise, output: 7 (0101 | 0011 = 0111 => hitung semua yang ada 1 dan dapat hasilnya 7)

# operators precedence => urutan prioritas operator dalam sebuah ekspresi
print(3 + 5 * 2) # output: 13 (perkalian dulu baru penjumlahan)