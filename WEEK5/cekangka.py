def cek_angka(a, b, c):
    if a != b and a != c and b != c:
        if (a + b == c) or (a + c == b) or (b + c == a):
            return True
        else:
            return False
    else:
        return False

print(cek_angka(2, 3, 5)) 
print(cek_angka(7, 10, 3))
print(cek_angka(5, 5, 10))