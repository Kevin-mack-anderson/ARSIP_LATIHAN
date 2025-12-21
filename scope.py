# Ini scope global
angka = 10
def hitung(n):
    """Variable Angka Adalah Global"""
    hasil = angka + n
    print(hasil)
print(hitung(2))
# Ini scope lokal
def perkalian(x,y):
    """Variable Hasil Adalah Lokal"""
    hasil = x * y
print(perkalian(2,2))
"""Variable lokal terutama function,
tidak dapat diakses keluar tanpa penulisan Global"""
# Contoh
def pembagian(a,b):
    global hasil
    hasil = a / b
pembagian(10,2)
print(hasil)
"""Kemudian ada tahapan eksekusi kode python"""
def sebut_nama():
    print(f"Halo {nama}, selamat pagi")
nama = "cecep"
print(sebut_nama())
"""dari contoh diatas, apabila variable nama dituliskan
sebelum pemanggilan fungsi, maka nama akan tetap bisa dieksekusi.
Beda cerita apabila variable nama ditulis sesudah pemanggilan fungsi."""