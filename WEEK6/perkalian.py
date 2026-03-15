def perkalian(a, b):
    print(f"{a} x {b} = ", end="")
    hasil = 0
    for i in range(1, a + 1):
        hasil += b
        if i < a:
            print(f"{b} + ", end="")
        else:
            print(f"{b} = {hasil}")
    return hasil

perkalian(6, 5)
perkalian(7, 10)