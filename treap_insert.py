from random import randint
RAND_MAX=100

class Node(object):
    #costruttore del nodo
    def __init__(self, key, priority=None):
        self.key = key
        #assegno ad x una priorità casuale
        if priority is not None:
            self.priority = priority  
        else: 
            self.priority=randint(1, RAND_MAX)
        #creo dei puntatori ai figli
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Key: {self.key}, Priority: {self.priority}"

class Treap(object):
    def __init__(self):
        self.root = None #Inizialmente è vuoto

    def insert(self, key, priority=None):
        node = Node(key, priority)
        self.root = self._insert(self.root, node)

    def _insert(self, root, node):
        if root is None:
            return node

        #Se la chiave è più piccola di quella della radice
        if node.key < root.key:

            #inseriamo nel sottoalbero di sinistra
            root.left = self._insert(root.left, node)
            #questo inserimento ha violato le proprietà dell'heap?
            if root.left.priority < root.priority:
                root = self._rightRotate(root)

        #altrimenti
        else:

            #inseriamo nel sottoalbero di destra
            root.right = self._insert(root.right, node)
            #questo inserimento ha violato le proprietà dell'heap?
            if root.right.priority < root.priority:
                root = self._leftRotate(root)

        return root

    def _rightRotate(self, root):
        #prendiamo il figlio sinistro e il figlio destro di questo
        #       root
        #      /     \
        #    fsx      fdx
        #   /   \
        #ffsx   ffdx

        fsx = root.left

        #Rotazione: disegniamo cosa deve succedere
        #      root         |      fsx
        #     /    \              /     \
        #   ffdx     fdx    |   ffsx    root
        #                             /     \    
        #                   |       ffdx     fdx

        root.left = fsx.right
        fsx.right = root

        return fsx

    def _leftRotate(self, root):
        #prendiamo il figlio destro e il figlio sinistro di questo
        #       root
        #      /     \
        #    fsx      fdx
        #            /   \
        #          ffsx   ffdx

        fdx = root.right

        #Rotazione: disegniamo cosa deve succedere
        #      root          |       fdx
        #      /   \               /    \
        #   fsx     ffsx     |   root    ffdx
        #                        /  \         
        #                    | fsx  ffsx        
        
        root.right = fdx.left
        fdx.left = root
        
        return fdx

    def visualize(self):
        if self.root is None:
            print("Treap is empty")
            return

        current_level = 1
        current_nodes = [self.root]

        while current_nodes:
            #Stampo il livello
            print(f"\nLevel {current_level}: ", end="") 
            next_nodes = []

            for node in current_nodes:
                print(f"\n({node.key}, {node.priority}), \nleft: {node.left}, \nright: {node.right}", end=" ")

                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)

            print()  # Newline
            current_level += 1
            current_nodes = next_nodes

def run():
    t = Treap()
    t.insert(4)
    print(f"\nNuovo inserimento...")
    t.visualize()
    t.insert(5)
    print(f"\nNuovo inserimento...")
    t.visualize()
    t.insert(6)
    print(f"\nNuovo inserimento...")
    t.visualize()
    t.insert(1)
    print(f"\nNuovo inserimento...")
    t.visualize()
    t.insert(2)
    print(f"\nNuovo inserimento...")
    t.visualize()
    t.insert(3)
    print(f"\nNuovo inserimento...")
    t.visualize()
    return t

if __name__ == "__main__":
    treap_instance = run()
    