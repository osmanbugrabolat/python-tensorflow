import numpy as np
import pandas as pd


#EKSİK VERİ DURUMU

havaDurumu = {"Tokat": [35,38,43], "Ankara": [25,np.nan,30],"Amasya": [np.nan,35,39]}

havaDurumuDataFrame = pd.DataFrame(havaDurumu)

print(havaDurumuDataFrame)

print(havaDurumuDataFrame.dropna()) #nan değer bulununan satırları siler
print(havaDurumuDataFrame.dropna(axis=1)) #nan değer bulunan sütunları siler


yeniHavaDurumu = {"Tokat": [35,38,43], "Ankara": [25,np.nan,30],"Amasya": [np.nan,35,39], "Istanbul": [np.nan, np.nan,38]}
yeniDataFrame = pd.DataFrame(yeniHavaDurumu)

print(yeniDataFrame)
print(havaDurumuDataFrame.dropna(axis=1, thresh=2)) #2 tane nan değer bulunan sütunları siler

yeniDataFrame =yeniDataFrame.fillna( yeniDataFrame.mean())
print(yeniDataFrame)



#GRUPLAMA DURUMU (groupby)

maasSozluk = {"Depertman": ["Yazılım", "Yazılım", "Finans","Finans", "İK","Hukuk"],
              "İsimler": ["Bugra", "Mehmet", "Ali", "Zeynep","Osman","Semra"],
              "Maaş": [100,2000,500,750,900,2000]}

maasDataFrame = pd.DataFrame(maasSozluk)

print(maasDataFrame)

gruplanmis = maasDataFrame.groupby("Depertman")  #Depertmana göre verileri grupla

print(gruplanmis.count()) #Gruplanmış verileri say
print(gruplanmis.max())

print(gruplanmis.describe())


#CONCAT İŞLEMİ

sozluk1 = {"İsim": ["a","b","c","d","e"],
           "Spor": ["Koşu","Basket","Futbol","Voleybol","Yüzme"],
           "Kalori": [100,200,230,350,500]}

sozluk2 = {"İsim": ["f","g","h","i","j"],
           "Spor": ["Koşu","Basket","Futbol","Voleybol","Yüzme"],
           "Kalori": [100,200,230,350,500]}

sozluk3 = {"İsim": ["k","l","m","n","o"],
           "Spor": ["Koşu","Basket","Futbol","Voleybol","Yüzme"],
           "Kalori": [100,200,230,350,500]}

dataFrame1 = pd.DataFrame(sozluk1,index=[0,1,2,3,4])
dataFrame2 = pd.DataFrame(sozluk2,index=[5,6,7,8,9])
dataFrame3 = pd.DataFrame(sozluk3,index=[10,11,12,13,14])
print(dataFrame1)
print(dataFrame2)
print(dataFrame3)

print(pd.concat([dataFrame1,dataFrame2,dataFrame3],axis=0))


#MERGE İŞLEMİ
#Belirli bir ortak noktaya göre birleştirmek
merge1 = {"İsim": ["a","b","c","d","e"],
           "Spor": ["Koşu","Basket","Futbol","Voleybol","Yüzme"]} 

dframe1 = pd.DataFrame(merge1)

merge2 = {"Spor": ["Koşu","Basket","Futbol","Voleybol","Yüzme"],
           "Kalori": [100,200,230,350,500]}
dframe2 = pd.DataFrame(merge2)

print(pd.merge(dframe1,dframe2,on="Spor"))


def carp(maas):
    return maas * 1.50

print(maasDataFrame["Maaş"].apply(carp))