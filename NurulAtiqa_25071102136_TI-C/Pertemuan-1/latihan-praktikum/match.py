# match mirip dengan switch case pada bahasa C
# digunakan untuk banyak kemungkinan kondisi (mirip if else namun lebih ringkas)
hari = 3
match hari:
    case 1:
        print("Senin")
    case 2:
        print("Selasa")
    case 3:
        print("Rabu")
    case 4:
        print("Kamis")
    case 5:
        print("Jumat")
    case 6:
        print("Sabtu")
    case 7:
        print("Minggu")
    case _: # default case jika tidak memenuhi case di atas, pakai _
        print("Hari tidak valid")