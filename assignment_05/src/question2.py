#!usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 05 question 2
since   : Friday-27-04-2018
"""

def composite_midpoint(f, m, a=0.0, b=1.0):
    h      = (b - a) / m
    result = h * sum([f((a+h/2.0) + i*h) for i in xrange(1, m+1)])
    return result

def composite_trapezium(f, m, a=0.0, b=1.0):
    h      = (b - a) / m
    result = h/2.0 * ( f(a) + f(b) + 2 * sum([ f(a + i * h) for i in xrange(1, m)]))
    return result

def composite_simpson(f, m, a=0.0, b=1.0, k=0.0):
    sum = 0.0
    sum += f(a)
    sum += f(b)
    h=(b-a)/(2*m) #width of segments
    oddSum = float()
    evenSum = float()
    for i in xrange(1, m):
        oddSum += f(2*h*i+a)

    sum += oddSum * 2

    for i in xrange(1, m+1):
        evenSum += f(h*(-1+2*i)+a)
    sum += evenSum * 4

    return sum * h/3


def debug(abs_err_cm, abs_err_ct, abs_err_cs, debug=True):
    if debug == True:
        print("DEBUG MODE STATUS = <ON>")
        print("Composite Midpoint\tComposite trapezium\tComposite_Simpson")
        for m, t, s in zip(abs_err_cm, abs_err_ct, abs_err_cs):
            print "{:10f}".format(m), "\t\t{:10f}".format(t), "\t\t{:10f}".format(s)
    else:
        print("DEBUG MODE STATUS = <OFF>")

def plot_abs_errs(abs_err_cm, abs_err_ct, abs_err_cs):
    plt.title("|xc-x| of: The Composite Midpoint, Simpson & Trapezium Methods against h")
    plt.ylabel("Composite Midpoint vs Composite Simpson vs Composite Trapezium")
    plt.xlabel("Number of Points")
    plt.xscale('linear')
    plt.yscale('log')
    plt.plot(M, abs_err_cm, 'k-', label="Composite Midpoint")
    plt.plot(M, abs_err_ct, 'r-', label="Composite Trapezium")
    plt.plot(M, abs_err_cs, 'b-', label="Composite Simpson")
    plt.legend(bbox_to_anchor=(.95, .9))
    plt.show()

# **************************************************************** #
import matplotlib.pyplot as plt
from math import (exp, pi, sin)
from scipy import (integrate, special)
from numpy import (abs, array, linspace)

f = lambda x : exp(sin(2 * pi * x))
I = integrate.quad(f, 0.0, 1.0)[0]
M = linspace(3, 19, 5)
# **************************************************************** #
if __name__ == "__main__":
    abs_err_cm = [abs(composite_midpoint(f, int(m)) - I) for m in M]
    abs_err_ct = [abs(composite_trapezium(f, int(m)) - I) for m in M]
    abs_err_cs = [abs(composite_simpson(f, int(m)) - I) for m in M]
    debug(abs_err_cm, abs_err_ct, abs_err_cs, debug=True)
    plot_abs_errs(abs_err_cm, abs_err_ct, abs_err_cs)
else:
    from sys import exit
    exit("USAGE: python question2.py")
