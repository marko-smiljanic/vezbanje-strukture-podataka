from timeit import timeit

# naredba a = """

# for i in range(1000):
#     rez = i**2

# """     #formatirani string
# rezultat = timeit(stmt = naredba, number=1000)    #ako ne stavimo number uzece dafultnu vrednost 1000 000, to je valjda koliko se puta poziva funkcija
# print(rezultat)                                 #u ovom slucaju ne treba da se navodi globals u parametrima jer smo naredbu oznacili kao pajton skriptu i celu je prosledili

def funkcija():
    for i in range(1000):
        rez = i**2
        print(rez)
        rez = None


rezultat = timeit(stmt="funkcija()", number = 1, globals = globals())
print(rezultat)

#meri poroteklo vreme rada programa