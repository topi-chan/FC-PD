import sys
import time
from magazyn import file_read

(saldo, lista, magazyn) = file_read(sys.argv[1])
dodanie = int(sys.argv[2])
komentarz = sys.argv[3]
saldo += dodanie
lista.append(dodanie)
lista.append(komentarz)

def file_write(fname):
    lista2 = []
    fd = open(fname, "a")
    for element in lista:
        element_str = str(element)
        lista2.append(element_str)
    for element_str in lista2:
        fd.write(element_str)
        fd.write("\n")

file_write(sys.argv[1])
