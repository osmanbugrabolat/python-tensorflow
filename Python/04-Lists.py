string = "Osman Buğra BOLAT" 
#String ifadeler immutability yani string[0] = A şeklinde değiştirilemez!

#Listelerde Sayılar
liste = [1,2,3,4.2,5,6,7,8,9.3]
liste[0] = 0  #mutable yani değiştirilebilir
print(type(liste))

print(liste[0])

print(liste)
liste.append(22) #Listeye eleman ekleme
print(liste)
liste.remove(2) #Listeden eleman çıkarma
print(liste)
liste.pop() #Listeden son elemanı çıkarma
print(liste)
liste.count(2) #Listede 2 elemanından kaç tane var
print(liste)


#Listelerde String
strliste = ["a", "b", "c", "d", "e", "f"]
strliste[0] = 0  #mutable yani değiştirilebilir
print(type(strliste))

print(strliste[0])

print(strliste)
strliste.append(22) #Listeye int eleman ekleme
print(strliste)
strliste.append("22") #Listeye str eleman ekleme
print(strliste)
karısıkliste = liste + strliste
print(karısıkliste)


#İç içe listeler
nestedList = [1,2,3,["a","b","c",4,5]]
print(nestedList)



