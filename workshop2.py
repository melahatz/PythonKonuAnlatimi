#faktöriyel bulma

sayi = int(input("sayı :"))

faktoriyel=1

if sayi<0 :
    print("negatif sayilarin faktoriyeli hesaplanamaz:")

elif sayi==0 :
    print("sonuc :1")

else: 
    for i in range(1,sayi+1):
        faktoriyel=faktoriyel*i
    print("sonuc: ", faktoriyel)    