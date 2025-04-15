def MinDiff(matrix):
    min=214748 #limite di rappresentazione di un tipo int
    curr=214748
    i=0
    for row in matrix:
        row.sort()
        if not (i==0):
            for x in row:
                for y in matrix[i-1]:

                    # Pruning se andare avanti coi confronti non mi porta vantaggio
                    if not (abs(x-y)<curr):
                        break

                    curr=abs(x-y)
                    print(curr,x,y)

                    if(curr<min):
                        min=curr
                        print("Aggiorno...")
        i+=1

    return min

def readTestList(path):
    testList=[]
    try:
        with open(path,'r') as file:

            for line in file:
                line=line.strip()
                numbers=[]
                if line:
                    try:
                        for x in line.split():
                            numbers.append(int(x))
                    except ValueError:
                        print(f"Errore alla riga {line.split()}: {x}. Deve essere un intero")
                testList.append(numbers)
    except FileNotFoundError:
        print(f"File {path} non found!")

    return testList

if __name__=="__main__":
    testList=readTestList("./test_minabsdiff.txt")

    T=testList[0][0]
    i=1

    for test in range(T):

        N,M=testList[i]
        i+=1
        matrix=testList[i:i+N]
        i+=N
        print(f"La differenza minima trovata nella matrice {matrix} è {MinDiff(matrix)}")

