def Swap_counter(input):

    diff=0

    def div_et_imp(start,end):
        nonlocal diff

        if(start==end):
            return input[start]
        
        m=(start+end)//2

        div_et_imp(start,m)
        div_et_imp(m+1,end)

        print(input[m],input[m+1])

        if(input[m]>input[m+1]):
            diff+=1
            temp=input[m]
            input[m]=input[m+1]
            input[m+1]=temp
            print(diff)

    for k in range(len(input)-1):

        for i in range(len(input)-1):
            if(input[i]>input[i+1]):
                print("DEVO ORDINARE...")
                div_et_imp(0,len(input)-1) 
                print(input)
                break

    return diff

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

    testlist=readTestFromFile("./test_swap.txt")
    i=0
    for test in testlist:
        print(test)
        if(i%2==0):
            dim=test[0]
        else:
            print(f"La sequenza in input è {test}, viene riordinato in  {Swap_counter(test)} swap")

        i+=1