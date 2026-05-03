def tampilkan_kata_unik(nama_file):
    try:
        with open(nama_file, 'r') as file:
            konten = file.read()
            kata_kata = konten.split()
            kata_unik = set(word.lower() for word in konten.split())
            print(sorted(list(kata_unik)))
    except FileNotFoundError:
        print("File tidak ditemukan.")
tampilkan_kata_unik('artikel.txt')