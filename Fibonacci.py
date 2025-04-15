#FIBONACCI 
#Realizzeremo questo algoritmo con 3 approcci differenti:
#   -Memoization
#       è un approccio "top-down": dal main case ai casi base
#       In questo caso vorrei non ricalcolare risultati che abbiamo già calcolato, 
#       ma salvarli in modo da accedervi direttamente

def fibonacci_memo(n,dp):
    #Definiamo i valori per il caso base 
    #(per 0 e 1 ho 0 e 1 rispettivamente)
    if n<=1:
        return n

    #Prima di calcolare la risposta per un dato input, 
    # verifichiamo di non averla già calcolata
    if dp[n] != -1:
        return dp[n]
    #se non lo trovo lo calcolo usando la relazione ricorsiva, 
    # ma prima di restituirla la salvo in dp[n]
    dp[n]=fibonacci_memo(n-1,dp)+fibonacci_memo(n-2,dp)
    return dp[n]

#   -Tabulation
#       è un approccio "bottom up": risolvo i casi base per risolvere il main case

def fibonacci_tab(n):
    #Inizializzo un array di dim n+1
    dp=[-1] * (n+1)
    
    #Definiamo i valori per il caso base 
    #(per 0 e 1 ho 0 e 1 rispettivamente)
    dp[0]=0
    dp[1]=1
    
    #usiamo un ciclo iterativo che attraversa l'array e 
    # per ogni valore calcola la funzione ricorsiva
    for i in range(2,n+1):
        dp[i]=dp[i-1] + dp[i-2]
    
    print (dp[n])
    
#   -Space Optimization
    
if __name__=="__main__":
    for n in range(0,20):
        #Inizializzo un array di dim n+1
        dp_memo=[-1] * (n+1)
        print(fibonacci_memo(n,dp_memo))
    
    for n in range(2,20):
            fibonacci_tab(n)
    