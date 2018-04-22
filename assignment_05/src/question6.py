#!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 05 question 1
since   : Friday-27-04-2018
"""

def question_a(n, G=9.81, C2=1.0/1000.0, t=10.0, debug=True):
    time = linspace(0.0, 10.0, n)
    h_size = time[1] - time[0]
    y = zeros(n, dtype=float)
    # consult Dr. Hale regarding the y(0) = ?
    # for progress sake i will assume y(0) = 0
    f_exact = lambda t : sqrt(G/C2) * tanh(t * sqrt(G*C2))
    f_dx_dy = lambda t : G - C2 * (t**2)
    yt10 = f_exact(10)
    y = [y[i-1] + h_size * f_dx_dy(t) for i, t in enumerate(time, start=1)]

    # also need to get clarity on what error is to be computed (abs_err, local/ global)
    # and how the each implies in the question paper

    """
    compute error here
    """
    return y

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
    from numpy import (linspace, array, zeros)
    from scipy import (integrate, special)
    import matplotlib.pyplot as plt
    from math import (sqrt, tanh)

    N = [10, 100, 1000]
    for n in N:
        plot_computed_error(n, question_a(n))
    #question_b()
else:
    from sys import exit
    exit("USAGE: python question1.py")
