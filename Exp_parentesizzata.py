import re

def Exp_parentesizzata(numbers,operators):

    max_val=[[float('-inf')]*len(numbers) for _ in range(len(numbers))]
    min_val=[[float('inf')]*len(numbers) for _ in range(len(numbers))]

    def dp(i,j):

        #Caso base
        if i==j:
            max_val[i][i]=numbers[i]
            min_val[i][i]=numbers[i]
            return max_val[i][i],min_val[i][i]
        
        #memo
        if max_val[i][j]!=float('-inf'):
            return max_val[i][j],min_val[i][j]
        
        
        for k in range(i,j): #per ogni k
            #divido in due parti
            left_max,left_min=dp(i,k)
            right_max,right_min=dp(k+1,j)

            #combino utilizzando l'operatore
            if operators[k]=='+':
                max_val[i][j]=max(max_val[i][j],left_max+right_max)
                min_val[i][j]=min(min_val[i][j],left_min+right_min)
            else:
                max_val[i][j]=max(max_val[i][j],left_max*right_max)
                min_val[i][j]=min(min_val[i][j],left_min*right_min)

        return max_val[i][j],min_val[i][j]
    
    sol=dp(0,len(numbers)-1)
    print(max_val)
    print(min_val)
    return dp(0,len(numbers)-1)

    




def readTestFile(path):
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
    testList=readTestFile("./test_exp_parentesizzata.txt")
    print(testList)
    
    for test in testList:
        print(test)
        exp=test[0]
        numbers = list(map(int, re.split(r'[+\*]', exp)))
        operators = [c for c in exp if c in '+*']
        print(numbers,operators)
        result=Exp_parentesizzata(numbers,operators)
        print(result)
        