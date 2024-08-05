import numpy as np

dizi = np.arange(0,20)

print(dizi[5])

print(dizi[3:8])
dizi[3:8] = 2

print(dizi)



newDizi = np.arange(0,50)

slicingDizi = newDizi[5:27]

slicingDizi[:] = 555

print(newDizi)  #Sadece slicingDiziyi değiştirmemize rağmen ana dizi de dğişti


ornekDizi = np.arange(0,25)

copyOrnekDizi = ornekDizi.copy()  #Bu sorunu kopyasını oluşturarak çözebiliriz

copyOrnekDizi[2:5] = 2323

print(ornekDizi)
print(copyOrnekDizi)



#MATRIX

benimDizim = np.random.randint(1,100,50)
benimMatrisDizim = benimDizim.reshape(10,5)

print(benimMatrisDizim[1,2])

print(benimMatrisDizim[:,2])
