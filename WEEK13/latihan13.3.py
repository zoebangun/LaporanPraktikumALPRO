counts = dict()

fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("File tidak ditemukan")
    quit()

for line in fhand:
    if line.startswith("From "):
        kata = line.split()

        waktu = kata[5]
        jam = waktu.split(":")[0]

        counts[jam] = counts.get(jam, 0) + 1

lst = list(counts.items())

lst.sort()

for jam, jumlah in lst:
    print(jam, jumlah)