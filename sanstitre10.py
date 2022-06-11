# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 13:06:48 2022

@author: Amdy Moustapha
"""

"convertion binaire decimal"
def bin2Dec(b):
    b1 = b
    dec, i, n = 0, 0, 0
    while(b != 0): 
        deci = b % 10
        dec = dec + deci * pow(2, i) 
        b= b//10
        i += 1
    print(dec)  
    
test=int(input("entrer un nombre binaire: "))
    
    
    
"""def decimalToBinary(n):  
    if(n > 1):  
        
        decimalToBinary(n//2)  
    print(n%2, end=' ') 
    """