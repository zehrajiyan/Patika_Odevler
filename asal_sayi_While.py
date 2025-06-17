sayi = int(input("Bir tam sayı girin: "))

if sayi <= 1:
    print("Asal sayı değildir.")
else:
    i = 2
    asal = True
    while i <= int(sayi**0.5):
        if sayi % i == 0:
            asal = False
            break
        i += 1

    if asal:
        print("Asal sayıdır.")
    else:
        print("Asal sayı değildir.")