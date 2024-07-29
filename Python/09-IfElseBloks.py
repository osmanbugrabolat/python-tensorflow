# İf Else Staetment

x = 5
y = 3

if x > y:
    print("x değişkeni y'den büyüktür")
else:
    print("x y'den büyük değildir")



a = 12
b = 25

if a > b:
    print("a > b")
elif b > a:
    print("b > a")
else:
    print("a = b")


username = input("Lütfen bir kullanıcı adı giriniz: ")
password = input("Lütfen bir şifre giriniz: ")

#Python büyük küçük harf duyarlıdır
if username == "Osman" and password == "12345":
    print("Tebrikler! Giriş yaptınız...")
elif username == "Osman" and password != "12345":
    print("Kullanıcı adı doğru fakat şifre yanlış!!!")
elif username != "Osman" and password == "12345":
    print("Kullanıcı adı yanlış fakat şifre doğru!!!")
else:
    print("Kullanıcı adı ve şifre yanlış!!!")


#Listelerde if else kullanımı

liste = [1,2,3,4,5,6,7,8,9,10]

sayi=int(input("Lütfen aramak istediğiniz sayıyı seçiniz: "))

if sayi in liste:
    print("Aradığınız sayı listenin içerisinde var.")
else:
    print("Aradığınız sayı liste içerisinde yok.")
