try:
    suhu = int(input("Masukkan suhu tubuh: "))
    if suhu >= 38:
        print("Anda Demam!!")
    else:
        print("Anda Tidak Demam!")
except:
    print("Input tidak valid. Silakan masukkan angka.")