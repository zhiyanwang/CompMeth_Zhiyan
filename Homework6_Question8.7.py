# Trajectory with air resistance

# Solve the differential equations for projectile under the influence of air resistance

# The differential equations are calculated from F=ma separately in x, y directions.

# The four differential equations are based on velocities and accelerations as dependent variables.


from numpy import arange, empty, array
from pylab import *


# Use class to calculate 4th order Runge-Kutta

class RK4:

    # Initialize function f, initial conditions, and solution

    def __init__(self, f):
        self.f = f
        self.initial_conditions = None
        self.solution = None

    # Define a function with loop to calculate

    def loop(self,a,b,N=1000):
        f = self.f  # Get f from class
        r0 = array(self.initial_conditions,float)  # Initial condition
        h = (b-a)/N  # Interval h
        tpoints = arange(a,b,h)  # Points for time
        solution = empty(tpoints.shape+r0.shape,float)  # Solutions
        r = r0  # Set initial value for r

        # 4th order Runge-Kutta loop

        for i,t in enumerate(tpoints):
            solution[i] = r
            k1 = h*f(r, t)
            k2 = h*f(r+0.5*k1,t+0.5*h)
            k3 = h*f(r+0.5*k2,t+0.5*h)
            k4 = h*f(r+k3,t+h)
            r += (k1+2*k2+2*k3+k4)/6

        # Assign values

        self.h = h
        self.solution = solution
        self.t = tpoints

# Define the function for array decorator

def array_decorator(f, *args, **kwargs):
    g = lambda *args, **kwargs: array(f(*args, **kwargs), float)
    return g

# Define the function for trajectory

def trajectory(m=1):

    # Give value to variables
    density = 1.22
    C = 0.47
    g = 9.81
    radius = 8*10**-2


    # Define the function for dependent variables
    @array_decorator
    def f(r, t):

        # Four dependent variables
        x, y, v_x, v_y = r

        # Calculate velocity
        v = sqrt(v_x ** 2 + v_y ** 2)

        # Calculate friction
        friction = 1/2*3.14*(radius**2)*density* C*(v**2)
        d_r = [v_x, v_y]

        # Calculate acceleration
        d_vx = -friction/m*v_x/v
        d_vy = -friction/m*v_y/v-g
        d_v = [d_vx,d_vy]

        return d_r + d_v

    # Get the coordinates
    p = RK4(f)
    r0 = [0, 0]
    v0e = 100*exp(1j*30/180*3.14)
    v0 = [v0e.real, v0e.imag]
    p.initial_conditions = r0 + v0
    p.loop(0, 10)
    x = p.solution[:,0]
    y = p.solution[:,1]

    # Plot the positions
    plot(x[y > 0], y[y > 0], label=m)
    xlabel("Distance (m)")
    ylabel("Height (m)")
    title("Trajectory of Projectile")

    return x[abs(y) < 0.2][-1]

# Plot a series of trajectories for cannonballs of different masses
m_range = arange(0.5, 5, 0.5)
x_ground = [trajectory(m) for m in m_range]
legend()
show()

# Make a graph of distance traveled as a function of mass
plot(m_range, x_ground)
xlabel("Mass (kg)")
ylabel("Distance (m/s)")
title("Relationship Between Mass and Distance for Projectile")
show()

# Answer:
# As shown in the plots, with greater mass, the projectile is less influenced by air resistance, and travels farther.