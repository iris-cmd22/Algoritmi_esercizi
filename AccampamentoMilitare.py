#Pattern LIS
def dp(A, n, index, prev, memo):
    # Caso base:
    if index == n:
        return 0

    # Memo
    if memo[index][prev + 1] != -1:
        return memo[index][prev + 1]

    not_take = dp(A, n, index + 1, prev, memo)

    take = 0
    #Se aumenta la aggiungo
    if prev == -1 or A[index][1] > A[prev][1]: 
        take = 1 + dp(A, n, index + 1, index, memo)

    memo[index][prev + 1] = max(take, not_take)
    return memo[index][prev + 1]


def Max_collegamenti(N, X, Y):
    # Creiamo la lista di tuple XY
    XY = [(X[i], Y[i]) for i in range(N)]

    # Ordiniamo le tuple per la prima coordinata (x)
    XY.sort(key=lambda t: t[0])

    # Calcoliamo la lunghezza di XY
    n = len(XY)

    # Inizializziamo la tabella memo
    memo = [[-1 for _ in range(n + 1)] for _ in range(n)]

    # Troviamo la lunghezza massima della sottosequenza
    max_length = dp(XY, n, 0, -1, memo)

    # Ricostruiamo la soluzione
    solution = []
    prev = -1
    for i in range(n):
        if prev == -1 or XY[i][1] > XY[prev][1]:
            if dp(XY, n, i + 1, i, memo) + 1 == dp(XY, n, i, prev, memo):
                solution.append(XY[i])
                prev = i

    return max_length, solution


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
    testList = readTestFile("./test_accampamento.txt")

    T = testList[0][0]
    i = 1
    # Per ogni caso di test
    for _ in range(T):
        # Leggiamo N
        N = testList[i][0]
        i += 1
        # Leggiamo i vettori X e Y
        X = testList[i]
        Y = testList[i + 1]
        i += 2

        # Troviamo e stampiamo la soluzione
        risultato = Max_collegamenti(N, X, Y)
        print(risultato)
