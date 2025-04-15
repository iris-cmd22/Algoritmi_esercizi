def min_segments_to_cover(segments, M):
    if not segments or M <= 0:
        return -1
    
    # Ordina i segmenti per punto di inizio
    segments.sort()
    
    if segments[0][0] > 0:  # Non possiamo coprire dall'inizio
        return -1
        
    current_end = 0     # Fine della copertura corrente
    selected = []       # Segmenti selezionati
    i = 0              # Indice segmento corrente
    best_end = 0       # Miglior punto di fine raggiungibile
    best_segment = None # Miglior segmento per estendere la copertura
    
    while current_end < M and i < len(segments):
        # Cerca il segmento che si estende più a destra
        # tra quelli che iniziano prima di current_end
        while i < len(segments) and segments[i][0] <= current_end:
            if segments[i][1] > best_end:
                best_end = segments[i][1]
                best_segment = segments[i]
            i += 1
            
        if best_segment is None:
            return -1  # Non possiamo procedere
            
        selected.append(best_segment)
        current_end = best_end
        best_end = current_end
        best_segment = None
        
    return selected if current_end >= M else -1



#Funzione di lettura da file
def readTestFile(path):
    try: 
        testsList = []
        with open(path, 'r') as file:
            for line in file:
                line = line.strip() #così tolgo gli spazi
                if line:
                    numbers=[]
                    for x in line.split():
                        try:
                            numbers.append(int(x))
                        except ValueError:
                            print(f"Errore alla riga {line.strip()}: '{x}'. Devi inserire numeri interi!")
                            break #Analizzo solo i caratteri corretti
                    testsList.append(numbers)
    except FileNotFoundError:
        print(f"File {path} non trovato.")
    
    return testsList

if __name__== "__main__":
    
    testsList = readTestFile(path="./test_coverseq.txt")

    M=testsList[0][0]
    segments=testsList[1:]

    result = min_segments_to_cover(segments, M)
    if result != -1:
        print(f"Numero minimo di segmenti: {len(result)}")
        print("Segmenti selezionati:", result)
    else:
        print("Impossibile coprire l'intervallo")
    

