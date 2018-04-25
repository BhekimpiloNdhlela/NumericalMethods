    #!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 05 question 1
since   : Friday-27-04-2018
"""

def question_a(dfdt, n, w0, I, G=9.81, C2=1.0/1000.0):
    T = linspace(0.0, 10.0, n)
    h = 10.0/float(n) # step size
    w = zeros(n+1, dtype=float)
    w[0] = w0
    for i in xrange(1, n+1):
        w[i] = w[i-1] + h * dfdt(w[i-1])
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

def debug_on(errors, N, I, debug_message):
    print "\n************************************************************"
    print "Method Used: ", debug_message
    print "The Exact Value I = {:.20f}".format(float(I))
    for error, n in zip(errors, N):
        print "@ n = ", n, "the approximation = {:.20f}".format(error)
    print "************************************************************"

def plot_computed_error(N, error, error1=None, error2=None):
    plt.title("")
    plt.ylabel("")
    plt.xlabel("")
    plt.xscale('log')
    plt.yscale('log')
    if error1 == None and error2 == None:
        plt.plot(linspace(0,10, N), error, 'k-')
        plt.show()
    else:
        plt.plot(linspace(0,10, N), error , 'k-')
        plt.plot(linspace(0,10, N), error1, 'b-')
        plt.plot(linspace(0,10, N), error2, 'r-')
        plt.show()

if __name__ == "__main__":
    from numpy import (linspace, array, zeros)
    from scipy import (integrate, special)
    import matplotlib.pyplot as plt
    from math import (sqrt, tanh)

    dfdy = lambda t : 9.81 - (1.0/1000.0) * (t**2)
    f = lambda t : sqrt(9.81/(1.0/1000.0)) * tanh(t * sqrt(9.81*(1.0/1000.0)))
    I, N = f(10), [10, 100, 1000]

    # get absolute error using Euler's meth6od
    abs_errors_eulr = [question_a(dfdy, n, 0.0, I) for n in N]
    debug_on(abs_errors_eulr, N, I, "Euler's Method")

    # get absolute error using explicit trapezium method
    abs_errors_trap = [explicit_trapezium(dfdy, n, 0.0, I) for n in N]
    debug_on(abs_errors_trap, N, I, "Explicit Trapezium Method")

    # get absolute error using explicit midpoint method
    abs_errors_midp = [explicit_midpoint(dfdy, n, 0.0, I) for n in N]
    debug_on(abs_errors_midp, N, I, "Explicit Midpoint Method")
else:
    from sys import exit
    exit("USAGE: python question1.py")
