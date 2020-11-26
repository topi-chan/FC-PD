
import sys

saldo = 0
lista = []
magazyn = {}
produkty = []
counts = {}


def file_read_mode(file):
    fhand = open(file)
    fh = fhand.readlines()
    for line in fh:
        print(line)


#file_read_mode(sys.argv[1])


while True:
    fhand = open(sys.argv[1])
    fh = fhand.readline().strip()
    if fh.startswith("saldo"):
        lista.append(fh)
        money = fhand.readline().strip()
        com = fhand.readline().strip()
        saldo += int(money)
        lista.append(money)
        lista.append(com)
        fh
        continue
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
            continue
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
                    continue
                else:
                    print("Błąd - brak wystarczającej ilości środków na koncie")
                    quit()
            else:
                print("Brak takiego produktu w magazynie")
                quit()
        if fh.startswith("stop"):
            break
print(saldo)
print(magazyn)
print(lista)


quit()


#
#
#
#
# def balance_mode(arg2, arg3):
#
#     agr2 = int(sys.argv[2])
#     arg3 = sys.argv[3]
#     saldo += arg2
#     lista.append(arg1)
#     lista.append(arg2)
#     lista.append(arg3)
#     print(saldo)



#def sell_mode ()

# ? file_read(argv[1], argv[2])
# ?name = sys.argv[1]
# ?mode = sys.argv[2]
