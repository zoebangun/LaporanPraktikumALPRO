Data = ('Zoe Azarya Bangun', '71251212', 'Sleman, DI Yogyakarta')
print("Data :", Data)

nama, nim, alamat = Data

print("NIM :", nim)
print("NAMA :", nama)
print("ALAMAT :", alamat)

perubahan_nim = tuple(nim)
print("NIM :", perubahan_nim)

nama_depan = nama.split()[0]
nama_depan = tuple(nama_depan[1:])
print("NAMA DEPAN :", nama_depan)

nama_terbalik = tuple(nama.split()[::-1])
print("NAMA TERBALIK :", nama_terbalik)