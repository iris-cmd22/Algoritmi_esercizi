
def process_solution(bool_input,input):

    sol=[]
    for i in range(len(bool_input)-1):
        sol.append(input[i])
        #Controllo: se il bool è vero metto lo spazio
        if bool_input[i]:
            sol.append(" ")
    
    sol.append(input[-1])
    print(sol)


def Space_maker(input):

    bool_input=[False for _ in range(len(input))]

    def dfs(i,size):
        sol=[]
        #Caso base: Ho le mie soluzioni
        if(i==size):
            #print(bool_input)
            process_solution(bool_input,input)
            return
        
        bool_input[i]=True
        dfs(i+1,size)
        bool_input[i]=False
        dfs(i+1,size)

    dfs(0,len(input)-1)

def readTestList(path):
    testList=[]

    try:
        with open(path,'r') as file:
            for line in file:
                line=line.strip()
                if line:
                    numbers=[]
                    for x in line.split():
                        numbers.append(x)
                    testList.append(numbers)

    except FileNotFoundError:
        print(f"File {path} non trovato")

    return testList

if __name__=="__main__":
    testList=readTestList("./test_spazi.txt")

    for test in testList:
        print(f"Le possibili soluzioni sono: ")
        Space_maker(test)

