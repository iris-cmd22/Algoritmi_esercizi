
def findPalindrome(input):
     
    dp = [[0 for _ in range(len(input)+1)] for _ in range(len(input)+1)]
    rev_input=input[::-1]
    print(input,rev_input)
	
    ans=0
    #Tabulation
    for i in range(1,len(input)+1): 
        for j in range(1,len(input)+1): 
            if(input[i-1]==rev_input[j-1]): 
                val=1+dp[i-1][j-1]
                dp[i][j]=val
                ans=max(ans,val)
                print(ans,input[i-1],rev_input[j-1])
            else:
                dp[i][j]=0
            
    print(dp)
    return ans


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
        
        input=testList[i+1][0]
        print(f"il palindromo più lungo è di {findPalindrome(input)} lettere")