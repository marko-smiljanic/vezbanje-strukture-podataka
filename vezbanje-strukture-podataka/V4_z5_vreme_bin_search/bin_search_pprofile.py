import random
from pprofile import Profile


def binarna_pretraga(niz, element):    #da bi ovo radilo niz MORA biti sortiran !!!!!
    if(len(niz) == 0):
        return print("Niz je prazan.")
    pocetak = 0
    kraj = len(niz) - 1
    while(pocetak <= kraj):
        sredina = (pocetak + kraj) // 2     #celobrojno deljenje, jer ne mora dobijeni broj biti deljiv sa 2
        if(element < niz[sredina]):         #napravljeno je za rastuci sortirani niz
            kraj = sredina - 1
        if(element > niz[sredina]):
            pocetak = sredina + 1
        else:
            print("Element pronadjen. Prva pojava elementa na indeksu:", sredina)
            return niz[sredina]


niz1 = []
for i in range(0, 100):
    broj = random.randint(0, 100)
    niz1.append(broj)

trazeni = random.randint(0, 100)
niz1.sort()



with Profile() as pr:
    binarna_pretraga(niz1, trazeni)

print("Vreme sa pprofile:")
pr.print_stats()