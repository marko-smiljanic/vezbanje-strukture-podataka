import random
from pprofile import Profile

def sekvencijalna_pretraga(niz, element):
    if(len(niz) == 0):
        return print("Niz je prazan.")
    for i in range(0, len(niz)):
        if(niz[i] == element):
            print("Element je pronadjen. Prva pojava elementa je na indeksu:", i)
            return element
    print("Trazeni element nije pronadjen.")


niz1 = []
for i in range(0, 100):
    broj = random.randint(0, 100)
    niz1.append(broj)

trazeni = random.randint(0, 100)



with Profile() as pr:
    sekvencijalna_pretraga(niz1, trazeni)

print("Vreme sa pprofile:")
pr.print_stats()