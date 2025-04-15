
def Traghetti(N_auto, T, orari_arrivo):
    """
    Calcola tempo minimo e numero minimo di viaggi per trasportare auto.

    Args:
        N_auto: Capacità del traghetto.
        T: Tempo di attraversamento (solo andata).
        orari_arrivo: Lista degli orari di arrivo delle auto.

    Returns:
        Tupla (numero viaggi, tempo minimo), o (-1, -1) se input non valido.
    """
    m = len(orari_arrivo)

    # Inizializzazione 
    dp = [float('inf')] * (m + 1)
    viaggi = [float('inf')] * (m + 1)

    #Caso base
    dp[0] = 0
    viaggi[0] = 0

    for i in range(1, m + 1):  # Considera le prime i auto
        for j in range(1, min(i + 1, N_auto + 1)):  # Auto caricate in QUESTO viaggio
            tempo_partenza = 0
            if i - j > 0:
                tempo_partenza = dp[i - j] #ultima partenza

            #devo considerare il massimo fra quando sono partito e quando arriva la prossima auto
            tempo_partenza = max(tempo_partenza, orari_arrivo[i - 1]) 
            tempo_totale_corrente = tempo_partenza + T #solo andata

            #Se avevo considerato un tempo maggiore
            if dp[i] > tempo_totale_corrente:
                dp[i] = tempo_totale_corrente #lo aggiorno
                viaggi[i] = viaggi[i - j] + 1 #aggiorno la scelta di partire o meno
            elif dp[i] == tempo_totale_corrente: #Se il tempo è lo stesso
                viaggi[i] = min(viaggi[i], viaggi[i - j] + 1) #verifico la scelat migliore a parità di tempo

    return viaggi[m], dp[m] #Restituisce il tempo di arrivo dell'ultima auto


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
    testList = readTestFile("./test_traghetti.txt")

    T_test = testList[0][0]
    i = 1
    for _ in range(T_test):
        N = testList[i][0]
        T_viaggio = testList[i][1]
        M = testList[i][2]
        i += 1
        orari = []
        for j in range(M):
            orari.append(testList[i + j][0])
        i += M
        risultato = Traghetti(N, T_viaggio, orari)
        print(risultato)