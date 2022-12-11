# SORU1
def onluktandonusum(num):
    if num >= 1:
        onluktandonusum(num // 2)
    print(num % 2, end=' ')


def ikiliktendonusum(num):
    value = 0
    for i in range(len(num)):
        digit = num.pop()
        if digit == '1':
            value = value + pow(2, i)
    print(value)


if __name__ == '__main__':
    decnum = int(input("Decimal sayı gir:"))
    binnum = list(input("binary sayi giriniz: "))
    onluktandonusum(decnum)
    ikiliktendonusum(binnum)


############################################################
# SORU2
def bolunduguSayilar(x):
    sayac = 1
    while (sayac < 10):
        if (x % sayac == 0):
            print(x, "sayısı", sayac, "sayısına tam bölünür.")
        sayac += 1


def asalMi(n):
    for i in range(2, int(n / 2)):
        if (n % i) == 0:
            return False
            break
        return True


def tekMiCiftMi(m):
    if (m % 2 == 0):
        return True
    return False


if __name__ == '__main__':
    sayi = int(input("Kontrol için sayı giriniz:"))
    if sayi:
        print("Evet bu sayı asaldır.")
    else:
        print("Hayır bu sayı asal değildir.")
    if (sayi % 2 == 0):
        print("Bu sayı çifttir.")
    else:
        print("Bu sayi tektir")
    asalMi(sayi)
    bolunduguSayilar(sayi)
    tekMiCiftMi(sayi)


############################################################
# SORU3
def mukemmelMi(m):
    toplam = 0
    for i in range(1, m):
        if (m % i) == 0:
            toplam += i
    if (toplam == m):
        print(m, "sayısı mükemmel sayıdır.")
    else:
        print(m, "sayısı mükemmel sayı değildir.")


if __name__ == '__main__':
    sayi = int(input("Sayıyı giriniz:"))
    mukemmelMi(sayi)


############################################################
# SORU4
def anagramMı(kelime1, kelime2):
    if (len(kelime1) == len(kelime2)):
        siralanmis_kelime1 = sorted(kelime1)
        siralanmis_kelime2 = sorted(kelime2)
        if (siralanmis_kelime1 == siralanmis_kelime2):
            return True
        return False


if __name__ == '__main__':
    kelime1 = str(input("İstenen birinci kelimeyi giriniz :"))
    kelime2 = str(input("İstenen birinci kelimeyi giriniz :"))
    sonuc = anagramMı(kelime1, kelime2)
    if sonuc:
        print("evet bu kelimeler anagram.")
    else:
        print("hayır bu kelimeler anagram değildir.")


############################################################
# SORU5
def fahrenheitToSantigrade():
    santigrade = (fahrenheit - 32) / 1.8
    print(fahrenheit, 'fahrenayt =', santigrade, "derece santigrata eşittir")


def santigratFahrenayt():
    fahrenayt = (santigrat * 1.8) + 32
    print(santigrat, 'santigrat =', fahrenayt, "fahrenayt değerine eşittir")


if __name__ == '__main__':
    fahrenheit = float(input("santigrata dönüştürmek için fahrenhayt değerini gir:"))
    santigrat = float(input("fahrenayta dönüştürmek üzere santigrat değeri gir:"))
    fahrenheitToSantigrade()
    santigratFahrenayt()
