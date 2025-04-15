
from math import floor


def Best_schedule(jobs):
    penalty=[]
    
    for i in range(len(jobs)):
        pen=jobs[i][1]/jobs[i][0]
        
        penalty.append((floor(pen*100.0)/100.0,i+1))
        
    penalty=sorted(penalty,reverse=True)
    return [x[1] for x in penalty]

def readTestFile(path):
    try:
        testList=[]
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
                            print(f"Errore alla riga {line.split()}: {x}")
                    testList.append(numbers)
    except FileNotFoundError:
        print(f"File {path} non trovato")
    return testList

if __name__=="__main__":
    
    testList=readTestFile("./test_artigiano.txt")
    #print(testList)
    
    n_test= testList[0][0]
    i=1
    for test in range(n_test):
        
        n=testList[i][0]
        i+=1
        jobs=testList[i:n+i]
        i+=n
        print(f"Un artigiano ha da svolgere {n} lavori: {jobs}")
        print(f"L'ordine che minimizza la penale è {Best_schedule(jobs)}")
        