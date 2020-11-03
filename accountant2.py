import sys

zakup = {}
sprzedaz = {}
saldo = 0
komentarz = tuple()

fhand = input()

x = str(sys.argv[1])

if x == "saldo":
    try:
        y = int(sys.argv[2])
        z = str(sys.argv[3])
        saldo = 0 + y
        komentarz += (z,)
        fhand
    except:
        print("Błąd - dla polecenia 'saldo' podaj wartość liczbową zmiany na koncie i komentarz")
        quit()

elif x == "sprzedaż":
    try:
        y = str(sys.argv[2])
        z = int(sys.argv[3])
        v = int(sys.argv[4])
    except:
        print("Błąd - dla polecenia 'sprzedaż' podaj nazwę produktu, cenę i liczbę sprzedanych sztuk")
        quit()

elif x == "zakup":
    try:
        y = str(sys.argv[2])
        z = int(sys.argv[3])
        v = int(sys.argv[4])
    except:
        print("Błąd - dla polecenia 'zakup' podaj nazwę produktu, cenę i liczbę zakupionych sztuk")
        quit()

else:
    print("Błąd - dozwolone akcje to: saldo, sprzedaż, zakup")
    quit()

if fhand == 0:
    quit()
