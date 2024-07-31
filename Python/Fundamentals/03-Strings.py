#Metinler ve İşlemler


x = "osman buğra bolat"
print(len(x)) # değişkenin bit olarak uzunluğu

x = x.capitalize() #Büyük harf
print(x)

x = x.split() #Parçalara böl
print(x)



#Tür Dönüşümü
y = "5"
y = int(y)  #İnputtan alınan veri int türüne dönüştürüldü
print(y/2)


z = "Bu bir satır bölme \n işlemidir."
print(z)



#İndexleme
isim = "BugraninYasi25"
print(isim[0])  # ilk indexteki harf

print(isim[-1]) # son indexteki harf

#Slicing İşlemleri

print(isim[2:]) # 2. indexten sonuna kadar (start index)

print(isim[:3]) # Baştan 3 tane al (stop index)

print(isim[-2:]) # Son iki karakteri al

print(isim[::2]) # Baştan sonra birer atlıyarak al (step size)

print(isim[::-1]) # Tersten yazma


#Stringde Bazı Fonksiyonlar
string = "bu bir metin formatıdır"
print(string.upper()) # Bütün harfleri büyüt

print(string + ".") # Stringde toplama

print((string+("-")) * 3) # Stringde çarpma
