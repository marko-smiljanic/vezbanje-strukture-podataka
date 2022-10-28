from tree.position import Position

class LinkedBinaryTreePosition:
    def __init__(self, container, node):
        self.container = container          #stablo kojem pripada pozicija
        self.node = node                    #cvor u stablu na koji se odnosi pozicija

    def element(self):
        return self.node.element

    def __eq__(self, other):
        #TODO: da li treba poredjenja i kontejnera
        if(type(self) == type(other) and self.node is other.node):      #== poredimo po vrednosti, is poredi po identitemia(memorijske lokacije na kojima je smesten obj.)
            return True
        return False

    def __ne__(self, other):
        return not self == other
        