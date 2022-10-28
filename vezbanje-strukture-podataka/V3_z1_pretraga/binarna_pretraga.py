def binarna_pretraga(niz, element): #da bi ovo radilo niz mora biti sortiran!!!
    if((len(niz)) == 0):
        return print("Prosledjeni niz je prazan.")
    i = 0                  #indeks pocetka
    j = len(niz) - 1       #indeks kraja
    while(i <= j):
        sredina_niza = (i + j) // 2
        if(element < niz[sredina_niza]):
            j = sredina_niza - 1
        elif(element > niz[sredina_niza]):
            i = sredina_niza + 1
        else:                           #ako je == onda je to taj element koji trazim
            return sredina_niza         #vraca indeks

    return print("Element nije pronadjen.")


niz1 = [2, 6, 1, 10, 3, 5]
niz1.sort()
print(niz1)   #obavezno ga sortirati!!!... ovaj deo sam mogao odraditi i u samoj funkciji, i na kraju bi trebao vracati element da bih mogao da niz vratim na staru(nesortiranu verziju)... znaci sortiram, odradim, vratim niz na originalno, vratim pronadjeni element... tako bi bili ulazni podaci isti a odradilo bi se sve sto treba

print(binarna_pretraga(niz1, 6))
