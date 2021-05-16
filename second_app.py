
e="34"*3 #str ifadeyi metin olrak algılayıp 3 defa yazdırıyor dikkar edceğimiz ikisinin de aynı tipte olması gerekir
print(e)

#***********indexleme ve dilimleme********
hello="dünya"
print(hello) 
print(hello[0]) #parantez içine yazdığın indeksin değerini çağırmış oluyorsun
print(hello[1])
print(hello[2])
print(hello[3])
print(hello[4]) 
print("\n")
ders="programlama"
print(ders[-2]) #tersten 1 den başlayarak istediği indeksin çıktısını vericektir.

print(hello[2:4]) #[x:y] x->başlagıç y-> bitiş x elemanını dahil eder fakat y elemanını dahil etmez.

hello[::-1] #[başlangıç:bitiş:adım] 
print(hello[::-1])
print("\n\n")
#.capitalize() metodunu baş harfi büyütmek için kullanırsın
deger="python learning"
print(deger.capitalize())
print("\n")
#upper metoduyla da bütün harfleri büyütüyoruz
print(deger.upper)
#input metodu değeri her zaman string olarak tutar,kullanıcıdan bilgi ister
y=input("lütfen bir mükemmel sayi giriniz:")
print(y)
x=int(input("lütfen bir int değer giriniz:"))

