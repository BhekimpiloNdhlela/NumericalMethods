#!/usr/bin/python3
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 06 question 1
since   : Friday-11-05-2018
"""
def plot_solution_functions(t_span, non_stiff_odes_s, stiff_odes_s):
    plt.subplot(211)
    plt.title("Solution Using A Non-Stiff ODE Method")
    plt.ylabel("y' = [dy1/dt ; dy2/dt]")
    non_stiff_t = linspace(t_span[0], t_span[1], len(non_stiff_odes_s[1]))
    plt.plot(non_stiff_t, non_stiff_odes_s[0,:], 'k-', linewidth=4, label=" v' = w + 0v")
    plt.plot(non_stiff_t, non_stiff_odes_s[1,:], 'r-', linewidth=4, label=" w' = -1001w - 1000v")
    plt.legend(bbox_to_anchor=(.4, .4))
    plt.subplot(212)
    plt.title("Solution Using A Stiff ODE Method")
    plt.xlabel("time = t")
    plt.ylabel("y' = [dy1/dt ; dy2/dt]")
    stiff_t = linspace(t_span[0], t_span[1], len(stiff_odes_s[1]))
    plt.plot(stiff_t, stiff_odes_s[0,:], 'k-', linewidth=4, label=" v' = w + 0v")
    plt.plot(stiff_t, stiff_odes_s[1,:], 'r-', linewidth=4, label=" w' = -1001w - 1000v")
    plt.show()

def plot_time_comparisons(t_span, non_stiff_odes_t, stiff_odes_t):
    plt.subplot(211)
    non_stiff_t = linspace(t_span[0], t_span[1], len(non_stiff_odes_t))
    plt.ylabel("Time Steps")
    plt.title("Method of Non-Stiff odes(RK45) = "+ str(len(non_stiff_t)) + " Steps.")
    plt.plot(non_stiff_t, non_stiff_odes_t, 'k-', linewidth=4)
    plt.subplot(212)
    plt.xlabel("Time = t")
    plt.ylabel("Time Steps")
    stiff_t = linspace(t_span[0], t_span[1], len(stiff_odes_t))
    plt.title("Method of Stiff ODEs(BDF) = "+ str(len(stiff_t)) + " Steps.")
    plt.plot(stiff_t, stiff_odes_t, 'r-', linewidth=4)
    plt.show()

if __name__ == "__main__":
    from numpy import linspace, array, shape
    import matplotlib.pyplot as plt
    from scipy.integrate import solve_ivp

    y0     = [1., 0.]
    t_span = [0., 1.]
    f      = lambda t, y: array([y[0], -1001*y[0] -1000*y[1]])

    non_stiff_odes = solve_ivp(f, t_span, y0, method='RK45')
    stiff_odes     = solve_ivp(f, t_span, y0, method='BDF')

    plot_solution_functions(t_span, non_stiff_odes.y, stiff_odes.y)
    plot_time_comparisons(t_span, non_stiff_odes.t,  stiff_odes.t)
else:
    from sys import exit
    exit("USAGE: python3 question01.py")
