#!/usr/bin/python
def solution(e, k):
    f = lambda u, v : (ln(u**e) / v) + u - v - k
    u = linspace(1., 20., 1000)
    v = linspace(1., 20., 1000)

    f_vals = [f(x,y) for x,y in zip(u,v)]
    plot_implicit_solution(u,v, f_vals)

def plot_implicit_solution(u,v, f_vals):
    plt.plot(u, f_vals, "k-", label="f(u)")
    plt.plot(v, f_vals, "r-", label="f(v)")
    plt.title("IMPLICIT SOLUTIOIN CURVE (NOTE: WITH negative lambda)")
    plt.xlabel("v")
    plt.ylabel("u")
    plt.legend(bbox_to_anchor=(.65, .9))
    plt.show()

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from sys import (argv, exit)
    from math import log as ln
    from numpy import linspace

    if len(argv) == 3:
        solution(int(argv[1]), int(argv[2]))
    else:
        exit("USAGE: solution.py <lambda> <k>")

else:
    from sys import exit
    exit("USAGE: solution.py")
