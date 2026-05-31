def prima(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return prima(n, i+1)

angka = int(input("Masukan Bilangan: "))
if prima(angka):
    print(f"{angka} adalah bilangan prima!")
else:
    print(f"{angka} bukan bilangan prima!")