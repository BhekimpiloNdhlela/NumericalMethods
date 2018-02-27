def sign(x):
	if x < 0:	return -1
	elif x > 0: return 1
	else:		return 0

def bisect(f,a,b,tol):
	fa, fb = f(a), f(b)

	if sign(fa)*sign(fb) >= 0:
		print 'f(a)f(b)<0 not satisfied!'
		quit()
	while (b-a)/2. > tol:
		c = (a+b)/2.
		fc = f(c)
		if fc == 0:                 # c is a solution, done
			return c
		if sign(fc)*sign(fa) < 0:   # a and c make the new interval
			b, fb = c, fc
		else:   	# c and b make the new interval
			a, fa = c, fc
	return (a+b)/2.		# new midpoint is best estimate

if __name__ == "__main__":
    from math import cos, tan
    f = lambda theta: 20.0 * tan(theta) - ((20.0**2 * 9.81) / (2 * (17.0**2) * cos(theta)**2)) - 3
    print bisect(f,0,1,   1.0e-5)
