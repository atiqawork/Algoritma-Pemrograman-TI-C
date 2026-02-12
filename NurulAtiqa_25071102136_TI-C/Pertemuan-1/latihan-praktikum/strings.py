# python strings
print('haii')
# sama dengan
print("hola hola")
# penggunaan single quote dan double quote sama saja dalam python
# pengguanaan triple quote untuk string yang panjang
print('''hari ini hari yang cerah, 
tidak mendung sama sekali,
matahari bersinar terang ''')

# slicing string => mengambil sebagian karakter dari string
a = "sayur"
print(a[1:4]) # diambil dari index ke 1 sampai index ke 3 (index ke 4 tidak diambil); output: ayu
# format umum slicing: string[start:end:step]
b = "memasak"
print(b[2:]) # output: masak (diambil dari index ke 2 sampai akhir), : setelah format slicing berarti sampai akhir
print(b[:4]) # output: mema (diambil dari awal sampai index ke 3), : sebelum format slicing berarti dari awal
print(b[::2]) # output: mmsk (diambil dari awal sampai akhir, dua : berarti stepnya 2)
print(b[::-1]) # output: kasamem (diambil dari belakang sampai depan, step -1 berarti dibalik) 

# modify string => mengubah string (bisa bentuknya upper atau lowercase, bisa juga isinya)
c = ("hari jumat")
print(c.upper()) # output: HARI JUMAT (c merujuk ke variabel string hari jumat, lalu diubah menjadi uppercase)
print(c.lower()) # output: hari jumat (c merujuk ke variabel string hari jumat, lalu diubah menjadi lowercase)
print(c.replace("jumat", "senin")) # output: hari senin (kata jumat diganti dengan senin)
print(c.split()) # output: ['hari', 'jumat'] (memisahkan string berdasarkan spasi, hasilnya berupa list)

# string concatenation => menggabungkan 2 atau lebih string menjadi 1 string
d = "selamat "
e = "pagi "
print(d + e + "semua") # output: selamat pagi semua (menggabungkan string d, e, dan string "semua")

# format string => menyisipkan variabel ke dalam string dengan menambahkan f sebelum tanda kutip pembuka
nama = "atiqa"
umur = 18
print(f"nama saya {nama}, umur saya {umur} tahun") # output: nama saya atiqa, umur saya 18 tahun

# escape character => karakter khusus yang diawali dengan backslash (\)
 # biasanya digunakan untuk menampilkan karakter khusus dalam string atau untuk mengatur format tampilan string
print("halo\tsemua") # output: halo	semua (menyisipkan tab di antara kata halo dan semua), \t = tab
print("selamat\npagi") # output: selamat pagi dengan baris baru tiap kata nya. \n = newline
print("kata anni, tulisan namanya bukan \"annie\" tapi anni") # \" \" = menampilkan tanda kutip ganda di dalam string"

# string methods => fungsi bawaan yang dimiliki string untuk memanipulasi atau mengubah string
f = " bahasa pemrograman "
print(f.lstrip()) # output: "bahasa pemrograman " (menghapus spasi di sebelah kiri string)
g = "bahasa pemrograman"
print(g.capitalize()) # output: "Bahasa pemrograman" (mengubah huruf pertama string menjadi kapital)