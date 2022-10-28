from dll.node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)                  #podrazumevano za pointere je none
        self.tail = Node(None)
        self.head.next_p = self.tail            #sentinel pocetni cvor, bez vrednosti, sluzi samo da znamo granicu liste
        self.tail.previous_p = self.head        #sentinel krajnji cvor
        self.size = 0

    def __len__(self):                          #magicna metoda... poziva se sa operatorom len(self)
        return self.size

    def __iter__(self):                         #specificna magicna metoda, vraca vise vrednosti, poziva se samo u for each
        current = self.head.next_p              #odakle pocinjemo prolazak, head je sentinel cvor i zbog toga necemo da ukljucimo njega
        while (current is not self.tail):       #tail je sentinel cvor i zbog toga necemo da ukljucimo njega
            yield current.value                 #yield je slucno sa return ali return vrati i obustavi funkciju, yield vrati i na zahtev sledece iteracije nastavi tamo gde je bila yield(gde je bila provera)
            current = current.next_p            #ovde bi moglo da stoji return None, ali to je podrazumevano u pajtonu

    def _iter_node(self):                       #po konvenciji koji pocinju sa _ oni su privatni(ne zapravo privatni jer je sve public u pajtonu, znaci trebalo bi da je samo koristimo u klasi)
        current = self.head.next_p                
        while(current is not self.tail):        #isto kao prethodna sam osto nam vraca ceo cvor. Poziva se for element(cvor) in self._iter_node()     
            yield current            
            current = current.next_p

    def __str__(self):
        rezultat = "["
        brojac = 0
        for element in self:                    #for i in range(len(self)) ali nemamo mehanizam indeksiranja, to je metoda __getitem__(self, i)
            rezultat += str(element)
            if(brojac < self.size() - 1):       #ili len(self) - 1 posto imam redefinsanu tu funkciju
                rezultat += ","                 #poslednji kome ce staviti zarez je pretposlednji
            brojac +=1
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

    def __setitem__(self, i, value):             #lista[0] = 1 na poziciju 0 stavi broj 1
        if(type(i) != int):
            raise TypeError("Indeks mora biti ceo broj")
        if(0 <= i < self.size):
            brojac = 0
            for node in self._iter_node():       #prolazimo kroz cvorove
                if(brojac == i):
                    node.value = value
                    break                        #nema potrebe da prolazi do kraja ako se vrednost postavila
                brojac += 1
        else:
            raise IndexError("Indeks izvan opsega")

    def prepand(self, value):                               #dodavanje nove vrednosti na pocetak(pre head-a jer je sentinel), tj. mroa se dodati novi cvor
        new_node = Node(value, self.head, self.head.next_p) #novi pocetak pokazuje na sentinel head i na sledeci od head
        self.head.next_p.previous_p = new_node              #azuriramo pokazivac elementu koji je bio prvi
        self.head.next_p = new_node                         #azuriramo da sentinel pokazuje na njega

        self.size += 1

    def append(self, value):                                     #dodaje novi cvor na kraj, tj. pre sentinela
        new_node = Node(value, self.tail.previous_p, self.tail)  #za razliku od jednostruke liste ovde se samo azuriraju cvorovi, ne moraju se pratiti izuzeci kada je prazna lista itd. jer imamo granicne-sentinel cvorove
        self.tail.previous_p.next_p = new_node                   #pokazuje na prethodni i na njegov (prethodni) next stavi novi node
        self.tail.previous_p = new_node

        self.size += 1

    def remove_first(self):                                 #uklanja ceo prvi cvor, nemamo izuzetaka kao kod jednostruke liste jer azuriramo samo cvorove, sentinel se ne gleda pa nam nije bitno da li ima samo jedan element
        if(self.size == 0):                                 #naravno ovo je redovan izuzetak jer ako ima 0 elemenata nema se sta ukloniti
            return
        self.head.next_p = self.head.next_p.next_p
        self.head.next_p.previous_p = self.head

        self.size -= 1
    
    def remove_last(self):                                      #nema izuzetaka kao u sll zbog sentinel cvorova
        if(self.size == 0):
            return
        self.tail.previous_p.previous_p.next_p = self.tail
        self.tail.previous_p = self.tail.previous_p.previous_p

        self.size -= 1

    def first(self):                                            #vraca vrednost prvog elementa (pre sentinela)
        if(self.size == 0):
            raise IndexError("Lista nema elemenata.")
        return self.head.next_p.value                           #prvi pravi element, jer sentinel je prvi i nema nikakvu vrednost!!!

    def last(self):                                             #vraca vrednost poslednjeg elementa (pre sentinela)
        if(self.size == 0):
            raise IndexError("Indeks izvan opsega.")
        return self.tail.previous_p.value                       #vrati sa cvora pre sentinela jer sentinel nema vrednost, sluzi samo kao granicnik

    def remove(self, value):                                    #uklanjanje elementa po prosledjenoj vrednosti
        if(self.size() == 0):
            raise IndexError("Lista je prazna.")
        for node in self._iter_node():
            if(node.value == value):                            #ovde ne treba izuzetak za prvu i poslednju poziciju zbog sentinel cvorova
                node.previous_p.next_p = node.next_p                #prethodni da pokazuje na sledeci od trenuitnog
                node.next_p.previous_p = node.previous_p            #sledeci od trenutnog pokazuje na prethodni od trenutnog
                
                # node.previous_p = None                        #kao u c++ obrisemo pokazivace pa onda i sam cvor
                # node.next_p = None
                node = None                                     #resetujemo cvor koji smo uklonili na none ali nije neophodno
                self.size -= 1
                break
        raise ValueError("Nije pronadjen dati element.")
    
    def pop(self, indeks=None):                                 #uklanja element iz niza po prosledjenom indeksu i vraca uklonjenog kao povratnu vrednost funkcije
        if(indeks is None):                                     #indeks=0 (po default-u 0 odma u parametrima jer ako se ne prosledi vrednost podrazumeva se 0)
            indeks = self.size - 1                              #ako je indeks = none onda treba da izvadimo poslednji element, ali valjda bi trebalo da vadimo prvi element?
        if(indeks >= self.size or indeks < 0):
            raise IndexError("Nepostojeci indeks.")
        if(self.size == 0):
            raise IndexError("Lista je prazna")
        brojac = 0
        for node in self._iter_node():
            if(brojac == indeks):
                vrednost = node.value
                node.previous_p.next_p = node.next_p
                node.next_p.previous_p = node.previous_p
                
                node = None                                     #nije neophodno obrisati cvor i pokazivace jer ima garbage collector
                self.size -= 1
                return vrednost                                 #moglo je i ovde da se stavi return node.value jer ga prethodno nismo menjali, menjali smo cvorove oko njega
            brojac += 1
        raise ValueError("Nije pronadjen dati element")

    def insert(self, indeks, value):                            #umece novu vrednost na vec postojeci cvor na datom indeksu
        if(indeks < 0 or indeks > len(self)):                   #treba len(self) - 1 da ne bi mogao da umetne na poslednji!!!
            raise IndexError("Nevalidna pozicija")
        if(indeks == len(self)):                                #ako hocemo da umetnemo na poslednju poziciji (u smislu da taj novi bude poslednji)                      
            self.append(value)
            return
        brojac = 0
        for node in self._iter_node():
            if(brojac == indeks):                               #doci ce do poslednjeg i umetnuce na poslednji i postace pretposlednji (jer starog poslednjeg pomera levo)
                new_node = Node(value, node.previous_p, node)
                node.previous_p.next_p = new_node               #cvor pre novog(umetnutog), pokazuje na taj novi cvor
                node.previous_p = new_node                      #stari cvor da pokazuje na novi(umetnut)
                
                self.size += 1
                break
            brojac += 1
               
