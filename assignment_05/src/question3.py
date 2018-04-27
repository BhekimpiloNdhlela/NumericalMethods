#!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 05 question 3
since   : Friday-27-04-2018
"""

def question_b(f0, f1, debug=True):
    r0, r1 = romberg(f0, 0.0, 1.0, 5), romberg(f1, 0.0, 1.0, 5)
    if debug == True:
        print "Debug Mode: [ON] Question 3(b)\n"
        debug_message = "Romberg results For Function in Problem 1 :"
        debug_on(r0, debug_message)
        debug_message = "\nRomberg results For Function in Problem 2 :"
        debug_on(r1, debug_message)
    else:
        print("Debug Mode: [OFF] Question 3(b)")
    return r0, r1

def question_c(r0, r1, f0, f1, N=5, debug=True):
    I0, I1 = integrate.quad(f0, 0.0, 1.0)[0], integrate.quad(f1, 0.0, 1.0)[0]
    e0, e1 = romberg_abs_error(r0, I0), romberg_abs_error(r1, I1)
    if debug == True:
        print "Debug Mode: [ON] Question 3(b)\n"
        debug_message = "Romberg Error results For Function in Problem 1 :"
        debug_on(e0, debug_message)
        debug_message = "\nRomberg Error results For Function in Problem 2 :"
        debug_on(e1, debug_message)
    else:
        print("Debug Mode: [OFF] Question 3(b)")
    return e0, e1

def romberg_abs_error(r, I):
    e = zeros((len(r), len(r)))
    for i in xrange(0, len(e)):
        for j in xrange(0, len(e)):
            if r[i][j] == 0.0:
                continue
            else:
                e[i][j] = abs(r[i][j] - I)
    return e

def debug_on(matrix, debug_message):
    print(debug_message)
    for row in matrix:
        print "[",
        for element in row:
            print "{:.15f}   ".format(element),
        print("]")

if __name__ == "__main__":
    from romberg import romberg
    import matplotlib.pyplot as plt
    from math import (exp, pi, sin)
    from scipy import (integrate, special)
    from numpy import (abs, array, linspace, zeros)

    f0, f1 = lambda x : exp(x), lambda x : exp(sin(2 * pi * x))
    r0, r1 = question_b(f0, f1)
    e0, e1 = question_c(r0, r1, f0, f1)
else:
    from sys import exit
    exit("USAGE: python question3.py")
