#!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 05 question 6
since   : Friday-27-04-2018
"""

def question_a(f, n, w0, I, G=9.81, C2=1.0/1000.0):
    h = 10.0/float(n) # step size
    w = zeros(n+1, dtype=float)
    w[0] = w0
    for i in xrange(1, n+1):
        w[i] = w[i-1] + h * f(w[i-1])
    return abs(w[-1] - I)

def explicit_trapezium(f, n, w0, I, G=9.81, C2=1.0/1000.0):
    h = 10.0/float(n) # step size
    w, wt = zeros(n+1, dtype=float), zeros(n+1, dtype=float)
    w[0] = w0
    for i in xrange(1, n+1):
        wt[i] = w[i-1] + h * f(w[i-1])
        w[i]  = w[i-1] + h * f(wt[i-1] + h/2.0 * f(wt[i]))
    return abs(w[-1] - I)

def explicit_midpoint(f, n, w0, I, G=9.81, C2=1.0/1000.0):
    h = 10.0/float(n) # step size
    w, wt = zeros(n+1, dtype=float), zeros(n+1, dtype=float)
    w[0] = w0
    for i in xrange(1, n+1):
        wt[i] = w[i-1] + 0.5 * h * f(w[i-1])
        w[i]  = w[i-1] + h * f(wt[i])
    return abs(w[-1] - I)

def debug_on(N, err_eulr,err_mdp, err_trap, debug=False):
    if debug == True:
        print "*" * 125
        print "The Exact Value I = {:.20f}".format(float(I))
        print "*" * 125
        print "N ", "\t\t\t\t","Euler's Method", "\t\t\t\t\t\t" , "Explicit Midpoint", "\t\t\t\t\t","Explicit Trapezium"
        print "*" * 125
        for n, em, emm, etm in zip(N, err_eulr, err_mdp, err_trap):
            temp = ""
            if n == 10:
                temp = "  "
            elif n == 100:
                temp = " "
            print n,"\t\t\t",temp,"{:.20f}".format(em), "\t\t", temp,"{:.20f}".format(emm), "\t\t",temp,"{:.20f}".format(etm)

def plot_computed_error(N, abs_err_0, abs_err_1=None, abs_err_2=None):
    plt.ylabel("n = number of points")
    plt.xlabel("h = step size)")
    plt.xscale('log'); plt.yscale('log')
    if abs_err_1 == None and abs_err_2 == None:
        plt.title("6(b.) Absolute Error of Euler's method with n = 10, 100 1000")
        plt.plot(N, abs_err_0, 'k-')
        plt.show()
    else:
        plt.title("(6a.) Absolute Error of Euler's, Explicit Midpoint"\
                   "and Explicit Trapezium methods with n = 10, 100 1000")
        plt.plot(N, abs_err_0, 'k-', label="Error Euler's Method")
        plt.plot(N, abs_err_1, 'b-', label="Error Explicit Midpoint Method")
        plt.plot(N, abs_err_2, 'r-', label="Error Explicit Trapezium Method")
        plt.legend(bbox_to_anchor=(1.0, 1.0))
        plt.show()

if __name__ == "__main__":
    from numpy import (linspace, array, zeros)
    from scipy import (integrate, special)
    import matplotlib.pyplot as plt
    from math import (sqrt, tanh)

    f = lambda t : 9.81 - (1.0/1000.0) * (t**2)
    I = sqrt(9.81/(1.0/1000.0)) * tanh(10. * sqrt(9.81*(1.0/1000.0)))
    N = [10, 100, 1000]

    # get absolute error using Euler's meth6od
    abs_err_eulr = [question_a(f, n, 0.0, I) for n in N]
    abs_err_trap = [explicit_trapezium(f, n, 0.0, I) for n in N]
    abs_err_mdp = [explicit_midpoint(f, n, 0.0, I) for n in N]

    # debug or print the acquired values
    debug_on(N, abs_err_eulr, abs_err_mdp, abs_err_trap, debug=True)

    # plot the error for question 6(a.)
    plot_computed_error(N, abs_err_eulr)
    #plot the error for question 6(a.) and 6(b.) on the same cartesion plane
    plot_computed_error(N, abs_err_eulr, abs_err_mdp, abs_err_trap)
else:
    from sys import exit
    exit("USAGE: python question6.py")
