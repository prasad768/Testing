# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 20:35:31 2020

@author: lenovo
"""


def Sum_of_digits1(num):
  sum1=0
  while(num>0):
      rema=num%10
      sum1=sum1+rema
      num=num//10
  return sum1
def sumdigits (num):
    return 10

num=345
sum1=Sum_of_digits1(num) 
if sum1==10:
    print("true")
else:
    print("false")    
    

