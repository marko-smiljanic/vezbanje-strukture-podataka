from sll.singly_linked_list import SinglyLinkedList

class Automobil:
    def __init__(self, marka, model, maksimalna_brzina):
        self.marka = marka
        self.model = model
        self.maksimalna_brzina = maksimalna_brzina

    #redefinisanje operatora ce nam omoguciti da soritramo listu u kojoj su objekti 
    def __eq__(self, other):    #operator poredjenja ==
        #pre svega se moglo dodati if isinstance(other, Automobil):, onda ne treba else return false nego jednostavno ako se ne ispuni taj if da vrati false
        if(self.maksimalna_brzina == other.maksimalna_brzina):
            #print("Jednaki su.")
            return True
        else:
            #print("Nisu jednaki.")
            return False

    def __ge__(self, other):    #operator >=
        if(self.maksimalna_brzina >= other.maksimalna_brzina):      #mozda sam mogao da obradim slucaj kada su i jednaki da obavestim korisnika, ali onda redefinisanje ovog operatora bas i nema smisla
            #print("Veci je (ili su jednaki): " + str(self.marka) + " " + str(self.model) + ".")
            return True
        else:
            #print("Veci je: " + str(other.marka) + " " + str(other.model) + ".")
            return False

    def __lt__(self, other):     #<
        return not self >= other

    def __le__(self, other):     #<=
        if(isinstance(other, Automobil)): 
            if(self.maksimalna_brzina <= other.maksimalna_brzina):      #mozda sam mogao da obradim slucaj kada su i jednaki da obavestim korisnika, ali onda redefinisanje ovog operatora bas i nema smisla
                return True
        return False

    def __gt__(self, other):     #>
        return not self <= other

    @staticmethod
    def pretrazi_listu_automobila(lista):
        if (isinstance(lista, SinglyLinkedList)):
            for element in lista:               #umesto ovoga bi sada isao poziv funkcije firs, last
                najbrzi = element
                break
            for element in lista:
                if(element >= najbrzi):         #koristimo redefinisani operator
                    najbrzi = element

            print("Najveci iz liste (po max brzini) je: " + str(najbrzi.marka) + " " + str(najbrzi.model) + ".")   #stavimo return i vraca samo ispis na konzolu najbrzeg
            return najbrzi                     #vracamo ceo objekat najbrzeg auta
        
        print("Prosledjena lista mora biti tipa sll!")
        return None

    @staticmethod
    def izbaci_sve_osim_najbrzeg(lista):
        if (isinstance(lista, SinglyLinkedList)):
            najbrzi = Automobil.pretrazi_listu_automobila(lista)
            
            nova_lista = SinglyLinkedList()
            nova_lista.append(najbrzi)
            return nova_lista
            #lista = nova_lista     #ovo ne radi u pajtonu, moram u main-u u listu koju kocu da menjam da pozovem ovu funkciju koja vraca novu listu. Ovde ne moze da se izmeni lista jer ne radi sa referencama kao java valjda, mozda bi moglo da sam stavio retrun lista
        else:
            print("Prosledjena lista mora biti tipa sll!")
            return None


