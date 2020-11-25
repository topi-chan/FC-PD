from sys import argv
arg = sys.argv[1]

persons = {}
classrooms = {}

class Classroom:
     def __init__(self, classroom):
         self.classroom = classroom
         self.teachers = []
         self.students = []
         self.mentor = ""


class Student:
    def __init__(self):
        self.fullname = ""
        self.classroom = ""

    def data_input(self):
        self.fullname = input("Podaj dane ucznia: ")
        classroom = input("Podaj nazwę klasy: ")
        if classroom not in classrooms:
            classrooms[classroom] = Classroom(classroom)
        self.classroom = classrooms[classroom]
        self.classroom.students.append(self)

# TODO: wydrukować ładnie listę w teacher.subject, for subject, in teacher.subject print subject
    def data_output(self):
        for teacher in self.classroom.teachers:
            print("Nauczyciel: ", teacher.fullname)
            print("Przedmioty: ", teacher.subject)
        print("Wychowawca: ", self.classroom.mentor)


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
        if classroom not in classrooms:
            classrooms[classroom] = Classroom(classroom)
        self.classroom = classrooms[classroom]
        self.classroom.teachers.append(self)

    def data_output(self):
        v = persons.values()
        for z in v:
            if isinstance (z, Mentor):
                for c in self.classroom:
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
        if classroom not in classrooms:
            classrooms[classroom] = Classroom(classroom)
        self.classroom = classrooms[classroom]
        self.classroom.mentor.append(self)

    def data_output(self):
        v = persons.values()
        for z in v:
            if isinstance (z, Student):
                if z.classroom in self.classroom:
                    print(z.fullname)


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

if arg in persons:
    v = persons.get(arg)
    v.data_output()

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
