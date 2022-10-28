from sll.singly_linked_list import SinglyLinkedList

class Queue:                                # FILO (first in last out) struktura slicna steku ali mozemo da dodajemo samo na kraj i da uklanjamo samo sa pocetka, i da dobavljamo vrednost sa pocetka
    def __init__(self):
        self.lista = SinglyLinkedList()     #ovde je pocetak reda, pocetak liste, nije kao kod steka obrnuto
    
    def __len__(self):
        return self.lista.size()
        #moze i return len(self.lista)      #automatski ce pozvati len iz liste

    def enqueue(self, value):               #dodavanje na kraj reda
        self.lista.append(value)

    def dequeue(self):                      #uklanja i vraca vrednost sa pocetka             
        try:
            value = self.lista.first()
            self.lista.remove_first()
            return value
        except IndexError:
            raise IndexError("Red je prazan.")

    def first(self):
        try:
            self.lista.first()
        except IndexError:
            raise IndexError("Red je prazan.")   #izuzetak je vec obradjen u sll ali ovde hocemo da ispise drugaciju poruku i zato ga ponovo odradjujemo

    