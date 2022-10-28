from abc import ABC, abstractmethod     #abstraktni model se mora importovati

class Osoba(ABC):                       #da bi klasa bila abstraktna mora da nasledjuje klasu ABC
    def __init__(self, ime, prezime):   #self je kao this i obavezan je parametar u konstruktoru... Ovo je na neki nacin konstruktor. U klasama u pajtonu se njeni atribudi definisu samo u konstruktoru
        super().__init__()              #kada se klasa nasledjuje mora da pozove super konstruktor obavezno
        self.ime = ime                  #ovde se u stvari definisu atrubuti u klasi... sve se radi u konstruktoru
        self.prezime = prezime

    #ako nema abstraktan metod klasa se nece gledati kao apstrakta!!!
    #ako se abstraktni metod ne redefinise u naslednici onda je i ta klasa abstraktna
    @abstractmethod                     #ovako se oznacava da je metod abstraktan
    def predstavi_se(self):
        return "Ja se zovem: {0} {1}".format(self.ime, self.prezime)   #ovako se radi ispis atributa klase

    # @abstractmethod                     #moze se definisati a i ne mora, onda ostavimo prazno telo
    # def apstrakta_metoda(self): ...     #moze i sa ... da se kaze da nema tela
    #     #pass
    #     #raise NotImplementedError("Metoda nije implementirana!")
        