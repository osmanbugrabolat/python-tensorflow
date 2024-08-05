import numpy as np
import pandas as pd

#Seriler

sozluk = {"Osman": 25, "Bugra": 12, "Bolat": 56}

seri = pd.Series(sozluk)

print(sozluk)
print(seri)

isimler = ["Osman", "Bugra", "Bolat"]
yaslar = [25,12,56]

newSeri = pd.Series(data=yaslar, index=isimler)


print(newSeri)