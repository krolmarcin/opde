# listy - "in" i "not in"
imiona = ["Arkadiusz", "Wioletta", "Karol", "Kuba", "Adrian"] #5 elementów, numerowane od 0
liczby = [3, 4, 7, -49]
mieszana = [7, "siedem", 14, "czternaście"]

# zwróci True
print("Adrian" in imiona)
# zwróci False
print("Marcin" in imiona)

if ("Marcin" in imiona):
    print("Cześć Marcin")
else:
    print("W tej liście nie ma Marcina")

# not in
if (2 not in liczby):
    print("2 nie ma w liczby...")

# not in v.2
if (7 not in liczby):
    print("7 nie ma w liście liczby")
else:
    print("7 jest w liczby :)")

# operacje na listach
print(3 * liczby)

# tymczasowe dodanie do listy
print([1, 2] + liczby)
print(liczby)

# dodanie liczb na stałe do listy
liczby = [1, 2] + liczby
print(liczby)
