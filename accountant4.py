import sys

saldo = 0
lista = []
magazyn = {}
produkty = []
komentarze = []
counts = {}
przeglad = []
sld = []
zkp = []
spd = []

x = str(sys.argv[1])

if x == "saldo":
    try:
        y = int(sys.argv[2])
        z = str(sys.argv[3])
        saldo += y
    except:
        print("Błąd - dla polecenia 'saldo' podaj wartość liczbową zmiany na koncie i komentarz")
        quit()
    while True:
        fhand = input()
        fhand
        lista.append(fhand)
        if fhand == "stop":
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
            cena = int(input())
            cena
            sztuk = int(input())
            sztuk
            if (cena * sztuk) <= saldo:
                magazyn[nazwa] = magazyn.get(nazwa, 0) +sztuk
            else:
                print("Błąd")
                continue
            saldo -= (cena * sztuk)
            continue
        if fhand == "sprzedaż":
            nazwa = str(input())
            nazwa
            if nazwa in magazyn:
                magazyn[nazwa] = magazyn.get(nazwa, 0) -sztuk
            else:
                print("Błąd")
                continue
            cena = int(input())
            cena
            sztuk = int(input())
            sztuk
            saldo += (cena * sztuk)
            continue
        else:
            print("Błąd")
            continue

# ten fragment kodu - nie rozumiem zasady wywołania, tzn. sensu
# "Jeśli jeśli na magazynie nie ma wystarczającej liczby sztuk
#program zwraca błąd" - a przecież w momencie wywołania l. szt. = 0
#tak samo dla zakupu - nie możemy nic kupić mając 0 zł na koncie
#zrobiłem "po swojemu" tj. dane argv dodają się 'ręcznie', na końcu, bez checka
#a reszta jak powinna być - czyli sprawdza $$ i stany magazynowe z inputa
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
            print("Stan magazynu: ", magazyn)
            break
        lista.append(fhand)
        if fhand == "saldo":
            zmiana = int(input())
            zmiana
            saldo += zmiana
            lista.append(zmiana)
            komentarz = str(input())
            komentarz
            lista.append(komentarz)
            continue
        if fhand == "zakup":
            nazwa = str(input())
            nazwa
            cena = int(input())
            cena
            if cena < 0:
                print("Błąd - cena nie może być mniejsza od zera")
                continue
            sztuk = int(input())
            sztuk
            if sztuk < 0:
                print("Błąd - liczba sztuk nie może być mniejsza od zera")
                continue
            if (cena * sztuk) <= saldo:
                lista.append(nazwa)
                lista.append(cena)
                lista.append(sztuk)
                magazyn[nazwa] = magazyn.get(nazwa, 0) +sztuk
                saldo -= (cena * sztuk)
                continue
            else:
                print("Błąd - brak środków na koncie")
                continue
        if fhand == "sprzedaż":
            nazwa = str(input())
            nazwa
            if nazwa in magazyn:
                lista.append(nazwa)
                cena = int(input())
                cena
                if cena < 0:
                    print("Błąd - cena nie może być mniejsza od zera")
                    continue
                lista.append(cena)
                sztuk = int(input())
                sztuk
                if sztuk < 0:
                    print("Błąd - liczba sztuk nie może być mniejsza od zera")
                    continue
                lista.append(sztuk)
                magazyn[nazwa] = magazyn.get(nazwa, 0) -sztuk
                saldo += (cena * sztuk)
                continue
            else:
                print("Błąd - nie ma takiego produktu w magazynie")
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
            print("Stan magazynu: ", magazyn)
            break
        lista.append(fhand)
        if fhand == "saldo":
            zmiana = int(input())
            zmiana
            saldo += zmiana
            lista.append(zmiana)
            komentarz = str(input())
            komentarz
            lista.append(komentarz)
            continue
        if fhand == "zakup":
            nazwa = str(input())
            nazwa
            cena = int(input())
            cena
            if cena < 0:
                print("Błąd - cena nie może być mniejsza od zera")
                continue
            sztuk = int(input())
            sztuk
            if sztuk < 0:
                print("Błąd - liczba sztuk nie może być mniejsza od zera")
                continue
            if (cena * sztuk) <= saldo:
                lista.append(nazwa)
                lista.append(cena)
                lista.append(sztuk)
                magazyn[nazwa] = magazyn.get(nazwa, 0) +sztuk
                saldo -= (cena * sztuk)
                continue
            else:
                print("Błąd - brak środków na koncie")
                continue
        if fhand == "sprzedaż":
            nazwa = str(input())
            nazwa
            if nazwa in magazyn:
                lista.append(nazwa)
                cena = int(input())
                cena
                if cena < 0:
                    print("Błąd - cena nie może być mniejsza od zera")
                    continue
                lista.append(cena)
                sztuk = int(input())
                sztuk
                if sztuk < 0:
                    print("Błąd - liczba sztuk nie może być mniejsza od zera")
                    continue
                lista.append(sztuk)
                magazyn[nazwa] = magazyn.get(nazwa, 0) -sztuk
                saldo += (cena * sztuk)
                continue
            else:
                print("Błąd - nie ma takiego produktu w magazynie")
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
            saldo += zmiana
            lista.append(zmiana)
            komentarz = str(input())
            komentarz
            lista.append(komentarz)
            continue
        if fhand == "zakup":
            nazwa = str(input())
            nazwa
            cena = int(input())
            cena
            if cena < 0:
                print("Błąd - cena nie może być mniejsza od zera")
                continue
            sztuk = int(input())
            sztuk
            if sztuk < 0:
                print("Błąd - liczba sztuk nie może być mniejsza od zera")
                continue
            if (cena * sztuk) <= saldo:
                lista.append(nazwa)
                lista.append(cena)
                lista.append(sztuk)
                magazyn[nazwa] = magazyn.get(nazwa, 0) +sztuk
                saldo -= (cena * sztuk)
                continue
            else:
                print("Błąd - brak środków na koncie")
                continue
        if fhand == "sprzedaż":
            nazwa = str(input())
            nazwa
            if nazwa in magazyn:
                lista.append(nazwa)
                cena = int(input())
                cena
                if cena < 0:
                    print("Błąd - cena nie może być mniejsza od zera")
                    continue
                lista.append(cena)
                sztuk = int(input())
                sztuk
                if sztuk < 0:
                    print("Błąd - liczba sztuk nie może być mniejsza od zera")
                    continue
                lista.append(sztuk)
                magazyn[nazwa] = magazyn.get(nazwa, 0) -sztuk
                saldo += (cena * sztuk)
                continue
            else:
                print("Błąd - nie ma takiego produktu w magazynie")
                continue
        else:
            print("Błąd")
            continue

