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

lista = []
inflacja = [1.59282448436825, -0.45350910, 2.324671717]

print("Podaję wysokość kredytu do spłaty w złotych polskich:")

styczen = (1 + ((x1+3)/1200)) * kredyt_flt - rata_flt
print("Styczeń: ", styczen)

luty = (1 + ((x2+3)/1200)) * styczen - rata_flt
print("Luty: ", luty)

marzec = (1 + ((x3+3)/1200)) * luty - rata_flt
print("Marzec: ", marzec)

kwiecien = (1 + ((x4+3)/1200)) * marzec - rata_flt
print("Kwiecień: ", kwiecien)

maj = (1 + ((x5+3)/1200)) * kwiecien - rata_flt
print("Maj: ", maj)

czerwiec = (1 + ((x6+3)/1200)) * maj - rata_flt
print("Czerwiec: ", czerwiec)

lipiec = (1 + ((x7+3)/1200)) * czerwiec - rata_flt
print("Lipiec: ", lipiec)

sierpien = (1 + ((x8+3)/1200)) * lipiec - rata_flt
print("Sierpień: ", sierpien)

wrzesien = (1 + ((x9+3)/1200)) * sierpien - rata_flt
print("Wrzesień: ", wrzesien)

pazdziernik = (1 + ((x10+3)/1200)) * wrzesien - rata_flt
print("Październik: ", pazdziernik)

listopad = (1 + ((x11+3)/1200)) * pazdziernik - rata_flt
print("Listopad: ", listopad)

grudzien = (1 + ((x12+3)/1200)) * listopad - rata_flt
print("Grudzień: ", grudzien)

styczen1 = (1 + ((x13+3)/1200)) * grudzien - rata_flt
print("Styczeń: ", styczen1)

luty1 = (1 + ((x14+3)/1200)) * styczen1 - rata_flt
print("Luty: ", luty1)

marzec1 = (1 + ((x15+3)/1200)) * luty1 - rata_flt
print("Marzec: ", marzec1)

kwiecien1 = (1 + ((x16+3)/1200)) * marzec1 - rata_flt
print("Kwiecień: ", kwiecien1)

maj1 = (1 + ((x17+3)/1200)) * kwiecien1 - rata_flt
print("Maj: ", maj1)

czerwiec1 = (1 + ((x18+3)/1200)) * maj1 - rata_flt
print("Czerwiec: ", czerwiec1)

lipiec1 = (1 + ((x19+3)/1200)) * czerwiec1 - rata_flt
print("Lipiec: ", lipiec1)

sierpien1 = (1 + ((x20+3)/1200)) * lipiec1 - rata_flt
print("Sierpień: ", sierpien1)

wrzesien1 = (1 + ((x21+3)/1200)) * sierpien1 - rata_flt
print("Wrzesień: ", wrzesien1)

pazdziernik1 = (1 + ((x22+3)/1200)) * wrzesien1 - rata_flt
print("Październik: ", pazdziernik1)

listopad1 = (1 + ((x23+3)/1200)) * pazdziernik1 - rata_flt
print("Listopad: ", listopad1)

grudzien1 = (1 + ((x24+3)/1200)) * listopad1 - rata_flt
print("Grudzień: ", grudzien1)

#
#
maks = rata_flt * 24
rata_flt1 = float()
while rata_flt1 < maks:
      rata_flt1 = rata_flt1 + rata_flt
      lista.append(rata_flt1)
print(lista)
#
# for i in inflacja:
# #    rata_flt1 = rata_flt1 + rata_flt
#     x = ((kredyt_flt - rata_flt) - ((i + oprocentowanie_flt)/1200))
#     y = kredyt_flt - x
#     print(y)
    # rata_pozostala = kredyt_flt - x
    # print(rata_pozostala)
miesiace = {}
miesiace = {'styczeń':1.59282448436825, 'luty':-0.453509101, 'marzec':2.324671717}
#
# while rata_flt1 < maks:
#     for k, v in miesiace.items():
#          rata_flt1 = rata_flt1 + rata_flt
#          print(((kredyt_flt - rata_flt1) - ((v + oprocentowanie_flt)/1200)))
#
#
# for i in inflacja and l in lista:
#     while rata_flt1 < maks:
#         rata_flt1 = rata_flt1 + rata_flt
#         x = (kredyt_flt - rata_flt1) - ((i + oprocentowanie_flt)/1200)
#         if x > 0:
#             print("Rata za kolejny miesiąc: ", x, "złotych")
#
#
#
# suma = []
# #
# for num1, num2 in zip(lista, inflacja):
# 	suma.append(num1 * num2)
# print(suma)
# #    print(rata_flt1)
#
# #print('grudzień', ((miesiace[x1]+oprocentowanie_flt)/1200) * kredyt_flt - rata_flt)
# print("Styczeń", (kredyt_flt - rata_flt) - ((x1 + oprocentowanie_flt)/1200), "złotych")
# print("Luty", (kredyt_flt - rata_flt *2 ) - ((x2 + oprocentowanie_flt)/1200), "złotych")
#
# for key, value in miesiace.items():
#     print(key, (kredyt_flt - rata_flt1) - ((value + oprocentowanie_flt)/1200))


#def y():
#    y = x+1

#def wydruk(x):
#    print(x)
