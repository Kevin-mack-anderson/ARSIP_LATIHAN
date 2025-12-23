import os
os.system("cls")
# # Kalkulator diperbaiki
# def lat_kalku():
#     """Looping"""
#     while True:
#      """Eksepsi"""
#      try:
#        mulai = input("Ingin Memulai? [Y,T] : ").upper()
#        """FLow mulai"""
#        if mulai == "T": 
#         print("terimakasih") 
#         break
#        elif mulai == "Y":
#          pass
#        pil_1 = int(input("Masukan Angka Pertama : "))
#        pil_2 = int(input("Masukan Angka Kedua : "))
#        jns_op = input("Masukan Jenis Op [*,/,+,-] : ")
       
#        """Flow penghitungan"""
#        if jns_op == "*": hasil = pil_1 * pil_2
#        elif jns_op == "/": hasil = pil_1 / pil_2
#        elif jns_op == "+": hasil = pil_1 + pil_2
#        elif jns_op == "-": hasil = pil_1 - pil_2
#        else: print("Jenis Op Tidak Valid") 
#        print(f"{pil_1} {jns_op} {pil_2} = {hasil}")
#        """Eksepsi selesai"""
#      except ValueError: 
#        print("Anda Bukan Memasukan Angka!") 
#        pass
# lat_kalku()

# def cek_angka():
#     while True:
#         input_user = int(input("Angka  (Masukan 0 untuk berhenti) : "))
#         if input_user == 0:
#             break
#         elif input_user % 2 == 0:
#             print(f"Angka ke- adalah GENAP")
#         else: print(f"Angka ke- adalah GANJIL")
# cek_angka()

# def table_perkalian():
#    """Inputan User"""
#    user = int(input("Masukan Angka : "))
#    for i in range (1,11):
#       hasil = user * i
#       print(f"{user} * {i} = {hasil}")
# table_perkalian()

# # Faktorial
# # dengan perulangan
# inputan = int(input("Masukan Angka : "))
# fak = 1
# if inputan == 0:
#     fak = 1
# elif inputan >= 1:
#     for i in range(1, inputan+1):
#         fak = fak * i
# else: print("Maaf tidak Bisa")
# print(f"!{inputan} = {fak}")

# # # dengan rekursi
# def faktorial(g):
#     if g == 0: return 1 
#     else: return g * faktorial(g-1)
# user = int(input("Masukan Angka : "))
# print(f"!{user} = {faktorial(user)}")
   
# def faktorial_again(n):
#     if n == 0: return 1
#     else: return n * faktorial_again(n-1)
# n = int(input("Masukan Angka"))
# print(f"!{n} = {faktorial_again(n)}")

# # Menjumlahkan semua bilangan genap
# bil_user = int(input("masukan angka : "))
# for i in range(bil_user):
#     if i % 2 == 0:
#        hasil = i + i
#     else: None
# print(hasil)

# # Mencari nilai max dari list
# my_list = [2,3,4,5,6,78,9]
# print(max(my_list))

# def flow():
#     funct_1 = True
#     chose = False
#     if funct_1:
#         if chose == False:
#             None
# flow()

# # Belajar Dictionary

# mahasiswa1 = {
#     'Nama':'Kasep',
#     'NIM':'1212',
#     'SKS':144,
#     'lulus':True
# }
# mahasiswa2 = {
#     'Nama':'Ucup',
#     'NIM':'4212',
#     'SKS':123,
#     'lulus':False
# }
# mahasiswa3 = {
#     'Nama':'Udin',
#     'NIM':'1262',
#     'SKS':140,
#     'lulus':True
# }

# data_mahasiswa = {
#     'MHS001': mahasiswa1,
#     'MHS002': mahasiswa2,
#     'MHS003': mahasiswa3
# }
# for data in data_mahasiswa:
#     KEY = data
#     NAMA = data_mahasiswa[KEY]['Nama']
#     NIM = data_mahasiswa[KEY]['NIM']
#     SKS = data_mahasiswa[KEY]['SKS']
#     lulus = data_mahasiswa[KEY]['lulus']
# print(f"{NAMA:<7} {NIM:<7}  {SKS:<5} {lulus:^4}")

