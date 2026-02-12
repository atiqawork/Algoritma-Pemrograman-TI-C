# while loops digunakan untuk melakukan perulangan yang kondisi nya belum diketahui pasti
# selama kondisi bernilai true, maaka perulangan akan terus dilakukan
# jika kondisi bernilai false, maka perulangan akan berhenti

i = 3
while i < 10: # selama i kurang dari 10, maka perulangan akan terus dilakukan
    print("nilai i adalah:", i) 
    i += 1  # i = i + 1, setiap perulangan nilai i akan bertambah 1

# contoh lain
a = 1
while a < 10: # selama a kurang dari 10, maka perulangan akan terus dilakukan
    print("nilai a adalah:", a)
    if a == 5:
        break  # hentikan perulangan jika a sama dengan 5
    a += 2  # a = a + 2, setiap perulangan nilai a akan bertambah 2

# contoh lain dengan continue
b = 0  
while b < 10: # selama b kurang dari 10, maka perulangan akan terus dilakukan
    b += 1  # b = b + 1, setiap perulangan nilai b akan bertambah 1
    if b % 2 == 0:  # jika b modulus 2 = 0 => b adalah bilangan genap
        continue  # lewati perulangan ini dan lanjut ke perulangan berikutnya
    print("nilai b adalah:", b)  # hanya bilangan ganjil yang akan dicetak