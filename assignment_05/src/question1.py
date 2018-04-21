#!usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 05 question 1
since   : Friday-27-04-2018
"""

def composite_midpoint(f, m, a=0.0, b=1.0):
    h = (b - a) / m
    sigma = sum([f((a + h / 2.0) + i*h) for i in xrange(1, m + 1)])
    return sigma * h

def composite_trapezium(f, m, a=0.0, b=1.0):
    h, hold = (b - a) / m, 0.5 * f(a) + 0.5 * f(b)
    sigma = hold + sum([ f(a + i * h) for i in xrange(1, m + 1)])
    return sigma * h

def composite_simpson(f, m, a=0.0, b=1.0, k=0.0):
    h = (b - a) / m; x = a + h
    for i in xrange(1, m / 2 + 1):
        k = k + 4 * f(x); x = x + 2 * h
    x = a + 2 * h
    for i in xrange(1, m / 2):
        k = k + 2 * f(x); x = x + 2 * h
    return (h / 3) * (f(a) + f(b) + k)

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
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(M, abs_err_cm, 'k-', label="Composite Midpoint")
    plt.plot(M, abs_err_ct, 'r-', label="Composite Trapezium")
    plt.plot(M, abs_err_cs, 'b-', label="Composite Simpson")
    plt.legend(bbox_to_anchor=(.65, .9))
    plt.show()

# **************************************************************** #
from numpy import (abs, array, linspace)
from scipy import (integrate, special)
import matplotlib.pyplot as plt
from math import exp

f = lambda x : exp(x)
I = integrate.quad(f, 0.0, 1.0)[0]
M = linspace(11, 101, 10)
# **************************************************************** #

if __name__ == "__main__":
    abs_err_cm = [abs(composite_midpoint(f, int(m)) - I) for m in M]
    abs_err_ct = [abs(composite_trapezium(f, int(m)) - I) for m in M]
    abs_err_cs = [abs(composite_simpson(f, int(m)) - I) for m in M]
    debug(abs_err_cm, abs_err_ct, abs_err_cs, debug=True)
    plot_abs_errs(abs_err_cm, abs_err_ct, abs_err_cs)
else:
    from sys import exit
    exit("USAGE: python question1.py")
