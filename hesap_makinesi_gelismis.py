def hesap_makinesi():

    print("===gelismis hesap makinesi===")
    print("toplama: +")
    print("cikarma: -")
    print("carpma: *")
    print("bolme: /")
    print("cikis: q")
    print("üs alma: ^")
    print("karekok alma: √")
    print("faktoriyel alma: !")
    print("mod alma: %")

    while True:
        islem = input("islemi giriniz: ")
        if islem == "q":
            print("cikis yapildi")
            break
        elif islem == "+":
            sayi1 = int(input("birinci sayiyi giriniz: "))
            sayi2 = int(input("ikinci sayiyi giriniz: "))
            print(sayi1 + sayi2)
            continue
        elif islem == "-":
            sayi1 = int(input("birinci sayiyi giriniz: "))
            sayi2 = int(input("ikinci sayiyi giriniz: "))
            print(sayi1 - sayi2)
            continue
        elif islem == "*":
            sayi1 = int(input("birinci sayiyi giriniz: "))
            sayi2 = int(input("ikinci sayiyi giriniz: "))
            print(sayi1 * sayi2)
            continue
        elif islem == "/":
            sayi1 = int(input("birinci sayiyi giriniz: "))
            sayi2 = int(input("ikinci sayiyi giriniz: "))
            print(sayi1 / sayi2)
            continue
        elif islem == "^":
            sayi1 = int(input("taban sayiyi giriniz: "))
            sayi2 = int(input("us sayiyi giriniz: "))
            print(sayi1 ** sayi2)
            continue
        elif islem == "√":
            sayi1 = int(input("sayiyi giriniz: "))
            print(sayi1 ** 0.5)
            continue
        elif islem == "!":
            sayi1 = int(input("sayiyi giriniz: "))
            faktoriyel = 1
            for i in range(1, sayi1 + 1):
                faktoriyel *= i
            print(faktoriyel)
            continue
        elif islem == "%":
            sayi1 = int(input("birinci sayiyi giriniz: "))
            sayi2 = int(input("ikinci sayiyi giriniz: "))
            print(sayi1 % sayi2)
            continue
        else:
            print("gecersiz islem girdiniz: ") 
hesap_makinesi()

 
