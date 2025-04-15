
def prog_arit(test):

    prog=[]
    
    def div_et_imp(start,end):
        nonlocal diff

        if(start==end):
            return test[start]
        
        m=(start+end)//2

        seq1=div_et_imp(start,m)
        seq2=div_et_imp(m+1,end)

        if diff==0:
            diff=test[m+1]-test[m]
        else:
            if not (test[m+1]-test[m]==diff):
                prog.append(test[m]+diff)
                
    diff=0
    div_et_imp(0,len(test)-1)

    return prog[0]

    

def readTestFromFile(path):

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
                        print(f"Devi inseire int!")
                    testlist.append(numbers)

    except FileNotFoundError:
        print(f"File {path} non trovato")
    return testlist

if __name__=="__main__":

    testlist=readTestFromFile("./test_progressione.txt")

    T=testlist[0][0]
    print(T)
    i=0
    for test in range(2*T):

        if(i%2==0):
            dim=testlist[test+1][0]
        else:
            A=testlist[test+1]
            print(f"La sequenza in input è {A}, quindi manca {prog_arit(A)}")

        i+=1




