from abc import ABC, abstractmethod

class Tree(ABC):        #abstraktna klasa mora imati bar jednu apstraknu metodu

    def __len__(self):
        return 0    #nije implementirano !!!!


    #vraca poziciju cvora koji je koren stabla
    @abstractmethod
    def root(self): ...

    #vraca true ukoliko je pozicija p cvor koji je koren stabla, u suprotnom false, p je pozicija za koju proveravamo da li je koren
    @abstractmethod
    def is_root(self, p): ...

    #vraca poziciju cvora (deteta) koji je roditelj od p, vracamo poziciju roditelja
    @abstractmethod
    def parent(self, p): ...

    #veraca broj dece od cvora na poziciji p
    @abstractmethod
    def num_children(self, p): ...

    #metoda koja prolazi (iterise) kroz svu decu cvora na poziciji p (koristi yield), p je roditelj ciju decu obilazimo
    @abstractmethod
    def children(self, p): ...

    #vraca true ako je cvor na poziciji p listni cvor, false ako nije, tj. ako je num_children == 0 onda znamo da je to lsitni cvor
    @abstractmethod
    def is_leaf(self, p):
        if(self.num_children(p) == 0):
            return True
        return False

    #vraca trure ako je stablo prazno
    def is_empty(self):
        return len(self) == 0

