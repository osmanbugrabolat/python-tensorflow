import numpy as np
import matplotlib.pyplot as plt


yas = [11,22,13,43,52,73,18,91,19,23]
kilo = [10,20,30,32,33,23,25,67,34,56]

yasnp = np.array(yas)
kilonp = np.array(kilo)

print(yasnp)
print(kilonp)

print(plt.plot(yasnp,kilonp,"g"))

