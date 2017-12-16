# Electronic capacitor

# Calculate the value of the potential at each grid point to a precision of 10^-6 volts

# Make a density plot of the result.


from pylab import *

# Set the constants
N = 100  # Number of grid squares on the side
error = 1e-6  # Required precision

# Set an array for the potentials
V = zeros([N+1,N+1],float)

# Set values for loop
a = 1.0
b = 0.8

# Use loop to calculate
while a > error:

    a = 0

    # Calculate new values of the potential
    for i in range(1, N):
        for j in range(1, N):

            # The capacitor plate with +1V
            if i==20 and j>20 and j<80:
                V[i,j]=1

            # The capacitor plate with -1V
            elif i==80 and j>20 and j<80:
                V[i,j]=-1

            # Calculate the difference
            else:
                diff=(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])/4-V[i,j]
                V[i,j]=V[i,j]+(1+b)*diff
            if diff > a:
                a = diff

# Make the density plot of the result
imshow(V.T, origin="lower")
gray()
title("Density Distribution of Potential")
show()