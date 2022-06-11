# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 18:13:16 2022

@author: Amdy Moustapha
"""

"calcul de puissance"
 

def puissance(n):
    if n==0:
        return 1
    else:
        return x*puissance(n-1)

n= int(input("saisir n: "))
x= int(input("saisir x: "))
print("le resultat de la puissance de x^n est: ",x*puissance(n-1))        
    