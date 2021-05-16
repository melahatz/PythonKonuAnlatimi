#fonksiyon tanımı---------------->def kayıt_oluştur(parametre1,parametre2,parametre3,parametre4)
#fonksiyon çağrısı yaparken ----->kayıt_oluştur(parametre1,parametre2,parametre3,parametre4)
#fonksiyon çağrısı bir formül sürekli yazmaktansa kolaylaştırmış oluyor.
#şimdi kısa fonksiyon çağrımı örnekleri yapalım
def toplama(a,b):
    toplam=a+b
    print(toplam)

toplama(4,9) #bunu bir adım içeride yazma çıktı alamazsın.
print("\n")
#**********************************************************************************************

def kayıt_olustur(isim,soyisim,issis,şehir):
    print("isim:           ",isim)
    print("soyisim:        ",soyisim)
    print("işletim sistemi:",issis)
    print("sehir:          ",şehir)

kayıt_olustur("melo", "zıkkelleci", "windows", "kayseri")    
print("\n")

#***********************************************************************************************

def ismin_ne():
    isim=input("ismin ne?")
    print(isim)
ismin_ne()    
print("\n")

#**********************************************************************************************


    



