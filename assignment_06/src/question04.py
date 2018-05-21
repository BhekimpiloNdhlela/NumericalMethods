#!/usr/bin/python3
def plot_function(x, y):
    hor_function = lambda x : 1
    plt.title("The function is less than 1 below \nthe horizontal black dashed line")
    plt.xlabel("horizontal axis")
    plt.ylabel("vertical axis")
    plt.plot(x, y, 'r-', lw=5)
    plt.plot(0, 1, 'mo', lw=5)
    plt.axhline(y=1.0, xmin=-0.5, xmax=1.0, color='k', ls='--', lw=4)
    plt.show()

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from numpy import linspace
    H = lambda h: 1 - 10*h + float(pow(-10 * h, 2))/2.0  + float(pow(-10 * h, 3))/6.0
    X = linspace(-0.5, 1, 100)
    Y = [H(x) for x in X]
    i = 0
    #for x, y in zip(X, Y):
    #    if y == 1.0 and i ==0:
    #        i += 1
    #        print'(x, y) |=> (', x, y, ')'
    plot_function(X, Y)
else:
    from sys import exit
    exit("USAGE: pthon[2/3] question04.py")
