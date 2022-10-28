import random
from pprofile import Profile

def bubble_sortiranje(niz):
    privremeno = 0
    duzina = len(niz)
    for i in range(0, duzina - 1):
        for j in range(0, (duzina - 1) - i):
            if(niz[j] > niz[j + 1]):
                privremeno = niz[j]
                niz[j] = niz[j + 1]
                niz[j + 1] = privremeno

niz1 = []
for i in range(0, 100):
    broj = random.randint(0, 100)
    niz1.append(broj)

with Profile() as pr:
    bubble_sortiranje(niz1)

print("Vreme sa pprofile:")
pr.print_stats()
#ili pokrenuti u konzoli
