#!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 04 question 1 (a. to b.)
since   : Friday-23-03-2018
"""
def question_a(steps, debug=False):
    c_ddx = lambda x, h : ((-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h))
    f = lambda x : sqrt(1 - 2 * sin(x))
    steps = logspace(-7, -1, num=100)
    abs_err = [abs(c_ddx(0.0, step) + 1.0) for step in steps]

    if debug is True:
        print "DEBUG MODE: [ON] QUESTION 1 a.)"
        print "i","\t" ,"Step Size", "\t", "Absolute Error"
        for i, (h, aE) in enumerate(zip(steps, abs_err)):
            print (i+1), "\t","{:.7f}".format(h), "\t", "{:.10f}".format(aE)
    return abs_err

def question_b(steps, M=11.0, debug=False):
    machine_eps = finfo(float).eps
    error = [(18.0 * machine_eps)/(12.0*h) + M*(h**4) for h in steps]

    if debug is True:
        print "DEBUG MODE: [ON] QUESTION 1 b.)"
        print "i","\t" ,"Step Size", "\t", "Absolute Error"
        for i, (h, aE) in enumerate(zip(steps, error)):
            print (i+1), "\t","{:.7f}".format(h), "\t", "{:.10f}".format(aE)
    return error

def plot_error_functions(steps, abs_err, error):
    #loglog plot to display the error as function of the step size
    plt.title("Plot of the Absolute Error as h(Step size) Changes")
    plt.xlabel("h (Step Size)")
    plt.ylabel("|xc - x| (Absolute Error)")
    plt.yscale('log')
    plt.xscale('log')
    plt.plot(steps, abs_err, "k-", label="question (a.)")
    plt.plot(steps, error, "k--", label="question (b.)")
    plt.legend(bbox_to_anchor=(1.0, 1), loc=0, borderaxespad=0.)
    plt.show()

if __name__ == "__main__":
    from numpy import (abs, cos, sin, sqrt, logspace)
    from numpy import (finfo, float)
    import matplotlib.pyplot as plt
    from math import pow

    steps = logspace(-7, -1, num=100)
    abs_err, error = question_a(steps), question_b(steps)
    plot_error_functions(steps, abs_err, error)
else:
    from sys import exit
    exit("USAGE: python q1.py")
