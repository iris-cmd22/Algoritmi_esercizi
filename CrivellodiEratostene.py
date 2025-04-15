def Crivello(n):
    prime = [True for _ in range(n+2)]
    i=2
    while (i*i<= n):
        if(prime[i]==True):
            #Marchiamo come falsi tutti i multipli di i
            for j in range(i*i,n+1,i):
                    prime[j]=False

        i+=1
        
    primes=[]
    primes.append(1)
    for i in range(len(prime)):
        if(prime[i]):
            primes.append(i)
    return primes