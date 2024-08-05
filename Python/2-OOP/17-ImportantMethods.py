class Meyve():
    def __init__(self,isim,kalori):
        self.isim=isim
        self.kalori=kalori
    
    def __str__(self):  #print işlemlerinde
        return f"{self.isim} meyvesi meyve sınıfına ait bir nesnedir."
    
    def __len__(self):  # len methodu özelleştirme
        return self.kalori
    


muz = Meyve("Muz", 200)



print(muz)
print(len(muz))
