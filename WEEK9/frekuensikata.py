kalimat = input("masukan kalimat yang ingin anda masukan: ")
kata_dicari = input("masukan kata yang ingin dicari: ")

kalimat = kalimat.lower()
kata_dicari = kata_dicari.lower()

import re
kalimat = re.sub(r'[^\w\s]', '', kalimat)

jumlah = kalimat.split().count(kata_dicari)

print(f"{kata_dicari} ada {jumlah} buah")