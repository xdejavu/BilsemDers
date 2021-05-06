print("""HESAP MAKİNESİ UYGULAMASI
"1.Toplama
2.Çıkarma
3.Çarpma
4.Bölme""")
islem=input("İşlem Seçiniz 1/4: ")
if islem=="1"or islem=="2" or islem=="3" or islem=="4":

 sayi1=int(input("1.sayıyı giriniz"))
 sayi2=int(input("2.sayiyi giriniz"))
if islem=="1":
    print("Sayılarımınız Toplamı:",(sayi1+sayi2))
elif islem=="2":
    print("Sayılarınızın Farkı:",(sayi1-sayi2))
elif islem=="3":
    print("Sayılarınızın Çarpımı:",(sayi1*sayi2))
elif islem == "4":
    print("Sayılarınızın Bölümü:",(sayi1/sayi2))

else:
    print("Geçerli Sayı Giriniz")