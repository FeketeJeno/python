"""2. feladat – Szelekció + logikai operátorok
Feladat: Kérj be három számot, majd írd ki, hogy mindhárom páros, mindhárom páratlan, vagy kevert."""

szam1=int(input("Kérem az első számot: "))
szam2=int(input("Kérem a második számot: "))
szam3=int(input("kérem a harmadik számot: "))

if szam1 % 2 == 0 and szam2 % 2 == 0 and szam3 % 2 == 0:
    print("Mindhárom szám páros szám.")
elif szam1 %2 == 1 and szam2 % 2 == 1 and szam3 % 2 == 1:
    print("Mindhárom szám páratlan szám.")
else:
    print("A számok kevertek.")
