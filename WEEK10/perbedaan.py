file1_name = input("Masukkan nama file pertama: ")
file2_name = input("Masukkan nama file kedua: ")

try:
    handle1 = open(file1_name)
    handle2 = open(file2_name)

    lines1 = handle1.readlines()
    lines2 = handle2.readlines()
    
    max_lines = max(len(lines1), len(lines2))
    
    for i in range(max_lines):
        line1 = lines1[i].strip() if i < len(lines1) else "[Baris Kosong]"
        line2 = lines2[i].strip() if i < len(lines2) else "[Baris Kosong]"
        
        if line1 != line2:
            print(f"Perbedaan pada baris {i+1}:")
            print(f"File 1: {line1}")
            print(f"File 2: {line2}")
            print("-" * 20)
            
    handle1.close()
    handle2.close()

except FileNotFoundError:
    print("Salah satu atau kedua file tidak ditemukan!")