
def Hamming(N,H):
    cont=0
    canditates=[]
    seq=[0 for _ in range(N)]
    def dfs(size):
        nonlocal cont
        #Caso base
        if(size==N):
            if(cont==H):
                canditates.append(list(seq))
            return

        seq[size]=0
        dfs(size+1)
        
        seq[size]=1
        cont+=1
        dfs(size+1)
        cont-=1

    #Chiamo la funzione
    dfs(0)
    print(canditates)
    return canditates

def readTestFromFile(path):

    testlist=[]
    try:
        with open(path,'r') as file:
            for line in file:
                line=line.strip()
                if line:
                    numbers=[]
                    try:
                        for x in line.split():
                            numbers.append(int(x))
                    except ValueError:
                        print(f"Devi inseire int!")
                    testlist.append(numbers)

    except FileNotFoundError:
        print(f"File {path} non trovato")
    return testlist

if __name__=="__main__":

    testlist=readTestFromFile("./test_hamming.txt")

    T=testlist[0][0]

    for test in range(T):
        N,H=testlist[test+1]
        print(f"Le possibili stringhe di lunghezza {N}, che hanno distanza di Hamming pari a {H} sono: ")
        Hamming(N,H)
