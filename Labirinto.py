
#definizione delle mosse valide
def isValid(board,x,y):
    if (x<0 or x>len(board)-1):
        return False
    if (y<0 or y>len(board[0])-1):
        return False
    if (board[x][y]!=1):
        return False
    return True

#definizione percorso trovato
def finished(board,x,y):
     return (x,y==len(board),len(board)-1)

def solve(path,board,i,j):
    #se ho finito
    if(finished(board,i,j)):
        #process_solution
        path.append((i,j))
        print("Sono fuori",path)
        return True
    #se la mossa è valida
    if(isValid(board,i,j)):
        #Make_move
        path.append((i,j))
    else:
        #Unmake_move
        path.pop()
        print("Ho incontrato un muro")
        return


    #Costruct_candidates
    #Posso muovermi solo in avanti e in basso
    directions=[(0,1),(1,0)]
    for dx,dy in directions:
        x,y=i+dx,j+dy 
        solve(path,board,x,y)


def Rat_Maze(board):
    path=[]
    path.append((0,0))
    return solve(path,board,0,0)



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
    testListFile=readTestFile("./test_labirinto.txt")
    #Prendiamo dimensione e labirinto di gioco
    M,N=testListFile[0]
    maze=testListFile[1:N+1]
    #Chiamiamo la funzione che risolve il problema
    Rat_Maze(maze)
   

