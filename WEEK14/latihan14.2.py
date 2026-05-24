list_awal = [1, 2, 3, 3, 4, 5, 5]
set_dari_list = set(list_awal)
print("1. Konversi List menjadi Set")
print(f"   Sebelum (List) : {list_awal}")
print(f"   Sesudah (Set)  : {set_dari_list}  <- (Duplikasi otomatis dihapus)")

set_awal = {'apple', 'banana', 'cherry'}
list_dari_set = list(set_awal)
print("\n2. Konversi Set menjadi List")
print(f"   Sebelum (Set)  : {set_awal}")
print(f"   Sesudah (List) : {list_dari_set}")

tuple_awal = ('A', 'B', 'C', 'A')
set_dari_tuple = set(tuple_awal)
print("\n3. Konversi Tuple menjadi Set")
print(f"   Sebelum (Tuple): {tuple_awal}")
print(f"   Sesudah (Set)  : {set_dari_tuple}")

set_awal_2 = {10, 20, 30}
tuple_dari_set = tuple(set_awal_2)
print("\n4. Konversi Set menjadi Tuple")
print(f"   Sebelum (Set)  : {set_awal_2}")
print(f"   Sesudah (Tuple): {tuple_dari_set}")