def hitung_rata_rata():
    angka_list = []
    while True:
        user_input = input("Masukkan angka (ketik 'done' untuk selesai): ")
        if user_input.lower() == 'done':
            break
        try:
            angka_list.append(float(user_input))
        except ValueError:
            print("Input tidak valid, silakan masukkan angka.")
    
    if len(angka_list) > 0:
        rata_rata = sum(angka_list) / len(angka_list)
        print(f"Rata-rata dari data tersebut adalah: {rata_rata}")
    else:
        print("Tidak ada data yang dimasukkan.")

hitung_rata_rata()