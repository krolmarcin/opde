"""
operatory porównania:
> większy niż
< mniejszy niż
== równy
!= nie równy
>= większy lub równy
<= mniejszy lub równy
"""
print(5 > 4)
print(3 > 3)
print(3 != 4)
print(3 != 3)
print(3 >= 4)
print(2 >= 2)
# Ważne: = to oerator przypisana, a do porównania służy ==
print(2 == 2)
# przypisanie do a inputa jako striga i porówanie do integera
print("Podaj liczbę 5:")
a = input()
print("nie print(5 = 5) tylko print(5 == 5), print(a == 5) zwróci False, bo = to operator przypsania, a == to porównanie. "
      "Żeby było True w przypdaku print(5 == 5) to trzeba dać: a = int(input())")
print(a == 5)
