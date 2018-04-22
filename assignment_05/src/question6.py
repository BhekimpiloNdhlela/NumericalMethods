#!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 05 question 1
since   : Friday-27-04-2018
"""

# quadratic: dv/dt = g - c2v
# if v(0) = 0 ->> v = sqrt(gc2)tanh(tsqrt(gc2))

def question_a(N, G=9.81, C2=1.0/1000.0, t=10.0, debug=True):
    H = linspace(0.0, 10.0, N)
    dxdt = lambda x : g - C2 * x

    y = zeros(N, dtype=float)

    #euler's method: yn+1 = yn + h * f(tn, yn)

def question_b(debug=False):
    pass

def plot_computed_error(N, error):
    plt.title("")
    plt.ylabel("")
    plt.xlabel("")
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(linspace(0,10, N), error, 'k-')
    plt.show()


if __name__ == "__main__":
    from numpy import linspace, array, zeros
    import matplotlib.pyplot as plt

    N = [10, 100, 1000]
    for n in N:
        plot_computed_error(n, question_a(n))
    question_b()

else:
    from sys import exit
    exit("USAGE: python question1.py")
