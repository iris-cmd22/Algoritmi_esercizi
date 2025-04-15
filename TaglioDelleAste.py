


def TaglioTravi(l,tagli):
    #definiamo la struttura di memorizzazione
    dp=[[-1  for _ in range(l+1)] for _ in range(l+1)]
    mins=[]
    def minCuts(i,j):
        
        if(dp[i][j] != -1):
            return dp[i][j]
            
            
        if(i == j):
            res = 0
        else:
            minimum = float("inf")
            for taglio in tagli:
                #Se sto nella mia sottosezione
                if taglio < j and taglio > i:
                    #Il minimo + la dimensione della trave iniziale + la dimensione delle due sottoaste rimaste
                    minimum = min(minimum, ((j-i) + minCuts(i, taglio) + minCuts(taglio, j)))
                    mins.append(minimum)
            if(minimum == float("inf")): 
                return 0
            else:
                return minimum
        dp[i][j]=res
        return res
    
    ris=minCuts(0,l)
    print(mins)
    return ris


def readTestFile(path):
    """funzione di lettura da file

    Args:
        path (_type_): path del file da leggere

    Returns:
        testList: lista di liste, ogni  lista  raccoglio i caratteri di una riga
    """
    try:
        testList=[]
        #Apro il file inmodalità lettura
        with open(path, 'r') as file:
            #per ogni riga del file
            for line in file:
                line=line.strip() #non considero gli spazi
                #print(line)
                if line:
                    numbers=[]
                    for x in line.split(): #Return a list of the substrings in the string, using sep (in None is whitespace) as the separator string
                        try:
                            #print(x)
                            if(int(x)<0):
                                raise ValueError
                            numbers.append(int(x))
                            #print(numbers)
                        except ValueError:
                            print(f"Errore alla riga {line.strip()}: '{x}'. Devi inserire numeri interi postivi!")
                            break
                    testList.append(numbers)
    except FileNotFoundError:
        print(f"File {path} non trovato")
    return testList


if __name__=="__main__":
    
    testList=readTestFile(path="./test_aste.txt")
    #print(testList)
    i=0
    for test in testList:
        
        if not test:
            break
        
        if (i%3==0):
            l=test[0]
            if (l==0):
                print("fine")
                break
            i+=1
            print(f"Ho un'asta da {l} metri")
            
        elif (i%3==1):
            n_tagli=test[0]
            i+=1
            print(f"e devo effettuare {n_tagli} tagli")
        elif (i%3==2):
            i+=1
            print(f"Ottenendo dei pezzi da: {test}")
            print(f"Il costo ottimo del taglio di questa trave è {TaglioTravi(l,test)}")
            
        
                    
            
        
        
        
        