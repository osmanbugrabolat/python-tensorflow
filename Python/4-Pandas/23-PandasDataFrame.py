import numpy as np
import pandas as pd

data = np.random.randn(4,3)

print(data)

dataFrame = pd.DataFrame(data)  #Excel tablosu formatında bir frmae oluşturur
print(dataFrame)

newDataFrame = pd.DataFrame(data, index=["Ata", "Bugra","Zeynep","Göktürk"], columns=["Maaş", "Yaş", "Ücret"])

print(newDataFrame)
print(newDataFrame["Maaş"]) #Sütun değerleri alınır

print(newDataFrame.loc["Bugra"])  #Satır değerleri alınır


newDataFrame["Çalışma Saati"] = newDataFrame["Maaş"] / 2  #Sütun ekleme

print(newDataFrame)



newDataFrame = newDataFrame.drop("Çalışma Saati", axis=1)  #Sütun silme Satır için axis 0 olmalı
print(newDataFrame)

newDataFrame["Çalışma Saati"] = newDataFrame["Maaş"] / 2
print(newDataFrame)

newDataFrame.drop("Çalışma Saati", axis=1, inplace=True) #Yapılırsa direkt data frame üzerinde siler
print(newDataFrame)



print(newDataFrame.loc["Zeynep","Yaş"])


print(newDataFrame[newDataFrame["Maaş"]>0])


yeniIndex = newDataFrame.reset_index()

print(yeniIndex)

indexList = ["a","b","z","g"]
newDataFrame["Yeni İndex"] = indexList

newDataFrame.set_index("Yeni İndex", inplace=True)

print(newDataFrame)


print(newDataFrame.loc["a"])


#Multi Index

ilkIndex = ["Z","Z","Z","B","B","B"]
icIndex = ["A","B","C","D","E","F"]


birlesmisIndex = list(zip(ilkIndex,icIndex))

birlesmisIndex = pd.MultiIndex.from_tuples(birlesmisIndex)

liste = [[40,"Ata"], [50,"Bugra"],[60,"Zeynep"],[70,"Göktürk"],[80, "Talat"],[100,"Enver"]]

numpyArray= np.array(liste)

multiFrame = pd.DataFrame(numpyArray,index=birlesmisIndex, columns=["Yaş", "İsim"])

print(multiFrame)

print(multiFrame.loc["Z"])

multiFrame.index.names = ["Koç","Grup"]

print(multiFrame)