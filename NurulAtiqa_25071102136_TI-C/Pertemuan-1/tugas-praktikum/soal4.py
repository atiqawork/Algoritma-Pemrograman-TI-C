# program menggunakan perulangan for
# menampilkan bilangan dari 1 sampai 10
# menghitung dan menampilkan jumlah dari bilangan 1 sampai 10
jumlah = 0
for i in range(1, 11): # start = 1, end = 10 (sebelum 11)
    print(i)
    jumlah += i
    print("jumlah sementara: ", jumlah)
print("Jumlah total dari 1 sampai 10 adalah: ", jumlah)