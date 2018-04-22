#!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 05 question 1
since   : Friday-27-04-2018
"""

def gauss_legendre(debug=True):
    pass

def gauss_chebyshev(debug=True):
    pass

if __name__ == "__main__":
    from scipy import (integrate, special)
    from math import (sqrt, exp)

    I = lambda x : exp(x) / sqrt(1 - x**2)
    exact_I = integrate.quad(I, -1, 1)[0]
    print exact_I

else:
    from sys import exit
    exit("USAGE: python question1.py")
