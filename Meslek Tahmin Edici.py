import time

doc_puan=0
av_puan=0
ogrt_puan=0
snt_puan=0
muh_puan=0
tam_puan=0

sorular=[""")Hangi alan sana daha yakın?
    1) Her türlü alan bana uygun
    2) Matematik ve Genetik
    3) Söz ve Edebiyat
    4) Teknoloji ve Tasarım
    5) Görsel Sanatlar ve Spor""",
""")Hangisi senin idolün olurdu?
    1) Steve Jobs
    2) Gazi Yaşargil
    3) Naim Süleymanoğlu
    4) Gönenç Gürkaynak
    5) Nurten Akkuş""",
""")Hangisi seni daha çok mutlu eder?
    1) Gerçek Yaşam Problemleri Çözmek
    2) Arkadaşlarımın Takıldığı Yerlerde Onlara Yardımcı Olmak
    3) Yeni Üretimler/Tasarımlar Yapmak
    4) Spor Yapmak/Müzik Çalmak/Çizim Yapmak
    5) Hesaplamalar Yapmak""",
""")Kendine hangi hediyeyi alırdın?
    1) Bir yığın okunacak kitap
    2) Müzik aleti / Top vs.""",
""")Hangisi seni korkutmaz?
    1) Kan
    2) Çok kişinin öninde performans sergilemek
    3) Çeşitli yollarla az tanıdığım insanlarla iletişime geçmek
    4) Herkes sana karşı çıksa da o kişiyi savunmak
    5) Çeşitli alet-edevatlar""",
""")Gelecekte nasıl bir yerde çalışmak isterdin?
    1) Devlet binasında
    2) Ofis
    3) Spor salonu""",
""")Son olaraak... Hangi nesne sana daha uygun?
    1) Müzik aleti / Spor aleti vs.
    2) Kablolar / Çizimler / Kodlar...
    3) Beyaz Önlük
    4) Tebeşir / Tahta Kalemi
    5) Kategorilerine göre renklendirilmiş dosyalar"""]
print("""
Merhaba!

7 soruyla gelecekteki mesleğini
tahmin etmeye çalışacağım. :)

Geliştirilmekte olduğumdan dolayı
şu anda sadece 5 meslek tahmin
edebilmekteyim. İşte onlar:
    
    > Doktor
    > Avukat
    > Öğretmen
    > Sanatçı
    > Mühendis

Hazırsan başlayalım!""")
ad=input("Öncelikle... İsmin Nedir? : ")
print(f"Tanıştığıma memnun oldum {ad}!")

for i in range(7):
    print(f"{i+1}.soru{sorular[i]}")
    cevap=int(input("Cevabınız: "))

    if i==0 and cevap==1:
        ogrt_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==0 and cevap==2:
        doc_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==0 and cevap==3:
        av_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==0 and cevap==4:
        muh_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==0 and cevap==5:
        snt_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    if i==1 and cevap==1:
        muh_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==1 and cevap==2:
        doc_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==1 and cevap==3:
        snt_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==1 and cevap==4:
        av_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==1 and cevap==5:
        ogrt_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    if i==2 and cevap==1:
        av_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==2 and cevap==2:
        ogrt_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==2 and cevap==3:
        muh_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==2 and cevap==4:
        snt_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==2 and cevap==5:
        doc_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    if i==3 and cevap==1:
        av_puan+=1
        doc_puan+=1
        ogrt_puan+=1
        muh_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==3 and cevap==2:
        snt_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    if i==4 and cevap==1:
        doc_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==4 and cevap==2:
        snt_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==4 and cevap==3:
        ogrt_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==4 and cevap==4:
        av_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==4 and cevap==5:
        muh_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    if i==5 and cevap==1:
        ogrt_puan+=1
        av_puan+=1
        doc_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==5 and cevap==2:
        muh_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==5 and cevap==3:
        snt_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    if i==6 and cevap==1:
        snt_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==6 and cevap==2:
        muh_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==6 and cevap==3:
        doc_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==6 and cevap==4:
        ogrt_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

    elif i==6 and cevap==5:
        av_puan+=1
        print("Yanıtınız kaydedildi. 3 Saniye bir sonraki soruya yönlendirileceksiniz.")
        time.sleep(3)

print(f"""
Mesleklere yakınlık dereceniz:
Doktor:{doc_puan}     ,     Avukat:{av_puan},
Sanatçı:{snt_puan}     ,     Mühendis:{muh_puan},
Öğretmen:{ogrt_puan}""")

if doc_puan>av_puan:
    if doc_puan>snt_puan:
        if doc_puan>muh_puan:
            if doc_puan>ogrt_puan:
                print("Sizin gelecekteki mesleğiniz.... Doktor!")

elif av_puan>doc_puan:
    if av_puan>snt_puan:
        if av_puan>muh_puan:
            if av_puan>ogrt_puan:
                print("Sizin gelecekteki mesleğiniz.... Avukat!")

elif snt_puan>doc_puan:
    if snt_puan>av_puan:
        if snt_puan>muh_puan:
            if snt_puan>ogrt_puan:
                print("Sizin gelecekteki mesleğiniz.... Sanatçı!")

elif ogrt_puan>doc_puan:
    if ogrt_puan>snt_puan:
        if ogrt_puan>muh_puan:
            if ogrt_puan>av_puan:
                print("Sizin gelecekteki mesleğiniz.... Öğretmen!")

elif muh_puan>doc_puan:
    if muh_puan>snt_puan:
        if muh_puan>av_puan:
            if muh_puan>ogrt_puan:
                print("Sizin gelecekteki mesleğiniz.... Mühendis!")