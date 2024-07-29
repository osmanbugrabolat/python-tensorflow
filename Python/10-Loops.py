#For Döngüsü

liste = [1,2,3,4,5,6,7,8,9,10]

for eleman in liste:
    print(eleman * 2)

for eleman in liste:
    if eleman % 2 == 0:
        print(eleman)
    else:
        print("Eleman çift değil...")




koordinat = [(10.23, 23.45), (76.31, 11.2), (90, 1.1)]

for (x,y) in koordinat:
    print("X koordinatları: ", x)



# Continue - Break - Pass

yeniListe = [5,10,15,20,25,30,35,40,45,50]

for num in yeniListe:
    if num / 5 == 7:
        break
    else:
        print(num / 5)

print("-----------------------")

for num in yeniListe:
    if num / 5 == 7:
        continue
    else:
        print(num / 5)

print("-----------------------")

for num in yeniListe:
    if num / 5 == 7:
        pass # Kodun hata vermemesi için pass geçmek istediğimiz yerlerde kullanılır.
    else:
        print(num / 5)




#While Döngüsü

x = 0

while x <= 10:
    print(x)
    x = x + 1


degisken = 0

while degisken < 15:
    print(f"Değişkenin yeni değeri: {degisken * 5}")
    degisken = degisken + 1