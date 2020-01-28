# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:56:07 2020

@author: lenovo
"""
no=73
def Isprime(numb):
    if(numb<2):
        return False
    for i in range(2,numb):
        if (numb%i==0):
             return False
    return True

#Please implement using arithmetic fashion
def sumdigits (numb):
    return 10




if Isprime(no) and sumdigits(no)==10 :
    print(no," true")
else:
    print(no," false")
    
