#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boyboy)) hesaplayınız.

'''boycm = int(input("Lütfen boyunuzu (santimetre cinsinde) girin: "))
agirlik = int(input("Lütfen ağirliğinizi (kilogram cinsinde) girin: "))


boym = boycm / 100


vki = agirlik / (boym * boym)


print("Vücut Kitle İndeksiniz (VKİ):", vki)'''

#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.


'''maas = float(input("Lütfen maasinizi giriniz:  "))
zam_orani = float(input("Lütfen zam oranini giriniz:  "))

yeni_maas = maas + (maas * zam_orani / 100)

print("Güncel Maasiniz:", yeni_maas)'''

#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.


'''sayi1 = float(input("Birinci sayiyi giriniz: "))
sayi2 = float(input("İkinci sayiyi giriniz: "))
sayi3 = float(input("Üçüncü sayiyi giriniz: "))

en_büyük_sayi = max(sayi1, sayi2, sayi3)

print("En Büyük Sayi:", en_büyük_sayi)'''


#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)


'''daire_yaricapi = float(input("Dairenin Yari Capini Giriniz: "))

alani = 3.14 * daire_yaricapi * daire_yaricapi
cevresi = 2 * 3.14 * daire_yaricapi

print("Dairenin Alani: ", alani)
print("Dairenin Cevresi: ", cevresi)'''


#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.


'''sayi = input("Lütfen bir sayi giriniz: ")

tersten = sayi[::-1]

if sayi == tersten:
    print("Bu sayi bir palindromdur.")
else:
    print("Bu sayi bir palindrom değildir.")'''