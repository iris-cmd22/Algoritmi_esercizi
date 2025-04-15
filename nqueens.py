def isMoveValid(N, scacchiera, row, col):

    #Controlliamo che non ci sia nessuna regina nella stessa riga
    for i in range(col):
        if scacchiera[row][i] == 1:
            return False
        
    #Controlliamo che non ci sia nessuna regina sulla diagonale superiore di sinistra
    # ad esempio se siamo in (2,2) in una 4x4
    # controlliamo in (2,2) (1,1) (0,0)
    i=row
    j=col
    while i >= 0 and j >= 0:
        if scacchiera[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    #Controlliamo che non ci sia nessuna regina sulla diagonale inferiore sinistra
    # ad esempio se siamo in (2,2) in una 4x4
    # controlliamo in (2,2) (3,1)
    i=row
    j=col
    while i < N and j >= 0:
        if scacchiera[i][j] == 1:
            return False
        i += 1
        j -= 1

    #non controllo in altre parti poichè inserisco una regina colonna per colonna
    return True

def solveNQueenUtil(N, scacchiera, col, counter):

    if col >= N:
        return counter + 1
    
    for i in range(N):

        if isMoveValid(N, scacchiera, i, col):
            
            scacchiera[i][col] = 1

            counter = solveNQueenUtil(N, scacchiera, col+1, counter)
            
            scacchiera[i][col] = 0

    return counter

def solveNQueen(N):

    counter = 0 # per conteggiare tutte le soluzioni valide

    #creo la scacchiera
    #usando una matrice inizializzata a tutti 0
    scacchiera = [[0 for _ in range(N)] for _ in range(N)]
    
    counter = solveNQueenUtil(N, scacchiera, 0, counter)

    return counter
    

if __name__ == "__main__":

    with open("./test_file.txt") as file:

        num_test = int(file.readline())

        while num_test > 0:

            N = int(file.readline())

            result = solveNQueen(N)

            print(result)

            num_test -= 1