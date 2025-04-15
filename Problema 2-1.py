#Sia data una matrice di N x M numeri interi positivi. 
# Si implementi un algoritmo di backtracking per determinare la lunghezza 
# della più lunga sequenza di numeri adiacenti strettamente crescenti 
# (un numero x è adiacente ad y si trova in alto, in alto a destra, 
# in alto a sinistra, a destra, a sinistra, in basso, in basso a destra, 
# in basso a sinistra rispetto ad y)

def LIS(matrix,n):
    
    rows = n
    cols = n
    
    numbers=[]

    def dfs(i, j, current_length):

        nonlocal max_length
        max_length = max(max_length, current_length)

        # Definisci le direzioni in cui muoversi
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < rows and 0 <= y < cols and matrix[x][y] > matrix[i][j]:
                dfs(x, y, current_length + 1)

    max_length = 1
    for i in range(rows):
        for j in range(cols):
            numbers.append(matrix[i][j])
            dfs(i, j, 1)

    return numbers, max_length

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
                            
                            if(int(x)<0):
                                raise ValueError
                            numbers.append(int(x))
                            
                        except ValueError:
                            print(f"Errore alla riga {line.strip()}: '{x}'. Devi inserire numeri interi e positivi!")
                            break #Analizzo solo i caratteri corretti
                    testsList.append(numbers)
    except FileNotFoundError:
        print(f"File {path} non trovato.")
    
    return testsList

if __name__=="__main__":
    
    #try:
        #input da tastiera
        #print("Inserisci n numeri interi separato da spazi: ")
        #array_n = input()
        
        testsList = readTestFile(path="./Test21.txt")

        n_test=len(testsList)
        i=0
        
        while n_test>  0:
            
            n=testsList[i][0]
            test=testsList[i+1:i+1+n]
            print(test)
            path, result = LIS(test,n)
            print("La lunghezza massima della sequenza crescente è:", result)
            print("path: ", path)
            
            n_test-=(n+1)
            i+=n+1
    #except ValueError:
    #    print("Devi inserire numeri interi!")