import sys
arg = sys.argv[1]

uczen_klasa = None
nauczyciel_przedmiot = None
klasy_nauczyciela = []
klasy_wychowawcy = []

x = input("Wprowadź polecenie")

while x != "koniec":
    if x == "uczeń":
        uczen_klasa = input("Klasa ucznia?")
        continue
    if x == "nauczyciel":
        nauczyciel_przedmiot = input("Prowadzony przedmiot?")
        klasa = input("Klasa?")
        if klasa != "\n":
            klasy_nauczyciela.append(klasa)
        else:
            continue
    if x == "wychowawca":
        klasy = input("Klasa?")
        if klasy != "\n":
            klasy_wychowawcy.append(klasy)
        else:
            continue
else:
    break

if arg = uczen_klasa:
    print


    fhand = input()

    if fhand == "C":
        print('haha')
    fhand
    if fhand == "stop":
        quit()

    try:
        sys.argv[1]
    except:
        pass

except:
    break



def wychowawca(klasa):
    return

def nauczyciel(klasa, przedmiot):
    return

def uczen(klasa):
    return
