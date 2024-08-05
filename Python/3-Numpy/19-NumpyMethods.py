import numpy as np

#ARANGE
np.arange(0,10)  #0'dan 10'a kadar bir numpy listesi oluştur

np.arange(0,10,2)  #0 dan 10a 2şer 2şer


#ZEROS & ONES

np.zeros(5)  # 5 tane 0 olan liste oluştur

np.zeros((2,2))  #2,2 şeklinde içinde 0 olan matris şeklinde liste

np.ones(3)   # 3 tane 1 olan liste

print(np.ones((6,6)))  #9,6 şeklinde içinde 1 olan matris şeklinde liste


#LINSPACE 

print(np.linspace(0,100,20))  #0 ile 100 arasını 20 eşit parçaya böl


#EYE

print(np.eye(10)) #10x10 Köşegen matris oluşturulur


#RANDOM

np.random.randn(4)

np.random.randn(4,4)

print(np.random.randint(1,50))

print(np.random.randint(1,50,5))


benimDizim = np.random.randint(1,100,15)

print(benimDizim)

#Numpy Dizi Methodları

benimMatrisDizim = benimDizim.reshape(3,5)
print(benimMatrisDizim)

print(benimDizim.max())

print(f"normal liste: {benimDizim.shape}, matris lise: {benimMatrisDizim.shape}")
