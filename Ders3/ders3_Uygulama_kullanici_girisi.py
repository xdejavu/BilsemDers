# kullanıcı adı admin parola 123456 olan bi rkullanıcı giriş ekranı yapınız.
# Doğru girildiğinde doğru giriş hatalı girildiğinde üzgünüm kullanıcı adınız ya da şifreniz yanlış yazsın.
kullaniciadi = input("Kullanıcı adını giriniz:")
sifre = input("Şifreyi giriniz:")
if kullaniciadi == "admin" and sifre == "123456":
    print("Doğru giriş")
else:
    print("Üzgünüm kullanıcı adınız ya da şifreniz yanlış")