print("merhaba dünya") #yadırırken tek tırnak ile de yapabilirisn

print("ali\'nin evi")#alinin evini tırak ayırırkne yazmak istersen kaçış karakterini kullan
print("merhaba\n dünya") #\t tab olarak anlar birkaç adım ileri gidip yazdırır, \n bir satır aşağıya yazdırır
print("\n")
#******değişken tanımlama****** bir defa değişken tanımla diğer yerlerde kolayca kullan
#variable(değişken)=value(değer)
n=2*3
print(n)
mesaj="I"
mesaj2="coding"
print(mesaj+" "+mesaj2) #ikisi birleşik yazmak isterken
print("\n\n")
#*****veri tipleri*****
#string
hello="world" #kırmızı ve tırnak içinde olanlar string
print(hello)
print("world")
print(n)
print("\n")
#type()
type(hello) #çıktısı str yani string olduğunu öğrenmek istiyorsak
print(type(hello))
int_value=5
print(type(int_value))#çıktısı int olur tipini öğrenmek isterken bunu kullan
print("\n")

#swamming(değiş tokuş etme)
data1=3
data2=4
data3=6
data4=8
data1,data2,data3,data4=data2,data4,data1,data3
print(data1,data2,data3,data4)
print("\n")

#len karakter sayisini sayar
metin=" " " merhaba benim adım melahat harran üniversitesi bilgisayar mühendisliği 1. sınıf okumaktayım\n"
len(metin) #yazmasanda olur buraya aşağıda çıktsını alıcaksın print ile.
print(len(metin))
#int ifadelerde ve float ifadelerde len yok sayısal ifadelerde len kullanılmaz.
print("\n")


 


