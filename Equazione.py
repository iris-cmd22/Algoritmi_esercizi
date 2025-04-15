import math 

def Equazione(input):
    
    p=input[0]
    q=input[1]
    r=input[2]
    s=input[3]
    t=input[4]
    u=input[5]

    def f(x):
        return p * math.exp(-x) + q * math.sin(x) + r * math.cos(x) + s * math.tan(x) + t * x**2 + u
    
    a, b = 0, 1  # intervallo [0,1]
    if f(a) * f(b) > 0:
        return None
    
    for _ in range(50):  # numero fisso di iterazioni
        x = (a + b) / 2
        
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

    ''' Bisezione, cerco qualcoa che si avvicini a 0
    * f(a)              
    |      \
----+-------\----+-----→ x
    |         \  |
    |          \ |
    |           \|
    |            * f(b)'''
    return round((a + b) / 2,4)

def readTestFile(path):
    testlist=[]

    try:
        with open(path,'r') as file:

            for line in file:
                line=line.strip()
                if line:
                    numbers=[]
                    try:
                        for x in line.split():
                            numbers.append(int(x))
                    except ValueError:
                        print(f"Devi inserire un int")
                    testlist.append(numbers)

    except FileNotFoundError:
        print(f"Non ho trovato il file {path}")

    return testlist


if __name__=="__main__":
    testlist=readTestFile("./test_equazione.txt")

    for test in testlist:
        print(f"Per i valori di p, q, r, s, t ed u {test} il risultato di p∗e^−x + q∗sin(x) + r∗cos(x) + s∗tan(x) + t∗x^2  + u = 0 è {Equazione(test)}")


    