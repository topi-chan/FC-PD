# wprowadzenie danych
kredyt = input("Podaj kwotę kredytu: ")
try:
    kredyt_flt = float(kredyt)
except:
    print("Wpisz wartość liczbową")
    quit()
if kredyt_flt == 0.0:
    print("W takim razie nie jesteś zadłużony, gratuluję :)")
    quit()

oprocentowanie = input("Podaj wysokość oprocentowania (przecinek podaj jako kropkę): ")
try:
    oprocentowanie_flt = float(oprocentowanie)
except:
    print("Wpisz wartość liczbową")
    quit()

rata = input("Podaj kwotę raty miesięcznej: ")
try:
    rata_flt = float(rata)
except:
    print("Wpisz wartość liczbową")
    quit()

# poszczególne miesiące po kolei
x1 = 1.59282448436825
x2 = -0.453509101
x3 = 2.324671717
x4 = 1.261254407
x5 = 1.782526286
x6 = 2.329384541
x7 = 1.502229842
x8 = 1.782526286
x9 = 2.328848994
x10 = 0.616921348
x11 = 2.352295886
x12 = 0.337779545
x13 = 1.577035247
x14 = -0.292781443
x15 = 2.48619659
x16 = 0.267110318
x17 = 1.417952672
x18 = 1.054243267
x19 = 1.480520104
x20 = 1.577035247
x21 = -0.07742069
x22 = 1.165733399
x23 = -0.404186718
x24 = 1.499708521

def wydruk(x):
    print(x)
