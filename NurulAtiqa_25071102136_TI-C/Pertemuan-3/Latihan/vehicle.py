# buat class bernama Vehicle, punya 3 atribut (jenis, merk, tahun_rilis)
# class Vechicle punya method sound() (mengembalikan string suara)
# buat 2 class anak yang mewarisi class induk (yang penting kendaraan), ada 1 atribut private wajib
# buat dan panggil 3 objek dalam program yaitu objek dari kelas vehicle dam masing masing satu objek dari kedua class turunan
# salah satu pada class anak pake getter atau setter


class Vehicle:
    def __init__(self, jenis, merk, tahun_rilis):
        self.jenis = jenis
        self.merk = merk
        self.tahun_rilis = tahun_rilis
    def sound(self):
        return "biipp biippp biipppp"
    
class Bus(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis, kapasitas_penumpang):
        super().__init__(jenis, merk, tahun_rilis)
        self.__kapasitas_penumpang = kapasitas_penumpang
    def get_kapasitas_penumpang(self):
        return self.__kapasitas_penumpang
    
class Motor(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis, hargajual):
        super().__init__(jenis, merk, tahun_rilis)
        self.__hargajual = hargajual
    def set_hargajual(self):
        return self.__hargajual
    
p1 = Vehicle("Mobil", "Toyota", 2020)
print(p1.jenis, p1.merk, p1.tahun_rilis)
print(p1.sound())

p2 = Bus("Bus", "Mercedes", 2018, 50)
print(p2.jenis, p2.merk, p2.tahun_rilis)
print("Kapasitas penumpang pada bus ini adalah: ", p2.get_kapasitas_penumpang())

p3 = Motor("Motor", "Yamaha", 2021, 15000000)
print(p3.jenis, p3.merk, p3.tahun_rilis)
print("Harga jual motor ini adalah: Rp", p3.set_hargajual())