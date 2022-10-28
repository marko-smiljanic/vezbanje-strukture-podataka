from max_element import maxx
import random

niz1 = []

#random odabir brojeva i njihov smestanje u niz1
i = 0
for i in range(50):
    broj = random.randint(0, 100)  #mogao sam i sa random() ...on vraca broj [0, 1), ako mi treba broj od 0 do 100 islo bi random() * 100 + 1 .. ili samo staviti 101
    niz1.append(broj)             #broj = broj.__round__(2)  #u slucaju da sam ostavio sa random onda bih morao da zaokruzim vrednost jer bih dobio vrednosti sa mnogo decimala
    i += 1

#ispis za po 10 brojeva u koloni
i = 0
brojac = 0
for i in range(50):
    if(brojac % 10 == 0):
        print("")             #svaki put kad se pozove print on automatski krece u novi red... znaci ovde kao da mi stoji System.out.println(); ili cout << endl; ... da sam stavio print("\n") jedan red bi bio prazan izmedju stampe brojeva
    print(niz1[i], end=" ")   #pisi ih u istom redu i na kraju svakog elementa zapisi razmak
    i += 1
    brojac += 1

najveci_element_indeks = maxx(niz1)  #funkcija vraca indeks
print("Najveci element na indeksu: " + str(najveci_element_indeks) + ", je: ", niz1[najveci_element_indeks])

#u pythonu da bi se u printu dodavali argumenti sa + moraju biti svi stringovi... znaci moram raditi kastovanje sa funkcijom str(element)
#ako necu da kastujem u string, onda moram da razdvojim elemente sa , ali ce tad dodati jedan space automatski izmedju elemenata koji su razdvojeni zarezom
#u printu u javi sam npr. int i string mogao da spojim sa + bez kastovanja... i u c++ takodje

