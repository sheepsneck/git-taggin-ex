#!.venv/bin/python3

import sys
from math import sqrt

# These are the args for "ax^2 + bx + c = 0"
A = int(sys.argv[1])
B = int(sys.argv[2])
C = int(sys.argv[3])


# This is the quadratic function being used
X1 = ((-1*B) + sqrt((B**2) - (4*A*C)))/(2*A)
X2 = ((-1*B) - sqrt((B**2) - (4*A*C)))/(2*A)


# We print and return our solutions found
print("x1: %f" % X1)
print("x2: %f" % X2)

# I'll use x^2 + 2x + 1 = 0, which is (x+1)*(x+1) = 0
