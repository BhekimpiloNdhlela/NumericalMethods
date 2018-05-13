#!/usr/bin/python3
def adam_bashforth_two_step(f, h, n=100.0, T=(1.0, 2.0), w0=4.0):
    wn   = lambda w0, w1, t0, t1 : w0 + (0.5*h)*(3*f(t0, w0) - f(t1, w1))
    W    = zeros((int(n),), dtype=float)
    t    = linspace(T[0], T[1], int(n))
    W[0] = w0
    W[1] = W[0] + h * f(t[1], W[0])    # w[1] evaluated by euler's method

    for i, j in zip(range(1, int(n - 1)), range(2, int(n))):
        W[i + 1] = wn(W[i], W[i-1], t[j], t[j-1])

    # Update global Variables befor returning
    global TWO_STEP_SOLUTIONS
    TWO_STEP_SOLUTIONS.append(W)
    return W[-1]

def adam_bashforth_mul_step(f, h, n=100.0, T=(1.0, 2.0), w0=4.0):
    wn   = lambda w0, w1, t0, t1 : -4.0*w0 + 5.0*w1 + h*(4*f(t0, w0) + 2*f(t1, w1))
    W    = zeros((int(n),), dtype=float)
    t    = linspace(T[0], T[1], int(n))
    W[0] = w0
    W[1] = W[0] + h * f(t[1], W[0])    # w[1] evaluated by euler's method
    for i, j in zip(range(1, int(n - 1)), range(2, int(n))):
        W[i + 1] = wn(W[i], W[i-1], t[j], t[j-1])

    # Update global Variables befor returning
    global MULTI_STEP_SOLUTIONS
    MULTI_STEP_SOLUTIONS.append(W)
    return W[-1]

def plot_solution_functions(W, t):
    plt.title("")
    plt.ylabel("dy/dt = -t * y, two_step vs multi_steps")
    plt.xlabel("time = t = linspace(1, 2, 100)")
    plt.xlim([1, 2])
    plt.plot(t, W[0], 'k-', linewidth=3, label="h = 0.0100")
    plt.plot(t, W[1], 'b-', linewidth=3, label="h = 0.0050")
    plt.plot(t, W[2], 'c-', linewidth=3, label="h = 0.0025")
    plt.plot(t, W[3], 'r-', linewidth=3, label="h = 0.0000")
    plt.legend(bbox_to_anchor=(.65, .9))
    plt.show()

def debug(abs_err_2, abs_err_m, debug_status=True):
    if debug_status == True:
        print("Absolute Errors:")
        print("Adam Bashforth Two Steps\t\tAdam Bashforth Multi Steps")
        for step_2, step_m in zip(abs_err_2, abs_err_m):
            print("{:.20f}".format(step_2) + "\t\t " + "{:.20f}".format(step_m))

# Global Variables
MULTI_STEP_SOLUTIONS = []
TWO_STEP_SOLUTIONS = []

if __name__ == "__main__":
    from numpy import exp, zeros, linspace
    import matplotlib.pyplot as plt

    f       = lambda t, y: -t * y
    I       = lambda t   : 4.0*exp(0.5*(1-((t)**2.0)))
    abs_err = lambda xc  : abs(xc - I(2.0))
    H       = [0.01, 0.005, 0.0025, 0]

    two_step_abs_err   = [abs_err(adam_bashforth_two_step(f, h)) for h in H]
    multi_step_abs_err = [abs_err(adam_bashforth_mul_step(f, h)) for h in H]

    debug(two_step_abs_err, multi_step_abs_err, debug_status=True)

    plot_solution_functions(MULTI_STEP_SOLUTIONS, linspace(1, 2, 100))
    plot_solution_functions(TWO_STEP_SOLUTIONS, linspace(1, 2, 100))
else:
    from sys import exit
    exit("USAGE: question3.py")
