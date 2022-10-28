def maxx(niz) :           
    if len(niz) <= 0:
        print("Greska. Prazan niz.")
        return
        #raise ValueError("Prazan niz!")
        #sys.exit()   
    najveci = niz[0]
    #i = 1                                        
    for i in range(1, len(niz)):   #mogao sam staviti range(1, len(niz)), onda ne treba naredba i = 1
        if(niz[i] > najveci):
            najveci = niz[i]          
        #i += 1                #suvisna naredba, python sam inkrementira na kraju petlje
    return najveci

niz1 = [8, 36, 15, 11, 14]

max_element = maxx(niz1)
print(max_element)