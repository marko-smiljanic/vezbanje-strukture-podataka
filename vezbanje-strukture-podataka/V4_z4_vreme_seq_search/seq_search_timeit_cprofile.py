import random
from timeit import timeit
from cProfile import Profile

def sekvencijalna_pretraga(niz, element):
    if(len(niz) == 0):
        return print("Niz je prazan.")
    for i in range(0, len(niz)):
        if(niz[i] == element):
            print("Element je pronadjen. Prva pojava elementa je na indeksu:", i)
            return element
    print("Trazeni element nije pronadjen.")

#T(n) = 
#O(n) = 

niz1 = []
niz2 = []
for i in range(0, 100):
    broj = random.randint(0, 100)
    niz1.append(broj)
    niz2.append(broj)

trazeni = random.randint(0, 100)


rezultat = timeit(stmt="sekvencijalna_pretraga(niz1, trazeni)", number=1, globals=globals())
print("Vreme sa timeit:", rezultat)


with Profile() as pr:
    sekvencijalna_pretraga(niz2, trazeni)

print("Vreme sa cprofile:")
pr.print_stats()