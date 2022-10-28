from osoba import Osoba       #ili import * da importuje sve iz tog fajla
from student import Student

# osoba1 = Osoba("Marko", "Markovic")

# print(osoba1.predstavi_se())
# osoba1.ime = "Janko"
# osoba1.prezime = "Jankovic"

# print(osoba1.predstavi_se())

student1 = Student("Nikola", "Jokic", "2019/271380", "SII")
print(student1.ime)
print(student1.prezime)
print(student1.broj_indeksa)
print(student1.smer)

print(student1.predstavi_se())