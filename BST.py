#Implementazione BST

class BSTreeNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        
#Attraversamento di un BST
def Inorder_Tree_walk(root):
    if root is not None:
        Inorder_Tree_walk(root.left)
        print(root.key, end=" ")
        Inorder_Tree_walk(root.right)

'''Complessità \Theta n '''

#Inserimento di un BST
def Tree_insert(root,key):
    
    #Se la radice è nulla 
    if root is None:
        #viene inserito un nuovo nodo con la chiave data nella radice
        return BSTreeNode(key)
    
    #Se la chiave sta nella radice
    if root.key == key:
        #ritorno la radice
        return root
    
    #Se la chiave è maggiore del valore della radice
    if root.key < key:
        #esploro il sottoalbero destro con chiamata ricorsiva
        root.right = Tree_insert(root.right, key)
    else:
        #altrimenti il sinistro
        root.left =Tree_insert(root.left, key)
    return root


def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr

#Eliminare da un BST
'''Questa procedura ha 3 casi base:
    - Il nodo è un nodo foglia
    - Il nodo ha un figlio
    - Il nodo ha due figli

'''
def Tree_delete(root,x):
    # Base case
    if root is None:
        return root

    # If key to be searched is in a subtree
    if root.key > x:
        root.left = Tree_delete(root.left, x)
    elif root.key < x:
        root.right = Tree_delete(root.right, x)
    else:
        # If root matches with the given key
        # Cases when root has 0 children or 
        # only right child
        if root.left is None:
            return root.right

        # When root has only left child
        if root.right is None:
            return root.left

        # When both children are present
        succ = get_successor(root)
        root.key = succ.key
        root.right = (root.right, succ.key)
        
    return root

#Ricerca di una chiave in un BST
def Tree_search(root,key):
    
    #Caso base: la radice è nulla o è la chiave
    if root is None or root.key == key:
        return root

    #La chiave è maggiore della chiave della radice
    if root.key < key:
        #Se y.key<=x.key allora sono nel sottoalbero destro
        return Tree_search(root.right, key)
    #La chiave è minore della chiave della radice
    #Se y.key>=x.key allora sono nel sottoalbero sinistro
    return Tree_search(root.left, key)



if __name__=="__main__":
    # Creiamo un BST
    #      50
    #     /  \
    #    30   70
    #   / \   / \
    #  20 40 60 80
    root = BSTreeNode(50)
    r = Tree_insert(root, 30)
    r = Tree_insert(r, 20)
    r = Tree_insert(r, 40)
    r = Tree_insert(r, 70)
    r = Tree_insert(r, 60)
    r = Tree_insert(r, 80)

    # Stampiamo il BST
    Inorder_Tree_walk(r)

    #Canceliamo il nodo 30
    #root = Tree_delete(root, 30)
    #Inorder_Tree_walk(root)
    
    # Cerchiamo chiavi nel BST
    print ('\n')
    print("Found" if Tree_search(root, 19) else "Not Found")
    print("Found" if Tree_search(root, 80) else "Not Found")