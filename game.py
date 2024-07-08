import random

para = int(input("Sayı Giriniz "))

say = random.randint(2,9)
sayı= str(say)

x = ("Yandın")
çek = ("çektim")
a1 = (input("ilerle (1) "))

if a1 == sayı:
    print =(x)
if a1 != sayı:
    a2 = (input("ileri? (2) "))
    if str(a2) == sayı:
        print(x , "-",para)
    if str(a2) == çek:
        print("çektiniz:" , para * 1.5 , "elenen basamak:" , sayı)
    if str(a2) != sayı:
        (a3) = (input("ilerle (3) "))
        if str(a3) == sayı:
            print(x , "-",para)
        if str(a3) == çek:
            print(çek , para * 1.80 , "elenen basamak:" , sayı)
        if str(a3) != sayı:
            (a4) = (input("ilerle (4) "))
            if str(a4) == sayı:
                print(x , "-",para)
            if str(a4) == çek:
                print(çek , para * 2 , "elenen basamak:" , sayı)
            if str(a4) != sayı:
                (a5) = (input("ilerle (5) "))
                if str(a5) == sayı:
                    print(x , "-",para)
                if str(a5) == çek:
                    print(çek , para * 2.25 , "elenen basamak:" , sayı)
                if str(a5) != sayı:
                    (a6) = (input("ilerle (6) "))
                    if str(a6) == sayı:
                        print(x , "-",para)
                    if str(a6) == çek:
                        print(çek , para * 2.75 , "elenen basamak:" , sayı)
                        (a7) = (input("ilerle (7) "))
                        if str(a7) == sayı:
                            print(x , "-",para)
                        if str(a7) == çek:
                            print(çek , para * 3 , "elenen basamak:" , sayı)
                            (a8) = (input("ilerle (8) "))
                            if str(a8) == sayı:
                                print(x , "-",para)
                            if str(a8) == çek:
                                print(çek , para * 3.5 , "elenen basamak:" , sayı)
                                (a9) = (input("ilerle (9) "))
                                if str(a9) == sayı:
                                    print(x , "-",para)
                                if str(a9) == çek:
                                    print(çek , para * 4 , "elenen basamak:" , sayı)
