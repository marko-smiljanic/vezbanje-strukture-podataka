def list_split(l):                          #razdvajamo listu na dva dela
    sredisnji = len(l) // 2
    l1 = l[0, sredisnji]
    l2 = l[sredisnji:len(l)]
    return l1, l2

def merge(s1, s2, s):                       #s1, sortirana leva polovina liste, s2 desna, s3 nova gde stavljamo iz ove dve
    i = 0                                   #indeksi za kretanje po sekvencama - s1
    j = 0                                   #s2
    k = 0                                   #s
    while i < len(s1) and j < len(s2):      #ukoliko nismo prosli bar jednu od listi
        if(s1[i] < s2[i]):                  #uporedi sa trenutnim pozicijama listi s1 i s2 koji je manji element
            s[k] = s1[i]                    #dodeli manji u s
            i += 1                          #inkrementujemo brojac tako da se element koji je vec ubacen ne bi poredio sa drugim elementima
        else:
            s[k] = s2[j]
            j += 1
        k += 1
        
    while j < len(s1):                      #ako su elementi ostali iz s1, dopisemo ih u listu, dodajemo na kraj samo jer znamo da je sortirano
        s[k] = s1[i]                        #najcesce ako posle podele ostane 1 element zbog celobrojnog deljenja
        i += 1
        k += 1
    while j < len(s2):
        s[k] = s2[j]
        j += 1
        k += 1

def merge_sort(s):
    if(len(s) > 1):                           #ako nije trivijalni problem (jedan element u listi ili 0 elementa)
        s1, s2 = list_split(s)                #podeli
        merge_sort(s1)                        #zavladaj
        merge_sort(s2)                        #TODO: kako zna da ovde odradi sort, kako ova npr linija uopste radi???
        merge(s1, s2, s)                      #kombinuj
    else:
        return

