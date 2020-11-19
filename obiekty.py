# Jeśli typ użytkownika to uczeń pobierz jedną linię - będzie to nazwa klasy (np
# 3C), przejdź do kroku 1 Jeśli typ użytkownika to nauczyciel pobierz 1 linię -
# nazwę przedmiotu prowadzonego a następnie w nowych liniach nazwy klas aż do
# otrzymania pustej linii. Przejdź do korku 1 Jeśli typ użytkownika to
# wychowawca pobieraj w nowych liniach nazwy klas które prowadzi wychowawca aż
# do pustej linii, przejdź do kroku 1
import sys
arg = sys.argv[1]

class Uczen:
    def __init__(self, fullname, classroom):
        self.fullname == ""
        self.classroom == ""

    def data_input(self):
        self.fullname = input()
        while True:
            classrooms = input()
            if not classrooms:
                break
            self.classroom.append(classrooms)

class Nauczyciel:
    def __init__(self, fullname, classroom, subject):
        self.fullname == ""
        self.classroom == []
        self.subject == []

    def data_input(self):
        self.fullname = input()
        while True:
            classrooms = input()
            if not classrooms:
                break
            self.classroom.append(classrooms)
        while True:
            subjects = input()
            self.subject = input()
            if not subjects:
                break
            self.subject.append(subjects)

class Wychowawca:
    def __init__(self):
        self.fullname == ""
        self.classroom == []

    def data_input(self):
        self.fullname = input()
        while True:
            classrooms = input()
            if not classrooms:
                break
            self.classroom.append(classrooms)

u = Uczen(fullname, classroom)
n = Nauczyciel(fullname, classroom, subject)
w = Wychowawca(fullname, classroom)

while True:
    fhand = input("Podaj typ użytkownika")
    if fhand == "uczeń" or "Uczeń":
        u.data_input()
    if fhand == "nauczyciel" or "Nauczyciel":
        n.data_input()
    if fhand == "wychowawca" or "Wychowawca":
        w.data_input()
    else:
        break


if arg == "uczen" or "Uczeń":
    print(u.classroom)
if arg == "nauczyciel" or "Nauczyciel":
    print(Nauczyciel.Nazwisko())
if arg == "wychowawca" or "Wychowawca":
    print(Nauczyciel.Nazwisko())

# while True:
#     x = input("Wprowadź polecenie: ")
#     if x == "koniec":
#         break
#
#     if x == "uczen":
#         uczen = input("Nazwisko ucznia?")
#         klasa = input("Klasa ucznia?")
#         uczen_klasa[uczen] = klasa
#         continue
#
#     if x == "nauczyciel":
#         nauczyciel = input("Nazwisko nauczyciela?")
#         nauczyciel_przedmiot = input("Prowadzony przedmiot?")
#         nauczyciel_klasy = input("Klasa?")
#         if nauczyciel_klasy == "\n":
#             continue
#
#     if x == "wychowawca":
#         wychowawca = input("Nazwisko wychowawcy?")
#         wychowawca_klasy = input("Klasa?")
#         if wychowawca_klasy == "\n":
#             continue
#
