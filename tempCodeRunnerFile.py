def LCS(s1, s2):
    # Corretto la creazione della matrice dp
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    
    # I casi base sono già gestiti dalla matrice inizializzata a 0
    
    # Tabulation - corretto gli indici
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[len(s1)][len(s2)]

def readTestFile(path):
    testList = []
    try:
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    numbers = [int(x) for x in line.split()]
                    testList.append(numbers)
    except FileNotFoundError:
        print(f"File {path} non trovato")
    return testList

if __name__ == "__main__":
    testList = readTestFile("./test_lcs.txt")
    
    n_test = testList[0][0]
    i = 1
    
    for _ in range(n_test):
        n = testList[i][0]  # numero di sequenze
        i += 1
        
        ref = testList[i]  # sequenza di riferimento
        print("Data la sequenza di riferimento:", ref)
        i += 1
        
        # Processa le n sequenze successive
        for _ in range(n):
            seq = testList[i]
            print(f"La sottosequenza più lunga per {seq} è di {LCS(ref, seq)} elementi")
            i += 1