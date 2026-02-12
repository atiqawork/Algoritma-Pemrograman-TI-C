# 1. penambahan
def penambahan(a, b):
    return a + b
hasil = penambahan(15, 3)
print("Hasil 2 penambahan adalah ", hasil)

# 2. pengurangan
def pengurangan(a, b):
    return a - b
total = pengurangan(15, 3)
print("Total dari 2 pengurangan adalah ", total)

# 3. perkalian
def perkalian(a, b):
    return a * b
hasil_akhir = perkalian(15, 3)
print("Hasil perkalian 2 bilangan adalah ", hasil_akhir)

# 4. pembagian
def pembagian(a, b):
    if b == 0:
        print("Pembagian tidak dapat dilakukan karena pembagi = 0")
    else:
        return a / b
total_bagi = pembagian(15, 0)
print("Hasil pembagian 2 bilangan adalah ", total_bagi)
    # contoh lain jika pembagi != 0

# 5. modulus
def modulus(m, n):
    return m % n
hasil_mod = modulus(17, 2)
print("Sisa bagi dari 2 bilangan adalah ", hasil_mod)

# 6.fibonacci(n)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))