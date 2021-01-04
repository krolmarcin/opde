# break and continue

w = 0

for i in range(3):
    x = int(input("Podaj liczbę dodatnią: "))
    if (x > 0):
        w += x
        print("Podałeś liczbę dodatnią. Ich suma to:", w)
    else:
        print("Podałeś liczbę ujemną, a miała być dodania... Kończę.")
        break

print("\n")

w = 0
i = 0
while i < 3:
    x = int(input("Podaj liczbę dodatnią: "))
    if (x > 0):
        w += x
    else:
        print("Podałeś liczbę ujemną, a miała być dodania... Nie dodam tego minusa.")
        continue
    print("Podałeś liczbę dodatnią. Ich suma to:", w)
    i += 1


print("\n")
# Napisz program, który doda kolejne 3 parzyste liczby dodatnie podane przez użytkownika
z = 0
a = 0
w = 0

while a < 3:
    z = int(input("Podaj liczbę parzystą i większą od 0: "))
    if (z % 2 == 0 and z > 0):
        w += z
    else:
        print("Podałeś liczbę nieparzystą lub niedodatnią, podaj parzystą i dodatnią...")
        continue
    print("OK liczba jest parzysta, ich suma to: ", w)
    a += 1
