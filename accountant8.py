
import sys
import time


def file_read_mode(file):
    fhand = open(file)
    fh = fhand.readlines()
    for line in fh:
        print(line)
argv = list
len(list)
for arg in sys.argv[2:]:

file_read(sys.argv[1])
#file_read_mode(sys.argv[1])
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
        if fh.startswith("sprzedaz"):
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
#file_read()

(saldo, lista, magazyn) = file_read()


#
print(saldo)
print(magazyn)
print(lista)


quit()


#
#
# #

#def balance_mode(arg2, arg3):
#
#     agr2 = int(sys.argv[2])
#     arg3 = sys.argv[3]
#     saldo += arg2
#     lista.append(arg1)
#     lista.append(arg2)
#     lista.append(arg3)
#     print(saldo)
# #
#
#
# def sell_mode ()
#
# ? file_read(argv[1], argv[2])
# ?name = sys.argv[1]
# ?mode = sys.argv[2]
