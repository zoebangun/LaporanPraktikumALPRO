def cek_digit_belakang(a, b, c):
    digit_a = a % 10
    digit_b = b % 10
    digit_c = c % 10
    
    if (digit_a == digit_b) or (digit_a == digit_c) or (digit_b == digit_c):
        return True
    else:
        return False

bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))
bil3 = int(input("Masukkan bilangan ketiga: "))

hasil = cek_digit_belakang(bil1, bil2, bil3)
print(f"Hasil: {hasil}")