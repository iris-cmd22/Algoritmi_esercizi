

def isSorted(input):
    for i in range(len(input)-1):
        if input[i]>input[i+1]:
            return False
    return True

def flip(start,input):
    sol=input[start:]
    sol.reverse()
    input[start:]=sol
    
def FlipSort(test):
    input=test.copy()
    n_flip=0
    def dfs(start,end):
        nonlocal n_flip
        #Is_a_solution
        if (isSorted(input[start:end])):
            #Process_solution
            print(input)
            return n_flip,input
        
        if not (min(input)==input[end]):

            for i in range(start,end):
                if input[i]==min(input):
                    break
            flip(i,input)
            n_flip+=1
        
        flip(start,input)
        n_flip+=1

        dfs(start+1,end)
        
    dfs(0,len(input)-1)

    return n_flip,input




def readTestList(path):
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
                        print(f"Devi inserire un intero")
                testlist.append(numbers)
                
    except FileNotFoundError:
        print(f"File {path} non trovato")

    return testlist


if __name__=="__main__":

    testlist=readTestList("./test_flip.txt")
    print(testlist)

    for test in testlist:
        print(test)
        n,seq=FlipSort(test)
        print(f"La sequenza {test} è stata ordinata in {n} flip: {seq}")