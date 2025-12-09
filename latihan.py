
# Kalkulator diperbaiki
def lat_kalku():
    """Looping"""
    while True:
     """Eksepsi"""
     try:
       mulai = input("Ingin Memulai? [Y,T] : ").upper()
       """FLow mulai"""
       if mulai == "T": 
        print("terimakasih") 
        break
       elif mulai == "Y":
         pass
       pil_1 = int(input("Masukan Angka Pertama : "))
       pil_2 = int(input("Masukan Angka Kedua : "))
       jns_op = input("Masukan Jenis Op [*,/,+,-] : ")
       
       """Flow penghitungan"""
       if jns_op == "*": hasil = pil_1 * pil_2
       elif jns_op == "/": hasil = pil_1 / pil_2
       elif jns_op == "+": hasil = pil_1 + pil_2
       elif jns_op == "-": hasil = pil_1 - pil_2
       else: print("Jenis Op Tidak Valid") 
       print(f"{pil_1} {jns_op} {pil_2} = {hasil}")
       """Eksepsi selesai"""
     except ValueError: 
       print("Anda Bukan Memasukan Angka!") 
       pass
lat_kalku()


def cek_angka():
    while True:
        input_user = int(input("Angka  (Masukan 0 untuk berhenti) : "))
        if input_user == 0:
            break
        elif input_user % 2 == 0:
            print(f"Angka ke- adalah GENAP")
        else: print(f"Angka ke- adalah GANJIL")
cek_angka()

def table_perkalian():
   """Inputan User"""
   user = int(input("Masukan Angka : "))
   for i in range (1,11):
      hasil = user * i
      print(f"{user} * {i} = {hasil}")
table_perkalian()

# Faktorial
# dengan perulangan
inputan = int(input("Masukan Angka : "))
fak = 1
if inputan == 0:
    fak = 1
elif inputan >= 1:
    for i in range(1, inputan+1):
        fak = fak * i
else: print("Maaf tidak Bisa")
print(f"!{inputan} = {fak}")

# # dengan rekursi
def faktorial(g):
    if g == 0: return 1 
    else: return g * faktorial(g-1)
user = int(input("Masukan Angka : "))
print(f"!{user} = {faktorial(user)}")
   
    
         
