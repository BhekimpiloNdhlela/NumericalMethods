#!usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 05 question 1
since   : Friday-27-04-2018
"""


# **************************************************************** #
# global variables I = exp(1) - 1, and M = [11, 21, 31, ..., 101]
from math import exp as e
from numpy import linspace
I = e(1) - 1
M = linspace(11.0, 101.0, 10)
f = lambda x : e(x)
# **************************************************************** #

def composite_midpoint(f, m, a=0.0, b=1.0):
    h, result = (b - a) / m, 0.0
    for i in xrange(1, int(m) + 1):
        result += f((a + h/2.0) + i*h)
    return result * h

if __name__ == "__main__":
    from numpy import (abs, array, linspace)
    import matplotlib.pyplot as plt

    res = [abs(composite_midpoint(f, int(m)) - I) for m in M]


    plt.plot(res, M, 'b-')
    plt.show()
    print res
else:
    from sys import exit
    exit("USAGE: python question1.py")
