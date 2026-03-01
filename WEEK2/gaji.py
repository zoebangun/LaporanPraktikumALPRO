print("--- Program Perhitungan Keuangan Budi Selama Libur 5 Minggu ---")

gaji_per_jam = float(input("Masukkan gaji per jam yang diinginkan: Rp. "))
jam_kerja_mingguan = float(input("Masukkan jumlah jam kerja dalam 1 minggu: "))

total_minggu = 5

pendapatan_kotor = gaji_per_jam * jam_kerja_mingguan * total_minggu

pajak = 0.14 * pendapatan_kotor
pendapatan_bersih = pendapatan_kotor - pajak

uang_pakaian = 0.10 * pendapatan_bersih

uang_alat_tulis = 0.01 * pendapatan_bersih

sisa_uang_setelah_belanja = pendapatan_bersih - uang_pakaian - uang_alat_tulis
total_sedekah = 0.25 * sisa_uang_setelah_belanja

sedekah_yatim = 0.30 * total_sedekah
sedekah_dhuafa = total_sedekah - sedekah_yatim

def format_rp(angka):
        hasil = "{:,.2f}".format(angka).replace(",", "X").replace(".", ",").replace("X", ".")
        return "Rp" + hasil

print("\n--- HASIL PERHITUNGAN KEUANGAN ---")
print(f"1. Pendapatan sebelum pajak         : {format_rp(pendapatan_kotor)}")
print(f"2. Pendapatan setelah pajak          : {format_rp(pendapatan_bersih)}")
print(f"3. Uang pakaian & aksesoris          : {format_rp(uang_pakaian)}")
print(f"4. Uang alat tulis                   : {format_rp(uang_alat_tulis)}")
print(f"5. Total uang sedekah                : {format_rp(total_sedekah)}")
print(f"6. Bagian anak yatim                 : {format_rp(sedekah_yatim)}")
print(f"7. Bagian kaum dhuafa                : {format_rp(sedekah_dhuafa)}")