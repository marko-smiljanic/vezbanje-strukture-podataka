def sekvencijalna_pretraga(niz, element):
    if len(niz) == 0:
        return print("Ne mozete proslediti prazan niz") 
    for i in range(0, len(niz)):    #moglo je i n = len(niz) i samo stavim for i in range(n)
        if niz[i] == element:
            return i
    print("Element nije nadjen.")