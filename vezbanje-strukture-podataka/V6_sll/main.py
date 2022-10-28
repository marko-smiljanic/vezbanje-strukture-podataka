from sll.singly_linked_list import SinglyLinkedList
from automobil.automobil import Automobil

#kao i u vecini ostalih jezika main se pravi izvan paketa klase(ako planiramo da imamo vise klasa), python paket se oznacava tako sto ima jedan
# __init__.py fajl - u kojem ne mora da bude nikakvog koda
#zato kad importujemo nesto iz drugog paketa idemo sa from imepaketa.imefajla import * ili samo ono sto nam treba


lista = SinglyLinkedList()
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)

lista.prepand(1)
lista.prepand(2)
lista.prepand(3)

for element in lista:
    print(element, end=" ")
print()
print("Duzina liste je:", len(lista))    #kao redefinisanje operatora u c++


a1 = Automobil("Renalut", "Clio", 175)
a2 = Automobil("Ford", "Focus", 180)
a3 = Automobil("Fiat", "Punto", 150)
a4 = Automobil("Peugeot", "206", 160)

print(a1 == a2)         #operatori vracaju true ili false, tako sam ih implementirao, mozda je moglo drugacije, operator != je negacija na == pa onda dobijamo i njega kada redefinisemo ==
print(a1 >= a2)

lista1 = SinglyLinkedList()
lista1.append(a1)
lista1.append(a2)
lista1.append(a3)
lista1.append(a4)

najbrzi = Automobil.pretrazi_listu_automobila(lista1) 
# print("Najveci iz liste (po max brzini) je: " + str(najbrzi.marka) + " " + str(najbrzi.model) + ".")

lista1 = Automobil.izbaci_sve_osim_najbrzeg(lista1)
print("Lista nakon izbacivanja svega osim najbrzeg: ")
for element in lista1:
    print(str(element.marka) + " " + str(element.model), end=" ")
print()

lista = SinglyLinkedList.dupliraj_listu(lista)      #vrednost postojeceg objekta lista sam morao da promenim ovde, nisam mogao samo da pozovem SinglyLinkedList.dupliraj_listu(lista)... nece je promeniti, u javi to radi
for element in lista:
    print(element, end=" ")
print()


lista92 = SinglyLinkedList()

lista92.append(11)
lista92.append(22)
lista92.append(44)
lista92.append(50)
lista92.append(12)
lista92.append(8)
print(lista92)

print(lista92[0])   #11

print("Posle uklanjanja po vrednosti: ")
lista92.remove(22)
print(lista92)

print("Posle pop-a: ")
lista92.pop(4)
print(lista92)

lista92.insert(2, 555555)
print(lista92)