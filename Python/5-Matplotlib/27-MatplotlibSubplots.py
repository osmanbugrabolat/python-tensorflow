import numpy as np
import matplotlib.pyplot as plt


npDizi = np.linspace(0,10,10)
npDizi2 = npDizi ** 3

(figure, eksenler) = plt.subplots(nrows=1, ncols=2) 

for eksen in eksenler:
    eksen.plot(npDizi,npDizi2,"b")


plt.tight_layout()



newFigure = plt.figure(dpi=100)
newEksen = newFigure.add_axes([0.1,0.1,0.8,0.8])

newEksen.plot(npDizi,npDizi2,"r*-", label = "label ** 3 ")
newEksen.plot(npDizi,npDizi ** 2,"g", label = "label ** 2 ")
newEksen.legend(loc=2)

newFigure.savefig("yenifigur.png",dpi=200)
plt.show()