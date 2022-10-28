from test_search import *
import random
from time import time

niz1 = []

broj = 0
for i in range(0, 100000):
    broj = random.randint(0, 70000)     #stavljam do 70 000 da ima vecu verovatnocu pronalaska elementa
    niz1.append(broj)

trazeni_br = random.randint(0, 70000)
niz1.sort()

############ merenje vremena #############
#merim sa time, jer je to najslicnije onome sto je profesor pokazivao za javu(studentima u bg)
#ispravnost funkcija je vec testirano u test_search.py



pocetak = time()
sekvencijalna_pretraga(niz1, trazeni_br)    #nisam stavljao u promenljivu(vraca element, jer u funkciji imam print na kojem je indeksu taj element)
kraj = time()
ukupno_vreme_sekvencijalna = kraj - pocetak
print("Ukupno vreme izvrsavanja za sekvencijalnu pretragu:", ukupno_vreme_sekvencijalna)
print()




pocetak = time()
binarna_pretraga(niz1, trazeni_br)
kraj = time()
ukupno_vreme_binarna = kraj - pocetak
print("Ukupno vreme izvrsavanja za binarnu pretragu:", ukupno_vreme_binarna)
print()



print("U zadatku se trazilo da se od SORTIRANOG niza rade ove dve pretrage." + "\n"
        + "Nekad prikaze za obe pretrage 0.0 vreme, ali kada se pokrene vise puta binarna pretraga je u vecini slucajeva brza.")