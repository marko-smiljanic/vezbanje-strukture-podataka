from sll.singly_linked_list import SinglyLinkedList

class Stack:                                        #struktura tipa FIFO (first in first out)
    def __init__(self):                             #ovde smo odabrali da bude sll, ali moze biti u doubly i py lista... svejedno
        self.lista = SinglyLinkedList()             #vrh steka ce nam biti kraj liste!!!

    def __len__(self):
        return len(self.lista)

    def push(self, value):                          #dodavanje vrednosti na pocetak(vrh) steka (tj. sa kraja liste)
        self.lista.append(value)

    def pop(self):                                  #pop mora da ukloni i vrati element sa vrha steka (tj. sa kraja liste)
        try:
            value = self.lista.last()
            self.lista.remove_last()
            return value
        except IndexError:                          #mogao sam da dodam posle indexerror as error: i da ga obradjujem slicno kao u javi
            raise IndexError("Stek je prazan.")

    def top(self):                                  #dobavlja vrednost sa vrha (tj. sa kraja liste)
        try:
            return self.lista.last()
        except IndexError:
            raise IndexError("Stek je prazan.")
        