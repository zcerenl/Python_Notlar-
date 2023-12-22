
# def selamla(ad,soyad):
#     print(f'Merhaba {ad} {soyad}')
#     print("Merhaba {} {}".format(ad,soyad))

# isim = input('Lütfen Adınızı Girin: ')
# soyisim = input('Lütfen Soyadınızı Girin: ')
# selamla(isim,soyisim)

# def topla(*args):
#     sonuc = 0

#     for i in args:
#         sonuc += int(i)
#     print(f'Girilen Sayıların Toplamı {sonuc}')


# topla(2,3,4)
# topla(5,11,16,2,-2,9,14,22)

# liste1 = [1,2,3,4,5]
# liste2 = []
# for i in liste1:
#     liste2.append(i * 2)

# print(liste1)
# print(liste2)


# liste1 = [1,2,3,4,5]
# liste2 = [i * 3 for i in liste1]
# print(liste1)
# print(liste2)

# def ikiyleCarp(x):
#     return x * 2
# def ciftMi(x):
#     return x % 2 == 0

# ikiyleCarp = lambda x : x * 2
# ciftMi = lambda x : x % 2 == 0


# def topla(x,y,z):
#     return x + y + z

# def topla2(x,y,z):
#     return print(x + y + z)

# topla = lambda x,y,z : x + y + z
# topla2 = lambda x,y,z : print(x + y + z)



# def my_func(a):
#     global x
#     x = a
#     print(x)


# my_func(175)
# print(x)

# Problem => girilen sayının asal olup olmadığını bulan program True yada False
#2 en küçük asal sayıdır.
#1 ve kendisi haricinde hiçbir sayıya tam bölünemeyen sayılar asal sayılardır. 
# Örnek => 2, 3, 7, 11, 13, 17, 19 ..... 127, 151

# def asalMi(x):
#     if x <= 1:
#         return False
#     elif x == 2:
#         print('elif çalıştı')
#         return True
#     for i in range(2, x): 
#         print(f'{x} % {i} == {x % i == 0}')
#         if x % i == 0:
#             return False
#     return True

# print(asalMi(121))


# def isPrime(n):
#     for i in range(2, int(n**0.5)+1):
#         # print(f'{int(n**0.5)+1} % {i} == {n % i == 0}')
#         if n % i == 0:
#             return False
#     return True

# # print(isPrime(157007))
# # 151

# # asal mı fonksiyonunu kullanarak 10001. asal sayıyı bulun.

# #104743

# def nthPrime(n):
#     counter = 0
#     for i in range(2, n**2):
#         if isPrime(i):
#             counter += 1
#             # print(f'{i}, {counter}. asal sayıdır.')
#         if counter == n:
#             # print(f'{counter}. asal sayı {i}dir.')
#             return i

# print(nthPrime(100001))

# def nth_prime(n):
#     counter = 2
#     for i in range(3, n**2, 2):
#         k = 1
#         while k*k < i:
#             k += 2
#             if i % k == 0:
#                break
#         else:
#             counter += 1
#         if counter == n:
#             return i

# print(nth_prime(10001))


# liste1 ve liste2 'ye 0'dan 10'a kadar olan sayıları atan, ardından bunları çarpıp çarpımlarını ve sayıları doğru formatta ekrana yazdıran bir program yazalım. program çalışması durmadan önce listelerdeki elemanlar silinsin.

# liste1 = []
# liste2 = []
# def carpimTablosu():
#     for i in range(0,10):
#         liste1.append(i)
#     liste2 = liste1.copy()
#     for i in liste1:
#         for x in liste2:
#             print(f'{i} * {x} = {i * x}')
#         print('------')
#     print(liste1, liste2)
#     liste1.clear()
#     liste2.clear()   
#     print(liste1, liste2)

# carpimTablosu()

#ekok bulma
# 6 * 5 = 
import math
def ekokBul(x,y):
    buyukSayi = max(x,y)
    
    for i in range(3, x * y + 1):
        # print(i)
        if x % i == 0 and y % i == 0:
            return int((x * y) / i)
        # elif x :

    return x * y


print(ekokBul(5,6))
print(ekokBul(2,6))
print(ekokBul(4,8))
print(ekokBul(16,12))
print(ekokBul(2,2))
print(ekokBul(6,9))
print(ekokBul(8,4))
print(ekokBul(9,27))
print(ekokBul(3,9))

# 2 * 6 / 2
# 4 * 8 / 2


# 
# 

# import math as matematik
# from math import *

# print(min(5,8)) #return en küçük sayı
# print(max(5,8)) #return en büyük sayı
# print(abs(-5)) #return tüm sayıları pozitife çevirir.
# print(pow(2,5)) # 2 üzeri 5 değerini alır.
# print(pow(2,pow(2,5))) # 2 üzeri 2 üzeri 5 değerini alır.
# print(2**2**5) # 2 üzeri 2 üzeri 5 değerini alır

# print(tau)
# print(pi)
# print(ceil(4.1))
# print(pow(2,5))
# print(factorial(6)) #   6 * 5 * 4 * 3 * 2 * 1
# print(perm())
# print(sqrt(36)) #6
# print(36**0.5) #6
# print(floor(4.9))
# print(int(4.9))

# print(isnan(9)) #is not a number (bu bir sayı değil mi?)
# print(isfinite(0 / 2)) # sayılabilir sayı mı
# print(isinf(0 / 2)) #sayılamaz bi sayı mı ?

import datetime as time


# # x = datetime.datetime.now()
# x = timee.datetime.now()
# # x = time.datetime(2012, )
# print(x.hour)
# print(x.second)

# print(x.strftime('%a')) #kısa gün ismi
# print(x.strftime('%A')) #uzun gün ismi
# print(x.strftime('%w')) #0'dan 6'ya gün sayısı
# print(x.strftime('%d')) #1'dan 31'a kadar aydaki gün sayısı
# print(x.strftime('%b')) #ay adı kısa
# print(x.strftime('%B')) #ay adı uzun
# print(x.strftime('%y')) # kısa yıl adı (23,18)
# print(x.strftime('%Y')) #(2017, 2023)
# print(x.strftime('%m')) # yılın hangi ayı sayıyla
# print(x.strftime('%H')) #saat 00 /23
# print(x.strftime('%I')) #saat 00 /12
# print(x.strftime('%M')) #dakika
# print(x.strftime('%S')) #saniye 
# print(x.strftime('%f')) #mikrosaniye
# print(x.strftime('%p')) #am-pm
# print(x.strftime('%j')) #yılın kaçıncı günü
# print(x.strftime('%W')) #yılın kaçıncı haftası
# print(x.strftime('%X')) #Local Zaman 17:16:00


# x = timee.datetime.now()
# t = x.strftime('%H:%M:%S')
# print(f'Saat: {t}')

# #gün/ay/yıl, saat:dakika:saniye
# t2 = x.strftime('%A/%B/%Y, %H:%M:%S')
# print(t2)

x = 2j
print(x)
print(type(x))

a = time.datetime.now()

print(f'gün: {a.day}')
gun = a.day
print(f'gün: {gun}')

