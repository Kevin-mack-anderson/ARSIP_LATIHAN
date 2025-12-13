# Modul Time
def mencoba_modul():
     print("FAIRUZ YAHDI MAYASSA \n" \
     "15250169")
     '''TIME'''
     import time
     '''Mendapatkan jam dan hari'''
     local = time.localtime()
     print("Hari:", local.tm_mday)
     print("Bulan:", local.tm_mon)
     print("Tahun:", local.tm_year)
     print("Jam", local.tm_hour,":", local.tm_min)
     '''Jeda 3 detik'''
     print("Kita Mulai Ya, ada jeda 3 detik..")
     time.sleep(3)
     print("Sudah selesaii")
     '''Mengukur lama eksekusi program'''
     start = time.time() 
     for i in range (1000000):
          pass
     end = time.time() 
     print(f"Durasieksekusi : {end}-{start} detik")

     '''DATETIME'''
     from datetime import datetime, timedelta
     '''Waktu sekarang'''
     now = datetime.now()
     print(f"Sekarang : {now}")
     '''Format waktu ke str'''
     future = now + timedelta(days = 5)
     print(f"5 hari lagi {future}")
     '''Parsing string ke datetime'''
     dt = datetime.strptime("2025-11-25 07:44:00", "%Y-%m-%d %H:%M:%S")
     print(f"Parsed: {dt}")

     '''RANDOM'''
     import random
     '''Angka acak sederhana'''
     print(f"Angka acak antara 0 dan 1: {random.random()}")
     print(f"Angka bulat acak 1-10 {random.randint(1, 10)}")
     '''Pemilihan acak dari list'''
     buah = ["apel", "pisang", "jeruk", "mangga"]
     print(f"Buah terpilih {random.choice(buah)}")
     '''Mengecek urutan list'''
     angka = [1, 2, 3, 4, 5]
     random.shuffle(angka)
     print(f"Urutan acak {angka}")
mencoba_modul()