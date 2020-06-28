# EulerNumber
A code that accurately calculates Euler's number (e) to any number of digits

<pre><code class="python">
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
    ...
</pre></code>
