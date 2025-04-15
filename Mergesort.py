
#MERGESORT

def Merge(A,p,q,r):
    
    #Calcoliamo la lunghezza dei due sottoarray
    #A[p...q] e A[q+1...r]
    n1= q - p + 1
    n2= r - q
    #print("n1: "+ str(n1)+" n2: "+ str(n2) )
    
    #Creo due array temporanei
    L=[0]*(n1)
    R=[0]*(n2)
    
    for i in range(0,n1):
        L[i]=A[p+i]
    for j in range(0,n2):
        R[j]=A[q+j+1]
    
    #print(L)
    #print(R)
    
    #Inizializziamo gli indici
    i=0
    j=0
    k=p
    
    while i <n1 and j<n2:
        if L[i] <= R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j +=1
        k+=1
        
    while i <n1:
        A[k]=L[i]
        i+=1
        k+=1
        
    while j<n2:
        A[k]=R[j]
        j+=1
        k+=1
    
def MergeSort(A,p,r):
    if p < r:
        #Prendo il valore mediano
        q=p+(r-p)//2
        
        #Chiamate ricorsive ai sottoarray
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        
        #Risolvo il problema sull'array
        Merge(A,p,q,r)
    
#Funzione di lettura da file
def readTestFile(path):
    try: 
        testsList = []
        with open(path, 'r') as file:
            for line in file:
                line = line.strip() #così tolgo gli spazi
                if line:
                    numbers=[]
                    for x in line.split():
                        try:
                            numbers.append(int(x))
                        except ValueError:
                            print(f"Errore alla riga {line.strip()}: '{x}'. Devi inserire numeri interi!")
                            break #Analizzo solo i caratteri corretti
                    testsList.append(numbers)
    except FileNotFoundError:
        print(f"File {path} non trovato.")
    
    return testsList

if __name__== "__main__":
    
    testsList = readTestFile(path="./Test12.txt")

    for test in testsList:
        
        if not test:
            break
        
        n=len(test)
        
        print("Array iniziale: ")
        print(test)
        
        print("Array ordinato: ")
        MergeSort(test,0,n-1)
        print(test)
        
        