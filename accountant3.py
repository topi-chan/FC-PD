import sys

saldo = 0
lista = []
produkty = []
komentarze = []
counts = {}

x = str(sys.argv[1])

if x == "saldo":
    try:
        y = int(sys.argv[2])
        z = str(sys.argv[3])
    except:
        print("Błąd - dla polecenia 'saldo' podaj wartość liczbową zmiany na koncie i komentarz")
        quit()
    while True:
        fhand = input()
        fhand
        lista.append(fhand)
        if fhand == "stop":
            saldo += y
            print(saldo)
            break
        if fhand == "saldo":
            zmiana = int(input())
            zmiana
            saldo += zmiana
            komentarz = str(input())
            komentarz
            komentarze.append(komentarz)
            continue
        if fhand == "zakup":
            nazwa = str(input())
            nazwa
            produkty.append(nazwa)
            cena = int(input())
            cena
            sztuk = int(input())
            sztuk
            saldo -= (cena * sztuk)
            continue
        if fhand == "sprzedaż":
            nazwa = str(input())
            nazwa
            produkty.remove(nazwa)
            cena = int(input())
            cena
            sztuk = int(input())
            sztuk
            saldo += (cena * sztuk)
            continue
        else:
            print("Błąd")
            continue

elif x == "sprzedaż":
    try:
        y = str(sys.argv[2])
        z = int(sys.argv[3])
        v = int(sys.argv[4])
    except:
        print("Błąd - dla polecenia 'sprzedaż' podaj nazwę produktu, cenę i liczbę sprzedanych sztuk")
        quit()
    while True:
        fhand = input()
        fhand
        if fhand == "stop":
            lista.append(x)
            lista.append(y)
            lista.append(z)
            lista.append(v)
            for l in lista:
                print(l)
            print("stop")
            break
        lista.append(fhand)
        if fhand == "saldo":
            zmiana = int(input())
            zmiana
            lista.append(zmiana)
            komentarz = str(input())
            komentarz
            lista.append(komentarz)
            continue
        if fhand == "zakup":
            nazwa = str(input())
            nazwa
            lista.append(nazwa)
            cena = int(input())
            cena
            lista.append(cena)
            sztuk = int(input())
            sztuk
            lista.append(sztuk)
            continue
        if fhand == "sprzedaż":
            nazwa = str(input())
            nazwa
            lista.append(nazwa)
            cena = int(input())
            cena
            lista.append(cena)
            sztuk = int(input())
            sztuk
            lista.append(sztuk)
            continue
        else:
            print("Błąd")
            continue


elif x == "zakup":
    try:
        y = str(sys.argv[2])
        z = int(sys.argv[3])
        v = int(sys.argv[4])
    except:
        print("Błąd - dla polecenia 'zakup' podaj nazwę produktu, cenę i liczbę zakupionych sztuk")
        quit()
    while True:
        fhand = input()
        fhand
        if fhand == "stop":
            lista.append(x)
            lista.append(y)
            lista.append(z)
            lista.append(v)
            for l in lista:
                print(l)
            print("stop")
            break
        lista.append(fhand)
        if fhand == "saldo":
            zmiana = int(input())
            zmiana
            lista.append(zmiana)
            komentarz = str(input())
            komentarz
            lista.append(komentarz)
            continue
        if fhand == "zakup":
            nazwa = str(input())
            nazwa
            lista.append(nazwa)
            cena = int(input())
            cena
            lista.append(cena)
            sztuk = int(input())
            sztuk
            lista.append(sztuk)
            continue
        if fhand == "sprzedaż":
            nazwa = str(input())
            nazwa
            lista.append(nazwa)
            cena = int(input())
            cena
            lista.append(cena)
            sztuk = int(input())
            sztuk
            lista.append(sztuk)
            continue
        else:
            print("Błąd")
            continue

