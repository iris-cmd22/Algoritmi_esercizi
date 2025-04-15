
def Esponenziale(input):
    base=input[0]
    n=input[1]

    def dfs(base,exp):
        
        if(exp==0):
            return 1
        if(exp==1):
            return base
            
        if(exp%2==0):
            ris=dfs(base,exp//2)
            return ris*ris
        else:
            ris=dfs(base,exp//2)
            return ris*ris*base

    return dfs(base,n)

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
    testlist=readTestFile("./test_esponenziale.txt")

    for test in testlist:
        print(f"Il risultato di {test[0]} alla {test[1]} è {Esponenziale(test)}")


    