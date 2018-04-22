#!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 05 question 1
since   : Friday-27-04-2018
"""

def computing_with_fejer():
    pass

def computing_with_gauss():
    pass

if __name__ == "__main__":
    from math import exp
    from fejer import fejer
    from gauss import gauss
    from scipy import integrate

    f = lambda x : exp(x)
    I = integrate.quad(f, 0.0, 1.0)[0]


else:
    from sys import exit
    exit("USAGE: python question1.py")
