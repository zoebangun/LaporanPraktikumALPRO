dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print(f"{'key':<5} {'value':<5} {'item':<5}")

for key, value in dictionary.items():
    print(f"{key:<5} {value:<5} {key:<5}")