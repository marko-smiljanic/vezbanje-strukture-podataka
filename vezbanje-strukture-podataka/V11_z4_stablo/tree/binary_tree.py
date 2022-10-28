from abc import ABC, abstractmethod
from tree.tree import Tree

class BinaryTree(Tree, ABC):        #abc mora da se pise na kraju u nasledjivanju uvek

    #vraca poziciju cvora koji je levo dete od cvora na poziciji p, none ako nema dete, pe je pozicija cvora cije dete trazimo
    @abstractmethod
    def left(self, p): ...

    #vraca poziciju cvora koji je desno dete od cvora na poziciji p, none ako nema dete
    @abstractmethod
    def right(self, p): ...

    #vraca poziciju rodjaka cvora na pozicji p ili none ako ga nema
    @abstractmethod
    def sibling(self, p): ...

    #generise iteracije pozicija koje predstavljaju decu od pozicije p (levo ili desno dete). pozicije cvoroa pravimo kao generator(sa yield)
    def children(self, p):          #slicno kao __iter__ ali samo nad jednim cvorom
        left = self.left(p)
        if(left is not None):
            yield left
        right = self.right(p)
        if(right is not None):
            yield right

