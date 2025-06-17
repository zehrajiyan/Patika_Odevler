sayi = int(input("Bir tam sayı girin: "))

if sayi <= 1:
    print("Asal sayı değildir.")
else:
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            print("Asal sayı değildir.")
            break
    else:
        print("Asal sayıdır.")