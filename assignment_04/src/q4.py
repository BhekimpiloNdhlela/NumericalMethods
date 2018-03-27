#!usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 04 question 4
since   : Friday-23-03-2018
"""
def trapezium(abs_err, exact_I, debug=True):
    if debug is True:
        print "DEBUG MODE: [ON] [Question 4 trapezium method]"

def midpoint(abs_err, exact_I, debug=True):
    if debug is True:
        print "DEBUG MODE: [ON] [Question 4 Midpoint Method]"

def simpson(abs_err, exact_I, debug=True):
    if debug is True:
        print "DEBUG MODE: [ON] [Question 4 Simpson's method]"

def plot_abs_errs(abs_err_t, abs_err_m, abs_err_s):
    #loglog plot to display the error as function of the step size
    plt.title("|xc-x| of: The Midpoint, Simpson & Trapezium Methods against h")
    plt.ylabel("Midpoint vs Simpson vs Trapezium")
    plt.xlabel("h")
    plt.yscale('log')
    plt.xscale('log')
    plt.plot([1, 0.1, 0.01], abs_err_t, "k-", label="Trapezium")
    plt.plot([1, 0.1, 0.01], abs_err_m, "r-", label="Midpoint")
    plt.plot([1, 0.1, 0.01], abs_err_t, "g-", label="Simpson")
    plt.legend(bbox_to_anchor=(.65, .9))
    plt.show()

if __name__ == "__main__":
    from numpy import (exp, abs)
    import matplotlib.pyplot as plt

    exact_I  = lambda h : exp(h) - 1
    abs_err  = lambda xc, x : abs(xc - x)

    abs_err_t = trapezium(abs_err, exact_I)
    abs_err_m = midpoint(abs_err, exact_I)
    abs_err_s = simpson(abs_err, exact_I)
    plot_abs_errs(abs_err_t, abs_err_m, abs_err_s)
else:
    from sys import exit
    exit("USAGE: python q5.py")
