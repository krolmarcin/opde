#krotki (szybkie operacje, mało miejsca w pamięci, ale nie można zmienić, korzystać kiedy można i nie trzeba
# zmieniać wartości w innym przypadku lista)
krotka_bez_nawiasów = 1, 7, 14, -7
krotka_z_nawiasami = (16, 32, 64, -128)

#Wyświetlanie
print(krotka_bez_nawiasów)
print(krotka_z_nawiasami)

#wyświetlanie miejsca drugiego
print(krotka_bez_nawiasów[1])

#krotki nie można zmienić, to będzie błąd [TypeError: 'tuple' object does not support item assignment]
#krotka_bez_nawiasów[0] = 28

#listę można zmienić [nawiasy kwadratowe]
lista01 = [1, 7, 14, -7]
print(lista01)

lista01[0] = 28
print(lista01)
