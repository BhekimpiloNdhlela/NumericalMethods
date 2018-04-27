    #!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 05 question 6
since   : Friday-27-04-2018
"""

def question_a(f, n, w0, I, G=9.81, C2=1.0/1000.0):
    T = linspace(0.0, 10.0, n)
    h = 10.0/float(n) # step size
    w = zeros(n+1, dtype=float)
    w[0] = w0
    for i in xrange(1, n+1):
        w[i] = w[i-1] + h * f(w[i-1])
    return abs(w[-1] - I)

def explicit_trapezium(f, n, w0, I, G=9.81, C2=1.0/1000.0):
    T = linspace(0.0, 10.0, n)
    h = 10.0/float(n) # step size
    w, wt = zeros(n+1, dtype=float), zeros(n+1, dtype=float)
    w[0] = w0
    for i in xrange(1, n+1):
        wt[i] = w[i-1] + h * f(w[i-1])
        w[i]  = w[i-1] + h * f(wt[i-1] + h/2.0 * f(wt[i]))
    return abs(w[-1] - I)

def explicit_midpoint(f, n, w0, I, G=9.81, C2=1.0/1000.0):
    T = linspace(0.0, 10.0, n)
    h = 10.0/float(n) # step size
    w, wt = zeros(n+1, dtype=float), zeros(n+1, dtype=float)
    w[0] = w0
    for i in xrange(1, n+1):
        wt[i] = w[i-1] + 0.5 * h * f(w[i-1])
        w[i]  = w[i-1] + h * f(wt[i])
    return abs(w[-1] - I)

def debug_on(errors, N, I, debug_message, debug=False):
    if debug == False:
        pass
    else:
        print "\n************************************************************"
        print "Method Used: ", debug_message
        print "The Exact Value I = {:.20f}".format(float(I))
        for error, n in zip(errors, N):
            print "@ n = ", n, "the abs_err = {:.20f}".format(error)
            print "************************************************************"

def plot_computed_error(N, abs_err_0, abs_err_1=None, abs_err_2=None):
    plt.ylabel("n = number of points")
    plt.xlabel("h = step size)")
    plt.xscale('log'); plt.yscale('log')
    if abs_err_1 == None and abs_err_2 == None:
        plt.title("Absolute Error of Euler's method with n = 10, 100 1000")
        plt.plot(N, abs_err_0, 'k-')
        plt.show()
    else:
        plt.title("Absolute Error of Euler's, Explicit Midpoint and" \
                  "Explicit Trapezium methods with n = 10, 100 1000")
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
    abs_errors_eulr = [question_a(f, n, 0.0, I) for n in N]
    debug_on(abs_errors_eulr, N, I, "Euler's Method")

    # get absolute error using explicit trapezium method
    abs_errors_trap = [explicit_trapezium(f, n, 0.0, I) for n in N]
    debug_on(abs_errors_trap, N, I, "Explicit Trapezium Method")

    # get absolute error using explicit midpoint method
    abs_errors_midp = [explicit_midpoint(f, n, 0.0, I) for n in N]
    debug_on(abs_errors_midp, N, I, "Explicit Midpoint Method")

    # plot the error for question 6(a.)
    plot_computed_error(N, abs_errors_eulr)
    # plot the error for question 6(a.) and 6(b.) on the same cartesion plane
    plot_computed_error(N, abs_errors_eulr, abs_errors_midp, abs_errors_trap)
else:
    from sys import exit
    exit("USAGE: python question6.py")
