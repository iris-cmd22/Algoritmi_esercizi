

#Voglio l'elemento più vicino all'anno A
def binarysearch(A,p,r,anno):
    
    #Finchè sono nel vettore
    while(p<r):
        print(p,r)
        #prendo il valore di mezzo
        q=(p+r)//2
        #Se il valore che voglio è minore o uguale del valore mediano di A
        if(A[q]<=anno):
            #se è uguale
            if A[q+1]>=anno or q+1>=r:
                return q
            else:
                p=q+1
        #Altrimenti esploro il sottoarray di sinistra
        else:
            r=q-1
    #Se esco dal vettore restituisco l'ultimo indice trovato
    print("sono fuori dal while")
    return -1

def maxEventi(periodo_storico,eventi):
    maxEvents=0
    
    for i in range(len(eventi)):
        
        q=binarysearch(eventi,i,len(eventi)-1,eventi[i]+periodo_storico)
        if(q!=-1):
            somma=len(eventi[i:q+1])
            print(i,q,eventi[i:q+1])
        else:
            print("q non trovato")
        
        if(somma>maxEvents):
            maxEvents=somma
            inizio=eventi[i]
            fine=eventi[q]
            print(q, len(eventi[i:q]),somma,maxEvents,inizio,fine)
    
    return maxEvents, inizio, fine
    
def readFromFile(path):
    testList=[]
    try:
        with open(path,'r') as file:
            for line in file:
                line=line.strip()
                if line:
                    numbers=[]
                    for x in line.split():
                        try:
                            numbers.append(int(x))
                        except ValueError:
                            print(f"Errore alla riga {line.split()}: {x}.")
                    testList.append(numbers)
    except FileNotFoundError:
        print(f"File {path} non trovato")
    return testList

if __name__=="__main__":
    
    testList=readFromFile("./test_eventistorici.txt")
    print(testList)
    
    n=testList[0][0]
    for i in range(n):
        
        Y=testList[i+1][0] #periodo storico
        K=testList[i+2][0] #numero di eventi
        eventi=[int(x[0]) for x in testList[i+3:i+3+K]]
        print(Y,K,eventi)
        
        maxEvents,inizio,fine=maxEventi(Y,eventi)
        print(f"Considerando gli eventi {eventi} il periodo storico più intenso va dal {inizio} al {fine}, per un totale di {maxEvents} eventi")