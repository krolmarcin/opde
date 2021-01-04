# Petla for
# i in range(5), i in 'trala', i n [0, 1, 2, 3],
wynik = 0
i = 0

for i in range(4):
    x = int(input("Podaj liczbę: "))
    wynik += x

print("Wynik dodawania liczb, które podałeś to:", wynik)

i = 0
for i in range(15):
    if (i % 2 == 0):
        print("Liczba", i, " jest parzysta")

l = 0
for l in range(201):
    if (l % 5 == 0 and l % 7 != 0):
        print(l)
