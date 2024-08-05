#Instance & Attribute

class Kahraman():
    def __init__(self,isim,yas,meslek): # Bir nesne oluşurken (initilize) çalışacak özel fonksiyon
        print("İnit çağrıldı")
        self.isim = isim
        self.yas = yas
        self.meslek = meslek

kahraman = Kahraman("Bugra", 30, "Developer")



