#!usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 04 question 4
since   : Friday-23-03-2018
"""
def trapezium(exact_I, H, x0=0., debug=True):
    apprx_I = array([h/2. * (exp(x0) + exp(h)) for h in H])
    return array([abs(apI - exI) for apI, exI in zip(apprx_I, exact_I)])

def midpoint(exact_I, H, x0=0., debug=True):
    W = array([x0 + (h / 2.0) for h in H])
    apprx_I = array([h * exp(w) for h, w in zip(H, W)])
    return array([abs(apI - exI) for apI, exI in zip(apprx_I, exact_I)])

def simpson(exact_I, H, x0=0., debug=True):
    apprx_I = array([h/6.*(exp(x0)+(4.*exp(h/2.))+exp(h)) for h in H])
    return array([abs(apI - exI) for apI, exI in zip(apprx_I, exact_I)])

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

if __name__ == "__main__":
    from numpy import (exp, abs, array)
    import matplotlib.pyplot as plt

    H         = array([1., .1, .01])
    exact_I   = array([exp(h) - 1 for h in H])

    abs_err_t = trapezium(exact_I, H)
    abs_err_m = midpoint(exact_I, H)
    abs_err_s = simpson(exact_I, H)

    debug(abs_err_s, abs_err_m, abs_err_t)
    plot_abs_errs(abs_err_t, abs_err_m, abs_err_s)

else:
    from sys import exit
    exit("USAGE: python q5.py")
