from dll.doubly_linked_list import DoublyLinkedList

class Magacin:
    def __init__(self, tip, kapacitet, zauzetost):
        self.tip = tip
        self.kapacitet = kapacitet
        self.zauzetost = zauzetost

    def __eq__(self, other):
        if(type(self.kapacitet) != int):
            raise TypeError("Uneli ste pogresan tip za kapacitet. Mora biti broj.")
        if(self.kapacitet == other.kapacitet):
            # print("Jednaki su.")
            return True
        else:
            # print("Nisu jednaki.")
            return False

    def __gt__(self, other):
        if(type(self.kapacitet) != int):
            raise TypeError("Uneli ste pogresan tip za kapacitet. Mora biti broj.")
        if(self.kapacitet == other.kapacitet):          #sve je moglo pod jedan if
            if(self.zauzetost < other.zauzetost):
                # print("Prvi je veci.")
                return True
        # print("Prvi nije veci.")
            else:
                return False
        else:
            return False

    def __ge__(self, other):
        if(type(self.kapacitet) != int):
            raise TypeError("Uneli ste pogresan tip za kapacitet. Mora biti broj.")
        if(self.kapacitet == other.kapacitet and self.zauzetost <= other.zauzetost):
            # print("Prvi je veci ili jednak (tj. nije manji).")
            return True
        # print("Prvi nije veci ili jednak drugom (tj. manji je).")
        return False
        
    @staticmethod
    def najveci(lista):
        if(isinstance(lista, DoublyLinkedList)):
            najveci = lista[0]
            for element in lista:                       #mogao sam dodati proveru za element da li je instance magacin
                if(element > najveci):
                    najveci = element
            print("Najveci magacin je:", najveci.tip)
            return najveci
        else:
            raise ValueError("Prosledjena lista nije tipa ddl.") 

    # @staticmethod
    # def napuniNajveciDoKraja(lista):
    #     if(isinstance(lista, DoublyLinkedList)):    
    #         najvMagacin = Magacin.najveci(lista)
    #         for element in lista:
    #             if(element == najvMagacin):
    #                 continue
    #             if(najvMagacin.kapacitet > najvMagacin.zauzetost):
    #                 mozeStati = najvMagacin.kapacitet - najvMagacin.zauzetost
    #                 if(element.zauzetost < mozeStati):
    #                     najvMagacin.zauzetost += element.zauzetost
    #                     mozeStati -= element.zauzetost
    #                     element.zauzetost = 0
    #                 while(element.zauzetost > mozeStati):
    #                         element.zauzetost -= 1
    #                         najvMagacin.zauzetost += 1
    #                         mozeStati -= 1
    #             else:
    #                 print("Najveci je popunjen!.", najvMagacin.kapacitet, najvMagacin.zauzetost)


