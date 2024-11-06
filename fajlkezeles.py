import random

def lista_letrehozas():
    # generalj 100 veletlen szamot [-50 es 150] kozott
    # a függvény térjen vissza egy listaval 
    lista = []
    i = 0
    for i in range (0,100,1):
        veletlen_szam:int = int(random.random()*(151+50))-50
        lista.append(veletlen_szam)
    return lista

lista=lista_letrehozas()
print(lista)

"""def szovegge_alakit(lista):
    szoveg = str(szoveg)
    print(szoveg)


    for i in range (0,len(szoveg)):
        print(f"{szoveg}",end=",")"""



def szovegge_alakit2(lista):
    szoveg:str=""
    for i in range(0,len(lista),1):
        if (i<len(lista)-1):
            szoveg+=f"{lista[i]};"
        else:
            szoveg+=f"{lista[i]}"
    return szoveg

szoveges_lista=szovegge_alakit2(lista)
print(szovegge_alakit2)




def fileba_mentes(szoveg):
    file = open("adatok.txt","w",encoding='utf-8')
    file.write(szoveg)
    file.close()

fileba_mentes(szoveges_lista)


def filebol_olvas():
    file = open("adatok.txt","r",encoding="utf-8")
    szoveg_filebol:str=file.read()
    szoveg_lista=szoveg_filebol.split(";")
    """vegig megyek a szovgelistan es minden elemet szamma alakiton es eltavolitom belole a feleseleges szokozoket"""
    lista = []
    for i in range(0,len(szoveg_lista),1):
        szam:int=int(szoveg_lista[i].strip())
        lista.append(szam)
        print(szoveg_filebol)
        print(lista)
        file.close()
        return lista





    


