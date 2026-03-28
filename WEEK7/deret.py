Tinggi = int(input("Masukan tinggi: "))
Lebar = int(input("Masukan Lebar: "))

angka = 1

for i in range(Tinggi):
    for j in range(Lebar):
        print(angka, end=" ")
        angka += 1
    print()