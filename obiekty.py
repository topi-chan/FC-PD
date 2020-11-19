import sys
arg = sys.argv[1]

class Uczen:
    def __init__(self):
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
    def __init__(self):
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

# TODO:
u = Uczen(self.fullname, self.classroom)
n = Nauczyciel(fullname, classroom, subject)
w = Wychowawca(fullname, classroom)
#tej części TODO nie wiem jak zrobić - krzaczy się. Jak się odwołać do obiektu?

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

#jak do KONKRETNEGO, jednego z wielu utworzonych, obiektu, przypisać "jego" listę?
#jak się do niej odwołać?
#czyli np. dla ucznia: jeden z uczniów to X, i jest w klasie Y, a jednocześnie
#nauczyciel Z uczy w klasie Y = muszę sprawdzić w liście tego nauczyciela
#jakie prowadzi przedmioty, żeby wypisać przedmioty na które uczęszcza uczeń
#przykładowa logika w 3 dalszych linijkach ale czy dobra i jak to zapisać?
if arg == u.fullname:
    if u.classroom in n.classroom:
        print(n.subject)
if arg == w.fullname:
    ...
if arg == n.fullname:
    print(Nauczyciel.Nazwisko())
# TODO:
#chodzi o argv = nazwa klasy
elif arg in u.classroom:
    .......
    .......
    .......
#ta część dość trudna, bo trzeba się do różnych klas odwoływać jednocześnie?
else:
    quit()
