import sys
arg = sys.argv[1]


class Student:
    def __init__(self):
        self.fullname = ""
        self.classroom = ""

    def data_input(self):
        self.fullname = input()
        self.classroom = input()
        break


class Teacher:
    def __init__(self):
        self.fullname = ""
        self.classroom = []
        self.subject = []

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


class Mentor:
    def __init__(self):
        self.fullname = ""
        self.classroom = []

    def data_input(self):
        self.fullname = input()
        while True:
            classrooms = input()
            if not classrooms:
                break
            self.classroom.append(classrooms)

    def data_output(self):
        self.students.append()
        print("")
    # pobrac osoby i klasy - slowniki
    # if d s f :
    #     dsdss"
    # else dsokdso:


class Classroom:
    def __init__(self):
        self.classroom = ""
        self.teachers = []
        self.students = []
        self.mentor = ""

    def appends(self):
        self.classroom


klasy = {}
osoby = {}

while True:
    fhand = input("Podaj typ użytkownika: ")
    if fhand == "uczen":
        person = Uczen()
        classroom = Classroom()
    elif fhand == "nauczyciel":
        person = Nauczyciel()
        classroom = Classroom()
    elif fhand == "wychowawca":
        person = Wychowawca()
        classroom = Classroom()
    else:
        break
    osoba.data_input()
    osoby[osoba.fullname] = osoba
print(osoby)
quit()


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
    dsdss
#ta część dość trudna, bo trzeba się do różnych klas odwoływać jednocześnie?
else:
    quit()
