import random

toplam=0
hak=3
say=random.randint(1,100)

for i in range(3):
    a = int(input("Sayı gir: "))
    b = int(input("Sayı gir: "))
    c = int(input("Sayı gir: "))
    toplam=a+b+c
    if toplam<say:
        hak-=1
        if hak<1:
            print(f"Kaybettiniz! Sistemin sizden istediği sayı {say}'dı.")
            break
        else:
            print(f"Girdiğiniz 3 sayının toplamı, \nsistemin sizden istediği sayıdan küçük. \n{hak} adet hakkınız kaldı.")
    elif toplam>say:
        hak -= 1
        if hak<1:
            print(f"Kaybettiniz! Sistemin sizden istediği sayı {say}'dı.")
            break
        else:
            print(f"Girdiğiniz 3 sayının toplamı, \nsistemin sizden istediği sayıdan büyük. \n{hak} adet hakkınız kaldı.")
    else:
        print("Tebrikler Kazandınız! Girdiğiniz sayıların toplamı sistemin \nsizden istediği sayıya eşit!")
        break