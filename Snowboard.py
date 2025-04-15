def isValid(path,board,x,y):
    if (x<0 or x>len(board)-1):
        return False
    if (y<0 or y>len(board[0])-1):
        return False
    if (not(path==[]) and path[-1]<board[x][y]):
        print("Mossa non valida: ",path[-1],"è minore di ", board[x][y])
        return False
    return True



def solve(path,board,i,j):
    #Il percorso sarà lungo almeno una casella
    max_run=0

    #se la mossa è valida
    if(isValid(path,board,i,j)):
        #Make_move
        path.append(board[i][j])
        print("Mossa valida")
    else:
        #Unmake_move
        return max_run
    
    #Costruct_candidates: Posso muovermi solo in avanti e in basso
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    for dx,dy in directions:
        x,y=i+dx,j+dy 
        print("nelle directions",x,y)
        max_run=max(max_run, 1 + solve(path,board,x,y))
    
    #paths.append(path)
    return max_run


def Snowboard_run(board):
    path=[]
    #global paths
    max_run=0
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(i,j)
            path.append(float("inf"))
            max_run=max(max_run, 1 + solve(path,board,i,j))
    
    return max_run


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
                            numbers.append(int(x))
                        except ValueError:
                            print(f"Errore alla riga {line.split()}:{x}.")
                    testList.append(numbers)
    except FileNotFoundError:
        print(f"File {path} non trovato")
    return testList

if __name__=="__main__":
    testListFile=readTestFile("./test_snowboard.txt")
    #Prendiamo dimensione e labirinto di gioco
    M,N=testListFile[0]
    area=testListFile[1:N+1]
    #Chiamiamo la funzione che risolve il problema
    print("Il percorso più lungo è ",Snowboard_run(area))
   