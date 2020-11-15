import sys
arg = sys.argv[1]

uczen_klasa = {}
nauczyciel_przedmiot = None
klasy_nauczyciela = []
klasy_wychowawcy = []

while True:
    x = input("Wprowadź polecenie: ")
    if x == "koniec":
        break
    if x == "uczeń":
        uczen = input("Nazwisko ucznia?")
        klasa = input("Klasa ucznia?")
        uczen_klasa.get(uczen, klasa)
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



if arg == "uczeń":
    print(uczen_klasa)

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
