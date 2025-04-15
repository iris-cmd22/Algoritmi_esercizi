# Python Program to implement merge sort using
# multi-threading
import threading
MAX=20
# number of threads
THREAD_MAX = 4
 
A = [0] * MAX
part = 0
 
# merge function for merging two parts
def Merge(low, mid, high):
    L = A[low:mid+1]
    R = A[mid+1:high+1]
 
    # n1 is size of left part and n2 is size
    # of right part
    n1 = len(L)
    n2 = len(R)
    i = j = 0
    k = low
 
    # merge left and right in ascending order
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1
 
# merge sort function
def MergeSort(low, high):
    if low < high:
        # calculating mid point of array
        mid = low + (high - low) // 2
 
        MergeSort(low, mid)
        MergeSort(mid + 1, high)
 
        # merging the two halves
        Merge(low, mid, high)
 
# thread function for multi-threading
def merge_sort_threaded():
    global part
    global MAX
    global A 
    
    MAX=len(A)
     
    # creating 4 threads
    for i in range(THREAD_MAX):
        t = threading.Thread(target=MergeSort, args=(part*(MAX//4), (part+1)*(MAX//4)-1))
        part += 1
        t.start()
         
    # joining all 4 threads
    for i in range(THREAD_MAX):
        t.join()
 
    # merging the final 4 parts
    Merge(0, (MAX // 2 - 1) // 2, MAX // 2 - 1)
    Merge(MAX // 2, MAX // 2 + (MAX - 1 - MAX // 2) // 2, MAX - 1)
    Merge(0, (MAX - 1) // 2, MAX - 1)

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
        A=test
        merge_sort_threaded()
        print(A)