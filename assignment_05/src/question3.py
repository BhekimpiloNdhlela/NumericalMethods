#!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 05 question 1
since   : Friday-27-04-2018
"""

def romberg(f,a,b,n):
    # this code block or the function romberg was aquired from the course website
    """
    def myf(x):
    	return sin(1.7*x)-x**2.5
    set_printoptions(precision=5)
    print romberg(myf,1,3,5)
    """

    h=(b-a)/2.**linspace(0,n-1,n)
    r = zeros((n,n))
    r[0,0]=(b-a)*(f(a)+f(b))/2.
    for j in xrange(2,n+1):
        subtotal = 0.
        for i in xrange(1,2**(j-2)+1):
            subtotal = subtotal + f(a+(2*i-1)*h[j-1])
        r[j-1,0] = r[j-2,0]/2. + h[j-1]*subtotal
        for k in xrange(2,j+1):
            r[j-1,k-1] = (4**(k-1)*r[j-1,k-2]-r[j-2,k-2])/(4.**(k-1)-1)
    return r

def question_b(debug=True):
    if debug == True:
        print("Debug Mode: [ON] Question 3(b)")
    else:
        print("Debug Mode: [OFF] Question 3(b)")

def question_c(debug=True):
    if debug == True:
        print("Debug Mode: [ON] Question 3(c)")
    else:
        print("Debug Mode: [OFF] Question 3(c)")

if __name__ == "__main__":
    question_a()
    question_b()
    question_c()

else:
    from sys import exit
    exit("USAGE: python question1.py")
