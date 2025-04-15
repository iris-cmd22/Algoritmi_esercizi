
def findPalindrome(input):
    
    palindromes=[]
    
    
    def dfs(input):
        nonlocal palindromes
        #Caso base
        if(input==[]):
            #print(palindromes)
            return 
        
        #Ricorsione
        if (input==input[::-1]):
            palindromes.append(input)
            dfs(input[1:len(input)-1])
        else:
            if (a!=b for a,b in input):
                dfs(input[1:])
                dfs(input[:len(input)-1])
            
    dfs(input)
    print(palindromes)
    
    longest=0
    for pal in palindromes:
        if(len(pal)>longest):
            longest=len(pal)
    
    return longest


def readTestFile(path):
    testList=[]
    try:
        with open(path,'r') as file:
            for line in file:
                line=line.strip()
                if line:
                    numbers=[]
                    for x in line.split():
                        try:
                            numbers.append(x)
                        except ValueError:
                            print(f"Errore alla riga {line.split()}; {x}")
                        testList.append(numbers)
    except FileNotFoundError: 
        print(f"File {path} non trovato")
    return testList

if __name__=="__main__":
    
    testList=readTestFile("./test_palindrome.txt")
    print(testList)
    
    n_test=testList[0][0]
    
    for i in range(int(n_test)):
        
        input=[x for x in list((testList[i+1][0]))]
        print(f"il palindromo più lungo è di {findPalindrome(input)} lettere")