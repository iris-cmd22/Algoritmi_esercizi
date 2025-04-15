


def maxSommaSubarray(array):

    lenght = len(array) #dimensione dell'array
    dp = [0]*(lenght+1)
    
    for i in range(lenght):
        #La scelta consiste nell'includere il valore al sottoarray corrente
        #oppure nel cominciarne uno nuovo
        dp[i+1]=max(dp[i]+array[i],array[i])  
    
    print(dp)  
    return max(dp[1:]) #Non considero lo zero iniziale

def readTestFile(path):
    testList=[]
    try:
       with open(path,'r') as file:
           for line in file:
               line=line.strip()
               if line:
                    numbers=[]
                    for x in line.split():
                            numbers.append(int(x))
                    testList.append(numbers) 
    except FileNotFoundError:
        print(f"File {path} non trovato")
    return testList 

if __name__ == "__main__":

    testsList = readTestFile(path="./test_maxSubArray.txt")

    for test in testsList:
        array = test[:]
        result = maxSommaSubarray(array)
        print(result)
    
    