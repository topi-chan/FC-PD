# Jeśli typ użytkownika to uczeń pobierz jedną linię - będzie to nazwa klasy (np
# 3C), przejdź do kroku 1 Jeśli typ użytkownika to nauczyciel pobierz 1 linię -
# nazwę przedmiotu prowadzonego a następnie w nowych liniach nazwy klas aż do
# otrzymania pustej linii. Przejdź do korku 1 Jeśli typ użytkownika to
# wychowawca pobieraj w nowych liniach nazwy klas które prowadzi wychowawca aż
# do pustej linii, przejdź do kroku 1


import sys
arg = sys.argv[1]

class Uczen:
    def __init__(self):
        self.fullname == ""
        self.classroom == ""

    def data_input(self):
        while True:
            self.fullname = input()
            self.classroom = input()
        else:
            break

class Nauczyciel:
    def __init__(self):
        self.fullname == ""
        self.classroom == []
        self.subject == []

    def data_input(self):
            self.fullname = input()
            while True:
                self.classroom = input()
            if not classroom:
                break
            while True:
                self.subject = input()
            if not subject:
                break

class Wychowawca:
    def __init__(self):
        self.fullname == ""
        self.classroom == []

    def data_input(self):
            self.fullname = input()
            while True:
                self.classroom = input()
            if not classroom:
                break


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
