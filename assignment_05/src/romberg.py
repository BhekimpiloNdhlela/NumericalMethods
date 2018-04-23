"""
    disclaimer i acquired this function the course website or
    directly from: http://blue.math.buffalo.edu/sauer2py/romberg.py
"""
# Program 5.1 Romberg integration
# Translated to Python by JR 2/17/2012.
# Computes approximation to definite integral
# Inputs: Matlab inline function specifying integrand f,
#    a,b integration interval, n=number of rows
# Output: Romberg tableau r
from numpy import *
from math import sin

def romberg(f,a,b,n):
	h=(b-a)/2.**linspace(0,n-1,n)
	r = zeros((n,n))
	r[0,0]=(b-a)*(f(a)+f(b))/2.
	for j in range(2,n+1):
		subtotal = 0.
		for i in range(1,2**(j-2)+1):
			subtotal = subtotal + f(a+(2*i-1)*h[j-1])
		r[j-1,0] = r[j-2,0]/2. + h[j-1]*subtotal
		for k in range(2,j+1):
			r[j-1,k-1] = (4**(k-1)*r[j-1,k-2]-r[j-2,k-2])/(4.**(k-1)-1)
	return r

if __name__ == "__main__":
    f = lambda x: sin(1.7*x)-x**2.5
    set_printoptions(precision=5)
    print romberg(f,1,3,5)
