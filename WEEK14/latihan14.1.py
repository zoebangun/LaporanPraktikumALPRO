n = int(input('Masukkan jumlah kategori: '))

data_aplikasi = {}

for i in range(n):
    nama_kategori = input('Masukkan nama kategori: ')
    print(f'Masukkan 5 nama aplikasi di kategori {nama_kategori}')
    
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)
        
    data_aplikasi[nama_kategori] = set(aplikasi)

print("\nData Aplikasi:")
print(data_aplikasi)

semua_aplikasi = []
for apps in data_aplikasi.values():
    semua_aplikasi.extend(list(apps))

frekuensi_aplikasi = {}
for app in semua_aplikasi:
    frekuensi_aplikasi[app] = frekuensi_aplikasi.get(app, 0) + 1

hanya_satu_kategori = {app for app, count in frekuensi_aplikasi.items() if count == 1}

tepat_dua_kategori = {app for app, count in frekuensi_aplikasi.items() if count == 2}

print("\n--- HASIL ANALISIS ---")
print(f"Aplikasi yang hanya muncul di satu kategori saja: {hanya_satu_kategori}")

if n > 2:
    print(f"Aplikasi yang muncul tepat di dua kategori sekaligus: {tepat_dua_kategori}")
else:
    print("Informasi aplikasi tepat di dua kategori hanya ditampilkan jika input kategori (n) > 2.")