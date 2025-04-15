# Voglio ottenere la somma maggiore data dai sottoarray dell'array dato in input


def maxSommaCentrale(arr, l, m, h): 

	#Partiamo dal sottovettore di sinistra
	left_sum = -10000 #massima somma globale a sinistra
	somma = 0 #massima somma corrente

	for i in range(m, l-1, -1): 
		somma += arr[i] 

		#La somma trovata è maggiore della massima trovata finora?
		if (somma > left_sum): 
			left_sum = somma #aggiorno la somma globale

	#Passiamo dal sottovettore di destra 
	right_sum = -1000 #massima somma globale a destra
	somma = 0 #inizializzo la massima somma corrente
	
	for i in range(m+1, h + 1): 
		somma += arr[i] 

		#La somma trovata è maggiore della massima trovata finora?
		if (somma > right_sum): 
			right_sum = somma #aggiorno la somma globale


	#devo far tornare il massimo fra la somma di destra, la somma di sinistra o 
	#la somma delle due
	return max(left_sum + right_sum, left_sum, right_sum) 


# Voglio ottenere la summa massima dei sottoarray in un array dato in input
#che parta dall'indice l (low) fino all'indice h (high)
def maxSommaSubarray(arr, l, h): 

	#low minore di high? 
	if (l > h): 
		#print("[ERRORE] Indici out of range!")
		return -10000 #errore
	# Caso base: se arrivo al singolo elemento restituisco il numero in quella posizione 
	if (l == h): 
		return arr[l] 

	# Dividiamo l'array a metà e analizziamone le sottosequenze
	m = (l + h) // 2

	#Il confronto avverrà fra le somme delle due sottosequenze e una somma ulteriore
	#la sottostringa a somma maggiore potrà infatti trovarsi anche a cavallo dei due sottoarray
	#in cui ho diviso quello iniziale, per questo chiamo la funzione 
	return max(maxSommaSubarray(arr, l, m-1), #uso m-1 per non ripetere somme che effettuerà maxSommaCentrale
			maxSommaSubarray(arr, m+1, h), #uso m+1 per non ripetere somme che effettuerà maxSommaCentrale
			maxSommaCentrale(arr, l, m, h)) 


#Funzione di lettura da file
def readTestFile(path):

    file = open(path, "r")

    testsList = []

    for line in file:
        if line.strip() == "END":
            break
        testsList.append([int(x) for x in line.split(' ')])
	
	
    print("\n".join(map(str, testsList)))
    
    return testsList

if __name__ == "__main__":

    testsList = readTestFile(path="./test_file.txt")

    for test in testsList:

        array = test[:]
        n = len(array)  
        max_sum = maxSommaSubarray(array, 0, n-1) 
        print(max_sum)



