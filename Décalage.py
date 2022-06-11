# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:29:39 2022

@author: Amdy Moustapha
"""
"Décalage"
import random
def decaleCircdriote():
    n= int(input("choissez la taille de votre tableau: "))
    tb=[random.randint(1,10) for i in range(n)]
    for i in range(0,n-1):
        tp=tb[0]
        for j in range(i+1,n+1):
            tb[j]=tb[j+1]
            tb[n+1]=tp
        print(tb)
print(decaleCircdriote())
