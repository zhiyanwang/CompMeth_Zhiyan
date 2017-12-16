import numpy as np


# Input height of the tower

h = float(input("Please enter the height of the tower: "))


# Calculate time for drop

t = np.sqrt((2*h/9.81))
print("the time for a ball dropped from a ", h, "m high tower is ", t, "seconds")