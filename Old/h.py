# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 09:44:36 2020

@author: lenovo
"""

    
num=91
def Isprime(numb):
    if(numb<2):
        return False
    for i in range(2,numb):
        if (numb%i==0):
             return False
    return True





      
def Sum_of_digits1(num):
  sum1=0
  while(num>0):
      
      rema=num%10
      sum1=sum1+rema
      num=num//10
  return sum1
def sumdigits (num):
    return 10
a=sumdigits(num)


sum1=Sum_of_digits1(num) 
print(sum1)
if sum1==10 and Isprime(num):
    print(num,"true")
else:
    print(num,"false")    
    





    
    
