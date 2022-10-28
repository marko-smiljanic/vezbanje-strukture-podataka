from magacin.magacin import Magacin
from dll.doubly_linked_list import DoublyLinkedList

m1 = Magacin("Hrana", 500, 200)
m2 = Magacin("Pirotehnika", 500, 300)
m3 = Magacin("Pice", 500, 450)

# print(m1 == m2) #jednaki su ako imaju siti kapacitet
# print(m1 == m3)
# print(m1 > m2)  #prvi je veci samo ako imaju isti kapacitet i prvi ima manju zauzetost(tj. vise slobodnog prostora, zato je verovatno operator >)
# print(m1 > m3)
# print(m1 >= m2) #prvi je veci ili jednak ako imaju isti kapacitet i prvi ako ima manju ili jednaku zauzetost(>= slobodnog prostora)
# print(m1 >= m3)

lista1 = DoublyLinkedList()
lista1.append(m1)
lista1.append(m2)
lista1.append(m3)

m4 = Magacin.najveci(lista1)       #ostao mi je jedan print u funkciji najveci
print(m4.tip)


#ne znam kako da odradim zadatak 3 i 4
# Magacin.napuniNajveciDoKraja(lista1)
# for element in lista1:
#     print(element.tip, element.kapacitet, element.zauzetost)

lista2 = DoublyLinkedList()     #test za insert TODO: treba i za pop !!!
lista2.append(2)
lista2.append(3)
lista2.append(7)
lista2.append(10)
lista2.append(2)

print(len(lista2))
for element in lista2:
    print(element, end=" ")
print()

lista2.insert(3, 55555)
#lista2.pop(1)
print(len(lista2))
for element in lista2:
    print(element, end=" ")
print()
