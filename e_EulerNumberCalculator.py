# -*- coding: utf-8 -*-
"""
Created on 9 Feb 2020; edited on 23 June 2020

@author: Charles Umesi
"""

from decimal import Decimal as Dec, getcontext as gc

def factorial(n):   # Factorial function Will be required in the e_Calculator function
    if not n:
        return 1
    return n*factorial(n-1)

def e_Calculator():
    """Based on the Binary Splittng Method"""
    print("'e' (Euler's number) Calculator")
    prec = 100
    gc().prec = prec
    digits = int(input('Enter the number of digits you want for your value of e : '))
    maxSteps = 1000  # You should stop when k! > 10^n
                     # See Gourdon & Sebah (2001) Mathematical constants and computation, Jan 11
    s = 1
    
    for k in range(1,maxSteps+1):
        numerator = 1
        denominator = factorial(k)
        s += Dec(1)/factorial(k) # Note, if you do Dec(1/factorial(k)), your answer will diverge after the 16th decimal place
   
    e = s
    e = Dec(str(e)[:digits+1]) # Drop few digits of precision for accuracy
    print(f'Your value for e = {e}')
    
if __name__ == '__main__':
    e_Calculator()

# The value should not diverge from http://www.numberworld.org/digits/E/
# If however it does diverge, increase prec or maxSteps
# If you can't get past a certain number of digits, increase prec
# WARNING: Increasing prec or maxSteps comes at the cost of processor power!