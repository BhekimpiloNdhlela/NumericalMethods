import math, sys

def fpi(x, k):
	g = lambda x : ((0.5 * x) + (1 / x))

	for i in range(k):
		print i, x, g(x)
		x = g(x)
	print 'The root is: ',
	return x

def main(argv):
	if (len(sys.argv) != 3):
		sys.exit('Usage: fixed_point.py <x> <k>')

	print 'The root is:',
	print fpi(float(sys.argv[1]),int(sys.argv[2]))

if __name__ == "__main__":
	main(sys.argv[1:])
