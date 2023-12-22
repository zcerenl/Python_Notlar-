# Sayı tahmin oyunu 1 ile 40 arasında ve 4 hak vererek 4.de kapanacak şekilde. 

# import random 

# randomsayi = random.randrange(0, 41)
# kalanHak = 4
# denemeSayisi = 1
# while True:
#     if kalanHak == 0:
#         print(f'Haklarınız tükendi. Girilen sayı {randomsayi} idi')
#         print('Programdan çıkılıyor...')
#         break
#     tahmin = input('Lütfen Tahmininizi Girin: ')
#     if  tahmin.isdigit():
#         tahmin = int(tahmin)
#         if not 0 <= tahmin <= 40:
#             print('Girilen sayı 0 ile 40 arasında olmalıdır.')
#             continue
#         elif tahmin > randomsayi:
#             print('lütfen daha küçük bir sayı giriniz.')
#             kalanHak -= 1
#             print(kalanHak)
#             denemeSayisi += 1
#             continue
#         elif tahmin < randomsayi:
#             print('Lütfen daha büyük bir sayı giriniz.')
#             kalanHak -= 1
#             print(kalanHak)
#             denemeSayisi += 1
#             continue
#         else: 
#             denemeSayisi += 1
#             print(f'Tebrikler {denemeSayisi}. denemede doğru bildin.')
#             break
#     else:
#         print('Lütfen geçerli bir sayı girin.')
#         continue 


# 10 sayısından küçük 3 veya 5'in katları 3, 5,6,9 sayıları ve bu sayıların topplamı 23'tür. 1000 sayısına kadar 3 ve 5'in katı olan tüm sayıları toplayın. sonuc 233168

# list1 = []
# for i in range(1,1000):
#     if i % 3 == 0 or i % 5 == 0:
#         list1.append(i)
# print(list1)
# sonuc = 0
# for i in list1:
#     sonuc += i
# print(sonuc)

# sonuc = 0
# for i in range(0,1000):
#     if i % 3 == 0 or i % 5 == 0:
#         sonuc += i
# print(sonuc)

# sonuc = sum(x for x in range(1,1000) if x % 3 == 0 or x % 5 == 0)

''' ilk fibonacci sayıları 1 ve 2'dir. her bir sonraki adım için son 2 adımdaki sayılar toplanarak ilerlenir. 
'''

# onceki = 0
# sonraki = 1
# sonuc = 0
# while onceki < 4000000:
#     if onceki % 2 == 0:
#         sonuc += onceki
#     if sonraki % 2 == 0:
#         sonuc += sonraki
#     onceki = sonraki + onceki
#     sonraki = onceki + sonraki
# else:
#     print(sonuc)


# onceki = 1
# sonraki = 1
# # onceki = sonraki = 1
# z = 0
# sonuc = 0
# z = sonuc = 0
# while onceki < 4000000:
#     if onceki % 2 == 0:
#         sonuc += onceki
#     z = onceki
#     onceki = sonraki
#     sonraki = z + sonraki

#     # z, onceki, sonraki = onceki, sonraki, z + sonraki

# print(sonuc)

list1 = [1,2,3,4,5,6,7,8,9,27,33,4,7]
list3 = []
sayi = 0
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] == list1[j]:
            sayi = list1[j]
            list3.append(sayi)
print(list3)





# list1 = [1,2,3,4,5,6,7,8,9,27,33,4,7]
# list2 = [10,11,12,13,14,15,16,27,33]
# list3 = []
# for i in list1:
#     for j in list2:
#         if i == j:
#             list3.append(i)

# print(list3)

