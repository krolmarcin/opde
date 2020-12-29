'''
Operaory logiczne:

and - 'i'
True True = True
True False = False
False True = False
False False = False
Koniunkcja jest prawdziwa wtedy i tylko wtedy, gdy OBA wyrażenia są prawdziwe (są typu True)

or - 'lub'
True True = True
True False = True
False True = True
False False = False
Koniunkcja jest fałszywa wtedy i tylko wtedy, gdy OBA wyrażenia są fałszywe (są typu False)

not - NIE
not() - zaprzeczenie True staje się Falase i odwrotnie

'''

wart = int(input("Sprawdzę, czy liczba jest z zakresu od 1 do 10: "))

if (wart >= 1 and wart <= 10):
    print("wartość jest od 1 do 10")
else:
    print("wartość, którą podałeś/aś jest spoza zakresu 1 - 10")

a = int(input("podaj a: "))
b = int(input("podaj b: "))
if (a >= 1 or b <= 10):
    print("wartość a lub b jest z zakresu a >= 1 lub b <= 10")
else:
    print("wartość a i b jest spoza zakresu a >= 1 lub b <= 10")
