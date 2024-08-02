class Kahraman():
    guc = "AI Development"

    def __init__(self,isim,yas,meslek): # Bir nesne oluşurken (initilize) çalışacak özel fonksiyon
        print("İnit çağrıldı")
        self.isim = isim
        self.yas = yas
        self.meslek = meslek
    
    def method1(self):
        print(f"Bu kahramanın mesleği: {self.meslek}")

kahraman = Kahraman("Bugra", 30, "Developer")

print(kahraman.guc)

kahraman.method1()


class Kopek():

    def __init__(self,yas=5): #nesne oluşturulurken yas için değer girilmezse default olarak 5 gir
        self.yas = yas

kopek = Kopek(3)

kopek2 = Kopek()

print(f"kopek: {kopek.yas}, kopek2: {kopek2.yas}")




