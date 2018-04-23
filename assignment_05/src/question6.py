#!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 05 question 1
since   : Friday-27-04-2018
"""

def question_a(n, G=9.81, C2=1.0/1000.0, debug=True):
    time = linspace(0.0, 10.0, n)
    h = time[1] - time[0] # step size
    y = zeros(n, dtype=float)
    f = lambda t : sqrt(G/C2) * tanh(t * sqrt(G*C2))
    dfdy = lambda t : G - C2 * (t**2)
    #I = integrate.quad(dfdy, 0, 10)[1]

    y = [y[i-1] + h * dfdy(t) for i, t in enumerate(time, start=1)]
    return (y[-1], f(10))

def question_b(debug=False):
    pass

def plot_computed_error(N, error):
    plt.title("")
    plt.ylabel("")
    plt.xlabel("")
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(linspace(0,10, N), error, 'k-')
    plt.show()

if __name__ == "__main__":
    from numpy import (linspace, array, zeros)
    from scipy import (integrate, special)
    import matplotlib.pyplot as plt
    from math import (sqrt, tanh)

    abs_errors = [question_a(n) for n in [10, 100, 1000]]
    print abs_errors
else:
    from sys import exit
    exit("USAGE: python question1.py")
