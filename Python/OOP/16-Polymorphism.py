#Aynı isimdeki methodun kendi sınıfına özel çalışabilmesi

class Elma():
    def __init__(self,isim):
      self.isim = isim
    def bilgiVer(self):
       return self.isim + " 100 kaloridir..."
    
class Muz():
    def __init__(self,isim):
      self.isim = isim
    def bilgiVer(self):
       return self.isim + " 200 kaloridir..."
    
elma = Elma("elma")
muz = Muz("muz")

meyveListesi = [elma,muz]


for m in meyveListesi:
   print(m.bilgiVer())
    