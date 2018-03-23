#!/usr/bin/python
def question_a(n=8.0, debug=True):
    f = array([exp(x) for x in linspace(0.0, 1.0, 8.0)])
    h = (1.0 / (n - 1.0))
    A = matrix([[1,-2, 1, 0, 0, 0, 0, 0],\
                [0, 1,-2, 1, 0, 0, 0, 0],\
                [0, 0, 1,-2, 1, 0, 0, 0],\
                [0, 0, 0, 1,-2, 1, 0, 0],\
                [0, 0, 0, 0, 1,-2, 1, 0],\
                [0, 0, 0, 0, 0, 1,-2, 1]])
    f_ = (1. / h**2.) * matmul(A, f).T

    if debug is True:
        print "DEBUG MODE: [ON] \t [QUESTION 5 A.)]"
        print "f\"(x) = ",
        for i in f_:
            print i,
            
if __name__ == "__main__":
    from numpy import (linspace, exp, array, shape, matrix, matmul)
    question_a()
else:
    from sys import exit
    exit("USAGE: python q5.py")
