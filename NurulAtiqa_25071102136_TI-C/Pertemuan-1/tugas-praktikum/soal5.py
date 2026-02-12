# fungsi hitung(a,b) yang:
# menerima dua parameter a dan b
# mengembalikan hasil penjumlahan a + b
# mengembalikan hasil pergurangan a - b
# yang kemudian fungsi tersebut dipanggil dan menampilkan hasil penjumlahan dan pengurangan as an output
def hitung(a,b):
    penjumlahan = a + b
    pengurangan = a - b
    return penjumlahan, pengurangan
hasil_tambah, hasil_kurang = hitung(15, 5) # memanggil fungsi hitung dengan 15 sebagai a dan 5 sebagai b
print("Hasil penjumlahan 15 + 5 adalah ", hasil_tambah)
print("Hasil pengurangan 15 - 5 adalah ", hasil_kurang)