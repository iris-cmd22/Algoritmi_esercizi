#DIVIDE ET IMPERA

import numpy as np


def BestAddress(n_civici):
    #metto il civico nella mediana
    n_civici=np.sort(n_civici)
    civico=n_civici[len(n_civici)//2]
    #Calcolo le distanze
    dist=[abs((civico)-civici) for civici in n_civici]
    return civico, sum(dist)

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
                            if(int(x)<0):
                                raise ValueError
                            numbers.append(int(x))
                        except ValueError:
                            print(f"Errore alla riga {line.split()}: {x}. Deve essere un numero intero e positivo!")
                    testList.append(numbers)
    except FileNotFoundError:
        print(f"File {path} non trovato")
    return testList

if __name__=="__main__":
    
    testList=readTestFile("./test_sigRossi.txt")
    print(testList)
    
    n_test=testList[0][0]
    i=1
    
    for test in range(n_test):
        n_parenti=testList[i][0]
        i+=1
        n_civici=[int(x[0]) for x in testList[i:n_parenti+i]] 
        i+=n_parenti
        print(f"Il sig Rossi ha {n_parenti} e i loro numeri civici sono {n_civici}")
        civico,min_dist=BestAddress(n_civici)
        print(f"Il miglior indirizzo per la nuova casa a Napoli del sig Rossi è Via Roma,{civico}. In questo modo disterà {min_dist} numeri civici dal suo parente più lontano. \n FNS")