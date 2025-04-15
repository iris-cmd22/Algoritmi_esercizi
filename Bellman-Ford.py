#Es. da https://www.geeksforgeeks.org/bellman-ford-algorithm-in-python/

#Iniziamo definendo un grafo
graph = {
    'A':{'B':-1, 'C': 4},
    'B':{'C':3, 'D': 2, 'E':2},
    'C':{},
    'D':{'B':1, 'C': 5},
    'E':{'D': -3},
    }
source='A'

###
###

def bellman_ford(graph,source):
    
    #Step 1: Inizializziamo le distanze da tutti i vertici come infinite
    distances ={vertex: float('inf') for vertex in graph}
    #e la distanza dal vertice di origine come 0
    distances[source]=0
    
    #Step 2: Rilassiamo tutti gli archi |V|-1 volte
    for _ in range (len(graph)-1):
        for u in graph:
            #per ogni arco appartenente al grafo
            for v,weight in graph[u].items():
            #Operazione di rilassamento per un arco (u,v)
            #consiste nel confrontare il costo precedentemente assegnata a v
            #con quella di u + il costo dell'arco (u,v)
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    #se il secondo è minore aggiorno v.d
                    distances[v]=distances[u]+weight
    
    #Step 3: Verifichiammo che non ci siano cicli negativi
    for u in graph:
        for v,weight in graph[u].items():
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                raise ValueError("IL grafo contiene un ciclo negativo")
    return distances

shortest_distances = bellman_ford(graph,source)
print(shortest_distances)