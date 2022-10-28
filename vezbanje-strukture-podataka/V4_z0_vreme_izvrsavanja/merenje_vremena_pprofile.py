from pprofile import Profile
from math import pow, sqrt

with Profile() as pr:
    for i in range(1000):
        rez = pow(i, 2)
    print(sqrt(2))

pr.print_stats()  

#Prikazuje ukupno vreme izvrsavanja. Ima detaljniji prikaz kad se pokrene u terminalu(u main.py)
#preko cd se udje u folder gde se nalazi .py fajl koji zelimo da pokrenemo(copy relative path), onda se pokrece sa komandom pprofile .\imepajtonfajla.py