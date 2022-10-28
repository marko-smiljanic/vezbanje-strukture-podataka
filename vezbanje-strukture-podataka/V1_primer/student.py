from osoba import Osoba

class Student(Osoba):           #kada se nasledjuje klasa se navodi u zagrade, dozvoljeno je visestruko nasledjivanje kao u c++
    def __init__(self, ime, prezime, broj_indeksa, smer) :
        super().__init__(ime, prezime)
        self.broj_indeksa = broj_indeksa
        self.smer = smer

    # def predstavi_se(self):
    #     return "Ja se zovem: {0} {1} i studiram na smeru {2} sa brojem indeksa {3}".format(self.ime, self.prezime, self.smer, self.broj_indeksa)
    #     #da nije redefinisano, ono bi pozvalo metodu iz osobe

    def predstavi_se(self):  #varijanta sa super
        rezultat = super().predstavi_se()  #nije moralo u promenljivu moglo je i direkto da se pozvia tamo gde treba
        return "{0} i studiram na smeru {1} sa brojem indeksa {2}".format(rezultat, self.smer, self.broj_indeksa)
    