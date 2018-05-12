#!/usr/bin/python3
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 06 question 1
since   : Friday-11-05-2018
"""

def lorenz_system_RK4(dx, dy, dz, T, N, h=0.1, x0=-14.0, y0=-15.0, z0=20.0, debug=True):
    x, y, z = zeros(100), zeros(100), zeros(100)
    x[0], y[0], z[0] = x0, y0, z0
    for i, t in zip(range(1, 100), T):
        x[i] = get_next_element(dx, x[i-1], y[i-1], z[i-1], h, x[i-1])
        y[i] = get_next_element(dy, x[i-1], y[i-1], z[i-1], h, y[i-1])
        z[i] = get_next_element(dz, x[i-1], y[i-1], z[i-1], h, z[i-1])
    return x, y, z

def get_next_element(d, x, y, z, h, db):
    s1 = lambda f, x, y, z   : f(x, y, z)
    a  = s1(d, x, y, z)
    s2 = lambda f, x, y, z, a: f(x+(h/2)*a, y+(h/2)*a, z+(h/2)*a)
    b  = s2(d, x, y, z, a)
    s3 = lambda f, x, y, z, b: f(x+(h/2)*b, y+(h/2)*b, z+(h/2)*b)
    c  = s3(d, x, y, z, b)
    s4 = lambda f, x, y, z, c: f(x+h*c, y+h*c, z+h*c)
    d  = s4(d, x, y, z, c)
    return db + (h/6)*(a + b*2 + c*2 + d)

def plot_lorenz_system_solution(x, y, z, t):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x, y, z, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")
    plt.show()

if __name__ == "__main__":
    from numpy import (linspace, array, zeros)
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    t  = linspace(0, 100, 100.0)
    dotx = lambda x, y, z : -10.0 * (x - y)
    doty = lambda x, y, z : x * (28.0 - z) -y
    dotz = lambda z, x, y : x * y - (8.0/3.0)*z

    x, y, z = lorenz_system_RK4(dotx, doty, dotz, t, 100)
    plot_lorenz_system_solution(x, y, z, t)

else:
    from sys import exit
    exit("USAGE: python3 question05.py")
