#Fonksiyon 2 tane parametre alacak. Buraya 2 sayı gönderilecek. Girilenlerden hangisi büyükse o büyük yazacak.

def buyukolan(sayi1,sayi2):

    if (sayi1 > sayi2):
        buyuk = sayi1

    elif (sayi2 > sayi1):
        buyuk = sayi2

    print("Daha büyük sayı:", buyuk)



sayi1=(input("sayi1"))
sayi2=(input("sayi2"))
buyukolan(sayi1,sayi2)
