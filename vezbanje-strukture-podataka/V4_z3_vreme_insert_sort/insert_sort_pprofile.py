import random
from pprofile import Profile

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

niz1 = []
for i in range(0, 100):
    broj = random.randint(0, 100)
    niz1.append(broj)

with Profile() as pr:
    insert_sortiranje(niz1)

print("Vreme sa pprofile:")
pr.print_stats()