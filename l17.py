"""
Instrukcja warunkowa:

Jeśli (prawda)
 to (zrób to)
Jeśli coś innego (prawda)
 to (zrób to)
A w całkowicie innym przypadku
 to (zrób to)
"""
print("Podaj int a:")
a = int(input())
print("Podaj int b:")
b = int(input())
if (a > b):
    print("a > b")
elif (a < b):
    print("a < b")
else:
    print("a = b")

print("Drugie podejście...")
wybor = input("* - mnożenie, / - dzielenie, + - dodawanie, - - odejmowanie\n")
a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))
if (wybor == "*"):
    print("a * b")
    print(a * b)
elif (wybor == "/"):
    if (b == 0):
        print("b podałeś 0, nie ma dzielenia przez 0...")
    else:
        print("a / b")
        print(a / b)
elif (wybor == "+"):
    print("a + b")
    print(a + b)
elif (wybor == "-"):
    print("a - b")
    print(a - b)
else:
    print("wybrałeś inny znak")
