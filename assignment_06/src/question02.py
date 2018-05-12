import numpy as np
import numpy.linalg as npla
import matplotlib.pyplot as plt

def ode45(f, tspan, y0, tol=1e-6):
    pass
    
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
    h = np.sqrt(tol);

    # Initialise solver
    t    = tspan[0];
    tend = tspan[1];
    yn   = y0;
    flag = 0;

    # Storage
    tt = t;
    yy = yn;

    # Loop through time:
    while (t < tend):

        # RK stages
        s1 = ... ;
        s2 = ... ;
        s3 = ... ;
        p  = 3;
        yn1 = yn + ... ;
        # Error estimate
        err = ... ;

        # Step size adjust
        hnew = 0.8*(tol*np.min(np.abs(yn1)/err))**(1.0/(p+1.0)) * h;
        hnew = np.min(hnew, 2.0*h);        # Don't let h grow too fast.

        if (npla.norm(err, np.inf) > tol): # Error is too large!
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
    plt.plot(tt, yy[:,0])
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
