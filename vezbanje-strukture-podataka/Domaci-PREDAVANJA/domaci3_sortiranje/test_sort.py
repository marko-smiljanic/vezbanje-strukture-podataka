def bubble_sortiranje(niz):
    privremeno = 0
    duzina = len(niz)
    for i in range(0, duzina - 1):      #ide do pretposlednjeg jer od poslednjeg nema nista desno
        for j in range(0, (duzina - 1) - i):
            if(niz[j] > niz[j + 1]):
                privremeno = niz[j]
                niz[j] = niz[j + 1]
                niz[j + 1] = privremeno

def select_sortiranje(niz):
    for i in range(0, len(niz)):
        indeks = i
        for j in range(i + 1, len(niz)):
            if(niz[j] < niz[indeks]):
                indeks = j
        privremeno = niz[indeks]
        niz[indeks] = niz[i]
        niz[i] = privremeno

def insert_sortiranje(niz):
    privremeno = 0
    j = 0
    for i in range(1, len(niz)):
        privremeno = niz[i]
        j = i - 1
        while(j >= 0 and niz[j] > privremeno):
            niz[j + 1] = niz[j]
            j -= 1
        niz[j + 1] = privremeno
    