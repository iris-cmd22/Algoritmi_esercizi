import numpy as np

def coinchange(coin,importo,n):
    dp = [[float('inf') for _ in range(importo+1)] for _ in range(n+1)]
    
    #CASO BASE
    for i in range(n + 1): #per avere 0$ servono 0 monete
        dp[i][0] = 0 

    for i in range(1,n+1): #per ogni tipo di moneta
        for j in range(1,importo+1):  #per ogni importo
            #Se la moneta è minore dell'importo totale
            if(coin[i-1]<=j):
                # oprendiamo il numero massimo di volte che possiamo quella moneta
                #e prendiamo l'ottimo per l'importo attuale
                #o non mi conviene prendere la moneta corrente  ma valuto quelle più piccole
                n_monete=j//coin[i-1]
                dp[i][j]=min(n_monete+dp[i-1][j%coin[i-1]],dp[i-1][j])
            else: #escludiamo la moneta
                dp[i][j]=dp[i-1][j]
    
    
    #Solo per visualizzare la struttura(non la contiamo nella complessità)
    print("Struttura [importi]x[coin]:",np.asarray(dp[1:]).T)
    return dp[n][importo]

def readTestFile(path):
    testList=[]
    try:
       with open(path,'r') as file:
           for line in file:
               line=line.strip()
               if line:
                    numbers=[]
                    for x in line.split():
                        numbers.append(int(x))
                    testList.append(numbers) 
    except FileNotFoundError:
        print(f"File {path} non trovato")
    return testList 

if __name__=="__main__":
    testList=readTestFile("./test_coinchange.txt")
    #print(testList)
    
    for test in testList:
        V=test[0]
        n=test[1]
        coin=test[2:]
        print(V,n,coin)
        result=coinchange(coin,V,n)
        if(result!=float('inf')):
            print(f"Per arrivare a {V}$ mi servono almeno {result} monete")
        else:
            print(f"Con le monete {coin} non posso arrivare a {V}")