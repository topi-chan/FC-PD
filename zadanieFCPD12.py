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

styczen = (1 + ((x1+3)/1200)) * kredyt_flt - rata_flt
print("Styczeń: ", styczen)

luty = (1 + ((x2+3)/1200)) * styczen - rata_flt
print("Luty: ", luty)

marzec = 

# print(Styczeń:)
#
#
# # maks = rata_flt * 24
# # rata_flt1 = float()
# # while rata_flt1 < maks:
# #       rata_flt1 = rata_flt1 + rata_flt
# #       lista.append(rata_flt1)
# # print(lista)
#
# for i in inflacja:
# #    rata_flt1 = rata_flt1 + rata_flt
#     x = ((kredyt_flt - rata_flt) - ((i + oprocentowanie_flt)/1200))
#     y = kredyt_flt - x
#     print(y)
    # rata_pozostala = kredyt_flt - x
    # print(rata_pozostala)
# miesiace = {}
# miesiace = {'y1':1.59282448436825, 'y2':-0.453509101, 'y3':2.324671717}
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
