from tree.linked_binary_tree import LinkedBinaryTree
from sll.singly_linked_list import SinglyLinkedList
from queue.queue import Queue
from stack.stack import Stack

class BinarySearchTree(LinkedBinaryTree):
    def __init__(self):
        super().__init__()
    
    def insert_element(self, e):    #dodaje element e kao novi cvor u stablo . Cvor se dodaje na odg poz spram vrednosti e koju zelimo da dodamo
        if(self.root() is None):
            self.add_root(e)
        else:
            self.insert_node(self.root(), e)    #nije problem sto smo definisali insert nod posle insert element

    def insert_node(self, root_p, value):   #dodaje cvor sa vrednoscu value na odg poziciju u stablu
        if(value < root_p.element()):
            if(root_p.node.left):           #ako postoji levo dete od pozicije root_p moramo se spustiti u podstablo sa korenskom pozicijom koja je levo podstablo
                self.insert_node(self.left(root_p), value)
            else:                           #ako ne postoji levo dete
                self.add_left(root_p, value)
        elif(value > root_p.element()):
            if(root_p.node.right):
                self.insert_node(self.right(root_p), value)     #ako postoji desno dete od rootp 
            else:
                self.add_right(root_p, value)
        else:
            raise ValueError("Ova vrednost vec postoji")

    def _subtree_preorder(self, p):
        yield p
        for child in self.children(p):
            for other in self._subtree_preorder(child):
                yield other

    def preorder(self): #generise iteracije preorder algoritma u stablu
        if(not self.is_empty()):
            for other in self._subtree_preoprder(self.root()):
                yield other

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def inorder(self):
        if(not self.is_empty()):
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for child in self.children(p):
            for other in self._subtree_preorder(child):
                yield other
        yield p

    def postorder(self):
        if(not self.is_empty()):
            for p in self._subtree_postorder(self.root()):
                yield p

    def breadth_first_search(self):         #mogli smo da dodamo u parametre i vrednost i umesto iterisanja (tj. da li je vrednost == nekoj od vrednosti iz iterisanja)
        if not self.is_empty():
            red = Queue()
            red.enqueue(self.root())
            while (not red.is_empty()):
                p = red.dequeue()
                yield p
                for(c in self.children(p)):
                    red.enqueue(c)

    def depth_first(self):                  #moze se dodati i odgovarajuci parametar
        if not self.is_empty():
            s = Stack()
            s.push(self.root())
            while(not s.is_empty()):
                p = s.pop()
                yield p
                for c in self.children(p):
                    s.push(c)

    def binary_search(self, e, p):
        if p is None:
            return False
        if p.element() == e:
            return True
        if(e < p.element()):
            return self.binary_search(e, self.left(p))      #pretrazi levo podstablo
        else:
            return self.binary_search(e, self.right(p))     #pretrazi desno podstablo



    #TODO: odgledati vezbe i dopisati komentare za metode i ostalo (trebalo bi odgledati kompletne vezbe sa stablima... znaci poslednjih dvoje)