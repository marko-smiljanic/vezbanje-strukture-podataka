import random
from timeit import timeit
from cProfile import Profile

def insert_sortiranje(niz):
    privremeno = 0
    j = 0
    for i in range(1, len(niz)):
        privremeno = niz[i]
        j = i - 1
        while(j >= 0 and niz[j] > privremeno):
            niz[j + 1] = niz[j]
            j -= 1
        niz[j + 1] = privremeno

#T(n) = 
#O(n) = 

niz1 = []
niz2 = []
for i in range(0, 100):
    broj = random.randint(0, 100)
    niz1.append(broj)
    niz2.append(broj)

rezultat = timeit(stmt="insert_sortiranje(niz1)", number=1, globals=globals())
print("Vreme sa timeit:", rezultat)


with Profile() as pr:
    insert_sortiranje(niz2)

print("Vreme sa cprofile:")
pr.print_stats()