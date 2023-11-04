from kütüphane import *

print("""********************

Kütüphane Programına Hoşgeldiniz.

İşlemler;

1.Kitapları göster
2.Kitap sorgulama
3.Kitap ekle
4.Kitap sil
5.baskı Yükselt

Çıkmak için 'q' ya basın.
**********************""")
kütüphane=Kütüphane()
while True:
    islem=input("Yapacağınız işlem: ")

    if(islem=="q"):
        print("Program Sonlandırılıyor...")
        print("Yine bekleriz..")
        break
    elif (islem=="1"):
        kütüphane.kitapları_goster()
    elif (islem == "2"):
        isim=input("Hangi kitabı istiyorsunuz?")
        print("Kitap Sorgulanıyor...")
        time.sleep(2)

        kütüphane.kitap_sorgula(isim)
    elif (islem=="3"):
        isim=input("İsim: ")
        yazar=input("Yazar: ")
        yayınevi=input("yayınevi: ")
        tür=input("tür: ")
        baskı=int(input("baskı:"))

        yeni_kitap=Kitap(isim,yazar,yayınevi,tür,baskı)

        print("Kitap ekleniyor...")

        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi...")



    elif (islem == "4"):
        isim=input("Hangi kitabı silmek istiyorsunuz ?")

        cevap=input("Emin misiniz? (E/H)")
        if cevap=="E":
            print("Kitap siliniyor...")
            time.sleep(1)
            kütüphane.kitap_sil(isim)
            print("Kitap silindi...")
        else:
            print("Vazgeçiliyor...")
            continue

    elif (islem=="5"):
        isim=input("Hangi Kitabın baskısını yükseltmek istiyorsunuz ?")
        print("Baskı yükseltiliyor... ")
        time.sleep(2)
        kütüphane.baskı_yükselt(isim)
        print("Baskı yükseltildi...")

    else:
        print("Geçersiz işlem!!!!")
