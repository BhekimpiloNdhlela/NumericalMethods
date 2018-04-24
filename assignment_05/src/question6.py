    #!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 05 question 1
since   : Friday-27-04-2018
"""

def question_a(dfdt, n, w0, I, G=9.81, C2=1.0/1000.0, debug=True):
    T = linspace(0.0, 10.0, n)
    h = 10.0/float(n) # step size
    w = zeros(n+1, dtype=float)
    w[0] = w0
    for i in xrange(1,n+1):
        w[i] = w[i-1] + h * dfdt(w[i-1])
    return w[-1]

def explicit_trapezium(f, n, w0, I, G=9.81, C2=1.0/1000.0, debug=True):
    T = linspace(0.0, 10.0, n)
    h = 10.0/float(n) # step size
    w, wt = zeros(n, dtype=float), zeros(n, dtype=float)
    w[0] = w0
    for i in xrange(1, n+1):
        wt[i] = w[i-1] + h * f(w[i-1])
        w[i]  = w[i-1] + h * f(wt[i-1] + h/2 * f(wt[i]))
    return w[-1]

def explicit_midpoint(f, n, w0, I, G=9.81, C2=1.0/1000.0, debug=True):
    T = linspace(0.0, 10.0, n)
    h = 10.0/float(n) # step size
    w, wt = zeros(n, dtype=float), zeros(n, dtype=float)

    w[0] = w0
    for i in xrange(1, n+1):
        wt[i] = w[i-1] + 0.5 * h * f(w[i])
        w[i]  = w[i-1] + 0.5*h * f(wt[i] + h/2.0 * f(wt[i]))
    return w[-1]

def debug_on(errors, N, I, debug_message):
    print("Method Used: ", debug_message)
    print "The Exact Value I = {:.20f}".format(float(I))
    for error, n in zip(errors, N):
        print "@ n = ", n, "the approximation = {:.20f}".format(error)

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

    dfdy = lambda t : 9.81 - (1.0/1000.0) * (t**2)
    f = lambda t : sqrt(9.81/(1.0/1000.0)) * tanh(t * sqrt(9.81*(1.0/1000.0)))
    I = f(10)
    N = [10, 100, 1000]

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
