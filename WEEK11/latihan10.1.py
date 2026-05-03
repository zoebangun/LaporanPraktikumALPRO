def cari_3_terbaik(data):
    data.sort(reverse=True)
    return data[:3]

daftar_nilai = [80, 95, 70, 100, 85, 90]
print(cari_3_terbaik(daftar_nilai)) 