#nie wiem jak zrobić, żeby mogła być dowolna liczba argv, przyjmuję trzy
elif x == "magazyn":
    try:
        y = str(sys.argv[2])
        z = str(sys.argv[3])
        v = str(sys.argv[4])
    except:
        print("Błąd - dla polecenia 'magazyn' podaj trzy identyfikatory produktu")
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
            for k, v in counts.items():
                print(k, v)
            break
        lista.append(fhand)
        if fhand == "saldo":
            zmiana = int(input())
            zmiana
            saldo += zmiana
            lista.append(zmiana)
            komentarz = str(input())
            komentarz
            lista.append(komentarz)
            continue
        if fhand == "zakup":
            nazwa = str(input())
            nazwa
            cena = int(input())
            if cena < 0:
                print("Błąd - cena nie może być mniejsza od zera")
                continue
            sztuk = int(input())
            sztuk
            if sztuk < 0:
                print("Błąd - liczba sztuk nie może być mniejsza od zera")
                continue
            if (cena * sztuk) <= saldo:
                lista.append(nazwa)
                lista.append(cena)
                lista.append(sztuk)
                magazyn[nazwa] = magazyn.get(nazwa, 0) +sztuk
            else:
                print("Błąd - brak środków na koncie")
                continue
            while True:
                if nazwa == y or nazwa == z or nazwa == v:
                    if sztuk > 0:
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
            if nazwa in magazyn:
                lista.append(nazwa)
                cena = int(input())
                cena
                if cena < 0:
                    print("Błąd - cena nie może być mniejsza od zera")
                    continue
                lista.append(cena)
                sztuk = int(input())
                sztuk
                if sztuk < 0:
                    print("Błąd - liczba sztuk nie może być mniejsza od zera")
                    continue
                lista.append(sztuk)
                magazyn[nazwa] = magazyn.get(nazwa, 0) -sztuk
                while True:
                    if nazwa == y or nazwa == z or nazwa == v:
                        if sztuk > 0:
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
                print("Błąd - nie ma takiego produktu w magazynie")
                continue
        else:
            print("Błąd")
            continue