elif x == "konto":
    while True:
        fhand = input()
        fhand
        if fhand == "stop":
            for l in lista:
                print(l)
            print("stop")
            break
        lista.append(fhand)
        if fhand == "saldo":
            zmiana = int(input())
            zmiana
            lista.append(zmiana)
            komentarz = str(input())
            komentarz
            lista.append(komentarz)
            continue
        if fhand == "zakup":
            nazwa = str(input())
            nazwa
            lista.append(nazwa)
            cena = int(input())
            cena
            lista.append(cena)
            sztuk = int(input())
            sztuk
            lista.append(sztuk)
            continue
        if fhand == "sprzedaż":
            nazwa = str(input())
            nazwa
            lista.append(nazwa)
            cena = int(input())
            cena
            lista.append(cena)
            sztuk = int(input())
            sztuk
            lista.append(sztuk)
            continue
        else:
            print("Błąd")
            continue

elif x == "magazyn":
    try:
        y = str(sys.argv[2])
        z = str(sys.argv[3])
        v = str(sys.argv[4])
    except:
        print("Błąd - dla polecenia 'magazyn' podaj komentarz")
        quit()
    while True:
        fhand = input()
        fhand
        if fhand == "stop":
            for produkt in produkty:
                if produkt not in counts:
                   counts[produkt] = 1
                else:
                    counts[produkt] = counts[produkt] + 1
            print(counts)
            break
        lista.append(fhand)
        if fhand == "saldo":
            zmiana = int(input())
            zmiana
            saldo += zmiana
            komentarz = str(input())
            komentarz
            komentarze.append(komentarz)
            continue
        if fhand == "zakup":
            nazwa = str(input())
            nazwa
            cena = int(input())
            cena
            sztuk = int(input())
            sztuk
            while True:
                if nazwa == y or nazwa == z or nazwa == v:
                    if sztuk > 1:
                        produkty.append(nazwa)
                        sztuk -= 1
                        continue
                    else:
                        break
                else:
                    break
            saldo -= (cena * sztuk)
            continue
        if fhand == "sprzedaż":
            nazwa = str(input())
            nazwa
            cena = int(input())
            cena
            sztuk = int(input())
            sztuk
            while True:
                if nazwa == y or nazwa == z or nazwa == v:
                    if sztuk > 1:
                        produkty.remove(nazwa)
                        sztuk -= 1
                        continue
                    else:
                        break
                else:
                    break
            saldo += (cena * sztuk)
            continue
        else:
            print("Błąd")
            continue

elif x == "przegląd":
    pass

else:
    print("Błąd - dozwolone akcje to: saldo, sprzedaż, zakup, konto, magazyn, przegląd")
    quit()
#
# while True:
#     fhand = input()
#     fhand
#     lista.append(fhand)
#     if fhand == "stop":
#         for produkt in produkty:
#             if produkt not in counts:
#                counts[produkt] = 1
#             else :
#                 counts[produkt] = counts[produkt] + 1
#         break
#     if fhand == "saldo":
#         zmiana = int(input())
#         zmiana
#         saldo += zmiana
#         komentarz = str(input())
#         komentarz
#         komentarze.append(komentarz)
#         continue
#     if fhand == "zakup":
#         nazwa = str(input())
#         nazwa
#         produkty.append(nazwa)
#         cena = int(input())
#         cena
#         sztuk = int(input())
#         sztuk
#         saldo -= (cena * sztuk)
#         continue
#     if fhand == "sprzedaż":
#         nazwa = str(input())
#         nazwa
#         produkty.remove(nazwa)
#         cena = int(input())
#         cena
#         sztuk = int(input())
#         sztuk
#         saldo += (cena * sztuk)
#         continue
#     else:
#         print("Błąd")
#         continue


    # if fhand == "konto":
    #     continue
    # if fhand == "magazyn":
    #     nazwa = str(input())
    #     nazwa
    #     if nazwa in counts:
    #         for nazwa in counts:
    #              print(nazwa, counts[nazwa])
    #     continue
    # if fhand == "przegląd":
    #     liczba = int(input())
    #     liczba
    #     liczba1 = int(input())
    #     liczba1
    #     fhand
    #     lista.append(fhand)
    #     if fhand == "stop":
    #         print(lista(range(liczba, (liczba1 - 1)))


#lista.append(fhand)
# if x == "saldo":
#     lista.append(y)
#     lista.append(z)
# else:
#     lista.append(y)
#     lista.append(z)
#     lista.append(v)
# for l in lista:
#     print(l)


#{key: value for key, value in variable}
