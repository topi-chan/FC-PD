import sys
arg = sys.argv[1]


class Student:
    def __init__(self):
        self.fullname = ""
        self.classroom = ""

    def data_input(self):
        self.fullname = input()
        self.classroom = input()

    def data_output(self):
        print(self.fullname)
        print(self.classroom)


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

    # def appends(self):
    #     if x
    #     self.classroom =
    #
    # def data_output(self):
    #

klasy = {}
persons = {}

while True:
    fhand = input("Podaj typ użytkownika: ")
    if fhand == "uczen":
        person = Student()
        classroom = Classroom()
    elif fhand == "nauczyciel":
        person = Teacher()
        classroom = Classroom()
    elif fhand == "wychowawca":
        person = Mentor()
        classroom = Classroom()
    else:
        break
    person.data_input()
    persons[person.fullname] = person
print(persons)
for k, v in persons:
    person = Student()
    print(k, v(person.data_output()))
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
