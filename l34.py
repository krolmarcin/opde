#Pętle, a typy zagnieżdżone
guestSetKrotka = {
    ('Zenek', 21, 'man'),
    ('Zenobia', 28, 'woman'),
    ('Kuba', 18, 'man')
}
guestSetKrotka2 = {
    ('Zenek', 21, 'man'),
    ('Zenobia', 28, 'woman'),
    ('Kamil', 18, 'man')
}

guestList3 = guestSetKrotka | guestSetKrotka2
guestList4 = guestSetKrotka & guestSetKrotka2

print("Części unikatowe:")
for name, age, gender in guestList3:
    print("Imię: ", name)
    print("Wiek: ", age)
    print("Płeć: ", gender)
    print("")

print("\nCzęści wspólne:")
for name, age, gender in guestList4:
    print("Imię: ", name)
    print("Wiek: ", age)
    print("Płeć: ", gender)
    print("")
