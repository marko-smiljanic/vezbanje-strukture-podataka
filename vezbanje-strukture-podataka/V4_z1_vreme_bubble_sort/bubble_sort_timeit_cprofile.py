import random
from timeit import timeit
from cProfile import Profile


def bubble_sortiranje(niz):
    privremeno = 0
    duzina = len(niz)
    for i in range(0, duzina - 1):
        for j in range(0, (duzina - 1) - i):
            if(niz[j] > niz[j + 1]):
                privremeno = niz[j]
                niz[j] = niz[j + 1]
                niz[j + 1] = privremeno

#T(n) = n-1 * ((n-1/2) * 3)
#O(n) = n-1**2

niz1 = []
niz2 = []
# niz3 = []
for i in range(0, 100):
    broj = random.randint(0, 100)
    niz1.append(broj)
    niz2.append(broj)
    # niz3.append(broj)


rezultat = timeit(stmt="bubble_sortiranje(niz1)", number=1, globals=globals())
print("Vreme sa timeit:", rezultat)


with Profile() as pr:
    bubble_sortiranje(niz2)

print("Vreme sa cprofile:")
pr.print_stats()

# with Profile() as pr:         #ista je komanda za pprofile, ne mogu da znam kad je pozvao sta
#     bubble_sortiranje(niz3)

# print("Vreme sa pprofile:")
# pr.print_stats()
