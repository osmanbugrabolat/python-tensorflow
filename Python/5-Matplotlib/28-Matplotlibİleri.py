import numpy as np
import matplotlib.pyplot as plt


npDizi = np.linspace(0,10,20)
npDizi2 = npDizi ** 2

(bnmFigure, bnmEksen) = plt.subplots()


bnmEksen.plot(npDizi,npDizi2,color = "#3A95A8", linestyle = "-.")
bnmEksen.plot(npDizi2,npDizi,color = "red", linewidth = 6.0)
bnmEksen.plot(npDizi,npDizi2+2 ,color = "blue",linewidth = 4.0 ,linestyle=":", marker = "o")

plt.show()

#Scatter

plt.scatter(npDizi,npDizi**5 +2)

plt.show()
#Histogram

yeniDizi = np.random.randint(0,100,50)

plt.hist(yeniDizi)


plt.show()

#Bokplot

plt.boxplot(yeniDizi)
plt.show()