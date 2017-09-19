# Input the distance to the Sun and velocity at perihelion
l1 = float(input("Please enter the distance to the Sun at perihelion in meter: "))
v1 = float(input("Please enter the velocity at the Sun's perihelion in meter per second: "))

# Parameter values
M = 1.9891e30    # Sun's mass in kg
G = 6.6738e-11 # Newton's gravitational constant in m**3/(kg*s**2)

# To calculate the distance to the Sun and velocity at aphelion, substitute l2 by l1*v1/v2 in the equation:
# 0.5*m*v1**2 - G*M*m/l1 = 0.5*m*v2**2 - G*M*m/l2
# Divide both side of the equation by 0.5*m, and we can get the quadratic equation of v2:
# v2**2 - (2*G*M/(v1*l1))*v2 - (v1**2 - 2*G*M/l1) = 0
# It can just be an equation for v1 if we switch the positions of v1 and v2 in the equation.
# The solution is v2 = (G*M/(v1*l1)) +/- np.sqrt((G*M/(v1*l1))**2+(v1**2 - 2*G*M/l1))
# The - sign gives a solution for the smaller velocity, and since v2 is the velocity at aphelion, it is the smaller root of the quadratic equation.

# Calculate v2
v2 = (G*M/(v1*l1)) - ((G*M/(v1*l1))**2+(v1**2 - 2*G*M/l1))**0.5
print("The velocity at the Sun's aphelion in is: ", v2, "m/s")

# Calculate l2
l2 = l1*v1/v2
print("The distance to the Sun at aphelion in is: ", l2, "m")

# Calculate Semi-major axis in meter
a = 0.5*(l1+l2)

# Calculate Semi-minor axis in meter
b = (l1*l2)**0.5

# Calculate Orbital period in year
T = (2*3.14*a*b/(l1*v1))/(60*60*24*365)
print("The orbital period T is: ", T, "years")

# Calculate the orbital eccentricity
e = (l2-l1)/(l2+l1)
print("The orbital eccentricity e is: ", e)