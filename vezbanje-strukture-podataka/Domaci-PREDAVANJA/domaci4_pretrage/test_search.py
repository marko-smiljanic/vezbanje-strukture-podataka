def sekvencijalna_pretraga(niz, element):
    if(len(niz) == 0):
        return print("Niz je prazan.")
    for i in range(0, len(niz)):
        if(niz[i] == element):
            print("Element je pronadjen. Prva pojava elementa je na indeksu:", i)
            return element
    print("Trazeni element nije pronadjen.")


def binarna_pretraga(niz, element):    #da bi ovo radilo niz MORA biti sortiran !!!!!
    if(len(niz) == 0):
        return print("Niz je prazan.")
    pocetak = 0
    kraj = len(niz) - 1
    while(pocetak <= kraj):
        sredina = (pocetak + kraj) // 2     #celobrojno deljenje, jer ne mora dobijeni broj biti deljiv sa 2
        if(element < niz[sredina]):         #napravljeno je za rastuci sortirani niz
            kraj = sredina - 1
        if(element > niz[sredina]):
            pocetak = sredina + 1
        else:
            print("Element pronadjen. Prva pojava elementa na indeksu:", sredina)
            return niz[sredina]


# niz22 = [0, 11, 2, 56, 90, 4, 77, 32]
# print(sekvencijalna_pretraga(niz22, 56))

# niz22.sort()
# print(niz22)
# print(binarna_pretraga(niz22, 56))