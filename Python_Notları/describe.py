'''
Kullanıcıdan vize1 vize2 ve final isteyelim.
BU değerler geçerli bir sayı mı kontrol edelim.
Geçerli not girildi mi kontol edelim.
x sayıda öğrenci için isteyelim
liste içine belirli bir sırayla atalım.
Problem => not hesaplama 
aa 90, 100 arası
ba 85, 90 arası
bb 80, 85 arası
cb 75, 80 arası
cc 70, 75 arası
dc 65, 70 arası
dd 50, 65 arası
fd 40, 50 arası
ff 40 altı
'''

import time

def harfNotu(deger):
    if deger >= 90:
        return "AA"
    elif deger >= 85:
        return "BA"
    elif deger >= 80:
        return "BB"
    elif deger >= 75:
        return "CB"
    elif deger >= 70:
        return "CC"
    elif deger >= 65:
        return "DC"
    elif deger >= 60:
        return "DD"
    elif deger >= 55:
        return "FD"
    elif deger < 55:
        return "FF"
    else:
        print('Not Hesaplaması bir hata verdi.')
        return "Hesaplama Başarısız"

def gectiMi(deger):
    if deger > 50:
        return "Geçti" 
    else: 
        return "Geçmedi"

def sonucGoster(deger1,deger2,deger3):
    yilsonu = (int(deger1) * 0.3) + (int(deger2) * 0.3) + (int(deger3) *  0.4)
    harf = harfNotu(yilsonu)
    gecerMi = gectiMi(yilsonu)
    print(f'''
    Yılsonu Not Ortalamanız: {yilsonu},
    Harf Notunuz: {harf},
    Durum: {gecerMi}
    ''') 

##################
print('''
----------------------
Not Hesaplama Programı
----------------------
''')
vize1 = input('Lütfen ilk vize notunuzu girin: ')
vize2 = input('Lütfen ikinci vize notunuzu girin: ')
final = input('Lütfen final notunuzu girin: ')
while True:
    if not vize1.isdigit() or 0 >= int(vize1) >= 100:
        print('Vize 1 Değerini Yanlış Girdiniz.')
        vize1 = input('Lütfen ilk vize notunuzu girin: ')
    elif not vize2.isdigit() or 0 >= int(vize2) >= 100:
        print('Vize 2 Değerini Yanlış Girdiniz.')
        vize2 = input('Lütfen ikinci vize notunuzu girin: ')
    elif not final.isdigit() or 0 >= int(final) >= 100:
        print('Final Değerini Yanlış Girdiniz.')
        final = input('Lütfen final notunuzu girin: ')
    else:
        print('Değerler Doğru Hesaplamaya Başlanıyor.')
        time.sleep(2)
        sonucGoster(vize1,vize2,final)
        break
##################