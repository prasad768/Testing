# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 20:35:31 2020

@author: lenovo
"""

num=64  
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
if sum1==a:
    print(num,"true")
else:
    print(num,"false")    
    

