import numpy as np
import matplotlib.pyplot as plt


yas = [11,22,33,44,55,66,77,88,99,111]
kilo = [10,20,30,40,50,60,70,80,90,100]

yasnp = np.array(yas)
kilonp = np.array(kilo)

print(yasnp)
print(kilonp)
plt.subplot(1,2,1) #1 satırda 2 grafiğin 1.si
plt.plot(yasnp,kilonp,"g")
plt.title("Kilonun Yaşa Göre Değişimi")
plt.xlabel("Yaş")
plt.ylabel("Kilo")





npDizi = np.linspace(0,10,20)
npDizi2 = npDizi ** 3

plt.subplot(1,2,2)#1 satırda 2 grafiğin 2.si
plt.plot(npDizi,npDizi2,"r--")
plt.title("Küp Değişim Grafiği")
plt.xlabel("Değer")
plt.ylabel("Değerin Küpü")



plt.show()  #grafiği görmek için



