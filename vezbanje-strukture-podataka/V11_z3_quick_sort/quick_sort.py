
def quick_sort(s):                  #sortiranje na osnovu pivot elementa deli strukturu s u 3 liste
    n = len(s)                      
    if(n < 2):                      #ako lista ima 1 element, vec je sortirana 
        return                       
    pivot = s[0]                    #uzimamo prvi element za pivot, ali moze biti i poslednji ili srednisnji
    l = []                          #l strukt. - u koju ce se smestiti svi elemeni iz s koji su manji od pivota
    e = []                          #e strukt. - u koju ce se smestiti svi jednaki pivotu
    g = []                          #g strukt. - u koju ce se smestiti svi veci od pivota
    while not(len(s) == 0):         #sve dok lista s nije prazna delimo je u podliste
        if(s[0] < pivot):
            l.append(s.pop(0))      #ukoliko se ne isprazne svi elementi iz lista, u nesortiranu ce se kasnije dodavati njeni sortirani
        elif(pivot < s[0]):         #posto to ne zelimo, pomocu pop uklonimo element
            e.append(s.pop(0))      #da smo pristupali elementima preko indeksa i na krajuy bi prepisivali listu s praznom listom
        else:                       #izgubili bi smo referencu na staru listu i onda ne bi smo mogli da je koristimo za kombinovanje sort
            e.append(s.pop(0))

    quick_sort(l)                   #rekurzivno sortiranje manje liste
    quick_sort(g)

    while not (len(l) == 0):        #sve dok ne ispraznimo listu
        s.append(l.pop(0))          #dodajemo ih redom u pocetnu listu koja ce biti nas rezultat
    while not (len(e) == 0):
        s.append(e.pop(0))
    while not (len(g) == 0):
        s.append(g.pop(0))

