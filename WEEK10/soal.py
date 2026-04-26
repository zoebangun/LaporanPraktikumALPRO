filename = input("nama file: ")

try:
    handle = open(filename)
    
    for line in handle:
        if "||" in line:
            parts = line.strip().split("||")
            pertanyaan = parts[0].strip()
            kunci_jawaban = parts[1].strip()
            
            print(pertanyaan)
            
            user_answer = input("Jawab: ")
            
            if user_answer.lower() == kunci_jawaban.lower():
                print("Jawaban benar!")
            else:
                print("Jawaban salah!")
            print() 
            
    handle.close() 

except FileNotFoundError:
    print("File tidak ditemukan!")