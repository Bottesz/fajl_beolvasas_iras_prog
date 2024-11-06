import fajlkezeles
import feladatok


#fajlkezeles.szovegge_alakit2()

lista=fajlkezeles.filebol_olvas()

"""
1.hany negativ szam van a listaban?
"""


print("1.feladat")
db:int=feladatok.negativszamok(lista)
print(f"A negatív számok száma {db}")


"""
2.melyik a legnagyobb szama listaban?
 nem a max fügvénnyel
"""

print("2. feladat")
max_index:int=feladatok.legnagyobb_szam(lista)
print(f"A legnagyobb szám a listában {max_index} ")