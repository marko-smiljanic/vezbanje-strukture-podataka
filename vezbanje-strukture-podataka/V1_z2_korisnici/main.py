from Korisnik import *
from Sluzbenik import *

k1 = Sluzbenik("korime1", "lozinka1", "A01", "Administracija")
k2 = Sluzbenik("korime2", "lozinka2", "PS01", "Pravna sluzba")
k3 = Sluzbenik("korime3", "lozinka3", "TP01", "Tehnicka podrska")
k4 = Sluzbenik("korime4", "lozinka4", "MG01", "Magacin")
k5 = Sluzbenik("korime5", "lozinka5", "TP02", "Tehnicka Podrska")

niz = [k1, k2, k3]
niz.append(k4)
niz.append(k5)

rezultat = False
rezultat = Sluzbenik.prijava(niz)

print(rezultat)

#da sam vracao korisnika mogao sam ga stampati ili dodavati u neki niz prijavljeni_korisnici