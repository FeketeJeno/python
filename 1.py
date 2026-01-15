"""1. feladat – Szelekció (if-elif-else)
Feladat: Írj egy programot, ami bekér egy egész számot, majd kiírja, hogy pozitív páros, pozitív
páratlan, negatív páros, negatív páratlan, vagy nulla."""

szam=int(input("Kérem egy egész számot: "))
if szam == 0:
    print("A szám: nulla.")
elif szam < 0 and szam % 2 ==0:
    print("A szám negatív, páros szám.")
elif szam < 0 and szam % 2 ==1:
    print("A szám negatív, páratlan szám.")
elif szam > 0 and szam % 2 ==0:
    print("A szám pozitív, páros szám.")
else:
    print("A szám pozitív, páratlan szám")
