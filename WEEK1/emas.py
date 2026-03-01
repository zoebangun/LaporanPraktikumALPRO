jumlahemas = 25
hargabeli = 650000
hargasekarang =685000

totalbeli = jumlahemas * hargabeli
totalnilaisekarang =jumlahemas * hargasekarang
untungrp = totalnilaisekarang - totalbeli
untungpersen = (untungrp / totalbeli) * 100

print(f"keuntungan: Rp {untungrp:,}")
print(f"persentase: {untungpersen:.2f}%")



jumlahemas2 = 15
hargabeli2 = 685000

totalgramakhir = jumlahemas + jumlahemas2
totalmodalakhir = totalbeli + (jumlahemas2 * hargabeli2)

hargabaru = 715000
nilaiakhir = totalgramakhir * hargabaru

untungrptotal = nilaiakhir - totalmodalakhir
untungpersentotal = (untungrptotal / totalmodalakhir) * 100

print(f"total keuntungan: Rp {untungrptotal:,}")
print(f"total persentase: {untungpersentotal:.2f}%")