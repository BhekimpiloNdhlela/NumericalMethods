import numpy as np
import numpy.linalg as npla
import matplotlib.pyplot as plt

def ode45(f, tspan, y0, tol=1e-6):
    '''
    function [tt, yy] = ode324(f, tspan, y0, tol)
    ODE324 - ODE IVP sovler by Dr Hale and Mr B. Ndhlela
    INPUTS:  A function handle f = @(t,y) ... such that dy/dt = f(t,y)
             The times span tspan(1) < t <tspane(end)
             The initial condition y(tspan(1)) - y0
             The required accuracy, tol.
    OUTPUTS: The selected time steps tt, and solution values yy.
    '''

    # Initial step size
    h = np.sqrt(tol)
    # Initialise solver
    t    = tspan[0]
    tend = tspan[1]
    yn   = y0
    flag = 0

    # Storage
    tt = t
    yy = yn

    # Loop through time:
    while (t < tend):

        # RK stages
        s1 = f(t, yn)
        s2 = f(t + (0.25)*h, yn + (0.25)*h * s1)
        s3 = f(t + (3./8.)*h, yn + (3./32.)*h*s1 + (9./32.)*h*s2)
        s4 = f(t + (12./13.)* h, yn + (1932./2197)*h*s1 - (7200./2197.)*h*s2 + (7296./2197.)*h*s3)
        s5 = f(t + h, yn  + (439./216.)*h*s1 - 8.0*h*s2 + (3680./513.)*h*s3 - (845./4104.)*h*s4)
        s6 = f(t + .5 * h, yn - (8./27.)*h*s1 + 2.0*h*s2 - (3544./2565.)*h*s3 + (1859.0/4104.0)*h*s4 - (11./40.)*h*s5)
        p  = 5;
        yn1 = yn + h*((16.0/135.0)*s1 + (6656.0/12825.0)*s3 + (28561.0/56430.0)*s4 - (9.0/50.)*s5 + (2./55.)*s6) ;
        # Error estimate
        err = h * abs((1.0/360.0)*s1 - (128.0/4275.0)*s3 - (2197.0/75240.0)*s4 + (1.0/50.0)*s5 + (2.0/55.0)*s6) ;
        # Step size adjust
        hnew = 0.8*(tol*np.min(abs(yn1)/err))**(1.0/(p+1.0)) * h
        hnew = min(hnew, 2.0*h)        # Don't let h grow too fast.

        if (npla.norm([err, 0], float("inf")) > tol): # Error is too large!
            if (flag == 0):                # Try the new time step
                flag = 1                  # Set flag to remember failure
            else:                          # Time step failed
                hnew = h/2.0              # Take half of old one
        else:                              # Error is small enough!
            # Store solution and move to next time
            yn = yn1
            t = t + h
            yy = np.hstack((yy, yn1))
            tt = np.hstack((tt, t))
            # Successful step. Set flag to happy.
            flag = 0

        # Choose next step (ensure we finish at the end of the interval!)
        h = min(hnew, tend - t)

    # Transpose for convenience
    tt = tt.T
    yy = yy.T

    # Plot first component of solution
    plt.subplot(211)
    plt.plot(tt, yy[:,])
    plt.title('First component of solution')

    # Plot time steps as a function of time
    dtt = tt[2:-1] - tt[1:-2]
    plt.subplot(212)
    plt.plot(tt[2:-1], dtt)
    plt.yscale('log')
    plt.ylabel('Time steps')
    plt.title('No. of time steps = %s'%np.size(tt))
    plt.show()

    return (tt, yy)

def ode23(f, tspan, y0, tol=1e-6):
    '''
    function [tt, yy] = ode324(f, tspan, y0, tol)
    ODE324 - ODE IVP sovler by Dr Hale and Mr B. Ndhlela
    INPUTS:  A function handle f = @(t,y) ... such that dy/dt = f(t,y)
             The times span tspan(1) < t <tspane(end)
             The initial condition y(tspan(1)) - y0
             The required accuracy, tol.
    OUTPUTS: The selected time steps tt, and solution values yy.
    '''

    # Initial step size
    h = np.sqrt(tol)

    # Initialise solver
    t    = tspan[0]
    tend = tspan[1]
    yn   = y0
    flag = 0

    # Storage
    tt = t;
    yy = yn;

    # Loop through time:
    while (t < tend):

        # RK stages
        s1 = f(t, yn)
        s2 = f(t + h, yn + h * s1)
        s3 = f(t + h/2.0, yn + (h/4.0)*(s1 + s2))
        p  = 3
        yn1 = yn + (h/6.0)*(s1 + 4.0*s3 + s2)
        # Error estimate
        err = h/3.0 * abs(s1 - 2.0*s3 + s2)

        # Step size adjust
        hnew = 0.8*(tol*np.min(abs(yn1)/err))**(1.0/(p+1.0)) * h;
        hnew = min(hnew, 2.0*h);        # Don't let h grow too fast.
        if npla.norm([err, 0], float('Inf')) > tol: # Error is too large!
            if (flag == 0):                # Try the new time step
                flag = 1;                  # Set flag to remember failure
            else:                          # Time step failed
                hnew = h/2.0;              # Take half of old one
        else:                              # Error is small enough!
            # Store solution and move to next time
            yn = yn1
            t = t + h;
            yy = np.hstack((yy, yn1));
            tt = np.hstack((tt, t));
            # Successful step. Set flag to happy.
            flag = 0;
        # Choose next step (ensure we finish at the end of the interval!)
        h = min(hnew, tend - t);

    # Transpose for convenience
    tt = tt.T
    yy = yy.T

    # Plot first component of solution
    plt.subplot(211)
    plt.plot(tt, yy[:,])
    plt.title('First component of solution')

    # Plot time steps as a function of time
    dtt = tt[2:-1] - tt[1:-2]
    plt.subplot(212)
    plt.plot(tt[2:-1], dtt)
    plt.yscale('log')
    plt.ylabel('Time steps')
    plt.title('No. of time steps = %s'%np.size(tt))
    plt.show()

    return (tt, yy)

if __name__ == "__main__":
    t_interval = [0, int(2.0/0.001)]
    f = lambda t, y: y**2 - y**3
    f0 = .001
    tt_a, yy_a = ode23(f, t_interval, f0)
    tt_b, yy_b = ode45(f, t_interval, f0)
