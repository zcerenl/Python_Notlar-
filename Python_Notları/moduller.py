# import os (operation system)
# import math (matematik işlemleri)
# import random (random değer üretimi)
# import time (zaman fonksiyonları)
# dir(modul_adi) fonksiyon listesi gösterir
# help(modul_adi) uzun açıklamalar yazar.
# python docs kullanılabilir.

# import math 

# x = math.factorial(12)
# print(x)

# 1'den 100'e kadar çift sayıları bir listeye ekle ve listeyi ekrana yazdır.

# liste1 = []
# liste2 = []
# for i in range(1,101):
#     print(i)
#     if i % 2 == 0:
#         liste1.append(i) 
#     else:
#         liste2.append(i)
# else: 
#     print("Sayı 100'ü geçti program duruyor.")
# print(liste1)
# print(liste2)

# i = 0
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print('İşlem Bitti')

# print(2**63)
# 2**(62 * 30)-1

#ekrana girilen sayının armstrong sayısı olup olmadığını bulma.

# 1**4 6**4 9**4 3**4 = 1693

# # x = int(input("bir sayı giriniz: "))
# print(x)

# basamaklar = list(f'{x}')
# print(basamaklar)

x = int(input("bir sayı giriniz: "))
y = len(str(x))
sonuc = 0
print(y)
for i in str(x):
    sonuc += int(i) ** y
if sonuc == x:
    print("yes")
else:
    print("no")
