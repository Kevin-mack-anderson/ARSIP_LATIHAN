import os 
import random

os.system("cls")

# Head Program
print("Selamat Datang Di Game Tebak Angka !!")
print("Saya Telah Memilih Angka Dari 1-100 ")
print("Coba Tebak Angka Tersebut!!")
# Program Start
def game_angka():
 """Membuat Angka Random"""
 angka = random.randint(1,100)
 i = 0
 while True:
  """Membuat Eksepsi"""
    try:
        tebakan = int(input("Masukan Tebakan Anda = "))
        i += 1
        if tebakan == angka:
            print(f"SELAMAT ANDA BENAR DI TEBAKAN {i} ")
            print(f"Tebakan anda adalah = {tebakan}")
            pilihan = input("Apakah Kamu Ingin Bermain lagi? (y/n) :").lower()
            if pilihan == "y":
               continue
            elif pilihan == "n":
               print("Terimakasih Telah Bermain !!")
               break
        elif tebakan < angka:
            print("TEBAKAN KAMU TERLALU RENDAH")
        elif tebakan > angka:
            print("TEBAKAN KAMU TERLALU TINGGI!!")
    except ValueError:
        print("Kamu Memasukan Tipe Data Yang Tidak Sesuai")  
# Main Program

game_angka()
