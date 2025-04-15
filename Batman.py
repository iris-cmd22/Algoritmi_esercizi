
def Sequence_check(seq1,seq2,m_list):
    see=True
    for i in range(len(m_list)):
        print(seq1,seq2,m_list[i][1:])
        if (seq1 in m_list[i][1:]) and (seq2 in m_list[i][1:]):
            see=False
    print("fine sequence check",see)
    return see

def daltonia(m_list,colori):
    
    #Funzione ricorsiva
    def dfs(start,end):

        nonlocal n_col

        #Caso base
        if start==end:
            return colori[start]
        
        #Calcolo mediana
        m=(end+start)//2
        print(m)
        dfs(start,m)
        dfs(m+1,end)

        if(Sequence_check(colori[m],colori[m+1],m_list)):
            n_col+=1
    
    n_col=1
    dfs(0,len(colori)-1)

    return n_col

def readTestFile(path):
    testList=[]
    try:
        with open(path,'r') as file:
            for line in file:
                line=line.strip()
                if line:
                    numbers=[]
                    for x in line.split():
                        try:
                            if (int(x)<0):
                                raise ValueError
                            numbers.append(int(x))
                        except ValueError:
                            print(f"Errore alla riga {line.split()}:{x}. Deve essere un intero e positivo!")
                    testList.append(numbers)
    except FileNotFoundError:
        print(f"File {path} non trovato")
    return testList

if __name__=="__main__":
    testList=readTestFile("./test_batman.txt")
    T=testList[0][0]
    i=1

    for test in range(T):
        print(testList[i])
        N,M,L=testList[i]
        i+=1
        print(testList[i:i+M])
        m_list=testList[i:i+M]
        i+=M
        colori=testList[i]
        i+=1
        
        print(f"Della stringa di colori {colori}, Batmat risce a riconoscere {daltonia(m_list,colori)} segmento")


        