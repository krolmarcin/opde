#wartość bezwzglęgna
import math
a = int(input("Podaj liczbę: "))

if (a < 0):
    print("a jest mniejsza od zera: ", a)
    print("wartość bezwzględna to: ", math.fabs(a))
elif (a > 0):
    print("liczba równa się: ", a)
else:
    print("liczba równa się 0")
