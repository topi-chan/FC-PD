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
        for k, v in classes:
            self.fullname
        print(self.classroom)


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
        self.students.append()
        print("")


class Classroom:
    def __init__(self):
        self.teachers = []
        self.mentor = ""

    def data_input_teacher(self):
        teacher = Teacher()
        self.teachers.append(teacher.fullname)

    def data_input_mentor(self):
        mentor = Mentor()
        sef.mentor = mentor.fullname

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
    if fhand == "uczen":
        continue
    classroom = Classroom()
    for x in person.classroom:
        classes[x] = classroom.data_input_teacher or classroom.data_input_mentor

print(classes)
print(persons)

if arg in persons:
    for arg, v in persons.items():
        if isinstance (v, Student):
            print("Uczeń!")
            output = Student()
        if isinstance (v, Teacher):
            print("Nie uczeń")
            output = Teacher()
        if isinstance (v, Mentor):
            print("Nie uczeń")
            output = Mentor()
    output.data_output()

elif arg in classes:
    for arg, v in classes.items():
        

else:
    print("Błąd")

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
