"Lancer de dés"
import random
"""
def simul1():
    d1= random.randint(1,6)
    d2= random.randint(1,6)
    S=d1+d2
    print("d1",d1)
    print("d2",d2)
    print("resultat ",S)
print(simul1())
  """  
    

def simul2():
    S=0
    n= int(input("choisisez le nombre de d�s que vous volais lancer" ,))
    dn=[random.randint(1,n) for i in range(n)]
    print(dn)
    for i in range(n):
        S=S+dn[i]
    print("le resultat est ",S)
print(simul2())
