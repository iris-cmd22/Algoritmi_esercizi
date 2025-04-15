
#MAXHEAP    
class MaxHeap:
    def __init__(self, maxsize):
        #Mi serve il numero di elementi massimo per inizializzarlo
        self.maxsize =maxsize
        self.size=0
        self.maxHeap=[0]*(self.maxsize + 1) #Inizializzo tutti 0
        
    #Per le proprietà dell'heap
    #Se voglio conoscere la posizione del genitore
    def parent(self,i):
        return i // 2
    
    #Se voglio la posizione del figlio sinistro
    def leftChild(self,i):
        return 2*i
    
    #Se voglio la posizone del figlio destro
    def rightChild(self, i):
        return (2*i)+1
    
    #Se voglio sapere se sono in una foglia
    def isLeaf(self,i):
        
        if i>=(self.size//2) and i>=self.size:
            return True
        return False
    
    #Se voglio scambiare due elementi dell'heap
    def scambia(self, pos1, pos2):
        self.maxHeap[pos1], self.maxHeap[pos2]=(self.maxHeap[pos2],self.maxHeap[pos1])
        
    def inserisci(self, element):
         
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.maxHeap[self.size] = element
 
        current = self.size
 
        while (self.maxHeap[current] > 
               self.maxHeap[self.parent(current)]):
            self.scambia(current, self.parent(current))
            current = self.parent(current)

# Function to insert a node into the heap
    def insert(self, element):
         
        if self.size >= self.maxsize:
            print("Added too many elements!")
            return
        self.size += 1
        #Aggiungiamo un elemento all'array
        self.maxHeap[self.size] = element
        #Prendiamoci l'indice dell'elemento appena aggiunto
        current = self.size
 
        #Se l'elemento appena aggiunto è più grande del padre, scambio i due nodi
        while (self.maxHeap[current] > self.maxHeap[self.parent(current)] and current>1):
            self.scambia(current, self.parent(current))
            current = self.parent(current)
    
#Stampa dell'albero per vedere cosa abbiamo fatto
    def Print(self):
         
        for i in range(0, (self.size // 2)):
            print("PARENT : " + str(self.maxHeap[i]) +
                  " LEFT CHILD : " + str(self.maxHeap[self.leftChild(i)]) +
                  " RIGHT CHILD : " + str(self.maxHeap[self.rightChild(i)]))


### Funzioni per l'ordinamento di un vettore 

#MAX-HEAPIFY 
#Serve a conservare la proprietà del max heap, viene chiamata quanto gli alberi con radici Left(i) e Righht(i) sono max-heap
#ma A[i] è il più piccolo dei suoi figli, violando la proprietà dell'heap    
def Max_Heapify(A,n,i):
    
    massimo=i #inizializziamo la radice
    
    l=2*i+1 #figlio sinistro
    r=2*i+2 #figlio destro
    
    #Se il nodo non è una foglia e ho un massimo in l
    if l < n and A[l]>A[i]:
        massimo=l
    
    #Se il nodo non è una foglia e ho un massimo in r
    if r < n and A[r]>A[massimo]:
        massimo=r
    
    if massimo != i: #Posso farlo scendere ancora
        (A[i],A[massimo])=(A[massimo],A[i])
        
        Max_Heapify(A,n,massimo)
            
'''
Il tempo di esecuzione è 
un tempo costante per individuare il massimo fra tre nodi ed effettuare lo scambio
+
il tempo di eseguire Max.Heapify su un problema di dimensione minore

Sia n la dimensione del problema originario,
m la dimensione del sottoalbero con più elementi,
h l'altezza del nodo oggetto del problema originario
possimao individuare 2 casi: 

Caso 1: l'ultimo livello è pieno
    O(n/2)
caso 2: l'ultimo livello è pieno a metà -> caso peggiore
    O(2n/3)
    
Il tempo di esecuzione è T(n)<=T(2n/3)+\Theta(1)
che rienta nel teorema dell'esperto, sarà quindi O(lg n)

Posso utilizzare Max-Heapify per convertire un array in un heap
Per farlo parto dal basso invocando Max-Heapify

'''
            
def Build_Max_Heap(A):
    for i in range (len(A)//2,-1,-1):
        Max_Heapify(A,len(A),i)
    return A

''' Quale sarà la posizione nell'array dell'ultimo nodo non foglia? len(A)//2 

Tutti i nodi foglia sono heap di 1 elemento, quindi
il ciclo inizia dall'ultimo nodo non foglia dell'albero e procede verso la radice.

Per ogni nodo non foglia, viene chiamata la funzione maxHeapify per assicurarsi che 
il sottoalbero con radice in quel nodo rispetti la proprietà di max-heap'''

#HeapSort
def HeapSort(A):
      
    A=Build_Max_Heap(A)
    n = len(A)
    for i in range(n-1, 0, -1):
          # Swap
          A[i], A[0] = A[0], A[i]
  
          # Heapify root element
          Max_Heapify(A, i, 0)
    return A

#CODE A PRIORITA'
'''
Un Max-Heap può essere usato per realizzare in maniera efficiente una coda a massima priorità,
che è una struttura dati che mantiene un insieme S di elementi e supporta le operazioni di:

-Insert(S,x)
-Maximum(S) (Minimum(S))
-Extract-Max(S)  (Extract-Min(S))
-Increase-Key(S,x,k) (Decrease-Key(S,x,k))

'''
def Heap_Maximum(A):
    return A.maxHeap[0]

def Heap_Extract_Max(A):
    if A.size<1:
        print("Heap underflow")
        return      
    max=A.maxHeap[0]                  #Prendo il massimo
    A.maxHeap[0]=A.maxHeap[A.size-1]  #Lo sostituisco con l'ultimo valore inserito
    A.size=A.size-1                   #Aggiorno la size
    Max_Heapify(A.maxHeap,A.size,0)   #Ripristino la proprietà del max heap
    return max

def Heap_Increase_Key(A,i,key):
    if key<A.maxHeap[i]:
        print("New key is smaller than current key")
    A.maxHeap[i]=key
    while i>0 and A.maxHeap[A.parent(i)]<A.maxHeap[i]:
        A.scambia(i,A.parent(i))
        i=A.parent(i) #Tecnica dei puntatori inseguitori 
        
def Max_Heap_Insert(A, key):
    A.inserisci(float('-inf'))
    print(A.maxHeap)
    Heap_Increase_Key(A,A.size-1,key)

#HOMEWORK
def Build_Max_Heap_v2(A):
    A_heap=MaxHeap(len(A))
    A_heap.size=1
    for i in range (0,len(A)):
        Max_Heap_Insert(A_heap, A[i])
    return A_heap

if __name__ == "__main__":
    
    A = [15, 5, 3, 17, 10, 84, 19, 22]
    print("\nBUILD_MAX_HEAP: \n")
    A=Build_Max_Heap(A)
    print(A)
    print("\nHEAPSORT: \n")
    A=HeapSort(A)
    print(A)
    #print("\nBuilding the heap... \n")
    #A_heap=Build_Max_Heap_v2(A)
    #print("\nBUILD_MAX_HEAP_V2: \n")
    #A_heap.Print()
    #print(A_heap.maxHeap)
    

# https://medium.com/@allan.sioson/max-heapify-build-max-heap-and-heapsort-algorithm-in-python-42c4dec70829