def Tartaglia(i):
    if i == 1:
        return [1]
        
    riga = [1]
    riga_prec = [1]
    
    # Genera ogni riga fino alla i-esima
    for k in range(2, i+1):
        riga = [1]  # Primo elemento
        
        # Calcola elementi centrali
        for j in range(len(riga_prec)-1):
            riga.append(riga_prec[j] + riga_prec[j+1])
            
        riga.append(1)  # Ultimo elemento
        riga_prec = riga
        
    return riga

def readTestFile(path):
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
                        print(f"Devi inserire un int")
                    testlist.append(numbers)

    except FileNotFoundError:
        print(f"Non ho trovato il file {path}")

    return testlist


if __name__=="__main__":
    testlist=readTestFile("./test_tartaglia.txt")

    for test in testlist:
        print(f"La riga {test[0]}-esima del triangolo è {Tartaglia(test[0])}")

