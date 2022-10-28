def select_sortiranje(niz):
    for i in range(0, len(niz)):             #prolazi do poslednjeg elementa, zakljucno sa njim
        indeks = i                           #cuvamo trenutnu poziciju
        for j in range(i + 1, len(niz)):     #krecemo od sledeceg elementa
            if(niz[j] > niz[indeks]):        #poredimo sledeci sa prethodnim   
                indeks = j                   #ako je manji onda cuvamo indeks manjeg
        privr = niz[indeks]
        niz[indeks] = niz[i]                 #menjamo vrednosti, ukoliko nije manji onda ce samo prelepiti staru vrednost
        niz[i] = privr                       #ukoliko je manji onda na poziciju j prelepimo i


#pamtim ineks najveceg i stavljam ga na poziciju i(blize pocetku)... u bubble sort je stavljano blize kraju.. isti je princip
#kako se i povecava ja imam najvece elemente od pocetka
#kao kod buble sort gde nisam gledao poslednju poziciju, ovde ne gledam prvu posle iteracija

niz1 = [43, 26, 13, 95, 5, 11, 31]
select_sortiranje(niz1)
print(niz1)