"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot have negative number")
    return math.sqrt(a)
   
def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b
    
def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
   
def logarithm(a, b):
    if b <= 0:
        raise ValueError("Cannot take logarithm of negative number")
    if a == 1 or a <= 0:
        raise ValueError("Cannot take logarithm of base 1, 0, or negative")
    return math.log(b, a)
   
def exponent(a, b):
    return a ** b
    
