#!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 04 question 1 (a. to b.)
since   : Friday-23-03-2018
"""
def exact(steps, x=0.0, debug=False):
    fpp = lambda x, h : ((-f(x+2*h)+16*f(x+h)-30*f(x)+16*f(x-h)-f(x-2*h))/(12*h*h))
    f = lambda x : sqrt(1 - 2 * sin(x))
    exact = [abs(fpp(x, h) + 1.0) for h in steps]
    if debug is True:
        print "DEBUG MODE: [ON] QUESTION 3 bi.)"
        print "i","\t" ,"Step Size", "\t", "Exact Error"
        for i, (h, err) in enumerate(zip(steps, exact)):
            print (i+1), "\t","{:.7f}".format(h), "\t", "{:.10f}".format(err)
    return exact

def bound(steps, M=11.0, debug=False):
    machine_eps = finfo(float).eps
    bound = [(18.0 * machine_eps)/(12.0*(h**2)) + M*(h**4) for h in steps]
    if debug is True:
        print "DEBUG MODE: [ON] QUESTION 3 bii.)"
        print "i","\t" ,"Step Size", "\t", "Bound"
        for i, (h, err) in enumerate(zip(steps, bound)):
            print (i+1), "\t","{:.7f}".format(h), "\t", "{:.10f}".format(err)
    return bound

def plot_error_functions(steps, exact, bound):
    #loglog plot to display the error as function of the step size
    plt.title("Plot of the Exact Error and Bound as h(Step size) Changes")
    plt.xlabel("h (Step Size)")
    plt.ylabel("Exact vs Bound")
    plt.yscale('log')
    plt.xscale('log')
    plt.plot(steps, exact, "k-", label="Exact")
    plt.plot(steps, bound, "k--", label="Bound")
    plt.legend(bbox_to_anchor=(.65, .9))
    plt.show()

if __name__ == "__main__":
    from numpy import (abs, cos, sin, sqrt, logspace)
    from numpy import (finfo, float)
    import matplotlib.pyplot as plt
    from math import pow

    steps = logspace(-7, -1, num=100)
    exact, bound = exact(steps), bound(steps)
    plot_error_functions(steps, exact, bound)
else:
    from sys import exit
    exit("USAGE: python q3.py")
