import string

def baca_dan_ambil_kata(nama_file):
    try:
        with open(nama_file, 'r', encoding='utf-8') as file:
            isi_teks = file.read()
            isi_teks = isi_teks.lower()
            
            isi_teks = isi_teks.translate(str.maketrans('', '', string.punctuation))
            
            kumpulan_kata = set(isi_teks.split())
            return kumpulan_kata
    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan atau tidak dapat dibuka.")
        return None

file1 = input("Masukkan nama file teks pertama : ")
file2 = input("Masukkan nama file teks kedua : ")

set_kata_file1 = baca_dan_ambil_kata(file1)
set_kata_file2 = baca_dan_ambil_kata(file2)

if set_kata_file1 is not None and set_kata_file2 is not None:
    kata_bersama = set_kata_file1.intersection(set_kata_file2)
    
    print("\n--- HASIL ANALISIS KATA ---")
    if kata_bersama:
        print(f"Kata-kata yang muncul di kedua file tersebut adalah:\n{kata_bersama}")
    else:
        print("Tidak ada kata yang sama di antara kedua file tersebut.")