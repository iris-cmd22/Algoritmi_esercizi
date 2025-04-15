
def Dec2Bin(dec,dim):
    conv=[0]*dim
    i=0
    while dec>0:
        conv[i]=dec%2
        i+=1
        dec //=2
    return conv
    
    
def Bin2Dec(n):
    conv = 0
    p = len(n)-1
    for j in range(len(n)):
        if(n[j] != 0):
            conv += 1*pow(2,p)
        p -= 1
    return conv


def seq_gen(n):
    bool_seq=[0 for _ in range(n)]
    j=0
    def dfs(i,size):
        nonlocal sol
        nonlocal j
        #Caso base
        if (i==size):
            #Passo da lista a stringa ma ho fatto delle conv che non lo richiedono
            #dec = ''.join(str(x) for x in bool_seq) 
            sol.append(list(bool_seq))
            print("sol",sol)
            return
        
        if(j%2==0):
            bool_seq[i]=1
            j+=1
            dfs(i+1,size)
            bool_seq[i]=0
            j+=1
            dfs(i+1,size)
        else:
            bool_seq[i]=0
            j+=1
            dfs(i+1,n)
            bool_seq[i]=1
            j+=1
            dfs(i+1,n)

        
    
    sol=[]
    dfs(0,n)
    sol.reverse()
    print("soluzione in decimale: ",sol)
    dim=pow(2,n)
    return [Bin2Dec(x) for x in sol]

def readTestFile(path):
    testList=[]
    try:
       with open(path,'r') as file:
           for line in file:
               line=line.strip()
               if line:
                    numbers=[]
                    for x in line.split():
                        try:
                            if (int(x)<2 and int(x)>5):
                                raise ValueError
                            numbers.append(int(x))
                        except ValueError:
                            print(f"Errore alla riga {line.split}: {x}. Il valore deve essere intero e compreso fra 2 e 5")
                    testList.append(numbers) 
    except FileNotFoundError:
        print(f"File {path} non trovato")
    return testList 

if __name__=="__main__":
    testList=readTestFile("./test_seq.txt")
    print(testList)
    
    for test in testList:
        
        print("Test output: ",seq_gen(int(test[0])))
        
        #Test conversione
        #print(f"il numero 7 in decimale è {Dec2Bin(7,4)}")
        #print(f"1001 in decimale è {Bin2Dec([1, 0, 0, 1])}")