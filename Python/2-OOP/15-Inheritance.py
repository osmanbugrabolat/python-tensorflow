 
class Hayvan():

    def __init__(self):
        print("Hayvan Sınıfı İniti çağırıldı")

    def method1(self):
        print("Method 1 çağırıldı")
      
    def method2(self):
        print("Method 2 çağırıldı")

    def method3(seelf):
        print("Method 3 çağırıldı") 


class Kedi(Hayvan):
    def __init__(self):
        print("Kedi Sınıfı İniti Çağırıldı")

    def method1(self):
        print("Bu override methoddur")
   


hayvan = Hayvan()

kedi = Kedi()

kedi.method1()
kedi.method2()