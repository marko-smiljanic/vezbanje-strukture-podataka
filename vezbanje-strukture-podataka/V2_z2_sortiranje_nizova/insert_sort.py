def insert_sortiranje(niz):
    privr = 0
    j = 0                                    #pozicija pre
    for i in range(1, len(niz)):
        privr = niz[i]
        j = i - 1
        while(j >= 0 and niz[j] > privr):
            niz[j + 1] = niz[j]              #pomeri desno(j + 1 == sledeca(i) pozicija, j == prethodna pozicija)
            j -= 1
        niz[j + 1] = privr


#proveravamo sve pozicije koje su levo od trenutne(od privremenog)
#ako je broj na poziciji(j tj. pozicija levo od trenutne) veci od trenutnog(privremenog) pomerimo ga na poziciju desno
#ako broj na poziciji nije veci(ili smo stigli do kraja) na to mesto upisemo privremeni

niz1 = [43, 26, 13, 95, 5, 11, 31]
insert_sortiranje(niz1)
print(niz1)
