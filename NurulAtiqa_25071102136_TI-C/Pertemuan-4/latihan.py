# try-except method 

# program menjalankan blok except karen blok try mengalami error
try:
    p = 3 / 0   # code cause an error; 3 tidak bisa dibagi 0
    print(p)
except:
    print("Blok 'try' mengalami error")     # executed the error in the try block
# program try except menggunakan else dan finally
try:
    print(x)    # code cause an error
except:
    print("Variabel tidak ditemukan")
else:
    print("Semua berjalan lancar")  # tidak ditampilkan ke layar karena try error
finally:
    print("Program berjalan")   # tetap berjalan
# program menggunakan user input
def floor_div(a, b):
    try:
        hasil = a // b
        print("Berhasil dieksekusi, hasil nya adalah: ", hasil)
    except:
        print("Terjadi kendala. Coba kembali")
floor_div(6, 3)     # code successfull
floor_div(7, "Hai")     # error di blok try, dieksekusi oleh except
# raise statement di luar try-except => mengalami error
# umur = -1
 #  if umur < 0:
    #   raise Exception("Nggak ada umur di bawah 0") 
# raise statement
try:
    umur = -1
    if umur < 0:
        raise Exception("Nggak ada umur di bawah 0")
except Exception as e:
    print("Error diketahui: ", e)
else:
    print("Program berjalan")