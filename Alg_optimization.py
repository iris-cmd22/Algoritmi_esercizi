def min_cost_division(n, pivots):
    pivots = sorted(pivots)  # ordiniamo i pivot per comodità
    memo = {}
    
    def dp(start, end, pivot_idx):
        # Se abbiamo usato tutti i pivot
        if pivot_idx >= len(pivots):
            return 0
            
        if (start, end, pivot_idx) in memo:
            return memo[(start, end, pivot_idx)]
        
        # Costo per dividere il segmento corrente
        current_cost = end - start
        
        # Proviamo ogni pivot rimanente
        min_cost = float('inf')
        for i in range(pivot_idx, len(pivots)):
            pivot = pivots[i]
            if pivot > start and pivot < end:
                # Dividiamo in [start,pivot] e [pivot,end]
                left_size = pivot - start
                right_size = end - pivot
                
                # Continuiamo con il segmento più grande
                if left_size > right_size:
                    next_cost = dp(start, pivot, i + 1)
                else:
                    next_cost = dp(pivot, end, i + 1)
                
                min_cost = min(min_cost, current_cost + next_cost)
        
        # Se non abbiamo trovato pivot validi, il costo è solo quello corrente
        if min_cost == float('inf'):
            min_cost = 0
            
        total_cost = current_cost + min_cost
        memo[(start, end, pivot_idx)] = total_cost
        print(memo)
        return total_cost
    
    return dp(0, n, 0)


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

if __name__=="__main__":
    testList=readTestFile("./test_algOptimization.txt")
    #print(testList)
    i=0
    for test in testList:

        if(i%3==0): N=test[0]
        if(i%3==1): P=test[0]
        if(i%3==2): 
            pivots=test

            print(f"Per {N,P,pivots}, Costo minimo: {min_cost_division(N, pivots)}")
        i+=1