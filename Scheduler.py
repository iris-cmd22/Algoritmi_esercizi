
def max_beneficio_jobs(jobs):
    if not jobs:
        return 0
        
    N = len(jobs)
    DP = [0] * N
    # Il primo job può sempre essere preso
    DP[0] = jobs[0][2]  # beneficio del primo job
    
    # Per ogni job successivo
    for i in range(1, N):
        # Prendiamo almeno il beneficio del job corrente
        DP[i] = jobs[i][2]
        
        # Controlliamo tutti i job precedenti
        for j in range(i):
            # Se non c'è sovrapposizione, possiamo aggiungere i alla soluzione di j
            if (jobs[i][1] <= jobs[j][0] or jobs[j][1] <= jobs[i][0]):
                DP[i] = max(DP[i], DP[j] + jobs[i][2])
    
    return max(DP)


def readTestFile(path):
    testList = []
    try:
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    numbers = []
                    for x in line.split():
                        numbers.append(int(x))
                    testList.append(numbers)
    except FileNotFoundError:
        print(f"File {path} non trovato")
    return testList


if __name__ == "__main__":
    testList = readTestFile("./test_scheduler.txt")
    print(testList)
    jobs=[]
    for test in testList:
        start, end, beneficio = map(int, test)
        jobs.append((start, end, beneficio))
    risultato = max_beneficio_jobs(jobs)
    print(risultato)
