"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a==0:
        raise ZeroDivisionError
    return b/a
def log(a,b):
    if b <= 0 or a <= 0 or a == 1:
        raise ValueError
    return math.log(b,a)
def exp(a,b):
    return a**b
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def logarithm(a, b):
    if b <= 0:
        raise ValueError("Cannot take logarithm of negative number")
    if a == 1 or a <= 0:
        raise ValueError("Cannot take logarithm of base 1, 0, or negative")
    return math.log(b, a)

def exponent(a, b):
    return a ** b

