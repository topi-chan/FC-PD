import sys
arg = sys.argv[1]

classes = {}
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
                            print(z.fullname)
                            print(z.subject)


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
                                print(z.fullname)

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



# class Classroom:
#     def __init__(self):
#         self.teachers = []
#         self.mentor = ""
#
#     def data_input_teacher(self):
#         teacher = Teacher()
#         self.teachers.append(person.fullname)
#
#     def data_input_mentor(self):
#         mentor = Mentor()
#         sef.mentor = mentor(self, self.fullname)
#
#     def data_output(self):
#         print(self.mentor)

    # pobrac osoby i klasy - slowniki
    # if d s f :
    #     dsdss"
    # else dsokdso:

#    def data_input(self):


    # def appends(self):
    #     if x
    #     self.classroom =
    #
    # def data_output(self):
    #



while True:
    fhand = input("Podaj typ użytkownika: ")
    if fhand == "uczen":
        person = Student()
    elif fhand == "nauczyciel":
        person = Teacher()
    elif fhand == "wychowawca":
        person = Mentor()
    else:
        break
    person.data_input()
    persons[person.fullname] = person
#    classroom = Classroom()
    # if fhand == "wychowawca":
    #     for x in person.classroom:
    #         classes[x] = person.fullname

print(classes)
print(persons)

if arg in persons:
    v = persons.get(arg, )
    if isinstance (v, Student):
        print("Uczeń!")
        output = Student()
    if isinstance (v, Teacher):
        print("Nauczyciel!")
        output = Teacher()
    if isinstance (v, Mentor):
        print("Wychowawca!")
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


# elif arg in classes:
#     output = Classroom()
#     for arg, v in classes.items():
#         print("Wychowawca: ", v.data_output)
#
# else:
#     print("Błąd")

quit()

# try:
#     x = persons[arg].classroom
#     print(x)
# except:
#     y = classes[arg].subject
#     print(y)
# quit()
#

#jak do KONKRETNEGO, jednego z wielu utworzonych, obiektu, przypisać "jego"
#listę? jak się do niej odwołać?
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
