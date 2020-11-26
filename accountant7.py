
import sys

saldo = 0
lista = []
magazyn = {}
produkty = []
counts = {}


def file_read_mode(file):
    fhand = open(file)
    fh = fhand.readlines()
    for line in fh:
        print(line)


#file_read_mode(sys.argv[1])


while True:
    fhand = open(sys.argv[1])
    fh = fhand.readlines()
    for line in fh:
        line = line.rstrip()
        if line.startswith("saldo"):
            lista.append(line)
        try:
            line = int(line)
            lista.append(line)
            continue
        except:
            pass
        print(line)
            # saldo += line+1
            # lista.append(line+2)
    break
print(saldo)
print(lista)

quit()
#

#
#
#
# def balance_mode(arg2, arg3):
#
#     agr2 = int(sys.argv[2])
#     arg3 = sys.argv[3]
#     saldo += arg2
#     lista.append(arg1)
#     lista.append(arg2)
#     lista.append(arg3)
#     print(saldo)



#def sell_mode ()

# ? file_read(argv[1], argv[2])
# ?name = sys.argv[1]
# ?mode = sys.argv[2]
