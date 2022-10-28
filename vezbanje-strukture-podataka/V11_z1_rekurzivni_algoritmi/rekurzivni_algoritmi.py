#zbir prvih n neparnih brojeva
def suma(n, pocetak=1):
    if n > 0:
        zbir = pocetak + suma(n - 1, pocetak+2) # n-1 sluzi za brojanje preostalih koraka(kao brojac), a pocetak+2 naredni sabirak(kao suma), suma je u ovom slucaju samo ime funkcije
        return zbir
    else:
        return 0

print(suma(5))

def fib(n):                             #Racuna vrednost n-tog broja u Fibonacijevom nizu.
    if n < 1:
        return
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)      #svaki naredni broj je zbir prethodna dva broja

print(fib(6))

def faktorijel(n):
    if n == 1:                          #0! == 1
        return 1
    else:
        return n * faktorijel(n-1)      #faktorijel od n je n * n! ...poziva se dok ne dodje do 1

print(faktorijel(5))

def palindrom(rec):

    if 0 <= len(rec) <= 1:              #palindrom je ako je string prazan ili ima jedan karakter
        return True                                      
    elif rec[0] == rec[-1]:             #(indeksiranje) ako je slozeniji string (ima vise od dva karaktera), onda se pocetni i krajnji karakteri ispituju, u slucaju njihove jednakosti, proveriti ostatak (unutrasnjost) datog stringa 
        return palindrom(rec[1:-1])     #isecanje
    else:                               #ako nisu isti karakteri onda vrati False (nije palindrom)
        return False

print(palindrom("ana"))

def plaindrom2():                                        #bez rekurzije
    prva_recenica = input("Unesite recenicu: ")
    druga_recenica = input("Unesite drugu recenicu: ")

    prva_bez_razmaka = ""
    druga_bez_razmaka = ""

    for karakter in prva_recenica:
        if karakter == " ":
            continue
        else:
            prva_bez_razmaka += karakter

    for karakter in druga_recenica:
        if karakter == " ":
            continue
        else:
            druga_bez_razmaka += karakter

    if len(prva_bez_razmaka) != len(druga_bez_razmaka):
        print("Recenice nisu iste duzine, samim tim nisu palindromi.")
    else:
        druga_obrnuta = ""
        for karakter in druga_bez_razmaka:
            druga_obrnuta = karakter + druga_obrnuta

        brojac1 = 0
        brojac2 = 0
        palindrom = True
        for karakter1 in prva_bez_razmaka:
            for karakter2 in druga_obrnuta:
                if brojac1 == brojac2:
                    if karakter1 != karakter2:
                        palindrom = False
                    print(karakter1, karakter2)
                    break
                brojac2 += 1
            brojac1 += 1
            brojac2 = 0

        if palindrom:
            print("Recenice su palindromi!")
        else:
            print("Recenice nisu palindromi!")