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
                    numbers = [x for x in line.split()]
                    testList.append(numbers)
    except FileNotFoundError:
        print(f"File {path} non trovato")
    return testList

if __name__ == "__main__":
    testList = readTestFile("./test_interrail.txt")
    
    i = 0
    
    for test in testList:
        seq1 = list(testList[i][0])
        i += 1
        if '#' in seq1:
                i=0
                break
        seq2 = list(testList[i][0])
        i += 1

        print(f"Caso {seq1,seq2}: numero massimo = {LCS(seq1, seq2)}")
        