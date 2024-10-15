import json

with open('users.json','r',encoding='utf-8') as users_dosyasi:
    kullanici_listesi = json.load(users_dosyasi)


#konsol ekranından girdi alıp değişkenlere atama yapıldı.
giris_yapan_kullanici_email = input("Lütfen email adresinizi giriniz:")
giris_yapan_kullanici_name = input("Lütfen adınızı giriniz:")

def login(email,name):
     for kullanici in kullanici_listesi:
         if kullanici["email"] == giris_yapan_kullanici_email and kullanici["name"] == giris_yapan_kullanici_name:
             print("Giriş işlemi başarılı")
             return True

     print("Kullanıcı adı veya isim hatalıdır. Tekrar dene.")
     return False




login(giris_yapan_kullanici_email,giris_yapan_kullanici_name)



