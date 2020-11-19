import sys, os
arg = sys.argv[1]

uczen_klasa = {}

class Nauczyciel:
    def __init__(self, Nazwisko, Przedmiot, Klasa):
        self.Nazwisko = nauczyciel
        self.Przedmiot = nauczyciel_przedmiot
        self.Klasa = nauczyciel_klasa
class Wychowawca:
    def __init__(self, Nazwisko, Klasy):
        self.Nazwisko = wychowawca
        self.Klasy = wychowawca_klasy

while True:
    x = input("Wprowadź polecenie: ")
    if x == "koniec":
        break
    if x == "uczen":
        uczen = input("Nazwisko ucznia?")
        klasa = input("Klasa ucznia?")
        uczen_klasa[uczen] = klasa
        continue
    if x == "nauczyciel":
        nauczyciel = input("Nazwisko nauczyciela?")
        nauczyciel_przedmiot = input("Prowadzony przedmiot?")
        nauczyciel_klasy = input("Klasa?")
        if nauczyciel_klasy == "\n":
            continue

    if x == "wychowawca":
        wychowawca = input("Nazwisko wychowawcy?")
        wychowawca_klasy = input("Klasa?")
        if wychowawca_klasy == "\n":
            continue



if arg == "uczen":
    print(uczen_klasa)
if arg == "nauczyciel":
    print(Nauczyciel.Nazwisko())

#
#     fhand = input()
#
#     if fhand == "C":
#         print('haha')
#     fhand
#     if fhand == "stop":
#         quit()
#
#     try:
#         sys.argv[1]
#     except:
#         pass
#
# except:
#     break
#
#
#
# def wychowawca(klasa):
#     return
#
# def nauczyciel(klasa, przedmiot):
#     return
#
# def uczen(klasa):
#     return
