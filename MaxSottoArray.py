
def MaxSub(input):

    max=sum(input)
    print("max",max)

    for i in range(len(input)):
        for j in range(len(input)):
            curr=sum(input[i:i+j])

            if curr>max:
                max=curr
                print(input[i:i+j],max)

    return max


def MaxSub_divetimp(input):

    max=sum(input)
    print("max",max)

    def div_et_imp(i,j):
        nonlocal max
        if(j==len(input)):
            return sum(input[i:j])

        curr=div_et_imp(i,j+1)

        if curr>max:
            max=curr
            print(input[i:j+1],max)

        return sum(input[i:j])



    for i in range(len(input)):
        curr=div_et_imp(i,i+1)

        if curr>max:
            max=curr
            print(input[i:i+1],max)

    return max


'''

-1 -3 4 2  #1 confronti      sum(input)

-1-34 -342   #2 confronti   

-1-3 -34 42 #3 confronti

-1 -3 4 2 #4 confronti

'''

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
    testlist=readTestFile("./test_maxsottoarray.txt")

    for test in testlist:
        print(f"Per {test} il massimo è {MaxSub_divetimp(test)}")


    