# # latihan baru tanggal 21 desember 2025
# """Level 1"""
# # 1. variabel dan tipe data
# nama = "python"
# umur = 21
# print(f"Halo nama saya {nama} dengan umur {umur}")
# # 2. Operasi Aritmatika
# hitung = 10 + 5 * 2 - 3
# print(f"Hasil dari penghitungan = {hitung}")
# # 3. Input dan Output 
# nama_pengguna = input("Masukan Nama = ")
# print(f"Halo{nama_pengguna}")
# # 4. Tipe Data String
# kata1 = "Hello"
# kata2 = "Worlld"
# print(kata1 + "" + kata2)
# """Level 2:Menegah"""
# # 5. Pengecekan Bilangan Genap Ganjil
# user = int(input("Masukan Angka"))
# if user % 2 == 0: print("Bilangan Genap")
# else: print("Bilangan Ganjil")
# # 6. Loop for
# for i in range(1,11):
#     print(i)
# # 7. Loop while
# """Level 3:Lanjutan"""
# # 8. Fungsi Kuadrat
# def kuadrat(number):
#     return number ** 2
# print(kuadrat(5))
# # 9. List
# list = [1,2,3,4,5]
# list.insert(5,6)
# print(list)
# # Dictionary
# data_diri = {
#     'nama':"bob",
#     'umur':30
# }
# print(f"Halo {data_diri['nama']}, umrunya {data_diri['umur']}")

# SOAL BARU 10
"""1. Menghitung Luas Persegi Panjang"""
def h_persegiPanjang(p,l):
   return p*l
P = int(input("Masukan Panjang : "))
L = int(input("Masukan Lebar : "))
print(f"Hasil Lebar : {h_persegiPanjang(P,L)}")
"""2. Konversi Celcius ke Farenheit"""
def ubah_suhu(c):
   change = int((9/5 * c)) + 32
   print(f"Hasil C -> F = {change}")
Celcius = int(input("Masukan Suhu C : "))
ubah_suhu(Celcius)
"""3. Menghitng Rata-Rata Nilai List"""
angka_list = [10,20,30,40,50]
rata_rata = sum(angka_list) / len(angka_list)
print(f"Rata-rata dari list = {rata_rata}")
"""4. Membalik Urutan Kata Dalam String"""
kalimat = "Kamu hari ini cantik sekali melisa"
kita_balik = " ".join(kalimat.split()[::-1])
print(kita_balik)
"""5. Menghitung Jumlah Kata Dalam String"""
kata_kata = "Jangan Ragu Jangan Bimbang"
panjang_kata = len(kata_kata)
print(f"Panjang Kata Dari Kalimat Diatas Adalah = {panjang_kata}")
"""6. Fibonaci Sequence"""
def fibonaci(n):
   if n <= 0:
      return []
   elif n == 1:
      return [0]
   elif n == 2:
      return [0,1]
   else:
      seq = [0,1]
      for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
        return seq
n = int(input("Masukan Angkanya : "))
print(f"Hasil Fibonacinya = {fibonaci(n)}")
"""7. Menghitung BMI"""
berat = float(input("Masukan Berat Anda : "))
tinggi = float(input("Masukan Tinggi Anda : "))
bmi = berat / (tinggi * 2)
print(f"BMI Anda Adalah = {bmi :.2f}")
"""8. Validasi Email Sederhana"""
def cek_email(eml):
  if "@" in eml and "." in eml:
     print("Login Berhasil")
  else:
     print("Email tidak valid!!")
email_user = input("Masukan email anda : ")
cek_email(email_user)
"""9. Menghitung Kuadrat"""
angka1 = int(input("Masukan Angka : "))
pangkat = int(input("Masukan Pangkat : "))
hasil = lambda a,b:a ** b
print(hasil(angka1,pangkat))