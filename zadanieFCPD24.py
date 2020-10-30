paka = 0
paka_maks = 0
puste_maks = 0
puste = 0
puste_suma = 0
wyslane = 0
dodanie = 0

print("Podaj wagę paczki w kg (aby zakończyć wpisz 0): ")

while True:
    fhand = input()
    try:
        fhand_flt = float(fhand)
    except:
        print("Wpisz wartość liczbową")
        continue
    if fhand_flt == 0:
        print("Podsumowanie: ")
        print("Liczba wysłanych paczek: ", paka)
        print("Liczba wysłanych kilogramów: ", wyslane)
        print("Najwięcej 'pustych' kilogramów: ", puste_maks)
        print("Suma 'pustych' kilogramów: ", puste_suma)
        quit()
    elif fhand_flt > 10:
        print("Błąd - podaj wagę od 1 do 10 kg")
        quit()
    elif fhand_flt < 1:
        print("Błąd - podaj wagę od 1 do 10 kg")
        quit()
    paka_maks = paka_maks + fhand_flt
    if paka_maks > 20:
        paka_maks = paka_maks - fhand_flt
        paka += 1
        puste = 20 - paka_maks
        if puste_maks <= puste:
            puste_maks = puste
        puste_suma = puste_suma + puste
        wyslane = wyslane + paka_maks
        paka_maks = fhand_flt
