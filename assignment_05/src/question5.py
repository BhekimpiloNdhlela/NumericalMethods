#!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 05 question 1
since   : Friday-27-04-2018
"""

from scipy import (integrate, special)
from math import (sqrt, exp, cos, pi)
from gauss import gauss

def gauss_legendre(n=5.0):
    X, C = gauss(5, [-1, 1])
    f = lambda x : exp(x) / sqrt(1 - x**2)
    return sum([f(float(x)) * float(c) for x, c in zip(X, C)])

def gauss_chebyshev(n=5.0):
    X = [cos(((2.0 * i - 1) * pi) / (2 * n)) for i in xrange(1, int(n + 1))]
    return (pi * (sum([exp(x) for x in X]))) / n

if __name__ == "__main__":
    exact_integral = integrate.quad(lambda x : exp(x) / sqrt(1 - x**2), -1, 1)[0]
    gauss_chebyshev, gause_legendre = gauss_chebyshev(), gauss_legendre()

    debug = True
    if debug == True:
        print("Debug Mode Status: <ON>")
        print("Exact Integral  = {:.20f}".format(float(exact_integral)))
        print("Gauss Chebyshev = {:.20f}".format(float(gauss_chebyshev)))
        print("Gauss Legendre  = {:.20f}".format(float(gause_legendre)))
else:
    from sys import exit
    exit("USAGE: python question1.py")
