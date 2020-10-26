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

def wydruk(x):
    print(x)
