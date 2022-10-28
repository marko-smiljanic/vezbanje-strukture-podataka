import random
from pprofile import Profile

def select_sortiranje(niz):
    for i in range(0, len(niz)):
        indeks = i
        for j in range(i + 1, len(niz)):
            if(niz[j] < niz[indeks]):
                indeks = j
        privremeno = niz[indeks]
        niz[indeks] = niz[i]
        niz[i] = privremeno


niz1 = []
for i in range(0, 100):
    broj = random.randint(0, 100)
    niz1.append(broj)

with Profile() as pr:
    select_sortiranje(niz1)

print("Vreme sa pprofile:")
pr.print_stats()