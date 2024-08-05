#Fonskiyon/Method Tanımlama

def fonksiyon(isim):  #isim adında bir parametre alıp bunu yazdıran fonksiyon
    print(isim)

fonksiyon("bugra")


#Input & Return İşlemleri

def fonk(isim="bugra"): #Eğer fonksiyona parametre verilmezse bugra verilirse verildiği değeri yazdır
    print(isim)

fonk("osman")
fonk()


def toplama(num1,num2):
    return num1+num2

toplam = toplama(2,3)
print(toplam)



#Args & Kwargs

def argsToplam(*args):  #Sınırsız sayıda(verilen kadar) argümanı
    return sum(args) #topla

sınırsızToplam = argsToplam(1,2,3,4,5,6,7,8,9,10)
print(sınırsızToplam)


def ornek(**kwargs):  #sınırsız anahtar değer eşleşmelerinde kullanılır(**)
    print(kwargs)  #return olursa türü dict

ornek(muz =100, elma=200,çilek=300, kivi=500,ananas=600)  



