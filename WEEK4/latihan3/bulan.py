try:
    bulan = int(input("Masukkan bulan (1-12): "))
    
    if bulan < 1 or bulan > 12:
        print("Bulan tidak valid. Masukkan angka 1 sampai 12.")
    else:
        # Tahun 2020 adalah tahun kabisat (Februari = 29 hari)
        if bulan == 2:
            hari = 28
        elif bulan in [4, 6, 9, 11]:
            hari = 30
        else:
            hari = 31
        print(f"Jumlah hari: {hari}")
except:
    print("Input tidak valid. Masukkan angka.")