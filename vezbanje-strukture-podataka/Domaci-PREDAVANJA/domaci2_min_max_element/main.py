import random
from min_max_element import *

niz1 = []
broj = 0
for i in range(0, 100):     #popunjavanje niza
    broj = random.randint(0, 100)
    niz1.append(broj)

for i in range(0, len(niz1)):   #stampanje niza
    if(i % 15 == 0):            #ova provera mora da ide prva jer ce mi na 14 indeksu biti 15 element
        print()
    print(niz1[i], end=" ")

print() #da predje u novi red
niz2 = []
niz2 = min_max_element(niz1)    #u print sam mogao staviti samo poziv funkcije sa parametrom jer u pajton stampa skoro sta god da se prosledi u vec definisanom formatu
print("Najmanji i najveci element niza je: ", niz2)
