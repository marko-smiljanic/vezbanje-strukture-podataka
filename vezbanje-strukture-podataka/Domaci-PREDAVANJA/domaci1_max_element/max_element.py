#a = [5, -3, 17, 10, 15, 25]

def maxx(niz) :                 #treba da vrati indeks najveceg elementa
    najveci = niz[0]            #pretpostavimo da je prvi najveci
    indeks = 0
    print(najveci)              #provera uzimanja prvog elementa
    i = 1                       #preskacemo prvi element u poredjenju jer smo preptostavili da je najveci
    for i in range(len(niz)):   #len je isto sto i length u javi ili size u c++, tj. vraca ukupnu duzinu ...znaci isto kao int i = 0; i < niz.length
        if(niz[i] > najveci):
            najveci = niz[i]    #ovo mi u stvari nije ni trebalo ali eto kao primer da je mozda bilo bolje da sam kao rezultat vratio vrednost a ne indeks
            indeks = i          #mogao sam preko neke ugradjene funkcije da dobavim indeks npr. index(element_niza)
        i += 1
    return indeks

