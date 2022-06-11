# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 11:55:18 2022

@author: Amdy Moustapha
"""
"suite de FIBONACCI"

"Algorithme"

"""def FIBONACCI(ntermes):
    ntermes = int(input("Entrez un nombre: ")) 
    n1=0
    n2= 1 

    for i in range(n1,ntermes): 

        TS = n1+n2 
        n1=n2
        n2=TS
        print(TS)"""

def fibonacci(ntermes):
    if ntermes <= 1 :
        return ntermes
    
    return(fibonacci(ntermes - 1) + fibonacci(ntermes - 2))


ntermes = int(input("Entrez un nombre: "))
print("la suite de fibonacci de ntermes est: ",fibonacci(ntermes))