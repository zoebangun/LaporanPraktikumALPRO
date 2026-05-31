def faktorial(n):
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n-1)

def kombinasi(n, r):
    return faktorial(n) // (faktorial(r) * faktorial(n-r))

print(kombinasi(5,2))
print(kombinasi(6,3))  