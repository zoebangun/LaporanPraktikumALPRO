modal = 200000000
target = 400000000
bunga = 0.10
tahun = 0

while modal < target:
    tahun += 1
    modal += modal * bunga
    print(f"Tahun ke-{tahun}, uang Erika jadi: Rp{modal:,.0f}")

print(f"\nWaktu yang dibutuhkan: {tahun} Tahun")