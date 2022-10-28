from dll.doubly_linked_list import DoublyLinkedList

class Dequeue:                              #kombinacija i reda i steka, moze da se ukllanja sa oba kraja i dodavanje na oba kraja, i naravno da se dobavljaju vrednosti sa pocetka i kraja
    def __init__(self):
        self.lista = DoublyLinkedList()

    def __len__(self):
        return len(self.lista)

    def add_first(self, value):             #dodavanje nove vrednosti na pocetak (add_left)
        self.lista.prepand(value)

    def add_last(self, value):              #dodavanje nove vrednosti na kraj (add_right)
        self.lista.append(value)

    def remove_first(self):                         #uklanja vrednost sa pocetka i vraca vrednost uklonjenog (remove_left)
        try:
            vrednost = self.lista.first()
            self.lista.remove_first()
            return vrednost
        except IndexError:
            raise IndexError("Dek je prazan.")

    def remove_last(self):                          #metoda koja uklanja vrednost sa kraja deka i vraca vrednost uklonjenog (remove_right)
        try:
            vrednost = self.lista.last()
            self.lista.remove_last()
            return vrednost
        except IndexError:
            raise IndexError("Dek je prazan.")

    def first(self):                                #dobavlja vrednost sa pocetka (left)
        try:
            return self.lista.first()
        except IndexError:
            raise IndexError("Dek je prazan.")

    def last(self):                                 #dobavlja vrednost sa kraja (right)
        try:
            return self.lista.last()
        except IndexError:
            raise IndexError("Dek je prazan.")

    #pogledati implementaciju python liste i njenih metoda, tj. koje su metode ekvivalente sll i dll metodama

    