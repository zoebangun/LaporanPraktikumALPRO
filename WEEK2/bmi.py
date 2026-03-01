print("--- Program Penghitung Berat Badan Berdasarkan Target BMI ---")
 
tinggi_cm = float(input("Masukkan tinggi badan Anda (dalam cm): "))
bmi_target = float(input("Masukkan nilai BMI (Body Mass Index) yang diharapkan: "))

tinggi_m = tinggi_cm / 100

berat_diperlukan = bmi_target * (tinggi_m ** 2)

print("\n--- HASIL ANALISIS ---")
print("Tinggi badan: %.2f m" % tinggi_m)
print("BMI yang diharapkan: %.1f" % bmi_target)
print("Berat badan yang diperlukan untuk mencapai BMI tersebut adalah: %.2f kg" % berat_diperlukan)