elif x == "przegląd":
    try:
        y = int(sys.argv[2])
        z = int(sys.argv[3])
        index = -1
    except:
        print("Błąd - dla polecenia 'przegląd' podaj wartości indeksu początkowego i końcowego")
        quit()
    while True:
        fhand = input()
        fhand
        if fhand == "stop":
            for s in sld[y:z+1]:
                przeglad.append(sld)
            for z in zkp[y:z+1]:
                przeglad.append(z)
            for s in spd[y:z+1]:
                przeglad.append(s)
            for p in przeglad:
                print(p)
            print("stop")
            break
        lista.append(fhand)
        if fhand == "saldo":
            sld.append("saldo")
            zmiana = int(input())
            zmiana
            sld.append(zmiana)
            komentarz = str(input())
            komentarz
            sld.append(komentarz)
            index += 1
            if index >= y and index <= z:
                przeglad.append(zmiana)
                przeglad.append(komentarz)
            continue
        if fhand == "zakup":
            zkp.append("zakup")
            nazwa = str(input())
            nazwa
            zkp.append(nazwa)
            cena = int(input())
            cena
            zkp.append(cena)
            sztuk = int(input())
            sztuk
            zkp.append(sztuk)
            continue
        if fhand == "sprzedaż":
            spd.append("sprzedaż")
            nazwa = str(input())
            nazwa
            spd.append(nazwa)
            cena = int(input())
            cena
            spd.append(cena)
            sztuk = int(input())
            sztuk
            spd.append(sztuk)
            continue
        else:
            print("Błąd")
            continue


else:
    print("Błąd - dozwolone akcje to: saldo, sprzedaż, zakup, konto, magazyn, przegląd")
    quit()
#
# elif x == "magazyn":
    # try:
    #     y = str(sys.argv[2])
    #     z = str(sys.argv[3])
    #     v = str(sys.argv[4])
    # except:
    #     print("Błąd - dla polecenia 'magazyn' podaj trzy identyfikatory produktu")
    #     quit()
    # while True:
    #     fhand = input()
    #     fhand
    #     if fhand == "stop":
    #         for produkt in produkty:
    #             if produkt not in counts:
    #                counts[produkt] = 1
    #             else:
    #                 counts[produkt] = counts[produkt] + 1
    #         print(counts)
    #         break
    #     lista.append(fhand)
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
    #         cena = int(input())
    #         cena
    #         sztuk = int(input())
    #         sztuk
    #         while True:
    #             if nazwa == y or nazwa == z or nazwa == v:
    #                 if sztuk > 1:
    #                     produkty.append(nazwa)
    #                     sztuk -= 1
    #                     continue
    #                 else:
    #                     break
    #             else:
    #                 break
    #         saldo -= (cena * sztuk)
    #         continue
    #     if fhand == "sprzedaż":
    #         nazwa = str(input())
    #         nazwa
    #         cena = int(input())
    #         cena
    #         sztuk = int(input())
    #         sztuk
    #         while True:
    #             if nazwa == y or nazwa == z or nazwa == v:
    #                 if sztuk > 1:
    #                     produkty.remove(nazwa)
    #                     sztuk -= 1
    #                     continue
    #                 else:
    #                     break
    #             else:
    #                 break
    #         saldo += (cena * sztuk)
    #         continue
    #     else:
    #         print("Błąd")
    #         continue



        # if fhand == "stop":
        #     for s in sld[y:z+1]:
        #         przeglad.append(sld)
        #     for z in zkp[y:z+1]:
        #         przeglad.append(z)
        #     for s in spd[y:z+1]:
        #         przeglad.append(s)
        #     for p in przeglad[y:z+1]:
        #         print(p)
