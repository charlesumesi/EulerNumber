# EulerNumber
A Python code that accurately calculates Euler's number (e) to any number of digits
```python
from decimal import Decimal as Dec, getcontext as gc

def factorial(n):   # Factorial function Will be required in the e_Calculator function
    if not n:
        return 1
    return n*factorial(n-1)

def e_Calculator():
    
    print("'e' (Euler's number) Calculator")
    digits = int(input('Enter the number of digits you want for your value of e : '))
    steps = int(input('Enter the maximum number of steps desired (if unsure, enter 500) : '))
    ...
```
