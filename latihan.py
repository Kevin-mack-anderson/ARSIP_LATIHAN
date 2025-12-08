# KALKULATOR SEDERHANA
def penghitungan (pertama,kedua,pilihan):
    if pilihan == "*":
        hasil = pertama * kedua
    elif pilihan == "/":
        hasil = pertama / kedua
    elif pilihan == "+":
        hasil = pertama + kedua
    elif pilihan == "-":
        hasil == pertama - kedua
    else:
        print('Jenis Operasi Tidak Valid ! [*,/,+,-]')
    print(hasil)
# Bagian Input
pil_1 = int(input('Masukan Angka Pertama : '))
pil_2 = int(input('Masukan Angka Kedua : ' ))
jenis_op = input('Masukan Jenis Operasi : ')
# Pemanggilan
penghitungan(pil_1,pil_2,jenis_op)

# SOAL CEK BILANGAN
def cek_angka():
  """Loop"""
  while True:
    try:
      angka = int(input("Masukan Angka Anda (Masukan Angka 0 Untuk Berhenti): "))
      if angka == 0:
        print("Program Berhenti")
        break
      elif angka % 2 == 0: print("Genap")
      else: print("Ganjil")
    except ValueError:
      print("Yang anda masukan bukan sebuah angka")
cek_angka()

# SOAL NILAI MAX MIN LIST
