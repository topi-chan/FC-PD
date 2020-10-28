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

# poszczególne miesiące po kolei - inflacja
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

#wydruk
print("Podaję wysokość kredytu do spłaty w złotych polskich:")

styczen = (1 + ((x1+oprocentowanie_flt)/1200)) * kredyt_flt - rata_flt
print("Styczeń: ", styczen)

luty = (1 + ((x2+oprocentowanie_flt)/1200)) * styczen - rata_flt
print("Luty: ", luty)

marzec = (1 + ((x3+oprocentowanie_flt)/1200)) * luty - rata_flt
print("Marzec: ", marzec)

kwiecien = (1 + ((x4+oprocentowanie_flt)/1200)) * marzec - rata_flt
print("Kwiecień: ", kwiecien)

maj = (1 + ((x5+oprocentowanie_flt)/1200)) * kwiecien - rata_flt
print("Maj: ", maj)

czerwiec = (1 + ((x6+oprocentowanie_flt)/1200)) * maj - rata_flt
print("Czerwiec: ", czerwiec)

lipiec = (1 + ((x7+oprocentowanie_flt)/1200)) * czerwiec - rata_flt
print("Lipiec: ", lipiec)

sierpien = (1 + ((x8+oprocentowanie_flt)/1200)) * lipiec - rata_flt
print("Sierpień: ", sierpien)

wrzesien = (1 + ((x9+oprocentowanie_flt)/1200)) * sierpien - rata_flt
print("Wrzesień: ", wrzesien)

pazdziernik = (1 + ((x10+oprocentowanie_flt)/1200)) * wrzesien - rata_flt
print("Październik: ", pazdziernik)

listopad = (1 + ((x11+oprocentowanie_flt)/1200)) * pazdziernik - rata_flt
print("Listopad: ", listopad)

grudzien = (1 + ((x12+oprocentowanie_flt)/1200)) * listopad - rata_flt
print("Grudzień: ", grudzien)

styczen1 = (1 + ((x13+oprocentowanie_flt)/1200)) * grudzien - rata_flt
print("Styczeń: ", styczen1)

luty1 = (1 + ((x14+oprocentowanie_flt)/1200)) * styczen1 - rata_flt
print("Luty: ", luty1)

marzec1 = (1 + ((x15+oprocentowanie_flt)/1200)) * luty1 - rata_flt
print("Marzec: ", marzec1)

kwiecien1 = (1 + ((x16+oprocentowanie_flt)/1200)) * marzec1 - rata_flt
print("Kwiecień: ", kwiecien1)

maj1 = (1 + ((x17+oprocentowanie_flt)/1200)) * kwiecien1 - rata_flt
print("Maj: ", maj1)

czerwiec1 = (1 + ((x18+oprocentowanie_flt)/1200)) * maj1 - rata_flt
print("Czerwiec: ", czerwiec1)

lipiec1 = (1 + ((x19+oprocentowanie_flt)/1200)) * czerwiec1 - rata_flt
print("Lipiec: ", lipiec1)

sierpien1 = (1 + ((x20+oprocentowanie_flt)/1200)) * lipiec1 - rata_flt
print("Sierpień: ", sierpien1)

wrzesien1 = (1 + ((x21+oprocentowanie_flt)/1200)) * sierpien1 - rata_flt
print("Wrzesień: ", wrzesien1)

pazdziernik1 = (1 + ((x22+oprocentowanie_flt)/1200)) * wrzesien1 - rata_flt
print("Październik: ", pazdziernik1)

listopad1 = (1 + ((x23+oprocentowanie_flt)/1200)) * pazdziernik1 - rata_flt
print("Listopad: ", listopad1)

grudzien1 = (1 + ((x24+oprocentowanie_flt)/1200)) * listopad1 - rata_flt
print("Grudzień: ", grudzien1)
