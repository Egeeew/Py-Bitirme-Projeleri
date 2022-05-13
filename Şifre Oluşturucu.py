import random
chars="AaBbCcÇçDdEeFfGgĞğHhIıİiJjKkLlMmNnOoPpRrSsŞşTtUuÜüVvYyZz1234567890<>£#$½{[]}\|@€₺"
sifre=""
k_ad=input("Kullanıcı ismi:")

for i in range(4):
    for j in range(4):
        say=random.randint(0,80)
        sifre+=chars[say]
        str(sifre)

sifreler={k_ad:sifre}
print(f"{k_ad}, şifreniz: {sifreler[k_ad]}")