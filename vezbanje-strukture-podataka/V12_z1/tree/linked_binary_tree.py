from tree.binary_tree import BinaryTree
from tree.linked_binary_tree_position import LinkedBinaryTreePosition as Position  #alijas(drugo ime)
from tree.linked_binary_tree_node import LinkedBinaryTreeNode as Node


class LinkedBinaryTree(BinaryTree):

    def __init__(self):
        self.root_node = None      #kada je stablo prazno, nema cvora koji je koren
        self.size = 0               #broj elemenata u stablu u praznom je 0

    def _make_position(self, node):     #krieira i vraca poziciju za cvor u stablu
        if(node is None):               #prva provera je mogla biti i tip da li je Node
            return Position(self, node)

    def _validate_position(self, p):        #proverava da li je pozicija ispravna i vraca cvor na toj poziciji ukoliko jeste
        if(type(p) != Position):
            raise TypeError("Pogresan tip prosledjen.")
        if(self is not p.container):
            raise ValueError("Pogresan kontejner.")
        if(p.parent is p.node):         #kada se cvor stabla obrise i zameni svojim detetom
            raise ValueError("Pozicija p vise nije dostupna")
        return p.node

    def root(self):                     #treba da vrati poziciju cvora koji je koren
        return self._make_position(self.root_node)

    def is_root(self, p):               #vraca true ukoliko je pozicja p cvor koji je koren
        return self.root() == p

    def parent(self, p):
        child = self._validate_position(p)
        if(child is not None):
            return self._make_position(child.parent)

    def num_children(self, p):
        brojac = 0
        if(self.left(p) is not None):
            brojac += 1
        if(self.right(p) is not None):
            brojac += 1
        return brojac

    def children(self, p):
        parent = self._validate_position(p)
        left = self._make_position(parent.left)
        right = self._make_position(parent.right)
        if(left is not None):
            yield left
        if(right is not None):
            yield right

    def left(self, p):
        parent = self._validate_position(p)
        if(parent is not None):
            return self._make_position(parent.left)

    def right(self, p):
        parent = self._validate_position(p)
        if(parent is not None):
            return self._make_position(parent.right)

    def sibling(self, p):
        child = self._validate_position(p)
        if(child is not None):
            parent = child.parent
            parent_position = self._make_position(parent)
            if(self.right(parent_position) == p):
                return self.left(parent_position)
            else:
                return self.right(parent_position)

    def add_root(self, e):
        if(self.is_empty()):            #ili self.root_node is None ili len(self) == 0, ...
            raise ValueError("Koren vec postoji")
        self.root_node = Node(e)        #TODO: proveriti!!!!!
        self.size += 1
        return self._make_position(self.root_node)

    def add_left(self, p, e):
        node = self._validate_position(p)
        if(node.left is not None):
            raise ValueError("Levo dete vec postoji")
        node.left = Node(e, node)                   #cvor koji je roditeljski ima levo dete koji je novi cvor
        self.size += 1
        return self._make_position(node.left)
    
    def add_right(self, p, e):
        node = self._validate_position(p)
        if(node.right is not None):
            raise ValueError("Desno dete vec postoji")
        node.right = Node(e, node) 
        self.size += 1             
        return self._make_position(node.right)

    def replace(self, p, e):        #prepisuje sadrzaj cvora na poziciji p sa e i vraca sadrzaj starog cvora
        node = self._validate_position(p)
        old = node.element  #p.element
        node.element = e
        return old

    def delete(self, p):    #radi samo ako ima 1 dete, brise cvor na poziciji p i menja ga sa njegovim detetom ako ga ima, return vrednost elementa p
        node = self._validate_position(p)
        if(self.num_children(p) == 2):
            raise ValueError("Roditelj ima dva deteta")
        child = node.left if node.left else node.right
        # if(node.left is not None):
        #     child = node.left
        # else:
        #     child = node.right
        if(child is not None):
            child.parent = node.parent
        if(node is self.root_node):
            self.root_node = child
        else:
            parent = node.parent
            if(node is parent.left):
                parent.left = child
            else:
                parent.right = child
        self.size += 1
        node.parent = node              #invalidiramo cvor
        return node.element

    def attach(self, p, t1, t2):    #dodaje stabla t1 i t2 kao levo i desno podstablo pozicije p
        if(not self.is_leaf(p)):
            raise ValueError("Pozicija p mora biti listni cvor")
        if(not type(self) == type(t1) == type(t2)):
            raise TypeError("Tipovi stabala se ne podudaraju")
        node = self._validate_position(p)
        if(not t1.is_empty()):
            t1.root_node.parent = node
            node.left = t1.root_node
            t1.root_node = None
            t1.size = 0
        if(not t2.is_empty()):
            t2.root_node.parent = node
            node.left = t2.root_node
            t2.root_node = None
            t2.size = 0

        self.size += len(t1) + len(t2)



