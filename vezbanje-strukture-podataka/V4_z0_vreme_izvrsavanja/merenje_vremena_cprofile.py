from cProfile import Profile
from math import pow, sqrt

with Profile() as pr:
    for i in range(1000):
        rez = pow(i, 2)
    print(sqrt(2))

pr.print_stats()

#koliko je vremenas bilo potrebno da se pozove unutrasnja funkcija(u ovom slucaju stepenovanja)