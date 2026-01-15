"""3. feladat – Iteráció (for loop) + lista kezelése
Feladat: Kérj be egy egész számot n, majd generálj egy listát az 1-től n-ig terjedő számokból. Írd ki, mely számok oszthatók 3-mal, és add össze ezeket."""

lista=[]
osszeg=0
print("1-től a megadott számig ellenőrzöm a 3-mal osztható számokat.")
n=int(input("Kérek egy egész számot: "))
for i in range(1,n+1):
    lista.append(i)

for x in range(len(lista)):
    if lista[x] % 3 == 0:
        szamok=lista[x]
        print(f"A hárommal osztható számok:{szamok}")
        osszeg= osszeg + lista[x]

print(f"A hárommal osztható számok összege: {osszeg}")
