# len() - długość - lenght
# .append - dodać
# .extend - rozszerzyć
# .insert(index, co) - wstawić
# .index - index danego elementu
# sort(reverse=False) - sortuj rosnąco, malejąco =True
# max()
# min()
# .count - ile razy coś wystąpi
# .pop - usuń ostatni element
# .remove - usuń pierwsze wystąpienie
# .clear - wyczyść listę
# .reverse - zmień kolejność

lista1 = [54, 1, -2, 20, 1]
lista2 = ["Arkadiusz", "Wioletta"]

# długość listy1
print(len(lista1))

# dodaję 4 na końcu listy1 na stałe i wypiszę ją
lista1.append(4)
print(lista1)

# rozszerzam listę1
lista1.extend([2, 12, 24, 2])
print(lista1)

# wstawiam
lista2.insert(0, "Marcin")
print(lista2)

# index
print(lista1.index(20))

# sort
lista1.sort()
print(lista1)
lista2.sort()
print(lista2)

# max
print(max(lista1))

# min
print(min(lista1))

# .count
print(lista1.count(4))
print(lista1.count(2))

# .pop
print("Usuwam z listy1 ostatnią wartość:", lista1.pop())
print(lista1)

# .remove
print("Usuwam z listy1 pierwsze wystąpienie 2:")
lista1.remove(2)
print(lista1)

# .clear
lista3 = [1, 2, 3, 4, 5, 6, 7]
print(lista3)
print("Czyszczę listę3. Lista3:")
lista3.clear()
print(lista3)

# .reverse
lista3 = [1, 2, 3, 4, 5, 6, 7]
print("Lista3:")
print(lista3)
lista3.reverse()
print("Odwracam listę3: lista3.reverse():")
print(lista3)
