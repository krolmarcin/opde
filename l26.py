#zgadnij liczbę
import random

w = 0
i = random.randint(1, 10)

while i != w:
    w = int(input("\nZgadnij jaką liczbę wylosowałem: "))
    if (i == w):
        print("Zgadłeś wylosowałem:", i)
    else:
        print("Nie zgadłeś, spróbuj jeszcze raz...")
        if (i < w):
            print("Twoja liczba jest za duża")
        else:
            print("Twoja liczba jest za mała")
        continue
