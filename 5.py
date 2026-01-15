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
