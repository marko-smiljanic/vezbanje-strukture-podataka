import random
from timeit import timeit
from cProfile import Profile

def select_sortiranje(niz):
    for i in range(0, len(niz)):
        indeks = i
        for j in range(i + 1, len(niz)):
            if(niz[j] < niz[indeks]):
                indeks = j
        privremeno = niz[indeks]
        niz[indeks] = niz[i]
        niz[i] = privremeno

#T(n) = 
#O(n) = 


niz1 = []
niz2 = []
for i in range(0, 100):
    broj = random.randint(0, 100)
    niz1.append(broj)
    niz2.append(broj)

rezultat = timeit(stmt="select_sortiranje(niz1)", number=1, globals=globals())
print("Vreme sa timeit:", rezultat)


with Profile() as pr:
    select_sortiranje(niz2)

print("Vreme sa cprofile:")
pr.print_stats()