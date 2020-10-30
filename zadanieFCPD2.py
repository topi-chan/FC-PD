# Napisz program do obsługi ładowarki paczek. Każda paczka moze maksymalnie zmieścić 20 kg towaru. do
# paczki dodawane są elementy każdy z nich może ważyć od 1 do 10 kg. Jeśli dodanie elementu do paczki
# zwiększyło by ciężar paczki powyżej 20kg, paczka powinna zostać wysłana (nie można już do niej dodać w
# przyszłości elementów) a bieżący element powinien zostać dodany do nowej paczki.
# Wszystkie elementy powinny zostać wysłane.
# Program powinien pobierać maksymalną liczbę elementów do wysyłki. Jeśli podano element o wadze 0,
# program powinien zakończyć działanie tak jakby maksymalna liczba paczek została osiągnięta.
# na koniec działania program powinien wyświetlić w podsumowaniu:
#
# Liczbę paczek wysłanych
# Liczbę kilogramów wysłanych
# Suma "pustych" - kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych
# Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik
# Program powinien kończyć się z błędem gdy element dodawany ma więcej niż 10kg, lub mniej niż 1 kg i nie
# był dokładnie równy 0

paka = 0
paka_maks = 0
paka_max = 0
puste_maks = 0
puste = 0
puste_suma = 0
wyslane = 0
dodanie = 0

print("Podaj wagę paczki w kg (aby zakończyć wpisz 0): ")

fhand = input()

while fhand:
    fhand = input()
    try:
        fhand_flt = float(fhand)
    except:
        print("Wpisz wartość liczbową")
        continue
    if fhand_flt == 0:
        break
    elif fhand_flt > 10:
        print("Błąd - podaj wagę od 1 do 10 kg")
        quit()
    elif fhand_flt < 1:
        print("Błąd - podaj wagę od 1 do 10 kg")
        quit()
    else:
        paka_maks = paka_maks + fhand_flt + dodanie
        if paka_maks > 20:
            paka_maks = paka_maks - fhand_flt
            paka += 1
            puste = 20 - paka_maks
            if puste_maks >= puste:
                puste_maks = puste
            puste_suma = puste_suma + puste
            wyslane = wyslane + paka_maks
            dodanie = 0 + fhand_flt
            paka_maks = 0
            continue
        else:
            continue


print("Podsumowanie: ")
print("Liczba wysłanych paczek: ", paka)
print("Liczba wysłanych kilogramów: ", wyslane)
#print("Maksymalna wielkość paczki: ", paka_maks)
print("Najwięcej 'pustych' kilogramów: ", puste_maks)
print("Suma 'pustych' kilogramów: ", puste_suma)
quit()
