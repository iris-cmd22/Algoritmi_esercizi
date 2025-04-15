#ESEMPI DI BACKTRACKING
'''Sia data una matrice di N x M numeri interi positivi. Si implementi un algoritmo di backtracking per determinare la lunghezza della più lunga sequenza di numeri adiacenti strettamente crescenti (un numero x è adiacente ad y si trova in alto, in alto a destra, in alto a sinistra, a destra, a sinistra, in basso, in basso a destra, in basso a sinistra rispetto ad y).
Si alleghi al PDF un file editabile riportante l’implementazione in un linguaggio a scelta, corredato da almeno tre casi di test con il corrispondente output atteso
'''
#Costruzione subsets
def Is_a_solution(A,k,n):
  return (k==n)

def Compute_Candidates(A,k,n):
  c=[True, False]
  return c

def process_solution(A,k):
  print('\n{')
  for i in k:
    if(A[i]==True):
        print("%d",i)
  print('}')

#Istanziamo quindi la main routine con la chiamata a backtrack con gli argomenti giusti
def generate_subsets(n):
  A=[0]*n
  Backtrack(A,0,n)
  return A

#Codice base
def Backtrack(A,k,input):
    
  if (Is_a_solution(A,k,input)):  #Sono sono arrivata alla soluzione?
    process_solution(A,k)
  else              :              #Estendo la mia soluzione parziale
    k=k+1
    c=Compute_Candidates(A,k,input)
    for i in len(c):
      A[k]=c[i]
      #Make_Move(A,k,input)        #Provo una configurazione raggiungibile
      Backtrack(A,k,input) #Verifico se è soluzione
      #Unmake_Move(A,k,input)      #Se torno dal backtracking non è una soluzione


  def readTestFile(path):
    pass
if __name__=="__main__":
    testList=readTestFile("./test_backtracking.txt")