# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 17:19:33 2022

@author: Amdy Moustapha
"""

"Factriel"

def factoriel(n):
    if n==0:
        return 1
    else:
        return n*factoriel(n-1)

n= int(input("saisir un nombre n ",))    
print("la factoriel de n est : ",factoriel(n))
    
