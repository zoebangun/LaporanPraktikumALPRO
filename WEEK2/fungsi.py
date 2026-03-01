print("--- Program Penghitung Fungsi f(x) = 2x^3 + 2x + 15/x ---")

prompt = 'Masukkan nilai x (bilangan bulat): '
x_str = input(prompt)
x = int(x_str)

hasil = (2 * (x ** 3)) + (2 * x) + (15 / x)
print("Hasil dari f(x) adalah: %.2f" % hasil)