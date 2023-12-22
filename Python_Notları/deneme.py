# print("Hello World!")

# degiskenAdi = "değer"
# x = 5.8
# print(type(x))
# print(type(degiskenAdi))
# x = int(x)
# print(x)

# y = "5"

# x, y, z = 5, 10, 15

# meyve1, meyve2, meyve3 = "elma", "muz", "kiraz"
# print(meyve1, meyve2, meyve3)

# a = b = c = "portakal"
# print(c)

# print(a + b + c)

# x = 5
# y = "Yağız"
# text = " {} Yağız"
# print(text.format(x))

# adet = 11
# birimFiyat = 22
# text = "Pazardan {1} tl'ye {0} ayakkabı aldım."
# print(text.format(adet, birimFiyat))

# text = "Merhabaa."
# text2 = "Hello, Hello"
#print(len(text))
#print(text[::-1])  metni tersten yazdırma
#print(text[başlangıç index'i: bitiş index'i:adım sayısı])
# print(text.strip())
# print(text.replace("M","H"))
# print(text2.split(','))



# print(text.capitalize()) #ilk harfi büyütür.
# print(text.find("aba")) # metin araması yaparak varsa index'ini döndürür.

# print(text.endswith('aa'))
# print(text[-8])
# print(text[0])
# print(text.lower())
# print(text.upper())
# print(text.swapcase())
# print(text.isalnum())
# print(text.isdigit())
# print(text.islower())
# print(text.isupper())
""" 
asdasd
"""

'''
asdasd
'''

#Number

# int, float, complex
x = 5
y = 5.0

# print(type(x))
# print(type(y))

#LİSTE =>

mylist = ["kiraz","armut","elma"]

print(len(mylist))

mylist[0] = "muz"
print(mylist)
print(type(mylist))

meyve = ("elma", "armut")

#boolean
isTrue = True
isFalse = False

"""
Karşılaştırma Operatörleri =>
== soldaki sağdakine eşit mi
<= soldaki sağdakinden küçük yada eşit mi
< soldaki sağdakinden küçük mü
>= soldaki sağdakinden büyük yada eşit mi
> soldaki sağdakinden büyük mü
!= soldaki sağdakine eşit değil mi

ARİTMETİK OPERATORLER =>
+ toplama
- çıkarma
/ bölme
* çarpma
%  mod alma
** üs alma
// Karekök alma

ATAMA OPERATORLERİ =>
= atama
+=   x += 1 // x = x + 1
-=   x -= 1
*=
/= 
%= 
//=
**=

MANTIKSAL OPERATORLER =>
and
or
not
"""
# gun = int(input('Gün sayısını giriniz: '))

# if 0 <= gun < 7:
#     if gun == 5:
#         print("Cuma")
#     elif gun == 0:
#         print("Pazar")
#     elif gun == 1:
#         print('Pazartesi')
#     elif gun == 2:
#         print('Salı')
#     elif gun == 3:
#         print('Çarşamba')
#     elif gun == 4:
#         print('Perşembe')
#     elif gun == 6:
#         print('Cumartesi')
# else:
#     print('Bir Hata Oluştu')

# saat = int(input("Lütfen saat Değerini Girin: "))

# if 0 <= saat < 24:
#     if 6 <= saat < 12:
#         print(f'Saat: {saat}, Günaydın.')
#     elif 12 <= saat < 18:
#         print(f'Saat: {saat}, İyi Günler.')
#     elif 18 <= saat < 22:
#         print(f'Saat: {saat}, İyi Akşamlar.')
#     else:
#         print(f'Saat: {saat}, İyi Geceler.')
# else: 
#     print("Saat Değeri Geçersiz.")

#ornek-2 ehliyet sorgusu

#18'den büyük ve en azından lise mezunu olan kişiler ehliyet alabilsin, aksi durumda alamasın.

yas = int(input('Lütfen Yaşınızı Giriniz: '))

if yas >= 18:
    egitimDurumu = input('Eğitim Durumunuz: ')
    if egitimDurumu == ("lise" or "universite"):
        print('Ehliyet Almaya Uygunsunuz.')
    else:
        print('Ehliyet almak için eğitim durumunuz yetersiz.')
else:
    print('Ehliyet almaya yaşınız tutmuyor.')


# listem = ["elma", "armut", 35, True]

# print(listem[2])
# print(len(listem))
# print(listem[::-1])
# print(listem[-1])
# print(listem[len(listem) -1])

# liste1 = [1,2,3]
# liste2 = [4,5,6]
# liste3 = liste1 + liste2
# print(liste3)
# liste4 = liste1 * 3
# print(liste4)

#list  / tuple / set / dict

# meyve1 = "elma"
# meyve2 = "armut"

# meyveler = ("elma",)
# meyveler = ("elma","armut")

# listem = ["elma", "armut", "muz", "şeftali", "karpuz"]
# listem[0] = "ejdermeyvesi"
# listem[-1] = "kavun"

# listem[0:-1] = ["ejdermeyvesi", "kavun"]

#listeye sondan yeni bir eleman eklemek için
# listem.append("ejdermeyvesi")
# print(listem)

#listeye spesifik bir index'ten ekleme yapmak
# liste2 = [1, 3, 4, 5] 
# print(liste2)
# liste2.insert(1,2)
# print(liste2)

#remove()  elemanın kendisi yazılır.
# liste2.remove(5)
# print(liste2)

#pop() index numarası ile eleman silmek
# liste2.pop(1)
# print(liste2)

# del liste2
# del liste2[0]


#listenin kendisini tutup içindeki elemanları silmek
# liste2.clear()

# liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in liste:
#     print(i)

# liste = ["Ahmet", "Mehmet", "Cemil"]
# liste.sort()
# print(liste)

# liste.reverse()
# print(liste)

# liste = ["100", "25", "28", "33"]
# liste.sort()
# # liste.sort(reverse = True)
# liste.reverse()
# print(liste)

# liste = [100, 25, 28, 33,"100"]
# liste2 = []

# for i in range(0, len(liste)):
#     liste[i] = int(liste[i])

# # liste.sort()

# print(liste)
# print(liste2)

# list = [1,2,3,4,5,6]
# list2 = []
# list3 = list("elma")
# print(list3)

# list2 = list.copy()
# list2 = list(list)
# print(list2)
# print(list)
# list.pop(0)
# print(list2)
# print(list)


# for i in "banana":
#     print(i)

# liste = [1,2,3,4,5,6]
# for i in liste:
#     print(i)

# for i in range(0,101):
#     print(i)

# for i in range(0,10):
#     for j in range(0,11):
#         print(f'{i} * {j} = {i * j}')


