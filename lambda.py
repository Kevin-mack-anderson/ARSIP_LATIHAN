import os
os.system("cls")

# Mencari Kuadrat Dengan Function Biasa
def kuadrat(num):
    return num**2
print(f"Hasil dari kuadrat biasa = {kuadrat(3)}")

def kuadrat2(num,pow):
    return num**pow
print(f"Hasil Kuadrat Dari Function Kedua = {kuadrat2(2,3)}")
# Menggunakan Lambda Function
f_kuadrat = lambda f_kuadrat:f_kuadrat**3
print(f"Hasil Kuadrat Dari Lambda = {f_kuadrat(2)}")