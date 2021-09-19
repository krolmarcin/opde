#zagnieżdżone typy danych
name = "Zenek"
age = 21
gender = "man"

name2 = "Zenobia"
age2 = 21
gender2 = "woman"

human1 = ('Zenek', 21, 'man')
human2 = ('Zenobia', 28, 'woman')
human3 = ('Kuba', 18, 'man')

guestlist = [
    ['Zenek', 21, 'man'],
    ['Zenobia', 28, 'woman'],
    ['Kuba', 18, 'man']
]

print(guestlist)
print(guestlist[0])
print(guestlist[0][0])
print(guestlist[1][1])
print(guestlist[1][2])

guestlist[0][1] = 28
print(guestlist[0])

#Krotka jest szybsza od listy, ale jest RO, to jest krotka w liście
guestlistakrotka = [
    ('Zenek', 21, 'man'),
    ('Zenobia', 28, 'woman'),
    ('Kuba', 18, 'man')
]
print(guestlistakrotka)
guestlistakrotka.append(('Maniek', 21, 'man'))
print(guestlistakrotka)

#tu krotka w krotce nie można append
guestkrotkakrotka = (
    ('Zenek', 21, 'man'),
    ('Zenobia', 28, 'woman'),
    ('Kuba', 18, 'man')
)
print(guestkrotkakrotka)

#set + krotka
guestSetKrotka = {
    ('Zenek', 21, 'man'),
    ('Zenobia', 28, 'woman'),
    ('Kuba', 18, 'man')
}
guestSetKrotka2 = {
    ('Zenek', 21, 'man'),
    ('Zenobia', 28, 'woman'),
    ('K', 18, 'man')
}
#po | dane się nie powtórzą = będą tylko unikalne wartości
guestList3 = guestSetKrotka | guestSetKrotka2
print(guestList3)

#tu będą części wspólne po &
guestList4 = guestSetKrotka & guestSetKrotka2
print(guestList4)
