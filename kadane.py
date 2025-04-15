def maxSommaSubarray(array):

    lenght = len(array) #dimensione dell'array

    max_curr_sum = 0  #massima somma corrente
    max_glob_sum = -100000000000 #massima somma globale 
		#numero piccolissimo per essere sicuro di aggiornarlo con un elemento dell'array

    for i in range(0, lenght): #scorro l'array

        max_curr_sum = max_curr_sum + array[i] #aggiorno la somma corrente
        
				#se la massima somma corrente è maggiore di quella più grande trovata fin'ora
        if(max_curr_sum > max_glob_sum): 
            max_glob_sum = max_curr_sum #aggiorno la massima somma globale

        if(max_curr_sum < 0): #se la massima somma corrente è negativa 
            max_curr_sum = 0 #la inizializzo a zero nuovamente
        
    return max_glob_sum #restituisco la somma globale

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
        maxSum = maxSommaSubarray(array)
        print(maxSum)