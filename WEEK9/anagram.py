def cek_anagram(kata1, kata2):
    kata1 = kata1.lower().replace(" ", "")
    kata2 = kata2.lower().replace(" ", "")
    
    return sorted(kata1) == sorted(kata2) 

k1 = input("masukan kata pertama: ")
k2 = input("masukan kata kedua: ")

if cek_anagram(k1, k2):
    print("kata ini adalah Anagram")
else:
    print("kata ini Bukan Anagram")