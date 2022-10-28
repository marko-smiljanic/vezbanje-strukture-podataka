class Node:
    def __init__(self, value, next_p = None):     #inicijalizator, sa parametrima sadrzaj na cvoru i pokazivac na sledeci element liste, podrazumevano je none
        self.value = value
        self.next_p = next_p