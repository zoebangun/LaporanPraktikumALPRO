kalimat = input("masukan sebuah kalimat: ")

kata = kalimat.split()

terpendek = min(kata, key=len)
terpanjang = max(kata, key=len)

print("kata Terpendek:", terpendek)
print("kata Terpanjang:", terpanjang)