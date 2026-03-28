n = int(input("masukan bilangan: "))

for i in range(n -1, 1, -1):
    prima = True
    for j in range(2, i):
        if i % j == 0:
            prima = False
            break

    if prima:
        print("maka prima terdekat <",n," adalah", i)
        break
else:
        print("tidak ada prima terdekat dari", n)