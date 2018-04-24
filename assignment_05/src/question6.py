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
    h = 1.0/float(n) # step size
    w = zeros(n, dtype=float)
    w[0] = w0
    w = [w[i-1] + h * dfdt(t) for i, t in enumerate(T, start=1)]
    return abs(w[-1] - I)

def explicit_trapezium(dfdt, n, w0, I, G=9.81, C2=1.0/1000.0, debug=True):
    T = linspace(0.0, 10.0, n)
    h = 1.0/float(n) # step size
    w = zeros(n, dtype=float)
    w[0] = w0
    w = [w[i-1] + .05 * h * (dfdt(T[i-1]) + dfdt(T[i])) for  i in xrange(1,10)]
    return abs(w[-1] - I)

def explicit_midpoint(dfdt, n, w0, I, G=9.81, C2=1.0/1000.0, debug=True):
    T = linspace(0.0, 10.0, n)
    h = 1.0/float(n) # step size
    w = zeros(n, dtype=float)
    w[0] = w0
    w = [w[i-1] + 0.5*h * dfdt(t + 0.5*h) for i, t in enumerate(T, start=1)]
    return abs(w[-1] - I)

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
    I = integrate.quad(dfdy, 0, 10)[1]
    N = [10, 100, 1000]

    # get absolute error using Euler's meth6od
    abs_errors_eulr = [question_a(dfdy, n, f(0), I) for n in N]
    debug_on(abs_errors_eulr, N, I, "Euler's Method")

    # get absolute error using explicit trapezium method
    abs_errors_trap = [explicit_trapezium(dfdy, n, f(0), I) for n in N]
    debug_on(abs_errors_trap, N, I, "Explicit Trapezium Method")

    # get absolute error using explicit midpoint method
    abs_errors_midp = [explicit_midpoint(dfdy, n, f(0), I) for n in N]
    debug_on(abs_errors_midp, N, I, "Explicit Midpoint Method")
else:
    from sys import exit
    exit("USAGE: python question1.py")
