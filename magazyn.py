import time

def file_read(fhand):
    saldo = 0
    lista = []
    magazyn = {}
    fhand = open(fhand)
    while True:
        fh = fhand.readline().strip()
        # print(fh)
        # time.sleep(1)
        if fh.startswith("saldo"):
            lista.append(fh)
            money = fhand.readline().strip()
            com = fhand.readline().strip()
            saldo += int(money)
            lista.append(money)
            lista.append(com)
            fh
        if fh.startswith("zakup"):
            lista.append(fh)
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
            lista.append(fh)
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
            lista.append(fh)
            return (saldo, lista, magazyn)
            break

def file_write_saldo(fname):
    from saldo import lista
    lista2 = []
    fd = open(fname, "a")
    for element in lista:
        element_str = str(element)
        lista2.append(element_str)
    for element_str in lista2:
        fd.write(element_str)
        fd.write("\n")

def file_write_sprzedaz(fname):
    from sprzedaz import lista
    print(lista)
    lista2 = []
    fd = open(fname, "a")
    for element in lista:
        element_str = str(element)
        lista2.append(element_str)
    for element_str in lista2:
        fd.write(element_str)
        fd.write("\n")

def file_write_zakup(fname):
    from zakup import lista
    lista2 = []
    fd = open(fname, "a")
    for element in lista:
        element_str = str(element)
        lista2.append(element_str)
    for element_str in lista2:
        fd.write(element_str)
        fd.write("\n")
