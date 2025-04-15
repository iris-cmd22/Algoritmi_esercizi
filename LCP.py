def longestCommonPrefix(str1, str2): #prendo 2 stringhe in input da comparare

    result = ""
    i = 0

    #finchè non arrivo alla fine della stringa più corta
    while i < min(len(str1), len(str2)): 
        #Al primo carattere diverso esco
        if str1[i]!=str2[i]:
            break

        result += str1[i]
        i = i+1
    
    return result #restituisco il prefisso 

def findLCP(array, start, end): 

    if start == end: #c'è solo una stringa nell'array
        return array[start] #restituisco la stringa come prefisso comune più lungo
    
    if(end > start): #se ci sono almeno 2 stringhe nell'array

        #prendo il mediano dell'array
        mid = (end + start) // 2 

        str1 = findLCP(array, start, mid) #prima metà dell’array
        str2 = findLCP(array, mid+1, end) #seconda metà dell’array

        return longestCommonPrefix(str1, str2) #confronto le 2 stringhe
    
    return "" #se non lo trovo -> stringa vuota

def readTestFile(path):
    testList=[]
    try:
        with open(path,'r') as file:
            for line in file:
                line=line.strip()
                if line:
                    words=[]
                    for x in line.split():
                        words.append(x)
                    testList.append(words)
    except FileNotFoundError:
        print(f"File {path} non trovato")
    return testList
        

if __name__ == "__main__":

    testList = readTestFile("./test_lcp.txt")

    for test in testList: 
        
        result = findLCP(test, 0, len(test) - 1) #trovo il prefisso comune più lungo
        print(f"il prefisso comune di {test} è '{result}'")