def file_read(fhand):
    saldo = 0
    lista = []
    magazyn = {}
    fhand = open(fhand)
    while True:
        fh = fhand.readline().strip()
        print(fh)
        time.sleep(1)
        if fh.startswith("saldo"):
            lista.append(fh)
            money = fhand.readline().strip()
            com = fhand.readline().strip()
            saldo += int(money)
            lista.append(money)
            lista.append(com)
            fh
        if fh.startswith("zakup"):
            name = fhand.readline().strip()
            price = int(fhand.readline().strip())
            if price < 0:
                print("Błąd - cena nie może być mniejsza od zera")
                quit()
            pieces = int(fhand.readline().strip())
            if pieces < 0:
                print("Błąd - liczba sztuk nie może być mniejsza od zera")
                quit()
            if (price * pieces) <= saldo:
                lista.append(name)
                lista.append(price)
                lista.append(pieces)
                magazyn[name] = magazyn.get(name, 0) +pieces
                saldo -= (price * pieces)
                fh
            else:
                print("Błąd - brak wystarczającej ilości środków na koncie")
                quit()
        if fh.startswith("sprzedaż"):
            name = fhand.readline().strip()
            if name in magazyn:
                price = int(fhand.readline().strip())
                if price < 0:
                    print("Błąd - cena nie może być mniejsza od zera")
                    quit()
                pieces = int(fhand.readline().strip())
                if pieces < 0:
                    print("Błąd - liczba sztuk nie może być mniejsza od zera")
                    quit()
                if (price * pieces) <= saldo:
                    lista.append(name)
                    lista.append(price)
                    lista.append(pieces)
                    magazyn[name] = magazyn.get(name, 0) -pieces
                    saldo -= (price * pieces)
                    fh
                else:
                    print("Błąd - brak wystarczającej ilości środków na koncie")
                    quit()
            else:
                print("Brak takiego produktu w magazynie")
                quit()
        if fh.startswith("stop"):
            return (saldo, lista, magazyn)
            break
