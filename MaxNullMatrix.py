def MaxNullMatrix(A, rows, cols):
    # Array per tenere traccia delle altezze consecutive di zeri
    h = [0] * cols
    # Array per i bordi sinistri
    l = [0] * cols
    # Array per i bordi destri
    r = [cols] * cols
    max_area = 0
    
    for i in range(rows):
        # Reset dei bordi per ogni riga
        current_left = 0
        current_right = cols
        
        # Aggiornamento altezze e bordi sinistri
        for j in range(cols):
            if A[i][j] == 0:
                h[j] += 1
                l[j] = max(l[j], current_left)
            else:
                h[j] = 0
                l[j] = 0
                current_left = j + 1
                
        # Aggiornamento bordi destri
        for j in range(cols - 1, -1, -1):
            if A[i][j] == 0:
                r[j] = min(r[j], current_right)
            else:
                r[j] = cols
                current_right = j
        
        # Calcolo dell'area massima per la riga corrente
        for j in range(cols):
            if h[j] > 0:
                width = r[j] - l[j]
                area = width * h[j]
                max_area = max(max_area, area)
    
    return max_area



def readTestFile(path):
    testList=[]
    try:
        with open(path,'r') as file:
            for line in file:
                if line:
                    line=line.strip()
                    numbers=[]
                    for x in line.split():
                        numbers.append(int(x)) 
                    testList.append(numbers)
    except FileNotFoundError:
        print(f"File {path} non trovato")
    return testList

if __name__=="__main__":
    testList=readTestFile("./test_maxNullMatrix.txt")
    i=1
    for test in range(testList[0][0]):
        rows=testList[i][0]
        cols=testList[i][1]
        i+=1
        matrix=testList[i:i+rows]
        i+=rows
        print(matrix,rows,cols)
        print(MaxNullMatrix(matrix,rows,cols))



        

