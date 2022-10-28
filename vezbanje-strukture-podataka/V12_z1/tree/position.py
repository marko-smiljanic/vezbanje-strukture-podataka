from abc import ABC, abstractmethod

class Position(ABC):
    
    @abstractmethod
    def element(self): ...          #vraca element na datoj poziciji stabla
        #pass
        #raise NitImplementedError("Nije implementirano")

    def __eq__(self, other): ...

    def __ne__(self, other):
        return not self == other