from abc import ABC, abstractmethod

class Korisnik(ABC):
    def __init__(self, korisnicko_ime, lozinka):
        super().__init__()
        self.korisnicko_ime = korisnicko_ime
        self.lozinka = lozinka
    
    @staticmethod
    @abstractmethod
    def prijava(niz): ...
