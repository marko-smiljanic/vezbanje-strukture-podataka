
def binary_search_rekurzivno(lista, element, indeks_pocetka, indeks_kraja):
    if(lista is None):
        return False
    if(lista.len() == indeks_pocetka):
        return True
    if(element < lista[indeks_pocetka]):
        sredisnji_indeks = (indeks_kraja - indeks_pocetka) // 2
        return binary_search_rekurzivno(lista, element, )
    