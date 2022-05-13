#Ufak hatalar var düzeltilmesi gerekiyor.

import time

giderler={"YS":2600,
          "YE":3000,
          "YD":2200,
          "KM":560,
          "MM":1340,
          "DM":670}

gelirler={"YM":36000,
          "DG":5800}

while True:
    msg = f"""
              ~~ GELİR-GİDER PROGRAMINIZ ~~     
    >Merhaba gelir-giderlerinizi görüntüleyebileceğiniz
    uygulamamıza hoş geldiniz!

    >Lütfen görüntülemek istediğiniz bilgilerinizi
    aşağıda verilen şemaya göre seçin!

                GİDERLER
       >  YILLIK SU MASRAFLARI  YS  <
    >  YILLIK ELEKTRİK MASRAFLARI  YE  <
    >  YILLIK DOĞALGAZ MASRAFLARI  YD  <
       >  KIRTASİYE MASRAFLARI  KM  <
        >  MUTFAK MASRAFLARI  MM  <
         >  DİĞER MASRAFLAR  DM  <
               >  Çıkış  Q  <

                GELİRLER
      >  YILLIK MAAŞ MİKTARINIZ YM  <
         >  DİĞER GELİRLER  DG  <
              >  Çıkış  Q  <

        Ulaşmak İstediğiniz Hizmet: """

    cvp=input(msg)

    if cvp.upper()=="YS":
        print(f"Yıllık su masrafınız: {giderler[cvp.upper()]}₺ 'dir.")
        print("3 saniye sonra tekrar seçim menüsüne yönlendirileceksiniz.")
        time.sleep(3)
    elif cvp.upper()=="YE":
        print(f"Yıllık elektrik masrafınız: {giderler[cvp.upper()]}₺ 'dir.")
        print("3 saniye sonra tekrar seçim menüsüne yönlendirileceksiniz.")
        time.sleep(3)
    elif cvp.upper()=="YD":
        print(f"Yıllık doğalgaz masrafınız: {giderler[cvp.upper()]}₺ 'dir.")
        print("3 saniye sonra tekrar seçim menüsüne yönlendirileceksiniz.")
        time.sleep(3)
    elif cvp.upper()=="KM":
        print(f"Yıllık kırtasiye masrafınız: {giderler[cvp.upper()]}₺ 'dir.")
        print("3 saniye sonra tekrar seçim menüsüne yönlendirileceksiniz.")
        time.sleep(3)
    elif cvp.upper()=="MM":
        print(f"Yıllık mutfak masrafınız: {giderler[cvp.upper()]}₺ 'dir.")
        print("3 saniye sonra tekrar seçim menüsüne yönlendirileceksiniz.")
        time.sleep(3)
    elif cvp.upper()=="DM":
        print(f"Yıllık diğer masraflarınız: {giderler[cvp.upper()]}₺ 'dir.")
        print("3 saniye sonra tekrar seçim menüsüne yönlendirileceksiniz.")
        time.sleep(3)
    elif cvp.upper()=="YM":
        print(f"Yıllık maaş geliriniz: {gelirler[cvp.upper()]}₺ 'dir.")
        print("3 saniye sonra tekrar seçim menüsüne yönlendirileceksiniz.")
        time.sleep(3)
    elif cvp.upper()=="DG":
        print(f"Yıllık elde ettiğiniz diğer gelirler: {gelirler[cvp.upper()]}₺ 'dir.")
        print("3 saniye sonra tekrar seçim menüsüne yönlendirileceksiniz.")
        time.sleep(3)

    elif cvp.upper()=="Q":
        print("Çıkış sağlanacak. \nYıllık toplam kârınızı/zararınızı görüntülemek ister misiniz?")
        while True:
            dg=input("E/H : ")
            if dg.upper()=="E":
                kar = (gelirler["YM"] + gelirler["DG"]) - (giderler["YS"] + giderler["YE"] + giderler["YD"] + giderler["KM"] + giderler["MM"] +giderler["DM"])
                if kar < 0:
                    print(f"{kar * -1}₺ zararınız bulunuyor. Programdan çıkış sağlandı.")
                    break
                elif kar > 0:
                    print(f"{kar}₺ kârınız bulunuyor. Programdan çıkış sağlandı.")
                    break
                else:
                    print("Ne kârınız ne de zararınız bulunmamaktadır. Programdan çıkış sağlandı.")
                    break
            elif dg.upper()=="H":
                print("Programdan çıkış sağlandı.")
                break
            else:
                print("Hatalı seçim.")
        break
    else:
        print("Hatalı seçim. Menüye yönlendiriliyorsunuz.")
        time.sleep(3)