from sll.node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None        #ovde se definisu atributi klase
        self.tail = None        #konstruktor pravimo tako da se napravi prazna lista pri instanciranju
        self.size = 0           #prazna lista ima 0 elemenata(cvorova)
    
    def __len__(self):
        return self.size

    def __iter__(self):                     #specificna magicna metoda, vraca, poziva se samo u for each
        current = self.head                 #odakle pocinjemo prolazak
        while(current is not None):         #da je ostalo current.next_p is not None ne bi vratio poslednji element jer je pokazivac od poslednjeg elementa None
            yield current.value             #yield je slucno sa return ali return vrati i obustavi funkciju, yild vrati i na zahtev sledece iteracije nastavi tamo gde je bila yield(gde je bila provera)
            current = current.next_p        #prelazak na sledeci element
                                            #ovde bi moglo da stoji return None, ali to je podrazumevano u pajtonu
    
    def _iter_node(self):                   #po konvenciji koji pocinju sa _ oni su privatni(ne zapravo privatni jer je sve public u pajtonu, znaci trebalo bi da je samo koristimo u klasi)
        current = self.head                
        while(current is not None):         
            yield current            
            current = current.next_p

    def __str__(self):
        rezultat = "["
        brojac = 0
        for element in self:                    #for i in range(len(self)) ali nemamo mehanizam indeksiranja, to je metoda __getitem__(self, i)
            rezultat += str(element)
            if(brojac < len(self) - 1):             #moram da idem do poslednjeg (zaljucno sa njim) jer se i on racuna (nije sentinel kao kod dvostruke liste). len(self)posto imam redefinsanu tu funkciju
                rezultat += ", "                #poslednji kome ce staviti zarez je pretposlednji
            brojac += 1
        return rezultat + "]"

    def __getitem__(self, i):                   #lista[0] vraca vrednost na toj poziciji    
        if(type(i) != int):
            raise TypeError("Indeks mora biti ceo broj")
        if(0 <= i < self.size):                 #ili i <= self.size - 1, ide se do poslednjeg
            brojac = 0
            for element in self:
                if(brojac == i):
                    return element
                brojac += 1
        else:
            raise IndexError("Indeks van opsega.")

    def __setitem__(self, i, value):                #lista[0] = 1 na poziciju 0 stavi broj 1
        if(type(i) != int):
            raise TypeError("Indeks mora biti ceo broj")
        if(0 <= i < self.size):
            brojac = 0
            for node in self._iter_node():          #prolazimo kroz cvorove
                if(brojac == i):
                    node.value = value
                    break                           #nema potrebe da prolazi do kraja ako se vrednost postavila
                brojac += 1
        else:
            raise IndexError("Indeks izvan opsega")

    def prepand(self, value):               #dodavanje nove vrednosti na pocetak, tj. mroa se dodati novi cvor
        new_node = Node(value, self.head)   #novi pocetak ce pokazivati na stari pocetak, i biti umetnut na pocetak
        if (self.size == 0):
            self.tail = new_node            #ako nema elemenata onda je takodje za kraj je proglasen novi cvor, head i tail su isti
        
        self.head = new_node                #proglasen novi pocetak(novododati cvor je sad pocetak liste), tj. umetanje novog cvora koji pokazuje na stari pocetak
        self.size += 1
    
    def append(self, value):                #ne preklapaju se funkcije, jer je ovo nova klasa. Dodaje novu vrednost na kraj liste u vidu cvora
        new_node = Node(value)
        if(self.size == 0):                 #ako je prazna lista i tail i head su isti
            self.head = new_node
        else:
            self.tail.next_p = new_node     #ako nije prazna azuriramo da kraj pokazuje na novi

        self.tail = new_node                #proglasimo da je novi kraj sad taj novi element
        self.size += 1

    def remove_first(self):                 #uklanja ceo prvi cvor
        if self.size == 0:
            return
        elif(self.size == 1):               #moramo obraditi izuzetak, jer ako je bio 1 element posle uklanjanja ce biti 0 i cvorovi head i tail moraju biti uvezani ponovo
            self.tail = None                #kraj moramo da azuriramo jer ako je bio jedan element, na njega pokazuju i kraj i pocetak
        self.head = self.head.next_p        #novi pocetni cvor je sledbenik od prethodno pocetkog cvora
        self.size -= 1

    def remove_last(self):
        if(self.size == 1):
            self.head = None
            self.tail = None
        else:
            current = self.head
            while(current.next_p != self.tail):    #ovde moramo da iteriramo jer ne mozemo dobiti predposlednjeg na drugi nacin
                current = current.next_p           #iteriramo dok current nije pretposlednji
            current.next_p = None                  #posto pravimo novog poslednjeg, on ne pokazuje na nista i proglasavamo ga posle novim krajem
            self.tail = current                    #pretposlednji proglasavamo za poslednji

        self.size -= 1

    def first(self):                                #vraca vrednost prvog elementa
        if(self.size == 0):
            raise IndexError("Prazan niz")
        return self.head.value

    def last(self):                                 #vraca vrednost drugog elementa
        if(self.size == 0):
            raise IndexError("Prazan niz")
        return self.tail.value

    def remove(self, value):                        #uklanjanje elementa po prosledjenoj vrednosti
        if(self.size == 0):
            raise IndexError("Lista je prazna.")
        if(self.size == 1):
            self.head = None
            self.tail = None
            return
        prosli = self.head
        for node in self._iter_node():
            if(node.value == value):
                if(node == self.head):
                    self.remove_first()
                    return
                elif(node == self.tail):
                    self.remove_last()
                    return
                node = node.next_p
                prosli.next_p = node

                self.size -= 1
                break
            prosli = node                           #ovde u proslom ce uvek biti cuvan cvor koji je prosao iteraciju(tj. jedan cvor pre ovog koji trenutno proverava)

    def pop(self, indeks=None):                          #uklanja element iz niza po prosledjenom indeksu i vraca uklonjenog kao povratnu vrednost funkcije
        if(indeks is None):                              #indeks=0 (po default-u 0 odma u parametrima jer ako se ne prosledi vrednost podrazumeva se 0)
            indeks = self.size - 1
        if(indeks >= self.size or indeks < 0):
            raise IndexError("Nepostojeci indeks.")
        if(self.size == 0):
            raise IndexError("Lista je prazna.")
        prosli = self.head
        brojac = 0
        for node in self._iter_node():
            if(brojac == indeks):
                vrednost = node.value
                if(brojac == 0):
                    self.remove_first()
                    return vrednost
                elif(brojac == len(self) - 1):
                    self.remove_last()
                    return vrednost
                node = node.next_p
                prosli.next_p = node
                self.size -= 1
                return vrednost

            brojac += 1
            prosli = node                               #ovde ce uvek biti prosli koji nije obradjen, tj. prvi pre ovog koji je na tom indeksu
        raise ValueError("Nije pronadjen dati element.")

    def insert(self, indeks, value):                    #umece novu vrednost na vec postojeci cvor na datom indeksu
        if(indeks < 0 or indeks > len(self)):           #ide do len(self) - 1
            raise IndexError("Ne moze se umetati na pocetak i kraj. Samo izmedju.")
        if(indeks == len(self)):                        #ako hocemo da umetnemo na poslednju poziciji (u smislu da taj novi bude poslednji)                      
            self.append(value)
            return
        if(indeks == 0):
            self.prepand(value)
            return
        brojac = 0
        prosli = self.head
        for node in self._iter_node():                  #nece nikad brojac doci do 0 ili do poslednjeg jer je to obradjeno pre, u eteraciji svakako moramo ici od pocetka do kraja             
            if(brojac == indeks):                       #izuzeci su obradjeni isto kao i u pop, ali ovde je obradjeno pre iteracije kroz cvorove, ali efekat je isti
                new_node = Node(value, node)
                prosli.next_p = new_node
                self.size += 1
                return

            brojac += 1
            prosli = node


    @staticmethod
    def dupliraj_listu(lista):
        nova_lista = SinglyLinkedList()
        if (isinstance(lista, SinglyLinkedList)):
            for i in range(2):
                for element in lista:
                    nova_lista.append(element)

            return nova_lista
            # lista = nova_lista                        #ovo ne radi u pajtonu (nece promeniti objekat u main-u kad ga samo prosledim funkciji da ne vraca nista), valjda ne radi sa referencama samo kao java
        else:
            print("Prosledjena lista mora biti tipa sll!")
            return None


