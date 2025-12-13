# Membuat perhitungan luas persegi
import os 

os.system("cls")
# Menghitung Keliling Persegi Panjang
# Heading section
def heading():
    print(f"{'HALO SELAMAT DATANG USER' :^40}")
    print(f"{'SENANG BERTEMU LAGI' :^40}")
    print(f"{'=' * 40 :^40}")

# Inputan User
def input_user():
    panjang = int(input("Masukan Panjang : "))
    lebar = int(input("Masukan Lebar : "))
    return panjang,lebar
# Penghitungan Luas
def hitung_luas(lebar,panjang):
    return lebar * panjang 
# Penghitungan Keliling
def hitung_keliling(lebar,panjang):
    return 2 * (PANJANG + LEBAR)
# Display
def display(message,value):
    print(f"Hasil dari {message} = {value}")
# Output Keluaran
while True:
  heading()
#   Pilihan operasi
  pilihan = input("Mau Melakukan Apa? (luas/keliling) : ")
  LEBAR,PANJANG = input_user()
#   Flow Pilihan
  if pilihan == "luas":
     LUAS = hitung_luas(LEBAR,PANJANG)
     display("Luas",LUAS )
  elif pilihan == "keliling":
      KELILING = hitung_keliling(LEBAR,PANJANG) 
      display("Keliling",KELILING )
  else: print("tidak ada")
  LUAS = hitung_luas(LEBAR,PANJANG)
  KELILING = hitung_keliling(LEBAR,PANJANG)
  display("Luas",LUAS )
  display("Keliling",KELILING )
  Main Program
  in_continue = input("Apakah Mau Lagi?(y/n) :  ").lower()
  if in_continue == "n":
     print("terimakasih banyak") 
     break



# JUALAN BAN MOTOR
# Implementasi kedalam function
# Heading Section
def heading_sn():
    print(f"{'TAMBAL BAN SEJATI' :^40}")
    print(f"{'MENYEDIAKAN BERBAGAI JENIS BAN' :^40}")
    print(f"{'=' * 44 :^40}")
# Data Section
D_PIRELLI = ["Pirelli",'Soft',700000 ]
D_CONTINENTAL = ["Continental",'Very Soft',900000 ]
D_SWALLOW = ["Swallow",'Medium',500000 ]
def data_sn():
    data_ban = {
        'JNS_001':D_PIRELLI[1],
        'JNS_002':D_CONTINENTAL[1],
        'JNS_003':D_SWALLOW[1],

        'MRK_001':D_PIRELLI[0],
        'MRK_002':D_CONTINENTAL[0],
        'MRK_003':D_SWALLOW[0],

        'HRG_001':D_PIRELLI[2],
        'HRG_002':D_CONTINENTAL[2],
        'HRG_003':D_SWALLOW[2],
    }

    return data_ban
# Table Section
def table_sn():
    print(f"{'No' :<5} {'Tipe Ban' :<10} {'Merk' :>10} {'Harga' :^25}")
    print(f"{'1' :<5} {DATA_BAN['JNS_001'] :<10} {DATA_BAN['MRK_001'] :>10} {DATA_BAN['HRG_001'] :>15}")
    print(f"{'2' :<5} {DATA_BAN['JNS_002']:<10} {DATA_BAN['MRK_002'] :>10}  {DATA_BAN['HRG_002']  :>15}")
    print(f"{'3' :<5} {DATA_BAN['JNS_003'] :<10} {DATA_BAN['MRK_003']:>10}  {DATA_BAN['HRG_003']  :>15}") 
# Inputan User
def inputan_sn():
    pilihan = input("Masukan Nomor Pilihan : ")
    qty = int(input("Masukan Banyak Jumlah : "))
    # ung_msuk = int(input("Masukan Uang : "))
    return pilihan,qty
# Penghitungan
def penghitungansb_sn(qty):
    if PILIHAN == "1":
        global merk
        global harga
        merk = DATA_BAN['MRK_001']
        hasil = DATA_BAN['HRG_001'] * qty
        harga = DATA_BAN['HRG_001']
    elif PILIHAN == "2":
        merk = DATA_BAN['MRK_002']
        hasil = DATA_BAN['HRG_002'] * qty
        harga = DATA_BAN['HRG_002']
        
    elif PILIHAN == "3":
        merk = DATA_BAN['MRK_003']
        hasil = DATA_BAN['HRG_003'] * qty
        harga = DATA_BAN['HRG_003']

    return hasil
# Display
def display_sn():
    print(f"{'=' * 44 :^40}")
    print(f"{'Merk' :<10} {'Harga' :>10} {'Qty' :^25}")
    print(f"{merk:<10} {harga :>10} {QTY :^25}")


HEADING = heading_sn()
DATA_BAN = data_sn()
table_sn()
PILIHAN,QTY = inputan_sn()
HITUNG = penghitungansb_sn(QTY)
display_sn()
