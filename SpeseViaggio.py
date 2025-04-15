from math import floor

def MinScambi(spese):
    
    spesa_pp=sum(spese)/ len(spese)
    credito=0.00
    debito=0.00
    
    for spesa in spese:
        diff=spesa-spesa_pp
        if(diff>0):
            credito +=floor(diff*100.0)/100.0
        else:
            debito += floor(-diff*100.0)/100.0
    return min(credito,debito)
    

def readTestFile(path):
    testList=[]
    try:
        with open(path,'r') as file:
            for line in file:
                line=line.strip()
                if line:
                    try:
                        for x in line.split():
                            numbers=float(x)
                    except ValueError:
                        print(f"Errore alla riga {line.split()}: {x}. Deve essere un valore intero")
                testList.append(numbers)
    except FileNotFoundError:
        print(f"Fine {path} non trovato")
    return testList

if __name__=="__main__":
    
    testList=readTestFile("./test_speseviaggio.txt")
    print(testList)
    i=0
    k=len(testList)
    
    while k>0:
        
        n=int(testList[i])
        i+=1
        spese=testList[i:n+i]
        i+=n
        
        scambio=MinScambi(spese)
        print(f"Devo pareggiare le spese {spese} fra gli {n} studenti, per farlo verranno scambiati $ {scambio}")
        
        k-=i