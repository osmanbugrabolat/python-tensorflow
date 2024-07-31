#Range Methodu

for i in range(7,25,2):  #7'den başlayıp 25'e kadar 2'şer 2'şer artır
    print(i)


#Enumerae Methodu


for (index,numara) in enumerate(list(range(0,15,2))):  #numaralandırma indexleme
    print(f"index: {index} , numara: {numara}")


#Random Methodu

from random import randint

print(randint(0,100)) # 0 ile 100 arasında rastgele bir int sayı oluştur

from random import shuffle

liste = [1,2,3,4,5,6,7,8,9,10]
shuffle(liste)  #listeyi rastgele karıştır
print(liste)


#Örnek çalışma
#bir listenin random elemanını yazdırma

newListe = ["a", "b", "c", "d", "e", "f", "g", "h"]

index = randint(0,7)

print(newListe[index])


#Zip Methodu

#Birden fazla listeyi birleştirmek için kullanılır

yemek = ["muz", "kivi", "çilek"]
kalori = [100,200,300]
gunler = ["pazartesi", "salı", "carsamba"]

ziplenmisListe = list(zip(yemek,kalori,gunler)) #indexe göre birleştir ve bir liste olarak oluştur
print(ziplenmisListe)


#Bir stringi listeye çevirme
bosListe = []
isim = "osman bugra bolat"

for harf in isim:
    bosListe.append(harf)

print(bosListe)

#Kısayolu
yeniListe = [eleman for eleman in isim]

print("yeni: ", yeniListe)




#Map Methodu
def kontrol(string):
    return "a" in string

strListe = ["a","b","c,","da","e","f","ag"]

sonucListesi = list(map(kontrol, strListe))
print(sonucListesi)

#Filter Methodu
trueListesi = list(filter(kontrol, strListe))

print(trueListesi)