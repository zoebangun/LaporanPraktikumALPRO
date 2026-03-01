try:
    bil = int(input("Masukkan suatu bilangan: "))
    hasil = "Positif" if bil > 0 else ("Negatif" if bil < 0 else "Nol")
    print(hasil)
except:
    print("Input tidak valid.")