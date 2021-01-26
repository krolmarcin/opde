# listy - pojemniki do przechowywania elementów, el. numerujemy od 0
imiona = ["Arkadiusz", "Wioletta", "Karol", "Kuba", "Adrian"] #5 elementów, numerowane od 0
liczby = [3, 4, 7, -49]
mieszana = [7, "siedem", 14, "czternaście"]

print(imiona)

for imie in imiona:
    print(imie)

# wypisze pierwsze imię z imiona
print("\nPierwsze imie w liście imiona (listy liczy się od 0) to:")
print(imiona[0])

print("\nOstatni (od końca -1) to:")
print(imiona[-1])

print("\nSzybka podmiana ostatniego:")
imiona[-1] = "Marcin"
print(imiona[-1])
print(imiona[4])
