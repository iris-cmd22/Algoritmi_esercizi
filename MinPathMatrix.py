
def MinPath(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    pos=[]
    path=[]
    min_pos=[]
    min_path=[]
    min=float("inf")
    def minCost(i, j):

        nonlocal min,min_pos,min_path

        if(j==cols-1):
            pos.append((i,j))
            #print("fine",path,pos,min)
            if min>sum(path):
                min=sum(path)
                min_path.append(path.copy())
                min_pos.append(pos.copy())
            if min==sum(path):
                min_path.append(path.copy())
                min_pos.append(pos.copy())
            pos.pop()
            return 

        # Definisci le direzioni in cui muoversi
        directions = [(0, 1), (1, 1), (-1, 1)]

        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= y < cols: 
                path.append(matrix[x%rows][y])
                pos.append((x%rows,y))
                minCost(x%rows, y)
                path.pop()
                pos.pop()
            
    for i in range(rows):
        path.append(matrix[i][0])
        pos.append((i,0))
        minCost(i,0)
        path.pop()
        pos.pop()

    print(min_pos)
    #Visualizzazione matrice
    sol=[]
    
    for i in range(len(min_path[0])):
        min=float("inf")
        for j in range(len(min_path)):
            print(list(min_path[j]),j)
            if min_path[j][i]<=min:
                sol=min_path[j]
                print(min_pos)
                min_pos=min_pos[j]
        
    
    print(sol)
    mat=[[0 for _ in range(cols)] for _ in range(rows)]
    print(mat)
    for i in range(len(sol)-1):
        x,y=min_pos[i]
        mat[x][y]=1

    print("Persorso minimo: ")
    for i in range(rows):
        print(mat[i])

    return min_path, min

def readTestFile(path):
    testList=[]
    try:
        with open(path,'r') as File:
            for line in File:
                line=line.strip()
                if line:
                    numbers=[]
                    for x in line.split():
                        try:
                            if (int(x)<0):
                                raise ValueError
                            numbers.append(int(x))
                        except ValueError:
                            print(f"Errore alla riga {line}: '{x}'.Devi inserire numeri interi e positivi!")
                testList.append(numbers)
    except FileNotFoundError:
        print(f"File {path} non trovato")
    return testList

if __name__=="__main__":
    
    testList=readTestFile("./test_minpath.txt")
    #print(testList)
    i=0
    n=0
    matrix=[]
    
    n_test=testList[0][0]
    for k in range(2*n_test):
        
        if(i%(n+1)==0):
            n,m=testList[i+1][0],testList[i+1][1]
            i+=1
        else:
            matrix=testList[i+1:i+n+1]
            i+=n
            print(matrix)
            path, sol= MinPath(matrix)
            print(f"Il cammino minimo {path} ci da un guadagno di {sol}")
        #print(i)
    