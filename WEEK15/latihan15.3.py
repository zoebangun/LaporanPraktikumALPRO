def deret_ganjil(n):
    if n == 1:
        return 1
    return n + deret_ganjil(n-2)

print(deret_ganjil(7))  