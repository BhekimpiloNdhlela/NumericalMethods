#!usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 05 question 1
since   : Friday-27-04-2018
"""

"""
def composite_trapezium(exact_I, H, a=0.0, b=1.0):
    # --------------------------------------
    H = array([(b - a) / (2.0 * m) for m in M])

    # --------------------------------------
    apprx_I = array([h/2. * (exp(x0) + exp(h)) for h in H])
    # return absolute Errors for composite_trapezium
    return array([abs(apI - exI) for apI, exI in zip(apprx_I, exact_I)])

def composite_simpson(exact_I, H, a=0.0, b=1.0):
    # --------------------------------------
    H = array([(b - a) / m for m in M])
    # --------------------------------------

    apprx_I = array([h/6.*(exp(x0)+(4.*exp(h/2.))+exp(h)) for h in H])
    # return absolute Errors for composite_simpson
    return array([abs(apI - exI) for apI, exI in zip(apprx_I, exact_I)])
"""

def debug(abs_err_s, abs_err_m, abs_err_t, debug=True):
    if debug is True:
        print "DEBUG MODE: [ON] [Question 4 Simpson's method]"
        print "SIMPSONS METHOD\t\tMIDPOINT METHOD\t\tTRAPEZIUM METHOD"
        for s, m, t in zip(abs_err_s, abs_err_m, abs_err_t):
            print "{:.20f}".format(s),"{:.20f}".format(m),"{:.20f}".format(t)
    else:
        print "DEBUG MODE: [OFF] [Question 4 Simpson's method]"

def plot_abs_errs(abs_err_t, abs_err_m, abs_err_s):
    #loglog plot to display the error as function of the step size
    plt.title("|xc-x| of: The Midpoint, Simpson & Trapezium Methods against h")
    plt.ylabel("Midpoint vs Simpson vs Trapezium")
    plt.xlabel("h")
    plt.yscale('log')
    plt.xscale('log')
    plt.plot([1., .1, .01], abs_err_t, "k-", label="Trapezium")
    plt.plot([1., .1, .01], abs_err_m, "r-", label="Midpoint")
    plt.plot([1., .1, .01], abs_err_s, "g-", label="Simpson")
    plt.legend(bbox_to_anchor=(.65, .9))
    plt.show()

def composite_midpoint(M, a=0.0, b=1.0):
    H = array([(b - a) / m for m in M])

    W = array([a + (h / 2.0) for h in H])

    S = lambda m: sum([exp(mi) for mi in xrange(1, int(m))])

    apprx_I = [h * S(m) for (h, m) in zip(H, M)]



    abs_error = array([abs(aI - (exp(1) - 1)) for aI in apprx_I])

    print "Abs Error:"
    print abs_error
    plt.yscale('log')
    plt.xscale('log')
    plt.plot(linspace(0.0, 115.0, 10), abs_error, "k--")
    plt.show()

if __name__ == "__main__":
    from numpy import (exp, abs, array, linspace)
    import matplotlib.pyplot as plt
    from scipy import integrate



    M = linspace(11.0, 101.0, 10)
    composite_midpoint(M)

    #abs_err_ct = composite_trapezium(exact_I, H)
    #abs_err_cm = composite_midpoint(M)
    #abs_err_cs = composite_simpson(exact_I, H)

    #debug(abs_err_ct, abs_err_cm, abs_err_cs)
    #plot_abs_errs(abs_err_ct, abs_err_cm, abs_err_cs)

else:
    from sys import exit
    exit("USAGE: python question1.py")
