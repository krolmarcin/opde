'''
        el. unikalne | kolejność | zmana konkretnego el. | nowe elementy
listy       NIE         TAK                 TAK                 TAK
krotki      NIE         TAK                 NIE                 NIE
słowniki    TAK         NIE                 TAK                 TAK
zbiory      TAK         NIE                 NIE                 TAK


        ZBIORY: BONUS w postaci | & - ^
'''
A = {1, 4, 21, 7, 21}
print(A) # -4, 1, 4, 21 (unikalne, nie ma kolejności)

A.add(7)
print(A)

#zbór zrobiony z listy, usuwa duplikaty
B = [1, 7, 21, 4, 21]
print(B)
print(set(B))

#lista: &
C = {1, 7, 21, 4, 21}
D = {2, 1, 25, 40, 21}
print(D)
print(C&D) #wyświetli tylko elm wspólne
print(C|D) #unikalne
print(C-D) #wszystko w C tylko to co nie w D
print(C^D) #alternatywa wykluczająca - wyklucza wsolne wartości

C.discard(1) #usunie "1"
print(C)

#czy jeden zbiór jest podzbiorem drugiego?
print(C.issubset(D))
