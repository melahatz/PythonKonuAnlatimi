#list herhangi bir sayıda diğer objeleri içinde bulunduran bir sandık vazifesi görüyor.Diğer dillerdeki listelerden en önemli
#farkı ise bir listede birden fazla tip ögenin yanyana bulunabilmesi. Diğer konteyner tarzı objelerden farkı ise,listeker değişebilir
#olması ve sıralı olması diyebiliriz. Diğer konteynerlar;kümeler(set) ve sözlükler(dict)

#liste oluştururken
mylist=[9,8,7,6,"melo"]
print(mylist)
type(mylist)
print("\n")
print(mylist[0]) #indeksine ulaşıp tek tek çıktısını almak isterken...
print(mylist[2])
print(mylist[-1])

mylist[2]="python" #listeler farklı veri tiplerini birarada bulundurabilir çıktısı->[9,8,'python',6,'melo']
print(mylist)
print("\n")

#append():->ile listenin sonuna bir eleman ekleyebiliriz.
mylist.append('java')
mylist.append('java')
print(mylist)
print("\n")

#pop() -> ile listenin sonundaki elemanı silebilriz.
thelast=mylist.pop()
print(mylist)
print("\n")

#count() ->listede belirttiğin elemandan kaç tane olduğunu öprenmek isterken kullanabilirsin.
list1=["python","java", "C","python","C#","Ruby","python"]
list1.count("python")
print(list1.count("python")) #direk list1 diye de yazdırabiliriz
print("\n")

#remove() -> metodu ile bir elemanı silmek için yararlanabiliriz.
mylist.remove("python") 
print(mylist)
print("\n")

#sort() -> metodu ile listeyi küçükten büyüğe sıralayabilirsiniz.
list2=[4,6,2,9,1,5,0,3]
list2.sort()
print(list2)

#reserve metodu ile de büyükten küçüğe sıralayabiliriz.
list2.reverse()
print(list2)
print("\n")

mylist2=["python","java","computer"]
mylist2.sort() #alfabetik sıraya göre sıralamış olur çıktısı->computer,java,python olur
print(mylist2)






