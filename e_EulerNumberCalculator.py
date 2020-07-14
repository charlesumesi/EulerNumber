# -*- coding: utf-8 -*-
"""
Created on 9 Feb 2020; edited on 23 June 2020
Name: e_EulerNumberCalculator.py
Purpose: Calculates the value of Euler's number (e) to a desired level of accuracy
Algorithm: Binary Splittng Method
@author: Charles Umesi (charlesumesi)
"""

from decimal import Decimal as Dec, getcontext as gc

def factorial(n):   # Factorial function Will be required in the e_Calculator function
    if not n:
        return 1
    return n*factorial(n-1)

def e_Calculator():
    
    print("'e' (Euler's number) Calculator")
    digits = int(input('Enter the number of digits you want for your value of e : '))
    steps = int(input('Enter the maximum number of steps desired (if unsure, enter 500) : '))
    prec = 3*digits
    gc().prec = prec
    maxSteps = steps  # You should stop when k! > 10^n
                      # See Gourdon & Sebah (2001) Mathematical constants and computation, Jan 11
    s = 1
    
    for k in range(1,maxSteps+1):
        numerator = 1
        denominator = factorial(k)
        s += Dec(1)/factorial(k) # Note, if you do Dec(1/factorial(k)), your answer will diverge after the 16th decimal place
   
    e = s
    e = Dec(str(e)[:digits+1]) # Drop few digits of precision for accuracy
    print(f'Your value for e = {e}')
    print('\nThe value obtained should not diverge from http://www.numberworld.org/digits/E/ or other reference value.')
    print('But if it does, then you must increase the number of steps.')
    print('However, increasing the number of digits or steps comes at the cost of processor power.')
    
if __name__ == '__main__':
    e_Calculator()
