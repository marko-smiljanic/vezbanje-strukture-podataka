def min_max_element(niz):
    najmanji = niz[0]
    najveci = niz[0]
    for i in range(1, len(niz)):
        if(niz[i] < najmanji):
            najmanji = niz[i]
    for i in range(1, len(niz)):
        if(niz[i] > najveci):
            najveci = niz[i]
    
    niz2 = [najmanji, najveci]
    return niz2
    #moze da se stavi odma return najmanji, najveci ...jer ovo je pajton
    #funkciju sam mogao da napravim tako da se korisnik pita da unese da li zeli 1. najmanji ili 2. najveci element
    #u zavisnosti od unosa bi imao samo jedan return, tako da bi funkcija morala da se poziva dva puta
    #ali u pajtonu funkcija moze da vrati skoro bilo sta u bilo kom formatu, i razlicite vrednosti takodje