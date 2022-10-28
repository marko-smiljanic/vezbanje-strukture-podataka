
def bubble_sortiranje(niz):
    privremeno = 0
    duzina = len(niz)                            #ide se do pretposlednjeg jer posle njega nemamo nista desno, da bi prelepili
    for i in range(0, duzina - 1):               #od 0 sa 0 do duzina - 1(tj. broj pre... ne racuna njega - isto kao java)... i petlja je samo brojac koji sluzi da pratimo koliko smo sortirali brojeva(jer kroz svaku iteraciju spoljasnje petlje se najmanji slazu na kraj)
        for j in range(0, (duzina - 1) - i):     #uvek se sortiranje krece iz pocetka ali nam je bitno da pratimo poslednje elemente jer su oni uvek sortirani... u prvom krugu (kad je i = 0) ide do sortira sve, posle ide do toga
            if(niz[j] > niz[j + 1]):             #ako hocemo drugi redosled sortiranja smao promenimo znak
                privremeno = niz[j]              #moramo staviti u privremenu prom. jer ga menjamo ali nam treba ta stara vrednost
                niz[j] = niz[j + 1]
                niz[j + 1] = privremeno          #inkrementuje se automatski!!!!
        print(niz)


#j petlja -> uvek krece od 0 u proverava sve elemente do kraja koji je specificno zadat.
#i petlja -> sluzi samo da bi u j petlji imali duzinu nesortiranog dela.
#cim se petlja i izvrsava top znaci da je na poziciji lenght - 1 - i najmanji element i da treba ici dalje
#zato celu duzinu skracujemo za indeks(i) tog elementa(tj. to nam je kao brojac da pratimo koliko smo elemenata sortirali). 
#Samim tim vise ne moramo da poredimo sa tim poslednjim jer svakako znamo da je tamo najmanji, nego jednostavno idemo do sortiranog dela

niz1 = [14, 1, 9, 12, 8]
bubble_sortiranje(niz1)
#print(niz1)
