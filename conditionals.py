istenenKredi= 100000
hesap= 9555
minimumOlmasiGerekenHesap= 10000

if hesap >= minimumOlmasiGerekenHesap:
    print("kredi verilebilir")
    print("ödemeler hesaplandi")

elif hesap >= 9000 and hesap<=9500 : #and iki durumun da geçerli olması gerektiğidir.
    print("müdüre sorulacak")

elif hesap>=9501 and hesap <=9999:
    print("Genel müdüre sorulacak")

else:
    print("kredi almak için bakiyeniz yetersizdir.")

print("işlem sonu")

