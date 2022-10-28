from Korisnik import *

class Sluzbenik(Korisnik):
    def __init__(self, korisnicko_ime, lozinka, id, sektor):
        super().__init__(korisnicko_ime, lozinka)
        self.id = id
        self.sektor = sektor

    @staticmethod
    def prijava(niz):           #posto je staticka metoda, ne mora da ima self za parametar
        kor_ime = input("Unesite korisnicko ime: ")
        loz = input("Unesite lozinku: ")
        for element in niz:         #mogao sam ubaciti i .lower() ili .upper()
            if(kor_ime == element.korisnicko_ime and loz == element.lozinka):
                id = input("Unesite id: ")
                id = id.upper()
                if(id == element.id):
                    print("Uspenso ste se prijavili.")
                    return True
        print("Pogresno ste uneli podatke. Pokusajte ponovo.")
        return False

        
