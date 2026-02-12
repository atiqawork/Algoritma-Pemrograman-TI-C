# menggunakan kondisi logika dari matematika, ==, !=, <, <=,>, >=
a = 10
b = 5
if a > b:
    print("a lebih besar dari b")

## contoh lain
tinggi = 170
if tinggi >= 170:
    print("kamu tinggi")
    print("kamu cukup minum susu")
    print("gizi mu bagus")
 
 # python elif
umur = 66
if umur < 13:
    print("kamu tuh anak-anak")
elif umur >= 13 and umur < 20:
    print("kamu masih remaja, enjoy aja")
elif umur >= 20 and umur < 65:
    print("kamu udah dewasa, kerja yang bener ya")
elif umur >= 65:
    print("kamu udah lansia, jaga kesehatan dan selamat nikmatin duit pensiunan ><")

# python else
height = 170
if height >= 170:
    print("kamu tinggi")
else:
    print("kamu pendek")

#shorthand if
## dilakukan jika hanya ada satu statement untuk dieksekusi, letak on the same line as the if statement
a = 10  
b = 5
if a > b: print("a lebih besar dari b")

# logical operators
## menggunakan and, or, not
a = 10
b = 5   
if a > 5 and b < 10:
    print("kondisi benar semua")
elif a > 5 or b > 10:
    print("salah satu kondisi benar")
elif not a < 5:
    print("a tidak kurang dari 5")

# nested if, kondisi if di dalam kondisi if lainnya
nilai = 75
if nilai >= 60:
    print("kamu lulus") # asal nilai di atas 60
    if nilai >= 85:
        print("dengan predikat sangat baik") # di atas 60 dan di atas 85 berarti lulus dengan predikat sangat baik
    elif nilai >= 75:
        print("dengan predikat baik") # di atas 60 dan di atas 75 berarti lulus dengan predikat baik
    else:
        print("dengan predikat cukup")  # di atas 60 tapi di bawah 75 berarti lulus dengan predikat cukup

# pass statements
# jika kita memiliki blok if kosong, kita bisa menggunakan pass statements agar tidak error
lahir = 2012
if lahir >= 2007:
    print("kamu diizinkan memiliki ktp")
else:
    pass   # program tidak melakukan apa apa dan tidak akan error
