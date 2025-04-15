import numpy as np

def MattiPerLaSpesa(budget, product_options):
    n = len(product_options)
    # Ogni cella conterrà una tupla: (costo, vettore booleano)
    dp = [[(float('inf'), [False] * n) for _ in range(budget + 1)] for _ in range(n + 1)]

    # CASO BASE: Con un budget di 0, non si prende niente
    for i in range(n + 1):
        dp[i][0] = (0, [False] * n)

    for i in range(1, n + 1):  # Per ogni prodotto
        for j in range(budget + 1):  # Per ogni budget possibile
            # Non prendere il prodotto i-1
            dp[i][j] = dp[i - 1][j]
            
            # Considerare tutte le opzioni per il prodotto i-1
            for option in product_options[i - 1]:
                if option <= j:  # Se l'opzione rientra nel budget
                    prev_cost, prev_taken = dp[i - 1][j - option]
                    new_cost = prev_cost + option
                    new_taken = prev_taken[:]
                    new_taken[i - 1] = True
                    
                    # Prendere il minimo costo tra la scelta attuale e quella precedente
                    if new_cost < dp[i][j][0]:
                        dp[i][j] = (new_cost, new_taken)

    # Ricerca del massimo costo che permette di acquistare tutti i prodotti
    max_cost = -1
    for j in range(budget + 1):
        cost, taken = dp[n][j]
        if cost != float('inf') and all(taken):
            max_cost = max(max_cost, j)

    # Verifica se è possibile acquistare tutti i prodotti
    if max_cost == -1:
        return float('inf')  # Denaro insufficiente

    # Per visualizzare la matrice (opzionale)
    print("Struttura [prodotti x budget]:")
    for i in range(n + 1):
        print([dp[i][j][0] for j in range(budget + 1)])

    return max_cost

def readTestFile(path):
    testList = []
    try:
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    numbers = list(map(int, line.split()))
                    testList.append(numbers)
    except FileNotFoundError:
        print(f"File {path} non trovato")
    return testList

if __name__ == "__main__":
    testList = readTestFile("./test_spesa.txt")
    
    i = 0
    for test in range(testList[0][0]):
        B = testList[i + 1][0]
        C = testList[i + 1][1]
        prods = testList[i + 2:C + i + 2]
        prods = [sublist[1:] for sublist in prods]

        i += (C + 1)
        print(f"Budget: {B}, Prodotti: {C}, Opzioni: {prods}")

        result = MattiPerLaSpesa(B, prods)
        if result != float('inf'):
            print(f"Con {B}$ si possono spendere al massimo {result}$ per comprare tutti i prodotti.")
        else:
            print(f"Con {B}$: denaro insufficiente")
