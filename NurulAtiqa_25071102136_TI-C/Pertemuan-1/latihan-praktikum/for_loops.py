# for loops digunakan jika jumlah perulangan sudah jelas atau diketahui
# juga digunakan untuk pengulangan pada tipe data seperti string, list, tuple, dictionary, set (loop data)

warna = ["merah", "kuning", "hijau"] # tipe data list, pake []
for i in warna:
    print(i) # output: merah, kuning, hijau (new line)

# contoh lain dengan range()
for j in range(5): # range(5) artinya dari 0 sampai 4 (5 tidak termasuk, karena indeks mulai dari 0)
    print("nilai j adalah:", j) # output: nilai j adalah: 0 ... 4 (new line)
    # contoh lain range dengan start, stop, step
for k in range(2, 10, 2): # dari 2 sampai 9, dengan step 2 (+ 2)
    print("nilai k adalah:", k) # output: nilai k adalah: 2, 4, 6, 8 (new line)