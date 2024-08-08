import numpy as np
import matplotlib.pyplot as plt

figure = plt.figure()

figureAxes = figure.add_axes([0.1,0.1,0.6,0.6])

npDizi = np.linspace(0,10,25)
npDizi2 = npDizi ** 3

figureAxes.plot(npDizi,npDizi2,"g")
figureAxes.set_xlabel("X değerleri")
figureAxes.set_ylabel("Y değerleri")

figure2 = plt.figure()

eksen1 = figure2.add_axes([0.1,0.1,0.7,0.7])
eksen2 = figure2.add_axes([0.25,0.4,0.3,0.3])

eksen1.plot(npDizi,npDizi2,"g")
eksen1.set_xlabel("X değerleri Eksen 1")
eksen1.set_ylabel("Y değerleri Eksen 1")

eksen2.plot(npDizi2,npDizi,"r--")
eksen2.set_xlabel("X değerleri Eksen 2")
eksen2.set_ylabel("Y değerleri Eksen 2")


plt.show()