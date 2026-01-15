"""4. feladat - Iteráció + feltételes logika + string kezelés
Feladat: Kérj be egy mondatot, majd számold meg a magánhangzók számát és listázd ki, hogy melyik magánhangzó hányszor fordul elő."""
mondat = input("Írj be egy mondatot: ")

mgh = {}
mh = "aáeéiíoóöőuúüű"
mghDarab = 0
for i in mondat:
    if i in mh:
        mghDarab += 1
        if i in mgh:
            mgh[i] += 1
        else:
            mgh[i] = 1