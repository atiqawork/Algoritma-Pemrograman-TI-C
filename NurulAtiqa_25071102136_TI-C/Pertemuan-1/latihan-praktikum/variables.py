# python variables

x = "budi" # variabel dengan tipe data string
y = 5 # variabel dengan tipe data integer
print("nama dia", x, "umur", y, end=" tahun")

# variable names
    # penamaan variabel harus didahului huruf atau _
    # tidak boleh dimulai dengan angka
    # tidak boleh spasi
print("kursi_ku") # ini contoh penamaan variabel yang benar = kursi_ku

# assign multiple values

x, y, z = "sepatu", "sandal", "kaos kaki"
print(x, y, z)

# output variables
x = "awesome"
print("Python is " + x) # bisa dengan cara ini
print("Python is", x) # atau dengan cara ini

# global variables

x = "hujan" # ini merupakan variabel global yang dideklarasikan di luar fungsi dan digunakan juga di dalamnya
def myfunc():
    print("hari ini", x)
myfunc()

