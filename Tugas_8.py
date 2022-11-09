from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

bil = int(input("Masukkan batasan: "))

def cetak(i):
	for i in range(bil):
		if i % 2 == 0:
			print(f"{i+1} Ganjil"," - ID Proses ", getpid() )
		else:
			print(f"{i+1} Genap"," - ID Proses" , getpid())
	sleep(1)

#Pemrosesan Sekuensial
print("Sekuensial")
sekuensial_awal = time()

for i in range(1):
	cetak(i)

sekuensial_akhir = time()
print(" ")

#Multiprocessing dengan kelas Process
print("Multiprocessing.Process")
kumpulan_proses = []
process_awal = time()

for i in range(1):
	p = Process(target=cetak, args=(i,))
	kumpulan_proses.append(p)
	p.start()
for i in kumpulan_proses:
	p.join()

process_akhir = time()
print(" ")

#Multiprocessing dengan kelas Pool
print("Multiprocess.Pool")
pool_awal = time()

pool = Pool()
pool.map(cetak, range(0,1))
pool.close()

pool_akhir = time()
print(" ")

#Bandingkan waktu eksekusi
print("Waktu eksekusi sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi multiprocessing.Process :", process_akhir - process_awal, "detik")
print("Waktu eksekusi multiprocessing.Pool :", pool_akhir - pool_awal, "detik")

