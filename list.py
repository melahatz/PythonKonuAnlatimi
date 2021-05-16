#anasayfada 20 tane ürün geliyor mesela köşeli parantez şeklinde koyduğun verilere list adını veriyrouz.

urunler=["laptop","mouse","keyboard"]
print(urunler)
print(type(urunler))
urunler.append("telefon")
print(urunler)

#liste bir referans tiptir. değer ve referansa değinecek olursak.claslar,dziler referans tiptir.heap de gerçekleşir.stack de tanımladığını
#heap de yer açıyor tutarken adres değeri vasıtasıyla tutuyor bellekte.Yani tanımladıkları referans numarasıyla eşleştirmiş oluyor tameamen
#sadece adresi bilmiş oluyorlar.

ogreciler1=["melo","tugba","esra"]
ogrenciler2=["gamze","halil","cavid"]
ogreciler1=ogrenciler2
ogrenciler2[0]="berkay"
print(ogreciler1)
print(ogrenciler2)
print("\n")

#değer tip int. sayısal veri tipleri değer tiptir.boolen float. olay stack de gerçekleşir.değer tipte atama yapıyorsn tamamen 
#değerle ilgilenir. 
sayi1=10
sayi2=20
sayi1=sayi2
sayi2=60
print(sayi2)
