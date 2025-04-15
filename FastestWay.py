def fastest_way(processing_time, transfer_time, entry_time, exit_time, n):
    """Trova il percorso più veloce in una catena di montaggio.

    Args:
        processing_time: Matrice dei tempi di lavorazione su ciascuna linea.
        transfer_time: Matrice dei tempi di trasferimento tra le linee.
        entry_time: Tempi di entrata sulle due linee.
        exit_time: Tempi di uscita dalle due linee.
        n: Numero di stazioni.

    Returns:
        Tuple contenente il tempo minimo e il percorso ottimale.
    """

    f1 = [0] * n
    f2 = [0] * n
    l1 = [0] * n
    l2 = [0] * n

    # Inizializza i tempi per la prima stazione
    f1[0] = entry_time[0] + processing_time[0][0]
    f2[0] = entry_time[1] + processing_time[1][0]

    # Calcola i tempi minimi e i percorsi per le stazioni successive
    for j in range(1, n):
        # Calcola il tempo minimo per arrivare alla stazione j sulla linea 1
        if f1[j-1] <= f2[j-1] + transfer_time[1][j-1]:
            f1[j] = f1[j-1] + processing_time[0][j]
            l1[j] = 1
        else:
            f1[j] = f2[j-1] + transfer_time[1][j-1] + processing_time[0][j]
            l1[j] = 2

        # Calcola il tempo minimo per arrivare alla stazione j sulla linea 2
        if f2[j-1] <= f1[j-1] + transfer_time[0][j-1]:
            f2[j] = f2[j-1] + processing_time[1][j]
            l2[j] = 2
        else:
            f2[j] = f1[j-1] + transfer_time[0][j-1] + processing_time[1][j]
            l2[j] = 1

    # Determina il percorso finale e il tempo minimo
    if f1[n-1] + exit_time[0] <= f2[n-1] + exit_time[1]:
        min_time = f1[n-1] + exit_time[0]
        last_line = 1
    else:
        min_time = f2[n-1] + exit_time[1]
        last_line = 2

    # Ricostruisci il percorso
    path = [last_line]
    for j in range(n-2, 0, -1):
        path.append(l1[j] if last_line == 1 else l2[j])
    path.reverse()

    return min_time, path

# Esempi di utilizzo
if __name__ == "__main__":
    A = [[2, 3, 5, 7, 9, 2], [7, 4, 8, 3, 6, 7]]
    t = [[1, 2, 3, 2, 1], [3, 2, 1, 2, 3]]
    e = [1, 0]
    x = [1, 2]
    n = 6

    min_time, path = fastest_way(A, t, e, x, n)
    print("Tempo minimo:", min_time)
    print("Percorso ottimale:", path)  # Es: [1, 2, 1, 2, 1]