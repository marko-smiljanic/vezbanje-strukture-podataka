import random                   #from random import randint   #direkto importujem ono sto mi treba
from test_sort import *
from time import time           #ili perf_counter


niz0 = []   #sva tri niza ce biti ista
niz1 = []
niz11 = []

broj = 0   #mozda i nije trebalo ovo da se stavi??? jer python moze bilo kojui vrednost da strpa u ne deklarisanu i definisanu promenljivu
for i in range(0, 10):
    broj = random.randint(0, 100)
    niz0.append(broj)
    niz1.append(broj)
    niz11.append(broj)

#prikaz nesortiranog niza sa random brojevima
print("Nesortirani niz.")
print(niz0)
#prikaz istog tog nisa sa sortiranjem(bubble)
bubble_sortiranje(niz0)
print("Bubble sortiranje: ")
print(niz0)
print()

print("Nesortirani niz.")
print(niz1)
select_sortiranje(niz1)
print("Select sortiranje: ")
print(niz1)
print()

print("Nesortirani niz.")
print(niz11)
insert_sortiranje(niz11)
print("Insert sortiranje: ")
print(niz11)
print("\n")
#testirano --- radi



################## vreme izvrsavanja ####################
#radim sa time, jer je to najslicnije onome sto je profesor rekao da se radi u javi

niz2 = []               #za bubble... mogao sam i stare nizove resetovati i ponovo raditi sa njima
niz3 = []               #za select
niz4 = []               #za insert, da ne biram 3 puta vrednosti za isti niz(kao gore)

broj = 0                              #nije potrebno, nema tipova u py
for i in range(0, 15000):             #stavio sam ipak 15000, jer drugacije se ne moze docekati
    broj = random.randint(0, 100)
    niz2.append(broj)
    niz3.append(broj)
    niz4.append(broj)                 #sva 3 niza imaju iste brojeve

# pocetak = 0
# kraj = 0                      #NE TREBA!!! u pajtonu nema tipova i ovo ne moram da radim...
# ukupno_vreme_bubble = 0       #jedne te iste promenljive mogu koristiti i prelepljivati vrednost preko njih jer verovatno radi sa referencama, nije kako c++


pocetak = time()
bubble_sortiranje(niz2)
kraj = time()
ukupno_vreme_bubble = kraj - pocetak
print("Ukupno vrme izvrsavanja za bubble:", ukupno_vreme_bubble)



pocetak = time()
select_sortiranje(niz3)
kraj = time()
ukupno_vreme_select = kraj - pocetak
print("Ukpno vreme izvrsavanja za select:", ukupno_vreme_select)



pocetak = time()
insert_sortiranje(niz4)
kraj = time()
ukupno_vreme_insert = kraj - pocetak
print("Ukupno vreme izvrsavanja za insert:", ukupno_vreme_insert)
