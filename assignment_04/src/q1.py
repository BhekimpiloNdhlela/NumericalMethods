#!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 04 question 1 (a. to b.)
since   : Friday-23-03-2018
"""
def question_a(debug=True):
    # need to add the error term to the anonymous function (c_ddx)
    c_ddx   = lambda x, h : ((-fx(x+2*h)+8*f(x+h)-8*f(x-h) + f(x-2*h))/(12*h))
    e_ddx   = lambda x    : -cos(x) / (sqrt(1 - 2 * sin(x)))
    fx      = lambda x    : sqrt(1 - 2 * sin(x))
    abs_err = lambda xc, x: abs(xc - x)

def question_b(debug=True):
    pass

if __name__ == "__main__":
    from numpy import abs, cos, sin, sqrt
    question_a()

else:
    from sys import exit
    exit("USAGE: python q1.py")
