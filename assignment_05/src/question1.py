#!usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 05 question 1
since   : Friday-27-04-2018
"""
def composite_trapezium(exact_I, H, a=0.0, b=1.0):
    # --------------------------------------
    H = array([(b - a) / (2.0 * m) for m in M])

    # --------------------------------------


    apprx_I = array([h/2. * (exp(x0) + exp(h)) for h in H])
    # return absolute Errors for composite_trapezium
    return array([abs(apI - exI) for apI, exI in zip(apprx_I, exact_I)])

def composite_midpoint(exact_I, M, a=0.0, b=1.0):
    # --------------------------------------
    H = array([(b - a) / m for m in M])
    W = array([a + (h / 2.0) for h in H])

    sigma = lambda m, w : sum(exp(w) for w in W)
    apprx_I = array([h * sigma(m, w) for (h, m) in zip(H, M, W)])
    # --------------------------------------
    # return absolute Errors for composite_midpoint
    return array([abs(apI - exI) for apI, exI in zip(apprx_I, exact_I)])

def composite_simpson(exact_I, H, a=0.0, b=1.0):
    # --------------------------------------
    H = array([(b - a) / m for m in M])
    # --------------------------------------

    apprx_I = array([h/6.*(exp(x0)+(4.*exp(h/2.))+exp(h)) for h in H])
    # return absolute Errors for composite_simpson
    return array([abs(apI - exI) for apI, exI in zip(apprx_I, exact_I)])

def debug(abs_err_ct, abs_err_cm, abs_err_cs):
    print "DEBUG MODE: [ON] [Question 1 Simpson's method]"
    print "SIMPSONS METHOD\t\tMIDPOINT METHOD\t\tTRAPEZIUM METHOD"
    for s, m, t in zip(abs_err_cs, abs_err_cm, abs_err_ct):
        print "{:.20f}".format(s),"{:.20f}".format(m),"{:.20f}".format(t)

def plot_abs_errs(abs_err_ct, abs_err_cm, abs_err_cs):
    #loglog plot to display the error as function of the step size
    plt.title("|xc-x| of: The Midpoint, Simpson & Trapezium Methods against h")
    plt.ylabel("Composite Midpoint vs Composite Simpson vs Composite Trapezium")
    plt.xlabel("h")
    plt.yscale('log')
    plt.xscale('log')
    plt.plot([1., .1, .01], abs_err_ct, "k-", label="Composite Trapezium")
    plt.plot([1., .1, .01], abs_err_cm, "r-", label="Composite Midpoint")
    plt.plot([1., .1, .01], abs_err_cs, "g-", label="Composite Simpson")
    plt.legend(bbox_to_anchor=(.65, .9))
    plt.show()

if __name__ == "__main__":
    from numpy import (exp, abs, array, linspace)
    import matplotlib.pyplot as plt
    from scipy import integrate

    #H         = array([1., .1, .01])
    #exact_I   = array([exp(h) - 1 for h in H])

    M = linspace(11.0, 101.0, 10)

    #abs_err_ct = composite_trapezium(exact_I, H)
    #abs_err_cm = composite_midpoint(exact_I, H)
    #abs_err_cs = composite_simpson(exact_I, H)

    #debug(abs_err_ct, abs_err_cm, abs_err_cs)
    #plot_abs_errs(abs_err_ct, abs_err_cm, abs_err_cs)

else:
    from sys import exit
    exit("USAGE: python question1.py")
