import sys
arg = sys.argv[1]

persons = {}

class Student:
    def __init__(self):
        self.fullname = ""
        self.classroom = ""

    def data_input(self):
        self.fullname = input("Podaj dane ucznia: ")
        self.classroom = input("Podaj nazwę klasy: ")

    def data_output(self):
        v = persons.values()
        for x in v:
            if x.fullname == arg:
                for z in v:
                    if isinstance (z, Teacher):
                        if x.classroom in z.classroom:
                            print("Nauczyciel: ", z.fullname)
                            print("Przedmioty: ", z.subject)


class Teacher:
    def __init__(self):
        self.fullname = ""
        self.classroom = []
        self.subject = []

    def data_input(self):
        self.fullname = input("Podaj dane nauczyciela: ")
        while True:
            classrooms = input("Podaj prowadzone klasy: ")
            if not classrooms:
                break
            self.classroom.append(classrooms)
        while True:
            subjects = input("Podaj nazwę przedmiotu: ")
            if not subjects:
                break
            self.subject.append(subjects)

    def data_output(self):
        v = persons.values()
        for x in v:
            if x.fullname == arg:
                for z in v:
                    if isinstance (z, Mentor):
                        for c in x.classroom:
                            if c in z.classroom:
                                print("Wychowawca: ", z.fullname)

class Mentor:
    def __init__(self):
        self.fullname = ""
        self.classroom = []

    def data_input(self):
        self.fullname = input("Podaj dane wychowawcy: ")
        while True:
            classrooms = input("Podaj prowadzone klasy: ")
            if not classrooms:
                break
            self.classroom.append(classrooms)

    def data_output(self):
        v = persons.values()
        for x in v:
            if x.fullname == arg:
                for z in v:
                    if isinstance (z, Student):
                        if z.classroom in x.classroom:
                            print(z.fullname)


while True:
    fhand = input("Podaj typ użytkownika: ")
    if fhand == "uczeń":
        person = Student()
    elif fhand == "nauczyciel":
        person = Teacher()
    elif fhand == "wychowawca":
        person = Mentor()
    else:
        break
    person.data_input()
    persons[person.fullname] = person

if arg in persons:
    v = persons.get(arg, )
    if isinstance (v, Student):
        output = Student()
    if isinstance (v, Teacher):
        output = Teacher()
    if isinstance (v, Mentor):
        output = Mentor()
    output.data_output()

else:
    v = persons.values()
    for x in v:
        if isinstance (x, Student):
            if x.classroom == arg:
                print("Uczeń: ", x.fullname)
    n = persons.values()
    for y in n:
        if isinstance (y, Mentor):
            if arg in y.classroom:
                print("Wychowawca: ", y.fullname)
quit()
