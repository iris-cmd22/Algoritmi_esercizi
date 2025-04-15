


def maxSommaSubarray(array):

    lenght = len(array) #dimensione dell'array
    memo = [[0]*(lenght)]*(lenght)
    
    maxsum_global=-1000000000000
    maxsum_global=maxSum(array,0,lenght-1,memo)

    for lenght in memo:
        print(lenght)
        
    return maxsum_global

def maxSum(arr,l,h,memo):

        #passo base 
        if(l == h):
            return arr[l]

        sum=0
        if(memo[l][h]):
            sum=memo[l][h] #memoization
        else:
            for i in range(l,h):
                sum += arr[i]
            memo[l][h]=sum

        return max(sum,maxSum(arr,l,h-1,memo),maxSum(arr,l+1,h,memo))

def readTestFile(path):

    file = open(path, "r")

    testsList = []

    for line in file:
        if line.strip() == "END":
            break
        testsList.append([int(x) for x in line.split(' ')])
    
    return testsList

if __name__ == "__main__":

    testsList = readTestFile(path="./test_file.txt")

    for test in testsList:
        array = test[:]
        result = maxSommaSubarray(array)
        print(result)
    
    