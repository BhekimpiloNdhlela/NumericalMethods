#!/usr/bin/python3
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 06 question 1
since   : Friday-11-05-2018
"""
if __name__ == "__main__":
    import numpy as np
    from scipy import integrate
    from scipy.integrate import odeint
    import matplotlib.pyplot as plt
    from question02 import *


    #print(help(odeint))

    y0, t_span = [1., 0.], np.linspace(0, 1, 100)
    f = lambda  y, t: np.array([y[0], -1001*y[0] -1000*y[1]])
    sol, info_dict = odeint(f, y0, t_span, full_output=1)
    plt.plot(t_span, sol[:,0], linewidth=3, label=" v' = w + 0v")
    plt.plot(t_span, sol[:,1], linewidth=3, label=" w' = -1001w - 1000v")
    plt.legend(bbox_to_anchor=(.4, .4))
    plt.show()

    print("STIFF OPTION:")
    print("value of t at the time of the last method switch (given for each time step) ", info_dict['tsw'])
    print("cumulative number of time steps                                             ", info_dict['nst'])


    """
    [question d]
    Solve again using a built-in solver designed for stiff
    ODEs. Compare the number of timesteps required by
    the two solvers and discuss.
    """
    sol, info_dict = odeint(f, y0, t_span, full_output=1, mxords=2)
    plt.plot(t_span, sol[:,0], linewidth=3, label=" v' = w + 0v")
    plt.plot(t_span, sol[:,1], linewidth=3, label=" w' = -1001w - 1000v")
    plt.legend(bbox_to_anchor=(.4, .4))
    plt.show()
    print("\nNON STIFF OPTION:")
    print("value of t at the time of the last method switch (given for each time step) ", info_dict['tsw'])
    print("cumulative number of time steps                                             ", info_dict['nst'])


else:
    from sys import exit
    exit("USAGE: python3 question01.py")
