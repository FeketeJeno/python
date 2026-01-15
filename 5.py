"""5. feladat: Hozz létre egy Diak osztályt a következőkkel: - Attribútumok:
nev (string), eletkor (int), jegyek (lista int) - Metódusok:
- atlag() – visszaadja a jegyek átlagát
- bemutatkozas() – kiírja: &quot;Szia, [név] vagyok, [életkor] éves.&quot;
- szinten() – visszaadja, hogy a diák Jó, Közepes vagy Gyenge a jegyek átlaga alapján."""
class Diak:
    def __init__(self,nev,eletkor,jegyek):
        self.nev = nev
        self.eletkor = eletkor
        self.jegyek = jegyek

def atlag(self):
        if len(self.jegyek) == 0:
            return 0
        return sum(self.jegyek) / len(self.jegyek)

def bemutatkozas(self):
        print(f"Szia, {self.nev} vagyok, {self.eletkor} éves.")

def szinten(self):
        atlag = self.atlag()
        if atlag>=4:
            return "Jó"
        elif atlag>=3:
            return "Közepes"
        else:
            return "Gyenge"

diak1 = Diak("Emese", 14, [4,3,5,5,5,5,5])

diak1.bemutatkozas()
print("Átlag", diak1.atlag(),"\n")
print("Szint", diak1.szinten(),"\n")