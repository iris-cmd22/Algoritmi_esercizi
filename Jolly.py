

    

def Jolly_detect(seq):
    
    bool_seq=[False for _ in range(1,len(seq)-1)] #c'è -1 perchè se no la mediana va fuori range
    
    
    def Difference_check(start,end):
    
        #Caso base
        if(start==end):
            return seq[start]
        
        #Ricorsione
        m= (start +end)//2
        Difference_check(start,m)
        Difference_check(m+1,end)
        #I valori assunti dalla differenza tra gli elementi successivi devono assumere tutti i valori da 1 a n-1
        diff=abs(seq[m]-seq[m+1])
        #print(diff)
        
        if diff in range(1,len(seq)-1):
            bool_seq[diff-1]=True
    
    Difference_check(0,len(seq)-1) #modifica bool_seq
    #print(bool_seq)
    #Check di bool_seq
    isJolly =True
    if False in bool_seq:
        isJolly=False
    
    return isJolly

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
                            numbers.append(int(x))
                        except ValueError:
                            print(f"Errore alla riga {line.split()}: {x}. Devi inserire caratteri interi")
                            break
                    testList.append(numbers)
    except FileNotFoundError:
        print(f"File {path} non trovato") 
    return testList


if __name__== "__main__":
    
    testList=readTestFile("./test_jolly.txt")
    print(testList)
    
    for test in testList:
        
        if not test:
            break
        
        if(Jolly_detect(test)):
            print(f"The sequence {test} is a jolly")
        else:
             print(f"The sequence {test} is not a jolly")
    