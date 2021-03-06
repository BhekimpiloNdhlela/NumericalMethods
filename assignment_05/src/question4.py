#!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 05 question 1
since   : Friday-27-04-2018
"""

def computing_with_gauss(f, n=5.0):
    X, C = gauss(int(n), [0, 1])
    return  sum([float(c) * f(float(x)) for x, c in zip(X, C)])

def computing_with_fejer(f, n=5.0):
    X, C = fejer(int(n), [0, 1])
    return sum([float(c) * f(float(x)) for x, c in zip(X, C)])

def abs_error(xc, x):
    return abs(float(xc) - float(x))

if __name__ == "__main__":
    from math import exp
    from fejer import fejer
    from gauss import gauss
    from scipy import integrate

    f = lambda x : exp(x)
    I = integrate.quad(f, 0.0, 1.0)[0]

    gauss_I, fejer_I = computing_with_gauss(f),  computing_with_fejer(f)
    abs_err_gauss, abs_err_fejer = abs_error(gauss_I, I), abs_error(fejer_I, I)

    debug = True
    if debug == True:
        print("Debug Mode Status: <ON>")
        print("exact_I = {:.20f}".format(float(I)))
        print"gauss_I = {:.20f}".format(float(gauss_I)), "\t",
        print"abs_err_gauss = {:.20f}".format(float(abs_err_gauss))
        print"fejer_I = {:.20f}".format(float(fejer_I)), "\t",
        print"abs_err_fejer = {:.20f}".format(float(abs_err_fejer))
    else:
        print("Debug Mode Status: <OFF>")
else:
    from sys import exit
    exit("USAGE: python question1.py")
