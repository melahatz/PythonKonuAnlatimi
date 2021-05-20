#liste,sözlük ve demet veri türü gibi birden çok veri türünü birlikte barındıran veri tipidir. Kümeler(set) ile ilgili yaptığınız her türlü
#işlevii(birleşme,kesişim vs.) bu veri tipi ile de yapabilrisiniz.

m={ "python",1,2,3,4,5,"learning","python","Icoding","python","python","java"}
print(m) #çıktısında pythondan bir tane yazdırmış olucak.

a=set("strong")
print(a) #çıktısı küme şeklinde -> s,t,r,o,n,g
len(m)
print(len(m)) #python yine 1 olarak sayılıyor çıktısı 9 olur
print("\n")

#.add eklemek için kullanıyorduk
m.add("html") 
print(m)
