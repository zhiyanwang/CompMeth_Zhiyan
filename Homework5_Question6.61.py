# The Lagrange point

# Use either Newton’s method or the secant method to solve for the distance r from the Earth to the L_1 point.

# Compute a solution accurate to at least four significant figures.



# Define f(r)=0 for secant method

def f(r):

    G = 6.674*(10**-11)

    M = 5.974*(10**24)

    m = 7.348*(10**22)

    R = 3.844*(10**8)

    omega = 2.662*(10**-6)

    return G*M/(r**2)-G*m/((R-r)**2)-(omega**2)*r

# Guess the expected value for Lagrange point's distance from Earth

x_1 = 290000000  # meters

x_2 = 290000001  # meters

# print (f(290000001))

# Use loop to calculate the root of the function
# Knowing the distance can't be bigger than the distance between Earth and Moon

while x_2 < 384400000:
    x_3 = x_2 - f(x_2)*(x_2-x_1)/(f(x_2)-f(x_1))
    if f(x_3)<0:
        print ("The distance r from the Earth to the L_1 point is ",  x_3, " meters")
        break
    else:
        x_1 = x_2
        x_2 = x_3
