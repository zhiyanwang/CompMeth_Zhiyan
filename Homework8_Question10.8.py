# Monte Carlo
#  Sample N=1,000,000 random points and evaluate the integral.

from pylab import *

# Sample N points
N = 10000000
random = random(N)
x = random**2

# Define function for integral
def f(x):
    return 1/(1+e**x)

# Calculate the integral
I = 2*sum(f(x))/N

print("The value of integral is I = ",I)

# It's consistent with the given value in the question
