def ganjil(bawah, atas):
    if bawah < atas:
        for i in range(bawah, atas + 1):
            if i % 2 != 0:
                print(i, end=", " if i < atas - 1 else "")
    else:
        for i in range(bawah, atas - 1, -1):
            if i % 2 != 0:
                print(i, end=", " if i > atas + 1 else "")
    print()

print("bawah = 10, atas = 30:")
ganjil(10, 30)

print("bawah = 97, atas = 82:")
ganjil(97, 82)